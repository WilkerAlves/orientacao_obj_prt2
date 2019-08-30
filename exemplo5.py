
class Pizza:
    slice = 8

    @classmethod
    def change_size(cls, slices):
        cls.slice = slices

    @staticmethod
    def ingredients():
        return 'ingredients'


class Mozzarella(Pizza):

    @staticmethod
    def ingredients():
        return ['Tomato sauce', 'cheese', 'onion']
