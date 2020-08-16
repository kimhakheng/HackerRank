n = int(input())
x = list(map(int, input().split()))
u = sum(x)/n
d = 0
for i in range(n):
    d += (x[i] - u)**2
res = (d/n)**(1/2)
print("{:.1f}".format(res))
