n = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))

dividend = 0
divisor = 0

#find dividend
for i in range(n):
    dividend += x[i] * w[i]
#find divisor
divisor = sum(w)

#find weighted mean
mw = dividend / divisor
print("{:.1f}".format(mw))
