def capitalize_words(input_string):
    words = input_string.split()

    capitalized_words = [word.capitalize() for word in words]
                         
    capitalized_sentence = ' '.join(capitalized_words)

    return capitalized_sentence
input=input("write-")
output_string=capitalize_words(input)
print(output_string)