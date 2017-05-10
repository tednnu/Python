low = 0
high = 100
ans = 50
print('Please give a number between 0 and 100!')
print('Is your secret number 50?')
print('''Enter 'h' to indicate the guess is too high.
Enter 'l' to indicate the guess is too low.
Enter 'h' to indicate I guessed correctly.''')
while True:
    ch = (raw_input('Pleas enter your choice:'))
    if ch != 'h' and ch != 'l' and ch != 'c':
        print('Please choose among h,l and c!')
    elif ch == 'l':
        low = ans
        ans = (high +ans)/2
        print('Is your number '+str(ans)+'?')
    elif ch == 'h':
        high = ans
        ans = (low + ans)/2
        print('Is your number '+str(ans)+'?')
    else:
        print('Game over.Your number is '+str(ans)+'!')
        break
