l = [0, 1, -5, 1, 19, 0, 13, 19, -24, -11]
k = set(l)
neg = 0
pos = 0
zero = 0
dup = len(l)-len(k)
for num in l:

    if num<0:
        neg += 1
    elif num>0:
        pos += 1
    else:
        zero += 1

print("Negative: ", neg)
print("Positive: ", pos)
print("Zero: ", zero)
print("Duplicates: ",dup)