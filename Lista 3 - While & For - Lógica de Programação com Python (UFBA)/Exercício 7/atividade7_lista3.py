a = int(input())
p = " "

for i in range(1, a + 1):
    x = i * 2 - 1
    y = (2 * a - 1 - x) // 2  
    print(p * y + x * str(i))