""" Common input. """
from typing import List, Union
from xml.etree import ElementTree

from excitingtools.input.base_class import ExcitingXMLInput


class ExcitingPointInput(ExcitingXMLInput):
    """
    Class for exciting point input.
    """
    name = "point"
    _valid_attributes = {"coord", "breakafter", "label"}


class ExcitingPathInput(ExcitingXMLInput):
    """
    Class for exciting path input.
    """
    name = "path"
    _valid_attributes = {"steps", "outfileprefix"}

    def __init__(self,
                 points: List[Union[dict, ExcitingPointInput]],
                 **kwargs):
        """Generate an object of ExcitingXMLInput for the path attributes."""
        super().__init__(**kwargs)

        # for i, point in enumerate(points):
        #     setattr(self, f"point-{i}", self._initialise_subelement_attribute(ExcitingPointInput, point))
        self.points = [self._initialise_subelement_attribute(ExcitingPointInput, point) for point in points]
        # self.point = self._initialise_subelement_attribute(ExcitingPlot1dInput, points)

    def to_xml(self) -> ElementTree:
        """Put class attributes into an XML tree, with the element given by self.name.
        :return ElementTree.Element sub_tree: sub_tree element tree, with class attributes inserted.
        """
        attributes = {key: self._attributes_to_input_str[type(value)](value) for key, value
                      in vars(self).items() if key != "points"}
        xml_tree = ElementTree.Element(self.name, **attributes)

        for point in self.points:
            xml_tree.append(point.to_xml())

        return xml_tree


class ExcitingPlot1dInput(ExcitingXMLInput):
    """
    Class for exciting plot 1d input.
    """
    name = "plot1d"

    def __init__(self,
                 path: Union[dict, ExcitingPathInput]):
        """Generate an object of ExcitingXMLInput for the plot 1d attributes."""
        super().__init__()

        self.path = self._initialise_subelement_attribute(ExcitingPathInput, path)
