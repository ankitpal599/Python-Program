sentence = input("enter a sentence:")
count = 0
for char in sentence:
    if char in "aeiouAEIOU":
        count += 1
        print(char)
        print("no of vowels:",count) 