class Pizza:
    slice = 8

    def __init__(self, flavor):
        self.flavor = flavor

    def get_slice(self):
        """Method of instance"""
        self.slice -= 1

    @classmethod
    def change_size(cls, slices):
        cls.slice = slices

    @staticmethod
    def ingredients():
        return 'Tomato sauce, cheese, onion'

