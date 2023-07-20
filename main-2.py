print("~tales of UMBC~")
print("(A works of ficition)")

print()

# description
print("you are a knight in the year 650CE, and you are trying to become the most famous knight of them all.")
print()
print(" you decide to go on an advemture at castle UMBC to earn glory!")

print()

# who would you help
print(" you are outside the castle grounds, and saw three diffrent peaple asking for help. could talk to: ")
print("A. The local blacksmith, who needs a rare sword")
print("B.  The town's teacher, who has a question")
print("C. The king, who has a question")
helpWho = input(" who will you talk to? please select option A- c: ")
helpWho = helpWho.capitalize()

if ( helpWho == "A"):
    # blacksmith story description
    print(" you will meet with the town blacksmith, looking for a legendary sword")
    print(" They tell you that the legend is tha the sword is frozen in ice waiting to be found")
    print(" you choose to search for it: ")
    print("A. In the desrt")
    print("B. In the forest")
    print("C. In the arctic")
    bsAct = input(" please select options A-C")
    bsAct = bsAct.capitalize()
    
    print()
    #right answer stamet
    if (bsAct == "C"):
        print("After looking long and hard through the arctic, you've found it - the legendary sword of programming!")
        print(" The blacksmith is thrilled and rewards you with a suit of armor worthy of a hero!")
        print("~ the end~")
        
        # incorrect answer statement
    else:
        print(" you searched and searched for the rest of your life, but you never founf it.")
        print(" it might've been a good idea to heed the blacksmith's advice and gog tot a cold place")
        print("~ the end~")

    print()
 # teacher's story

elif ( helpWho == "B"):
    print(" you meet with the town teacher, who is asking you a question")
    print(" 'I have to be honest with you,' they say. 'I am not really qualified to teach and am struggling with this question'")
    print(" They gesture to a math equation that reads as follows: ")
    
    print()
    print(" y = 6 + 2 + 1")
    solution = int(input(" please eneter the solution to this problem: "))
    
    print()
    check = solution == 9
    
    # correct solution statement
    if (check == True):
        print(" ' that makes perfect sense!' the teacher cries, and they award you with an honorary degree.")
        print(" you are foreever known as one of the smartest in the land")
        print("~ the end~")
        
        # incorrect solution statement
    else:
        print(" That's bad!!")

    print()
    
# king's story
else:
    print(" you meet with the king of UMBC, looking for a brave warrior")
    print(" ' i need someone to conqure a nearby fragon to save the kingdom! there is no time, head east and be ready for battle!'")
    print()
    print(" you head east and find the dragon, you ready yourself for battle. but in a twist, the dragon asks you to solve a riddle in exchenge for the kingdon.")
    print()
    print(" ' what two numbers, when added togther, equal 10?' ")
    print()
    first = int(input(" enter 1st number: "))
    second = int(input(" enter 2st number: "))
    answer = first + second
    check = answer == 10
    
    print()
    if (answer == True):
        print(f" 'AH yes, {first}, and {second}, equl 10!")
        print(" The dragon decides to leave the kingdon and the king declares you are teh greates hero in all the land!")
        print("! the end!)")
        
    

     

