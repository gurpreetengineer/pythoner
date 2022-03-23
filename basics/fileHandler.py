file = open('./dumdum.txt', 'r')


# print(file.read())
print("is it closed?", file.closed)
# file_writable = open('./dumdum.txt', 'w')
print("is it closed?", file.closed)

# file = open('./dumdum.txt', 'r')
print(file.read())
file.close()

print("is it closed?", file.closed)

r8 = 'write'
_this_ = ('is', 'what', 'we', 'going', 2, r8)
# file_writable.write(str(_this_))

# print(file.read())

#
# with file as openedFile:
#     read_data = openedFile.read()
#     print('read_data', read_data, openedFile, openedFile.read())


f = open('dumdumwrite.txt', 'wb+')
f2 = open('dumdumwrite.txt', 'r')

f.write(b'0123456789abcdef')

print('123', f.read())
print('123', f2.read())

# with f2 as newFile:
#     print('inside', newFile.read())

# print(f2.read(1))


f.close()
