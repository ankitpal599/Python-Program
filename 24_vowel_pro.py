#Python program to take a sentence as input from the user,find & print all vowels in the sentence and count the total no of vowels using for loop. 
sentence = input("enter a sentence:")
count = 0
for char in sentence:
    if char in "aeiouAEIOU":
        count += 1
        print(char)
        print("no of vowels:",count) 
