import random
the =random.randint(1,100)
#print(the)
guess=int(input("Please give me a number"))
guessCounter=0
while the!=guess:
    if guess>the:
        guess=int(input("Please tell me smaller number babe"))
    elif guess<the:
        guess=int(input("Babe! give me biggest number:P"))
    guessCounter+=1
print("COngrat! you found the number which is {0} in your {1}. try".format(the,guessCounter))

