"""Base class for exciting input classes.
"""
from abc import ABC, abstractmethod
from typing import Union, Set, Callable
from xml.etree import ElementTree
from pathlib import Path
import numpy as np

from excitingtools.utils.dict_utils import check_valid_keys
from excitingtools.utils.jobflow_utils import special_serialization_attrs


class ExcitingInput(ABC):
    """Base class for exciting inputs."""
    name = "base"

    @abstractmethod
    def to_xml(self) -> ElementTree:
        """ Convert class attributes to XML ElementTree."""
        ...


class ExcitingXMLInput(ExcitingInput):
    """Base class for exciting inputs that only consist of many attributes."""

    # Convert python data to string, formatted specifically for
    _attributes_to_input_str = {int: lambda x: str(x),
                                np.int64: lambda x: str(x),
                                np.float64: lambda x: str(x),
                                float: lambda x: str(x),
                                bool: lambda x: str(x).lower(),
                                str: lambda x: x,
                                list: lambda mylist: " ".join(str(x).lower() for x in mylist).strip(),
                                tuple: lambda mylist: " ".join(str(x).lower() for x in mylist).strip()
                                }
    _valid_attributes: Set[str] = None
    parse_element: Callable = lambda x: x

    @staticmethod
    def _initialise_subelement_attribute(XMLClass, element, skip_none: bool = True):
        """
        Initialize given elements to the ExcitingXSInput constructor. If element is already ExcitingXMLInput class
        object, nothing happens. For None elements None is returned. In any other case, the class constructor of the
        given XSClass is called.
        :param skip_none: if False, add empty subtree without attributes for given element
        """
        if isinstance(element, XMLClass):
            return element
        elif element is None and skip_none:
            return None
        elif element is None and not skip_none:
            return XMLClass()
        elif isinstance(element, dict):  # assume kwargs
            return XMLClass(**element)
        else:
            # Assume the element type is valid for the class constructor
            return XMLClass(element)

    def __init__(self, **kwargs):
        """Initialise class attributes with kwargs.

        Rather than define all options for a given method, pass as kwargs and directly
        insert as class attributes.

        :param name: Method name.
        """
        if self._valid_attributes:
            check_valid_keys(kwargs.keys(), self._valid_attributes, self.name)
        self.__dict__.update(kwargs)

    def to_xml(self, **kwargs) -> ElementTree:
        """Put class attributes into an XML tree, with the element given by self.name.

        Example ground state XML subtree:
           <groundstate vkloff="0.5  0.5  0.5" ngridk="2 2 2" mixer="msec" </groundstate>

        Note, kwargs preserve the order of the arguments, however the order does not appear to be
        preserved when passed to (or perhaps converted to string) with xml.etree.ElementTree.tostring.

        kwargs argument allows to specify additional attributes.

        :return ElementTree.Element sub_tree: sub_tree element tree, with class attributes inserted.
        """
        none_keys = set([key for key, value in vars(self).items() if value is None])
        attributes = {key: self._attributes_to_input_str[type(value)](value) for key, value
                      in vars(self).items() if value is not None and not isinstance(value, ExcitingInput)}
        subtrees = [self.__dict__[key] for key in set(vars(self).keys()) - set(attributes.keys()) - none_keys]

        xml_tree = ElementTree.Element(self.name, **attributes, **kwargs)

        for subtree in subtrees:
            xml_tree.append(subtree.to_xml())

        # Seems to want this operation on a separate line
        xml_tree.text = ' '

        return xml_tree

    def to_xml_str(self) -> str:
        """ Convert attributes to XML tree string. """
        return ElementTree.tostring(self.to_xml(), encoding='unicode', method='xml')

    def as_dict(self) -> dict:
        """ Convert attributes to dictionary. """
        serialise_attrs = special_serialization_attrs(self)
        return {**serialise_attrs, "xml_string": self.to_xml_str()}

    @classmethod
    def from_xml(cls, xml_string: str):
        """ Initialise class instance from XML-formatted string.

        Example Usage
        --------------
        xs_input = ExcitingXSInput.from_xml(xml_string)
        """
        return cls(**cls.parse_element(xml_string))

    @classmethod
    def from_dict(cls, d):
        """ Recreates class instance from dictionary. """
        return cls.from_xml(d["xml_string"])


def query_exciting_version(exciting_root: Union[Path, str]) -> dict:
    """Query the exciting version
    Inspect version.inc, which is constructed at compile-time.

    Assumes version.inc has this structure:
     #define GITHASH "1a2087b0775a87059d53"
     #define GITHASH2 "5d01a5475a10f00d0ad7"
     #define COMPILERVERSION "GNU Fortran (MacPorts gcc9 9.3.0_4) 9.3.0"
     #define VERSIONFROMDATE /21,12,01/

    TODO(Fab) Issue 117. Parse major version.
     Would need to parse src/mod_misc.F90 and regex for "character(40) :: versionname = "
     Refactor whole routine to use regex.

    :param exciting_root: exciting root directory.
    :return version: Build and version details
    """
    if isinstance(exciting_root, str):
        exciting_root = Path(exciting_root)

    version_inc = exciting_root / 'src/version.inc'

    if not version_inc.exists():
        raise FileNotFoundError(f'{version_inc} cannot be found. '
                                f'This file generated when the code is built')

    with open(version_inc, 'r') as fid:
        all_lines = fid.readlines()

    git_hash_part1 = all_lines[0].split()[-1][1:-1]
    git_hash_part2 = all_lines[1].split()[-1][1:-1]
    compiler_parts = all_lines[2].split()[2:]
    compiler = " ".join(s for s in compiler_parts).strip()

    version = {'compiler': compiler[1:-1], 'git_hash': git_hash_part1 + git_hash_part2}
    return version
