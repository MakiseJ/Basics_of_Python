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


globalV = 33
x=19
b=13
test_function(x, b)
# Pass by value
print(x, b)
test_global()
print("now globalV actually is", globalV)
some_function()