text = input('Enter text: ')
text = text.upper()
dict_one = {}
for char in text:
    if char.isalpha():
        if char in dict_one:
            dict_one[char] = dict_one[char] + 1
        else:
            dict_one[char] = 1
for key, value in dict_one.items():
    print(key, '-', value)