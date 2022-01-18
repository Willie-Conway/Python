# Willie Conway
# Introduction to Python
# This is program that showcases how to use a local
# variable and global variable in Python

x = "Python" # Global variable

def myfunc(): # defines function myfunc
    x = "Programming" # local variable
    print("I Love " + x) # prints and concatenates  local variable to string

myfunc() # ends myfunc function

print("I Love " + x) # prints and concatenates local variable to string
