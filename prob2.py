strings = 'dog', 'dinosaur', 'donkey', 'pterodactly', 'cat'

sorted_lengths = sorted(strings, key=lambda x: (len(x), x))
print(sorted_lengths)