print("Welcome to Raj's Grade 10 class!")
num_students = int(input("How many students want to enroll? "))
for i in range(num_students):
    name = input("Enter student name: ")
    for attempt in range(3):
        age = int(input("Enter age of " + name + ": "))
        
        if age < 10:
            print("Too young! Must be at least 10.")
        elif age > 20:
            print("Too old! Must be 20 or younger.")
        else:
            print("Yay! " + name + " is enrolled in the class. ")
            break  
    else:
        print(name + " could not enroll due to invalid age.")
