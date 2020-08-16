n = int(input())
x = list(map(int, input().split()))

#Mean
u = sum(x)/n
#Median
x.sort()
if n % 2 == 0:
    xx = (x[n//2 - 1] + x[n//2])/2
else:
    xx = (x[n//2 + 1])
#Mode
l = list(set(x))
l.sort()

#Print the answers
print("{:.1f}".format(u))
print("{:.1f}".format(xx))
print(max(l, key = x.count))
