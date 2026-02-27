from calendar import c

from attr import has


vowels = ['a', 'e', 'i', 'o', 'u']

# print(vowels)
# print(consonants)

hash_vowels = {}
hash_consonants = {}

string = "aeiaeia"

vowels_count = 0
consonants_count = 0

for char in range(len(string)):
    if string[char] in vowels:
        hash_vowels[string[char]] = hash_vowels.get(string[char], 0) + 1
    else:
        hash_consonants[string[char]] = hash_consonants.get(string[char], 0) + 1
    

for key in hash_vowels:
    vowels_count  = max(vowels_count, hash_vowels[key])

for key in hash_consonants:
    consonants_count = max(consonants_count,hash_consonants[key])

print(vowels_count + consonants_count)