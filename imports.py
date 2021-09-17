from functions import test_function
import sys
import functions
#print(format.name)
print(sys.argv)
# dot to access the imported modules
print(sys.path)
# import with from to avoid typing 'functions.' everytime
test_function(3, 2)