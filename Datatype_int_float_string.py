# """ 
# Date : 29.03.23
# Description : Datatype of int
# """
# print(type(4))
# print(type(2))
# print(type(768797867))
# print(type(254))

# ""
# Date : 29.03.2023
# Description : Datatype of String
# ""
# print(type('python'))
# print(type("""python"""))
# print(type('''python'''))
# print(type("python"))

# print('a'.isidentifier())
# print('_'.isidentifier())
# print('3b'.isidentifier())
# print("a b".isidentifier())

import keyword as ky
print(ky.kwlist)
# print(len(ky.kwlist))

print(ky.iskeyword("or"))
print(ky.iskeyword("""True"""))
print(ky.iskeyword('while'))
print(ky.iskeyword('''print'''))
print(ky.iskeyword("and"))

