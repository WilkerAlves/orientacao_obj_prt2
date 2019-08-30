class Pizza:
    slice = 8

    @classmethod
    def change_size(cls, slices):
        cls.slice = slices


class Mozzarella(Pizza):
    ...


class Pepperoni(Pizza):
    ...


class Halftohalf(Mozzarella, Pepperoni):
    ...

