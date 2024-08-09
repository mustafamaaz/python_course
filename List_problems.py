filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.


new_filenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        new_filenames.append( filename[:-3] + "h")
    else:
        new_filenames.append(filename)


print(new_filenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]



#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
new_filenames = [  x[:-3] + "h" if x.endswith("hpp") else x  for x in filenames ]  # Start your code here


print(new_filenames) 
# Should print ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]






def pig_latin(text):
  say = " "
  # Separate the text into words
  words = text.split(" ")
  print(words)
  for word in words:
    # Create the pig latin word and add it to the list
    say =  say +  word[1:] + word[0] + "ay"+" "
  
  return say
    
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"









def biography_list(people):
    # Iterate over each "person" in the given "people" list of tuples. 
    for peoples in people:


        # Separate the 3 items in each tuple into 3 variables:
        # "name", "age", and "profession"   
        name , age , profession = peoples


        # Format the required sentence and place the 3 variables 
        # in the correct placeholders using the .format() method.
        print( "{} is {} year old and works as a {} ".format(name,age,profession))




# Call to the function:
biography_list([("Ira", 30, "a Chef"), ("Raj", 35, "a Lawyer"), ("Maria", 25, "an Engineer")])










# This function accepts two variables, each containing a list of years.
# A current "recent_first" list contains [2022, 2018, 2011, 2006].
# An older "recent_last" list contains [1989, 1992, 1997, 2001].
# The lists need to be combined with the years in chronological order.
def record_profit_years(recent_first, recent_last):

    # Reverse the order of the "recent_first" list so that it is in 
    # chronological order.
    recent_first.reverse()

    # Extend the "recent_last" list by appending the newly reversed 
    # "recent_first" list.
    recent_last.extend(recent_first)

    # Return the "recent_last", which now contains the two lists 
    # combined in chronological order. 
    return recent_last

# Assign the two lists to the two variables to be passed to the 
# record_profit_years() function.
recent_first = [2022, 2018, 2011, 2006]
recent_last = [1989, 1992, 1997, 2001]



# Call the record_profit_years() function and pass the two lists as 
# parameters. 
print(record_profit_years(recent_first, recent_last))
# Should print [1989, 1992, 1997, 2001, 2006, 2011, 2018, 2022]

