import random

while True:
    print("###############################################################################################")


    def win(comp, user):

        if comp == user:
            return None
        if comp == 'r':
            if user == 'p':
                return True
            elif user == 's':
                return False

        elif comp == 'p':
            if user == 'r':
                return False
            elif user == "s":
                return True

        elif comp == 's':
            if user == 'p':
                return False

            elif user == 'r':
                return True


    print("Computer Turn : Rock(r),Paper(p),Scissors(s)")
    a = random.randint(1, 3)
    if a == 1:
        comp = 'r'
    elif a == 2:
        comp = 'p'
    elif a == 3:
        comp = 's'
    user = input("Your Turn : Rock(r) , Paper(p) , Scissors(s) ::>")

    results = win(comp, user)

    if results == None:
        print(f"Game is a Tie , Computer chose '{comp}' , You chose '{user}'")

    elif results:
        print(f"You Win , Computer Chose '{comp}'  ,You chose '{user}'")

    else:
        print(f"Computer Wins  , Computer Chose '{comp}'  ,You chose '{user}'")
