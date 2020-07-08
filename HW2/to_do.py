# Created by Marina Dunn on 6/20/20
# W18 Intro to Python for Data Science, UC Berkeley Summer 2020
# Homework 2

# creating an empty dictionary to start with (step 1)
dict = {}
# key for actions to have program perform (step 2)
dict["actions"] = ['get', 'add']
# key for days of the week
dict["days"] = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# key for various daily activities to be added, stores items (step 3)
dict["activities"] = {}

#print (dict.keys())
#print (dict.values())

def todo(action):
    
    if action in dict["actions"]:
        day = raw_input("What day? ")
        #print (day)
        
        if day in dict["days"]:
            # adding 'get' option (step 5)
            if action == 'get':
                print("activities: ", dict["activities"])
            # adding 'add' option (step 6)    
            elif action == 'add':
                item = raw_input("What would you like to add to " + day + "'s to-do list? ")
                if item in dict["activities"]:
                    print ("You also have to do this activity: " + dict["activities"])
                else:
                    dict.update({"activities": item})
                    print (day + ': ' + dict["activities"])
            else:
                pass
            
        else:
            print("invalid: please choose a day Monday-Sunday.")
            
    else:
        print("invalid: choose different action.")

# creating prompt to initiate to-do list (step 4)
prompt = raw_input("Would you like to view/add to your to-do list? ")
print(prompt)
if prompt == 'yes':
    while True:
        action = raw_input("What would you like to do? ")
        # adding 'quit' option (step 7)
        if action == "quit":
            break
        else:
            todo(action)
else:
    pass


