# Pig latin just for a word

word = input("Give me a word and I'll translate it into pig latin: ")

# Make the string lowercase
word = word.lower()

# Check if word have only letters

if word.isalpha():

# Vowel letters

    vowel = ["a", "e", "i", "o", "u"]


# Check if word starts with vowel sounds

    if word[0] in vowel:
         latin_word = word + "way"


# Check if words starts only with a consonant

    elif word[1] in vowel:
         latin_word = word[1:-1] + word[0] + "ay"


# for words that begin with consonant clusters

    else:
        i = 0
        while word[i] not in vowel:
            i = i + 1
            latin_word = word[i:] + word[0:i] + "ay"


else:
     print("Please give me a string that has only letters... :( ")

# print the final word
print(str(latin_word))