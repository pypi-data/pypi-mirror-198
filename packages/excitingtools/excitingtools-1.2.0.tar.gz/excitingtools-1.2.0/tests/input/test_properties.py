""" Test properties. """
from ase.build import bulk

from excitingtools.input.properties import ExcitingPropertiesInput, ExcitingBandStructureInput
from excitingtools.input.input_xml import ExcitingInputXML
from excitingtools.input.structure import ExcitingStructure
from excitingtools.input.ground_state import ExcitingGroundStateInput


def test_bandstructure():
    properties = {
        "bandstructure": {"plot1d": {"path": {
            "steps": 100,
            "points":
                [
                    {"coord": [1, 0, 0], "label": "Gamma"},
                    {"coord": [0.625, 0.375, 0], "label": "K"},
                    {"coord": [0.5, 0.5, 0], "label": "X", "breakafter": True},
                    {"coord": [0, 0, 0], "label": "Gamma"},
                    {"coord": [0.5, 0, 0], "label": "L"},
                ]
        }}}}
    properties_input = ExcitingPropertiesInput(**properties)
    print(properties_input.to_xml_str())


def test_bs_from_ase():
    atoms = bulk("Si")
    bs = ExcitingBandStructureInput.from_ase_atoms_obj(atoms)
    properties_input = ExcitingPropertiesInput(bandstructure=bs)
    print(properties_input.to_xml_str())


def test_bs_input():
    atoms = bulk("Si")
    gs = ExcitingGroundStateInput(rgkmax=5.0)
    struct = ExcitingStructure(atoms)
    bs = ExcitingBandStructureInput.from_ase_atoms_obj(atoms)
    properties_input = ExcitingPropertiesInput(bandstructure=bs)
    input_xml = ExcitingInputXML(struct, gs, title="BS exciting", properties=properties_input)
    input_xml.write("input.xml")
