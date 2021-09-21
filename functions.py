def test_function(a,b):
    a=a+10
    b=b+10
    if(a<b):
        print(b, "wins!")
    elif(b<a):
        print(a, "wins!")
    else:
        print("draw!")


def test_global():
    global globalV
    globalV = 45
    print("now globalV is", globalV)


def some_function():

    pass


def afuncwithparam(a, b=10, c=12):
    print(f"a={a},b={b},c={c}")


def testTuple():
    a=10
    b=3
    return a,b


def testDoc():
    """This is a comment

    Try to print me:)."""
    print("Hi!")
    a=13
    """This is another comment"""


globalV = 33
x=19
b=13
test_function(x, b)
# Pass by value
print(x, b)
test_global()
print("now globalV actually is", globalV)
some_function()
afuncwithparam(33,c=32)
# afuncwithparam(12, 2, b=33) # duplicated passing is invalid
# afuncwithparam(a=12,32) # cannot use keyword before positional parameter
a,b=testTuple()
print(f"now b is {b}")
print(testDoc.__doc__)