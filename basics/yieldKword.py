# A Python program to generate squares from 1
# to 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1
def nextSquare():
    i = 1
    print('2222222222')

    # An Infinite loop to generate squares
    while True:
        print('3333333333')
        yield i*i
        print('++++++++++++++++')
        i += 1  # Next execution resumes
        # from this point
        print('444444444')


# Driver code
for num in nextSquare():
    print('1111111111')
    if num > 5:
        break
    print('==============>>>>>>>>', num)
