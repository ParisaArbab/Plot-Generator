# Plot-Generator
Defines a system to generate plots (stories) in two ways: randomly and interactively, using data from text files.
implements a plot generation system using the Model-View-Controller (MVC) design pattern, with the PlotViewer class acting as both the view and the controller. The plot generators (SimplePlotGenerator, RandomPlotGenerator, InteractivePlotGenerator) function as the models. Here's how each component fits into the MVC architecture and the functionality of each method:

Models: Plot Generators
SimplePlotGenerator: Represents the simplest form of data/model. It generates a static plot statement without any input or variability.

RandomPlotGenerator: A more complex model that generates plots by randomly selecting components (names, adjectives, professions, etc.) from text files.
InteractivePlotGenerator: The most complex model, it generates plots interactively by asking the user to choose components for the plot through a series of prompts.
View/Controller: PlotViewer
__init__(self): Initializes the PlotViewer instance. Sets self.plot_generator to None, preparing it to hold a reference to a plot generator (model).

registerPlotGenerator(self, plot_generator):
Functionality: Registers a plot generator with the PlotViewer.
MVC Role: Acts as a controller method allowing the view (PlotViewer) to select which model (plot generator) to use for generating plots. This method enables dynamic switching between different plot generation strategies/models based on user choice or predefined logic.
generate(self):

Functionality: Generates a plot using the currently registered plot generator.
MVC Role: Functions as a controller method that delegates the request to generate a plot to the current model (the registered plot generator). It then acts as the view by either returning the generated plot for presentation or indicating that no plot generator is registered. This method showcases how the controller mediates between the user interface and the application logic/models, handling the application flow and output presentation.

Functionality Explanation Based on MVC:
Registering Generators: The registerPlotGenerator method allows the controller (PlotViewer) to dynamically select and switch between different models (plot generators). This flexibility demonstrates how the controller can change the application's behavior by changing the model it interacts with.

Sending Request to Generate Plots: By calling the generate method of the currently registered plot generator, the controller (PlotViewer) effectively sends a request to the model to perform its designated function (plot generation) and then handles the output (view functionality).

Accepting User Input: While the shared code snippet does not explicitly show the PlotViewer accepting user input directly for the models, the design implies that models like InteractivePlotGenerator would use PlotViewer's methods (e.g., a hypothetical queryUser method) to interact with the user. This setup would ensure that user input collection is consistent and centralized, regardless of the model in use.

Presenting Plots: The generate method in PlotViewer takes the plot created by the model and presents it, fulfilling the view's role. This design separates the concern of how plots are generated (model) from how they are presented to the user (view), with the controller (PlotViewer) orchestrating this interaction.
