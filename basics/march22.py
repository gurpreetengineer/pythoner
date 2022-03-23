# {} Sets
# [] List
# () Tuple
# {key:value} Dictionary


# class lamb:
#     def __init__(self, __input_one__):
#         self.__input_one__ =
#


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")


make_pretty(ordinary)


# [resultYouWant] for var in the_var_list if _condition_


# Transpose of a matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

row = []

print('here', [[anElement[i] for anElement in matrix]
      for i in range(len(matrix[0]))])


a, b = 10, 20

new_str = 'there is no {0} + {1} = 0 in this universe'.format(a, b)

print(new_str)
print('there is no {a} + {b} = 0 in this universe'.format(a=a, b=b))
# print('there is no {0} + {1} = 0 in this universe'.format(a, b))


new_comparison_list = (
    (1, 2, 3) < (1, 2, 4),
    [1, 2, 3] < [1, 2, 4],
    'ABC' < 'C' < 'Pascal' < 'Python',
    (1, 2, 3, 4) < (1, 2, 4),
    (1, 2) < (1, 2, -1),
    (1, 2, 3) == (1.0, 2.0, 3.0),
    (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4),
)

print(' new_comparison_list ', new_comparison_list)
