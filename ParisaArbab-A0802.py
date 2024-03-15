"""
Author: Parisa Arbab
Date: March 5 2024
Statement:“I have not given or received any unauthorized assistance on this assignment.”
YouTube Link:https://youtu.be/RBFzt2SkAgg

answered this question in the above link:
• Show how the PlotViewer registers the generators: by using registerPlotGenerators assigns the plotgenerator instance to its attribute(plot_generator)
• Show how the PlotViewer sends the request to generate plots to the plot generator. by calling generate method on the current registered plot generator stored in its plot_generator attribute.
• Show how the PlotViewer is able to accept requests for user input from the plot generators.PlotViewer would implement a method like queryUser,
   which the plot generators could call to interact with the user. This method would collect user input and return it to the generator.
• Show how the PlotViewer accepts and presents the plots created by the plot generators.The PlotViewer presents the plots by returning the result of the generate method call on the current plot generator.
  This result can then be printed or displayed in the desired format, showing the generated plot to the user.

"""

from ParisaArbab_A0801 import SimplePlotGenerator
from ParisaArbab_A0801 import RandomPlotGenerator
from ParisaArbab_A0801 import InteractivePlotGenerator


# The PlotViewer class integrates the Model-View-Controller (MVC) architectural pattern by acting as both the view and the controller
# within the context of a plot generation system.
# This class interfaces with different types of plot generators (Models) to produce and manage plot outputs
# based on user interactions or predefined logic.
class PlotViewer:
    """
    The PlotViewer class serves as both the view and the controller for the plot generator classes.
    It can register any plot generator and generate plots using them.
    """

    def __init__(self):
        """
        Initializes the PlotViewer.
        """
        self.plot_generator = None

    def registerPlotGenerator(self, plot_generator):
        """
        Registers a plot generator with the PlotViewer.

        Parameters:
        plot_generator (object): An instance of a plot generator class.
        """
        self.plot_generator = plot_generator

    def generate(self):
        """
        Generates a plot using the registered plot generator.
        Registers a plot generator with the PlotViewer.
        This method allows the PlotViewer to be flexible and work with any plot generator that follows the expected interface,
        specifically having a generate() method.
    """

        if self.plot_generator:
            return self.plot_generator.generate()
        else:
            return "No plot generator registered."""
# Example

mvc = PlotViewer()
mvc.registerPlotGenerator( SimplePlotGenerator )
mvc.registerPlotGenerator( RandomPlotGenerator )
mvc.registerPlotGenerator( InteractivePlotGenerator)


