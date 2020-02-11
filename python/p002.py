total = 0
last, curr = 1, 2
while curr < 4000000:
    if curr % 2 == 0:
        total += curr
    last, curr = curr, last+curr
print(total)
