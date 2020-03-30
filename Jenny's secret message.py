name1=input('name:')
if name1 == "Johnny":
    print ("Hello, my love!")
else:
    print("Hello, " + name1 + '!')

#################################################

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)