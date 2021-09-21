listTest=[1,   4,   3,   2,   46,   6]
print(listTest[4:2:-1])
print(listTest[2:4:-1])  # nothing
print(listTest[4:2:1])  # nothing!
print(listTest[2:9:3])
print(listTest[-1:-4:-1])

a = "hi"
b = 23
# Here is a tuple
tu = (a, b)
# you cannot modify a tuple
# so tu[0]=9 is unacceptable
print(tu)
