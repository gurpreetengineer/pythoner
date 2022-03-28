# Cannot do like this. Exceptions need to be classes and not a list,
# tuple or dictionary. Refer from line 23 onwards.

# uncomment the code and you'll get the Error: TypeError:
# catching classes that do not inherit from BaseException is not allowed
# ============================================================================

# an_exceptional_list = ['A', 'B', 'C', 'D']
# for exception in an_exceptional_list:
#     try:
#         # a = '12'
#         raise exception
#     except 'A':
#         print(f'Error {exception} occurred')
#     except 'B':
#         print(f'Error {exception} occurred')
#     except 'C':
#         print(f'Error {exception} occurred')
# except BaseException as error:
#     print(f'Some different error occurred: {error}')
# ============================================================================
#
# class A(Exception):
#     pass
#
#
# class B(A):
#     pass
#
#
# class C(B):
#     pass
#
#
# for a_class_exception in [A, B, C]:
#     try:
#         print(10**10**10)
#         raise a_class_exception()
#     except KeyboardInterrupt:
#         print('Bye fella, unable to calculate such dumb thing 10**10**10')
#         print('will run 3 times because loop is executing 3 times', end='')
#         print(f': {a_class_exception}.')
#     except A:
#         print(f'Class "AA" occurred :{a_class_exception}')
#     except B:
#         print('Exception is handled once in the first ((except A)) block.')
#         print('Blocks after ((except A)) block will never get executed.')
#         print('Class "BB" occurred')
# except BaseException as error:
#     print(f'A Base exception occurred: {error}')


# There are many exceptions but some of them are:
# 1) NameError
# 2) ZeroDivisionError
# 1) OSError
# 1) KeyboardInterrupt
# 1) NameError

# try except else finally


# class AnyNewOne:
#     def classicalFunc(self):
#         print('This will handle exceptions')
#         try:
#             what_if = 10**10**10
#         except KeyboardInterrupt:
#             print('fookin huge amounta time, bruv')
#         else:
#             print('oops: The norms skipped exceptional blocks. ')
#         finally:
#             print("this ain't shit. M gona run anyway cuz I go' stamina n**ga")
#
#
# anObject = AnyNewOne()
# anObject.classicalFunc()


class Mapping:
    def __init__(self, iterating_list):
        self.items_list = []
        self.__update(iterating_list)

    def update(self, iterating_list):
        for item in iterating_list:
            self.items_list.append(item)

    __update = update


class MappingSubclass(Mapping):
    def __init__(self):
            super().__init__(self, items_list)
        # pass

    # def update(self, keys, values):
    #     for item in zip(keys, values):
    #         self.items_list.append(item)


newObject = MappingSubclass()

# newObject.update(['abc', 'def', 'ghi', 'jkl', 'lmo'],
#                  [1234, 34, 345, 34534, 5345])
newObject.update([555555, 123, 12334, 36456, 56678])


print('newObject', newObject)
