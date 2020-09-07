import pandas as pd
import numpy as np

class Character:
    """
    This class should be used to create characters in the main running portion, the character should have a name, title and background type as a base type
    There should be a function to create a timeline and branchoff characters that can be used to create a family inside of a town or region alternatively
    Characters should be created within a region, and assigned to places to live, then a history of them is created and they interact with one another
    """
    def __init__(self, name, family, background, aspirations, quests):
        checked_family = self.check_family(self, family)
        print("Creating new character")

    def check_family(self, family):
        #METHOD: checks the families in a region, if the last name exists then it either adds the characer to the family or creates a new cadet branch, else it creates a new family
        town_groups = []


