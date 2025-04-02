from dragon import Dragon
# Ice Dragon class
class IceDragon(Dragon):
    def __init__(self, name, image):
        super().__init__(name, image)

    def can_breath_fire(self):
        return False