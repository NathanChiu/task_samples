result = 0
ind = 0
for i in range(2, 14+3, 3):
    result += 1
    ind = i
if ind > 13:
    result += 100
print(result)
