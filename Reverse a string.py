# def reverse_string(text):
#     reversed_text = text[::-1]
#     return reversed_text

# reversed_text = reverse_string("fresh")

# print(reversed_text)

#Bonus Challenge
def reverse_string(text):
    reversed_text_characters = reversed(text)
    reversed_text = "".join(reversed_text_characters)
    return reversed_text

reversed_word = reverse_string("fresh")

print(reversed_word)
