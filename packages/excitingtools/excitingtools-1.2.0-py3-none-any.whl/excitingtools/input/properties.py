""" Add properties subtree. Only bandstructure now. """
from typing import Optional, Union, List

from ase import Atoms
from ase.cell import Cell
from ase.dft.kpoints import BandPath

from excitingtools.input.base_class import ExcitingXMLInput
from excitingtools.input.common import ExcitingPlot1dInput


class ExcitingBandStructureInput(ExcitingXMLInput):
    """
    Class for exciting bandstructure input.
    """
    name = "bandstructure"
    _valid_attributes = {"character", "deriv", "scissor", "wannier"}

    def __init__(self,
                 plot1d: Optional[Union[dict, ExcitingPlot1dInput]] = None,
                 **kwargs):
        """Generate an object of ExcitingXMLInput for the bandstructure attributes."""
        super().__init__(**kwargs)

        self.plot1d = self._initialise_subelement_attribute(ExcitingPlot1dInput, plot1d)

    @classmethod
    def from_cell(cls, cell: Cell, steps: Optional[int] = 100):
        """ Get band path from lattice cell. """
        bandpath: BandPath = cell.bandpath()
        points = []
        for point in bandpath.path:
            if point == ",":
                points[-1]["breakafter"] = True
            else:
                points.append({"coord": list(bandpath.special_points[point]), "label": point})

        return cls(plot1d={"path": {"steps": steps, "points": points}})

    @classmethod
    def from_lattice(cls, lattice_vectors: List[List[float]], steps: Optional[int] = 100):
        """ Get band path from lattice vectors as array or list of lists. """
        return cls.from_cell(Cell(lattice_vectors), steps=steps)

    @classmethod
    def from_ase_atoms_obj(cls, atoms_obj: Atoms, steps: Optional[int] = 100):
        """ Get band path from ase object. """
        return cls.from_cell(atoms_obj.cell, steps)


class ExcitingPropertiesInput(ExcitingXMLInput):
    """
    Class for exciting properties input.
    """

    # Reference: http://exciting.wikidot.com/ref:groundstate
    name = 'properties'

    # parse_element = parse_groundstate

    def __init__(self,
                 bandstructure: Optional[Union[dict, ExcitingBandStructureInput]] = None,
                 ):
        """Generate an object of ExcitingXMLInput for the groundstate attributes."""
        super().__init__()

        self.bandstructure = self._initialise_subelement_attribute(ExcitingBandStructureInput, bandstructure)
