#  string are imuatable it means one it doesnot change at any specific index 
# while list are muatable it changes we can append more items in list at any index

# slicing
fruit = "Pineapple"
print(fruit[:4])
print(fruit[4:])

# find index of letter

pets="Cats & Dogs"
print(pets.index("&"))

# modification
message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)

def Replace_domain ( email , old_domain , new_domain ):
    if '@' + old_domain in email:
        index = email.index("@" + old_domain)
        new_mail = email[:index]
        new_mail = new_mail + "@" + new_domain
        return new_mail
    return email
   
print(Replace_domain("abc@gmail.com", "gmail.com" , "hotmail.com" ) )   

# some functions

text =  "The number of times e occurs in this string is 4"
print(text.count("e") )
print("The number of times e occurs in this string is 4".count("e"))


print("Forest".endswith("rest"))
print("Forest".isnumeric())
print("12345".isnumeric())


print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))
print("...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"]))
print("This is another example".split())



# advance string function

name = "Manny"
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))

# this curly braces is place holder for variable that are in formet function we can concatenate the interger and string at same string 

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))
# this colon is just for seperate the value of float with string 



def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print("{:>5} F | {:>10.2f} C".format(x, to_celsius(x)))
#   this >3 for adding spaces before values that will be printing


# Returns True if there are only letters in the string. If not, returns False.
print("xyzzy".isalpha())

test = "How-much-wood-would-a-woodchuck-chuck"
print(test.split("-"))

# string.replace(old, new) - Returns a new string where all occurrences of old have been replaced by new.
print(test.replace("wood", "plastic"))

# delimiter.join(list of strings) - Returns a new string with all the strings joined by the delimiter
print("-".join(test.split()))


