

class Family:
    """
    This class should be used to create families in the main running portion, the families should have a name, rank, moto, relations and heraldry
    There should be a function to create a timeline and branchoff of important events for characters within the family (eg. new rivalries, new opportunities)
    That can be used to create a family inside of a town or region alternatively
    Families should be created within a region, and assigned how wide spread they are (eg. they exist in most towns, or only 2), then a history of important figures and relations is created as families interact with one another
    """
    def __init__(self, regional_check, family_name, rank, moto, relations, heraldry):
        print("This function should initialise a family inside of a region")
        self.family_name = family_name
        self.regional_check = self.check_region(family_name)

    def check_region(self, name):
        regions = []
        print("Checking if {} exists in only a single town or in the entire region".format(name))

        return regions

class CadetBranch(Family):
    print("Should use information from family to make local branches")