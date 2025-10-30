strs = strs = ["eat","tea","tan","ate","nat","bat"]

hash_freq = {}

for str in strs:
  sorted_str = ''.join(sorted(str))

  if sorted_str not in hash_freq:
    hash_freq[sorted_str]=[]

  hash_freq[sorted_str].append([str])

print(list(hash_freq.values()))