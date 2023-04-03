name = input("Type your name: ")
print("Welcome", name, "to your own adventure!")

answer = input("You have reached the end of your path, will you go left or right? ").lower()

if answer == "left":
    answer = input("You have come across an abandoned cabin. Do you choose to go in or walk around it (in/walk)? ")

    if answer == "walk":
        answer = input("You walked around the cabin and a man is standing outside with a shotgun. He tells you to get off his property. Do you run away or fight (run/fight)?")
        
        if answer == "run":
            print("You run away and spook the man. He shoots you and you have lost the game. ")
        elif answer == "fight":
            print("You decide to fight the man with a shotgun barehanded. You lose the game.")
        else:
            print("Not a vlid option. You have lost.")

    elif answer == "in":
        print("You go into the abandoned cabin. When you open the door a trap goes off and you die. You have lost the game.")
    else:
        print("Not a valid option. You have lost.") 

elif answer == "right":
    answer = input("You stumble across a woman hidden by her hoodie with a broken down car. Do you help or ignore her (help/ignore)? ")
   
    if answer == "help":
        print("You walk towards the woman and ask her what has happened. She takes off her hoodie and you are met with the most terrifying face you have ever seen. She mauls you and you have lost the game.")
    elif answer == "ignore":
        answer = input("You ignore the woman and proceed on your path. You are met with a river. Do you swim across or try to find a way around (swim/find)? ")

        if answer == "swim":
            print("You try to swim across the river. Unfortunately, you are unathletic so you run out of breath and drown. You have lost the game.")
        elif answer == "find":
            answer = input("You walk many miles to find your way around this seemingly infinite river. In the distance you see freedom and hope. Do you run or walk towards it (walk/run)? ")

            if answer == "walk":
                print("You walk towards your freedom and hope. You are gifted with a golden ticket. You have won the game, congratulations!")
            elif answer == "run":
                print("You run towards your freedom and hope. Running is not your strong suit. You twist your ankle and tumble into the river and die. You have lost the game.")
            else:
                print("Not a valid option. You have lost the game.")

    else:
        print("Not a valid option. You have lost the game.")   
    
else:
    print("Not a valid option. You have lost.") 