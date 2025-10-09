
s="azyxyyzaaaa"

q=["d","a","y","x"]

hash_map = {}

for ch in s:
  if ch in hash_map:
    hash_map[ch]+=1
  else:
    hash_map[ch]=1

for ch in q:
  if ch in hash_map:
    print(hash_map[ch],end=" ")
  else:
    print(0,end=" ")