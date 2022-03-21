'''
this_is_a_variable = 'this is its value'

if this_is_a_variable:
    print('this exists' + this_is_a_variable)
    print('this exists', this_is_a_variable)
    print(repr('this exists, ${this_is_a_variable}'))

print('hello world dear')
'''


class C:
    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def delX(self):
        del self._x

    def thisIsAClassFunc(self):
        newVariable = list(range(4, 19, 3))
        print(newVariable)
        for i in range(10):
            # if newVariable[i]:
            #     print(newVariable[i], " =>> ", i)
            # else:
            #     print(" =>>", i)
            try:
                print(f"{newVariable[i]},  =>> , {i}")
            except IndexError:
                print('no index found')
            else:
                print(" =>>", i)
    x = property(getX, setX, delX, "I',m the _x property")


thisC = C()

thisC.setX("22")
thisC.getX()
thisC.thisIsAClassFunc()
print(thisC.x)


def fib(n):
    aList = []
    a, b = 0, 1
    while a < n:
        aList.append(a)
        # print(a, end=' ')
        a, b = b, a+b
    return aList
    # print()


def fibAtSomePosition(n):
    n -= 1
    theGoldenRatio = 1.618
    rootOfFive = 2.236

    fibAtPosition = ((theGoldenRatio ** n)
                     - (1 - theGoldenRatio) ** n) / rootOfFive
    return fibAtPosition


print(round(fibAtSomePosition(10)))
print(fib(2000))

# match case require python version 3.10 or newer
# I have 3.8.10 which is an old one
# python3 --version


# def alarm(a):
#     match a:
#     case[time, someAction]:
#         print(f'I am going to perform {someAction} in the afternoon')
#     case[time, *someActions]:
#         print(f'I am going to perform ')
#         for anAction in someActions:
#             print(anAction, end=' ')
#         print(f'at {time}')
#

# alarm(['afternoon', 'lunch'])


# def alarm2(item):
#     match item:
#         case[time, action]:
#             print(f'Good {time}! It is time to {action}!')
#         case[time, *actions]:
#             print('Good morning!')
#             for action in actions:
#                 print(f'It is time to {action}!')


def anoo(someVar, **kwargs):
    return someVar in kwargs


def addSepe(*args, separator='&&'):
    return separator.join(args)


print(addSepe("earth", "mars", "venus"))


def lambdabro(firstVal):
    return lambda secondValue: secondValue + firstVal


helperfunc = lambdabro(22)

v = helperfunc(3)
print('vvv', v)


def aNewSorter(**kwargs):
    newList = []
    newList.insort(key=lambda anArg: anArg[1])


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
aNewSorter(**pairs)
