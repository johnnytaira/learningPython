word = input("Gimme a word: ")
wordreverse = word[::-1]

if word == word[::-1]:
    print ("Is palindrome")
else:
    print ("Is not palindrome")