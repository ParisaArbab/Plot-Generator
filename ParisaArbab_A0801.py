"""
Author: Parisa Arbab
Date: March 5 2024
Statement:“I have not given or received any unauthorized assistance on this assignment.”
YouTube Link:https://youtu.be/FFc3nLskoxA

answered this question in the above link:
1- Show how you randomly produce a plot in RandomPlotGenerator.
2- In InteractivePlotGenerator, show how you manage user input when you are connected to a
view/controller.

"""
# Model-View-Controller (MVC)
# This code demonstrates an application of the MVC pattern in a simplified form.
# The plot generator classes act as the Model, responsible for the data and logic of plot generation.
# The PlotViewer class combines the roles of View and Controller, managing user input (Controller)
# and presenting the output (View). This setup allows for flexible I/O mechanisms (console, GUI, etc.)
# without changing the underlying plot generation logic (Model).

import random

class SimplePlotGenerator:
    """
    This class generates a static plot. Represents the simplest form of the Model.
    """
    def generate(self):
        """
        Returns a simple plot.
        """
        return "Something happens"

class RandomPlotGenerator(SimplePlotGenerator):
    """
    This class generates a random plot from data read from text files.
    """
    def __init__(self, plot_viewer):
        """
        Initializes the RandomPlotGenerator with a plot viewer and loads plot data from files.
                """
        self.pv = plot_viewer
        # Define the text files from which to load plot components.
        self.files = {
            'plot_names': 'plot_names.txt',
            'plot_adjectives': 'plot_adjectives.txt',
            'plot_professions': 'plot_profesions.txt',
            'plot_verbs': 'plot_verbs.txt',
            'plot_adjectives_evil': 'plot_adjectives_evil.txt',
            'plot_villain_jobs': 'plot_villian_job.txt',
            'plot_villains': 'plot_villains.txt'
        }
        # Load data from files
        self.plot_data = self.load_plot_data()

    def load_plot_data(self) :
        """
        Loads plot components from specified files into a dictionary.
                """
        plot_data = {}
        # Attempt to open each file and load its contents.
        for key, filename in self.files.items () :
            try :
                with open ( filename, 'r' ) as file :
                    plot_data[ key ] = [ line.strip () for line in file.readlines () ]
                #print ( f"Loaded {key} successfully." )  # Debug: Confirm each file is loaded
            except FileNotFoundError :
                print ( f"Couldn't find the file: {filename}" )
                plot_data[ key ] = [ ]  # Empty list in case of missing file
        return plot_data

    def generate(self):
        """
        Uses random selections from loaded data to generate a plot.
        Demonstrates dynamic plot generation based on Model data.
        Question 1: This method demonstrates how a random plot is produced in RandomPlotGenerator.
        """
        try:
            name = random.choice(self.plot_data['plot_names'])
            adjective = random.choice(self.plot_data['plot_adjectives'])
            profession = random.choice(self.plot_data['plot_professions'])
            verb = random.choice(self.plot_data['plot_verbs'])
            evil_adjective = random.choice(self.plot_data['plot_adjectives_evil'])
            villain_job = random.choice(self.plot_data['plot_villain_jobs'])
            villain = random.choice(self.plot_data['plot_villains'])

            return f"{name}, a {adjective} {profession}, must {verb} the {evil_adjective} {villain_job}, {villain}."
        except IndexError:  # If any list is empty due to missing file
            return "Plot generation failed due to missing data."



class InteractivePlotGenerator(SimplePlotGenerator):
    """
        Generates a plot interactively by querying the user to choose components.
        """
    def __init__(self, plot_viewer) :
        """
     Initializes the InteractivePlotGenerator with a plot viewer and loads plot data from files.
                """
        super ().__init__ ()
        self.pv = plot_viewer
        self.files = {
            'plot_names' : 'plot_names.txt',
            'plot_adjectives' : 'plot_adjectives.txt',
            'plot_professions' : 'plot_profesions.txt',
            'plot_verbs' : 'plot_verbs.txt',
            'plot_adjectives_evil' : 'plot_adjectives_evil.txt',
            'plot_villain_jobs' : 'plot_villian_job.txt',
            'plot_villains' : 'plot_villains.txt'
        }
        self.plot_data = self.load_plot_data ()

    def load_plot_data(self) :
        """
      Loads plot components from specified files into a dictionary.
     """
        plot_data = {}
        for key, filename in self.files.items () :
            try :
                with open ( filename, 'r' ) as file :
                    plot_data[ key ] = [ line.strip () for line in file.readlines () ]
            except FileNotFoundError :
                print ( f"Couldn't find the file: {filename}" )
                plot_data[ key ] = [ ]  # Empty list in case of missing file
        return plot_data

    def query_user_for_choice(self, options, category):
        """
      Queries the user for a choice among provided options for a specific category.
     #Question 2:an example of Controller functionality within the Model.
         """
        print(f"Choose a {category} by entering the number next to it:")
        for i, option in enumerate(options):
            print(f"{i + 1}: {option}")
        while True:
            try:
                selection = int(self.pv.queryUser("Your choice number[1-5]: ")) - 1
                if 0 <= selection < len(options):
                    return options[selection]
                else:
                    print("Invalid choice. Please select a number from the list.")
            except ValueError:
                print("Please enter a numeric value.")

    def generate(self):
        """
         Interactively generates a plot by asking the user to select components.
         A Model method influenced by user input (Controller).
         """
        plot_components = ['plot_names', 'plot_adjectives', 'plot_professions', 'plot_verbs', 'plot_adjectives_evil', 'plot_villain_jobs', 'plot_villains']
        selections = []
        for component in plot_components:
            # Ensure there are at least 5 components or adjust accordingly
            options = random.sample(self.plot_data[component], min(5, len(self.plot_data[component])))
            choice = self.query_user_for_choice(options, component)
            selections.append(choice)
        # Assemble and return the final plot
        # This return statement is just an example; adjust according to your actual data structure
        return f"{selections[0]}, a {selections[1]} {selections[2]}, must {selections[3]} the {selections[4]} {selections[5]}, {selections[6]}."

# Example usage

class PlotViewer:
    """
    Handling I/O, combining View and Controller functionalities.
    use to interact between the user and plot generators(Model).
    demonstrating how the system abstracts I/O operations from the logic of plot generation.
    This design allows changing the I/O mechanism without affecting the plot generation logic.
    """
    def queryUser(self, message):
        """
        Queries the user, acting as part of the Controller.
        """
        return input(message)

# example just for test: pv is an instance of PlotViewer
pv = PlotViewer()
##
pg = SimplePlotGenerator()
print("1. Simple Plot Generator**********************************************")
print(pg.generate())

RandomPlotGenerator = RandomPlotGenerator(pv)
print("\n2. Random Plot Generator**********************************************")
print(RandomPlotGenerator.generate(),"\n")
#
interactive_plot_generator = InteractivePlotGenerator(pv)
print("3.Interactive Plot Generator**********************************************")
print(interactive_plot_generator.generate())