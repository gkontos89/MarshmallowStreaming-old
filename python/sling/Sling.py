from Provider import Provider
from sling.SlingBlue import SlingBlue
from sling.SlingOrange import SlingOrange
from sling.SlingOrangeAndBlue import SlingOrangeAndBlue


class Sling(Provider):
    def __init__(self):
        super().__init__("Sling")
        self.packages['Sling Blue'] = SlingBlue()
        self.packages['Sling Orange'] = SlingOrange()
        self.packages['Sling Orange And Blue'] = SlingOrangeAndBlue()
