""" Parsers for input.xml.

TODO(Fabian): Issues 117 & 121:
As more sub-elements are implemented in the input files, also add parsers here
"""
import pathlib
import warnings
from typing import Dict, Union
from xml.etree import ElementTree

from excitingtools.parser_utils.parser_decorators import xml_root
from excitingtools.parser_utils.parser_utils import find_element

# Valid input formats for all parsers
root_type = Union[str, ElementTree.Element, pathlib.Path]


@xml_root
def parse_title(root: root_type) -> str:
    """
    Parse exciting input.xml title element to find the title.
    :param root: Input for the parser.
    :returns: Title as string.
    """
    ground_state = find_element(root, 'title')
    return ground_state.text


@xml_root
def parse_groundstate(root: root_type) -> dict:
    """
    Parse exciting input.xml groundstate element into python dictionary.
    :param root: Input for the parser.
    :returns: Dictionary containing the groundstate input element attributes.
    """
    valid_xml_elements = {'spin', 'solver'}

    ground_state = find_element(root, 'groundstate')
    groundstate_dict: dict = ground_state.attrib

    subelements = {elem.tag: elem.attrib for elem in ground_state}
    tags = set(subelements)
    unsupported_tags = tags - valid_xml_elements
    supported_tags = tags - unsupported_tags

    if unsupported_tags:
        warnings.warn(f'Subelements {unsupported_tags} not yet supported. Groundstate will ignore it.')

    groundstate_dict.update({tag: subelements[tag] for tag in supported_tags})
    return groundstate_dict


@xml_root
def parse_structure(root: root_type) -> dict:
    """
    Parse exciting input.xml structure element into python dictionary.
    :param root: Input for the parser.
    :returns: Dictionary containing the structure input element attributes and subelements. Looks like:
        {'atoms': List of atoms with atom positions in fractional coordinates,
         'lattice': List of 3 lattice vectors, 'species_path': species_path as string,
         'crystal_properties': dictionary with the crystal_properties,
         'species_properties': dictionary with the species_properties,
         all additional keys are structure attributes}
    """
    structure = find_element(root, 'structure')
    structure_properties = structure.attrib
    species_path = structure_properties.pop('speciespath')
    crystal = structure.find('crystal')
    crystal_properties = crystal.attrib
    lattice = []
    for base_vect in crystal.findall('basevect'):
        lattice.append([float(x) for x in base_vect.text.split()])

    atoms = []
    species_properties = {}
    for species in structure.findall('species'):
        species_attributes = species.attrib
        species_file = species_attributes.pop('speciesfile')
        species_symbol = species_file[:-4]
        species_properties[species_symbol] = species_attributes
        for atom in species:
            atom_attributes = atom.attrib
            coord = [float(x) for x in atom_attributes.pop('coord').split()]
            atom_dict = {'species': species_symbol, 'position': coord}
            atom_dict.update(atom_attributes)
            atoms.append(atom_dict)

    return {
        'atoms': atoms,
        'lattice': lattice,
        'species_path': species_path,
        'crystal_properties': crystal_properties,
        'species_properties': species_properties,
        **structure_properties
    }


@xml_root
def parse_xs(root: root_type) -> dict:
    """
    Parse exciting input.xml xs element into python dictionary.
    :param root: Input for the parser.
    :returns: Dictionary containing the xs input element attributes and subelements. Could look like:
        {all toplevel xs_properties as dict keys,
         'energywindow': dictionary with the energywindow_properties,
         'screening': dictionary with the screening_properties, 'BSE': dictionary with bse_properties,
         'qpointset': List of qpoints, 'plan': List of tasks}
    """
    valid_xml_elements = {'BSE', 'energywindow', 'screening'}
    special_elements = {'qpointset', 'plan'}
    all_valid_elements = valid_xml_elements | special_elements

    xs = find_element(root, 'xs')
    if xs is None:
        return {}
    xs_dict: dict = xs.attrib

    subelements = {elem.tag: elem.attrib for elem in xs}
    tags = set(subelements)
    unsupported_tags = tags - all_valid_elements
    supported_xml_tags = tags - unsupported_tags - special_elements

    if unsupported_tags:
        warnings.warn(f'Subelements {unsupported_tags} not yet supported. XS will ignore it.')

    xs_dict.update({tag: subelements[tag] for tag in supported_xml_tags})

    qpointset_xml = xs.find('qpointset')
    if qpointset_xml:
        qpointset = []
        for qpoint in qpointset_xml:
            qpointset.append([float(x) for x in qpoint.text.split()])
        xs_dict['qpointset'] = qpointset

    plan_xml = xs.find('plan')
    if plan_xml:
        xs_dict['plan'] = [doonly.attrib['task'] for doonly in plan_xml]

    return xs_dict


@xml_root
def parse_input_xml(root: root_type) -> Dict[str, dict]:
    """
    Parse exciting input.xml into python dictionaries.
    :param root: Input for the parser.
    :returns: Dictionary which looks like: {'structure': structure_dict,
        'ground_state': groundstate_dict, 'xs': xs_dict}.
    """
    title = parse_title(root)
    structure = parse_structure(root)
    ground_state = parse_groundstate(root)
    xs = parse_xs(root)
    return {'title': title, 'structure': structure, 'groundstate': ground_state, 'xs': xs}
