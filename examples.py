a_number = 420
another_number = 9_000
specific_number = 3.431

a_string = "Hello World"
another_string = 'Alice\'s greeting'
yet_another_string = """
    A whole other level
"""

a_boolean = True
not_a_boolean = False

nothing_here = None

a_list = [0, 1, 4, 3, 4]

a_tuple = ("a", "b", "d", "d")

print(a_tuple)

a_dict = {
    "key-a": "value a",
    "key-b": 2_000_000,
    "key-c": [
        1,
        'hello',
        {
            "sub-item-key-a": "Hi"
        },
        4
    ]
}

a_set = {0, 1, 2, 3}


def func_no_param_no_return() -> None:
    print('Hello World')


def func_no_param() -> int or None:
    print('Hello World')

    return -1


def param_func(my_param = "deufalt value") -> int:
    print(my_param)

    return -1


def another_param_func(my_other_param: str) -> None:
    print(my_other_param)


class Chair:
    _dimensions: dict = None

    def __init__(self, **kwargs):
        if kwargs.get("dimensions"):
            self.dimensions = kwargs.get("dimensions")

        else:
            self.dimensions = {"x": 5, "z": 5}

    @classmethod
    def sit(cls, chair, person) -> None:
        if type(chair) is not Chair:
            return

        chair.assign_person(person)

    # TODO: Provide implementation
    def assign_person(self) -> None:
        pass

    def _calculate_surface_area(self) -> int:
        return self.dimensions.get("x") * self.dimensions.get("z")

    # GETTERS / SETTERS

    @property
    def dimensions(self):
        return self._dimensions

    @dimensions.setter
    def dimensions(self, value: dict):
        self._dimensions = value

    # def get_dimensions(self):
    #     return self._dimensions
    #
    # def set_dimensions(self, value: dict):
    #     self._dimensions = value
    #
    # dimensions = property(get_dimensions, set_dimensions)

    # def dimensions(self, value: dict = None):
    #     if value is not None:
    #         self._dimensions = value
    #
    #     return self._dimensions

chair = Chair()
chair_b = Chair(dimensions={"x": 10, "z": 10})

Chair.sit(chair, None)

print(chair.dimensions)
print(chair_b.dimensions)
