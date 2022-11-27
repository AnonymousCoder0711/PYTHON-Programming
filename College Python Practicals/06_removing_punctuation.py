#Program for removing Punctuations from string

string = "A string, containing.. lot's of unneccessary ! punctuation'''s"
punctuation = '''!@#$%^&*()-_=+:;"'[]{}\|,.?/'''
new_string = str()
for v in string:
    if v not in punctuation:
        new_string += v

print(new_string)       