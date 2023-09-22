word = input()
croatia_words = ["c=","c-","dz=","d-","lj","nj","s=","z="]
count = 0

for i in croatia_words:
    word = word.replace(i,"*")
print(len(word))