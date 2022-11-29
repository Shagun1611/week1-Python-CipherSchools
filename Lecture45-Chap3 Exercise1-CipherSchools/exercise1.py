winning_number=50
guessed_number=int(input())
if winning_number==guessed_number:
    print("YOU WIN !!!")
elif guessed_number>winning_number:
    print("too high")
elif  guessed_number<winning_number:
    print("too low")
