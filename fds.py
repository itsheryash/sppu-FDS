football = []
cricket = []
badminton = []
fc2 = []
cb2 = []
fb2 = []
temp = int(input("enter the number of total players"))
for i in range(temp):
    name = input("enter the name of player")
    gp = int(input("enter the names of games played by player"))
    if gp == 1:
        option = int(input("press 1: badminton\npress 2: cricket\npress 3: football\n"))

        if option == 1:
            badminton.append(name)
        elif option == 2:
            cricket.append(name)
        elif option == 3:
            football.append(name)

    else:
        for j in range(gp):
            option = int(input("press 1: badminton\npress 2: cricket\npress 3: football\n"))
            
            if option == 1 or option == 2:
                cb2.append(name)
            elif option == 2 or option == 3:
                fc2.append(name)
            elif option == 1 or option == 3:
                fb2.append(name)
    
print("player who play footbal::",football)
print("player who play cricket::",cricket)
print("player who play badminton::",badminton)

print("player who play footbal  & cricket::",fc2)
print("player who play cricket & badminton::",cb2)
print("player who play badminton & football::",fb2)

