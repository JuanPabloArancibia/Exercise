list = [1,2,3,6,6,8,4]

# Supposed way to do it
max = max(list)
[i for i, j in enumerate(list) if j == max]

# -------------------------------------------------------
# Way of I did it
mayor = 0
index = 0

for n in range(len(list)):
    if list[n] > mayor:
        mayor = list[n]
        index = list.index(mayor)

print(index)







