print("Hi! Welcome to the Python Calculator!")
print("what operation do you want?")
print("options are: add, subtract, multiply, divide.")
#answer stuff
m = "m"
a = "a"
d = "d"
s = "s"
answer = input()
if answer == m:
    import multiply.py
if answer == a:
    import add.py
if answer == d:
    import divide.py
if answer == s:
    import subtract.py
