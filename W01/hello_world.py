import time

phrase = "Hello World"
final_phrase = ""
clock = 60 # can be increased to make the program run faster

for letter in phrase: # loop through each letter
    letter_num = ord(letter) # get the ASCII code for the letter
    for char in range(letter_num - 10, letter_num + 1): # slowly increment up to the letter
        # NOTE: ChatGPT was used to learn how to overwrite a line of text
        print(final_phrase + chr(char), end='\r', flush=True) # prints out final phrase, then adds the current character to the end
        time.sleep(1 / clock) # small delay
    final_phrase += letter # add the finished letter to the final phrase

print(final_phrase)