import sys

if __name__ == '__main__':
    # Create a result dictionary
    vowels = {}
    # Initialise the count for vowel keys to zero
    for character in 'aeiou':
        vowels[character] = 0
    # read the line in from standard input and split words
    # by spaces -> list of words
    words = sys.stdin.readline().split(' ')
    # check every character in every word
    for word in words:
        for character in word:
            if character in 'aeiou':
                vowels[character] += 1
    # TODO: using an f-string, print the character and it's frequency
    for character in 'aeiou':
        print(f"{character} : {vowels[character]}")
    
