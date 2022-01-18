# Willie Conway
# Introduction to Programming
# This is program that identifies data types
# in Python then prints out the data type that
# is set when you assign a value to a variables

a = "Hello World" # str

print(a)

print(type(a))

b = 20 # int

print(b)

print(type(b))

c = 20.5 # float

print(c)

print(type(c))

d = 1j # complex

print(d)

print(type(d))

e = ["apple", "banana", "cherry"] # list

print(e)

print(type(e))

f = ("apple", "banana", "cherry") # tuple

print(f)

print(type(f))

g = range(6) # range

print(g)

print(type(g))

h = {"name" : "Willie", "age" : 36} # dict

print(h)

print(type(h))

n = {"apple", "banana", "cherry"} # set

print(n)

print(type(n))

i = frozenset({"apple", "banana", "cherry"}) # frozenset

print(i)

print(type(i))

j = True # bool

print(j)

print(type(j))

k = b"Hello" # bytes

print(k)

print(type(k))

l = bytearray(5) # bytearray

print(l)

print(type(l))

m = memoryview(bytes(5)) # memoryview

print(m)

print(type(m))
