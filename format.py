age=20
name="Joey"
height=170
# different ways of format output
print("""Hi, this is {0:_^12}, I am {age}
my height is {height:.3f}""".format(name,age=age,height=height))
# format string
print(f"Hi, this is {name},I am {age}")
# the using of escape sequences
print("use \\n to new line")
print("Hi \
this is a sentence")
# raw string (ignore Escape Sequences )
print(r"use \n to new line")