string_val = "10"
int_val = int(string_val)
print(int_val)

# string_val="abc"
# int_val=int(string_val)       # value Error
# print(int_val)


float_val = 3.14
int_val = int(float_val)
print(int_val)

int_val = 10
float_val = float(int_val)
print(float_val)

string_val = "3.14"
float_val = float(string_val)
print(float_val)

# string_val = "abc"
# float_val = float(string_val)       # Value Error
# print(float_val)


int_val = 123
string_val = str(int_val)
print(string_val)

float_val = 3.14
string_val = str(float_val)
print(string_val)

list_val = [1, 2, 3, 4, 5]
string_val = str(list_val)
print(string_val)

string_val = "hello"
list_val = list(string_val)
print(list_val)

tuple_val = (1, 2, 3, 4, 5)
list_val = list(tuple_val)
print(list_val)

set_val = {1, 2, 3, 4, 5}
list_val = list(set_val)
print(list_val)

list_val = [1, 2, 3, 4, 5]
tuple_val = tuple(list_val)
print(tuple_val)

string_val = "hello"
tuple_val = tuple(string_val)
print(tuple_val)

set_val = {1, 2, 3, 4, 5}
tuple_val = tuple(set_val)
print(tuple_val)

list_val = [1, 2, 3, 4, 5]
set_val = set(list_val)
print(set_val)

string_val = "hello"
set_val = set(string_val)
print(set_val)

tuple_val = (4, 5, 6, 6)
set_val = set(tuple_val)
print(set_val)

list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
dict_val = dict(list_of_tuples)
print(dict_val)

list_of_lists = [[1, 'a'], [2, 'b'], [3, 'c']]
dict_val = dict(list_of_lists)
print(dict_val)

int_val = 0
print(bool(int_val))
int_val = 10
print(bool(int_val))
string_val = ""
print(bool(string_val))
string_val = "abc"
print(bool(string_val))
none_val = None
print(bool(none_val))
set_val = {}
print(bool(set_val))
set_val = {1, 2, 3}
print(bool(set_val))
list_val = []
print(bool(list_val))
list_val = [1, 2, 3]
print(bool(list_val))
tuple_val = ()
print(bool(tuple_val))
tuple_val = (1, 2, 3)
print(bool(tuple_val))
