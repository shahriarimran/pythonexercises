letter = input('input letter:')
letter = letter.lower()

if letter in ('a', 'e', 'i', 'o', 'u'):
    print("The letter is a vowel")
else :
    print("The letter is a consonant")