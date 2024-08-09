#  list is mutable and use for sequence and string are imutable also use for sequence when we return multiple values it is tuples  
fruits = ["apple" , "banana" , "orange"]
fruits.append("kiwi")
fruits.insert(0 , "mango")
fruits.remove("apple")
print(fruits)
print("pop = " , fruits.pop(2))
print(fruits)
fruits[2]= "strawebaery"
print(fruits)

# Tuples is also for sequence but it is imutable it is write in (    ) this brackets 
# use of tuples is for when we never chnage the any thing in tuple (filename , size)

# As we mentioned earlier, strings and lists are both examples of sequences. Strings are sequences of characters, and are immutable.
# Lists are sequences of elements of any data type, and are mutable. The third sequence type is the tuple. Tuples are like lists, since they can contain elements of any data type. 
# But unlike lists, tuples are immutable.They’re specified using parentheses instead of square brackets.

# You might be wondering why tuples are a thing, given how similar they are to lists. Tuples can be useful when we need to ensure that an element is in a certain position and will not change.
# Since lists are mutable, the order of the elements can be changed on us. Since the order of the elements in a tuple can't be changed, the position of the element in a tuple can have meaning. 
# A good example of this is when a function returns multiple values. In this case, what gets returned is a tuple, with the return values as elements in the tuple. The order of the returned values is important,
# and a tuple ensures that the order isn’t going to change. Storing the elements of a tuple in separate variables is called unpacking. This allows you to take multiple returned values from a function and store each value in its own variable.


def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)


# convert tuples into list 
def full_emails(people):
  result = []
  for email, name in people:
    result.append("{} <{}>".format(name, email))
  return result
print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))


winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
  print("{} - {}".format(index + 1, person))
#   this enumerate return 2 values in tuples one index of element and 2nd is element itself


# common list creation
multiples = []
for x in range(1,11):
    multiples.append(x*7)
print(multiples)    


#  by using list comprehension method 
multiples = [x*7 for x in range(1,11)]
print(multiples)    
languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)

z = [x for x in range(0,101) if x % 3 == 0]
print(z)

# Convert a list to a tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)



# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@22 A tuple with a list as an element
my_tuple = (1, 2, ['a', 'b', 'c'])
# You can't change the tuple itself
# my_tuple[0] = 3  # This would raise a TypeError

# But you can modify the mutable elements within the tuple
my_tuple[2][0] = 'x'  
print(my_tuple)  # Outputs: (1, 2, ['x', 'b', 'c'])



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ use map function

# A simple function to add 1 to a given number
def add_one(number):
    return number + 1
# A list of numbers
numbers = [1, 2, 3, 4, 5]
# Use map to apply the function to each element in the list
result = map(add_one, numbers)
# Convert the map object to a list to print the result
print(list(result))
# Outputs: [2, 3, 4, 5, 6]


##################$$$$$$$$$$$$$$$$$$ zip function

# Two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Use zip to combine the lists
combined = zip(names, ages)

print("combine" , combined)

# Convert the zip object to a list to print the result
print(list(combined))




