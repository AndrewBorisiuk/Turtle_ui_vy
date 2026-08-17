print("Which game do you want to play?")
print("1 - Tic-Tac-Toe")
print("2 - Guess the Number")

choice = input("Type 1 or 2: ")

if choice == "1":
    import cross
elif choice == "2":
    import guess
else:
    print("Oops! You must type 1 or 2.")