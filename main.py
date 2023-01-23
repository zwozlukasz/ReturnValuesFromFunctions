# return few values from function
class MultiValues:
    def __init__(self):
        self.value_1 = "test value_1"
        self.value_2 = 23
        self.value_3 = 23.43


def return_values():
    return MultiValues()


results = return_values()
print(results.value_1)
print(results.value_2)
print(results.value_3)


def return_tuple():
    value_1 = "This is value_1 returned from return_many_values() function"
    value_2 = 2344
    value_3 = 34.34
    return value_1, value_2, value_3


a, b, c = return_tuple()
print(f"Returned values: '{a}', {b}, {c}")


def return_list():
    value_1 = "This is value returned via list"
    value_2 = 88
    value_3 = 88.55
    return [value_1, value_2, value_3]


a1, b1, c1 = return_list()
print(f"Values returned from list: {a1}, {b1}, {c1}")
list_results = return_list()
print(list_results)


def return_dict():
    di = {"value_1": "Return values from dictionary",
          "value_2": 34,
          "value_3": 342.22
          }
    return di


results_dict = return_dict()
print(results_dict)


def return_dict_1():
    return {"value_1": "Values returned from retun_dict_1() function: ",
            "value_2": 334,
            "value_3": 33.241}


print(return_dict_1())


def return_dict_2(value_1: str, value_2: int, value_3: float):
    # di = {}
    # di["value_1"] = value_1
    # di["value_2"] = value_2
    # di["value_3"] = value_3
    di = {"value_1": value_1, "value_2": value_2, "value_3": value_3}
    return di


print(return_dict_2("Values returned from return_dict_2() function", 2345, 2.3432))

# Try to check how works data class (it works for python 3.7 and higher)

from dataclasses import dataclass


@dataclass
class TestDataClass:
    value_1: str
    value_2: int
    value_3: float


def return_values_from_data_class(value_a: str, value_b: int, value_c: float):
    return TestDataClass(value_1=value_a, value_2=value_b, value_3=value_c)


print(return_values_from_data_class("This is set of values returned from dataClass: ", 344477777, 777.9999))


# generator

def return_single_value():
    yield "This is valur_1 returned from generator"
    yield 55
    yield 99.77
    yield 23, 442, 42432, 424, "This is string"
    yield [2, 4, 5, 6, 7, 8, 44, 36, 3]

# It does not works, it does not returnt next value
print(next(return_single_value()))
print(next(return_single_value()))
print(next(return_single_value()))
print(next(return_single_value()))

results = return_single_value()
print("Next round")
print(next(results))
print(next(results))
print(next(results))
print(next(results))
print(next(results))
