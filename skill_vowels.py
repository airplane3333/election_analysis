#python to coun the number of vowels in a input word
def count_the_vowels(str):
#input of passphrase
    passphrase = input("Please enter your passphase?")

#need to take input and count the number of times a vowel appears
#vowels should be in a list
    vowels = ["a", "e", "i", "o", "u"] 

#need a counter to store the number of time a vowel appers
    count_vowels = 0
#loop thru the passphrase to count
    for char in str:
        if char in passphrase : [vowels]
        count_vowels =+ 1

#counter should incrase by one when vowel is found


#output is the number of vowels in input
    return count_vowels