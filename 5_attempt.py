def hello_fromBot():
    print("Bot : Hello im your bot ")
    user_name = input()
    print('Hello ' + user_name)

def save_numbers(number):
    print("This is the number " + str(number))


def mapNumbers_to_Person(person):
    print("This is the name of the person " + person )
    

#In this main we are going to use the bot functions
#main
hello_fromBot()
Save_numbers = []
Save_person = []

for i in range(0,3):
    numbers = int(input())
    save_numbers(numbers)
    Save_numbers.append(numbers)
    
    print("Give me the person name")
    person = input()
    mapNumbers_to_Person(person)
    Save_person.append(person)
    
print(Save_numbers)
print(Save_person)
# Mapping the list values
PhoneBook = dict(zip(Save_numbers,Save_person))
print(PhoneBook)


   
    
    