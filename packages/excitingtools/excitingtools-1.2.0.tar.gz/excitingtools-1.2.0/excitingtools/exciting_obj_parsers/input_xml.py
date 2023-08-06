""" Parse input XML data directly into corresponding python classes.
"""
from typing import Dict, Union

from excitingtools.input.base_class import ExcitingInput
from excitingtools.input.ground_state import ExcitingGroundStateInput
from excitingtools.input.structure import ExcitingStructure
from excitingtools.input.xs import ExcitingXSInput
from excitingtools.parser_utils.parser_decorators import xml_root
from excitingtools.exciting_dict_parsers.input_parser import root_type, parse_xs as parse_xs_to_dict, \
    parse_groundstate as parse_groundstate_to_dict, parse_structure as parse_structure_to_dict, parse_title


@xml_root
def parse_groundstate(root: root_type) -> ExcitingGroundStateInput:
    """
    Parse exciting input.xml groundstate element into python ExcitingGroundStateInput.
    :param root: Input for the parser.
    :returns: ExcitingGroundStateInput containing the groundstate input element attributes.
    """
    groundstate: dict = parse_groundstate_to_dict(root)
    return ExcitingGroundStateInput(**groundstate)


@xml_root
def parse_structure(root: root_type) -> ExcitingStructure:
    """
    Parse exciting input.xml structure element into python ExcitingStructure object.
    :param root: Input for the parser.
    :returns: ExcitingStructure containing the structure input element attributes and subelements.
    """
    structure: dict = parse_structure_to_dict(root)
    return ExcitingStructure(**structure)


@xml_root
def parse_xs(root: root_type) -> Union[ExcitingXSInput, None]:
    """
    Parse exciting input.xml xs element into python ExcitingXSInput object.
    :param root: Input for the parser.
    :returns: ExcitingXSInput containing the xs input element attributes and subelements. Returns None if no xs element
    was found.
    """
    xs: dict = parse_xs_to_dict(root)
    if xs == {}:
        return None
    return ExcitingXSInput(**xs)


exciting_input_type = Union[ExcitingInput, None]


@xml_root
def parse_input_xml(root: root_type) -> Dict[str, exciting_input_type]:
    """
    Parse exciting input.xml into the different python ExcitingInput Objects.
    :param root: Input for the parser.
    :returns: Dictionary which looks like: {'structure': ExcitingStructure,
        'ground_state': ExcitingGroundstateInput, 'xs': ExcitingXSInput}
    All subelements which are not present are removed in the end.
    """
    parsed_data = {'title': parse_title(root),
                   'structure': parse_structure(root),
                   'groundstate': parse_groundstate(root),
                   'xs': parse_xs(root)}
    return {key: value for key, value in parsed_data.items() if value}
