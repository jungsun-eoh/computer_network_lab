
# Python basics form lectures

"""
print 
    python print will print multiple var in one statement.

print("print string", 1, 23.32)
"""

"""
variable (static and dynamic)
    python var doesn't need datatype.

s1 = "string"
v1 = f'my name is {v1}'     # f means format
v2 = "my name is {}".format(v1)     # this is useful when you create query

print(v2)

i1 = 23
print(type(i1))
"""

"""
python querry

q1 = \"""SELECT * FROM @@@\"""    # the statement will autometically recognize as query with triple quotes

q2 = \"""SELECT * FROM grades WHERE student = %s\"""      # var %s will get passed value later. 
                                                        # having var will prevent querry injection, but you have to have supporting library like pymysql to use this.
cursor.execute(q2, 918590990)                           # passing value on var %s

"""

"""
user input

name = input("Enter your name: ")
age = int(input("age: "))

if age > 30:
    print(name)
"""

"""
if statements


grade = 80
if grade < 80 and grade > 0:
    print(grade)
elif grade > 0:
    print(grade)
else:
    print(grade)

var1 = None
var2 = []
# var3 = Null  <- error
if var1:
    print("var1 has a value")
else:
    print("no value assigned.")
"""

"""
loop

for i in range(0,100):
    print(i)    # print 0 to 99

int_list = [1,2,3,4,5]
for i in range(len(int_list)):
    print(i)    # print 0 to 4

for element in range(len(int_list)):
    print(element)    # print 1 to 5
"""

"""
list

my_list = ["js"] * 5    # ['js', 'js', 'js', 'js', 'js']

my_list = [1,2,3,4,5]
print(my_list.pop(0))

my_list.append(-1)
print(my_list)

last = my_list[-1]
print(last)     # python list index get negative number. it count from backward.

print(my_list[2:4])     # index from 2 to 3. 
print(my_list[:3])     # index from 0 to 3. 
"""

"""
tuple
    tuple are imutable. <- you can't update/insert/delete value
    good on DB. <- avoid modification

data = [(1,"1",1), (2, "2", 2), (3, "3", 3)]
query = \"""INSERT INTO Student (sid, name, last_name) VALUES (%S, %S, %S)\"""
cursor.execute(query, data)

# how to modify? 
my_tuple = (1, "js", 13)
my_tuple1 = list(my_tuple)
my_tuple1[0] = 333
my_tuple = tuple(my_tuple1)
print(my_tuple) 

"""


"""
function

def get_full_name(name, lastName):
    try:
        return
    except ConnectionError as err:
        return err.args     # throw error connection
"""

