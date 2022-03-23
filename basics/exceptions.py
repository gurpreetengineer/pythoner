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

class A(Exception):
    pass


class B(A):
    pass


class C(B):
    pass


for a_class_exception in [A, B, C]:
    try:
        print(10**10**10)
        raise a_class_exception()
    except KeyboardInterrupt:
        print('Bye fella, unable to calculate such dumb thing 10**10**10')
        print('will run 3 times because loop is executing 3 times', end='')
        print(f': {a_class_exception}.')
    except A:
        print(f'Class "AA" occurred :{a_class_exception}')
    except B:
        print('Exception is handled once in the first ((except A)) block.')
        print('Blocks after ((except A)) block will never get executed.')
        print('Class "BB" occurred')
    # except BaseException as error:
    #     print(f'A Base exception occurred: {error}')


# There are many exceptions but some of them are:
# 1) NameError
# 2) ZeroDivisionError
# 1) OSError
# 1) KeyboardInterrupt
# 1) NameError
