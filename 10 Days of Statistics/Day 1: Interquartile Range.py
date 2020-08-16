n = int(input())
x = list(map(int, input().split()))
f = list(map(int, input().split()))

s =[]
for i in range(n):
    for j in range(f[i]):
        s.append(x[i])

s.sort()
n = len(s)
if n % 2 != 0:
    q1 = [s[i] for i in range(0, n//2)]
    q3 = [s[i] for i in range(n//2 +1, n)]
    len_q1 = len(q1)
    len_q3 = len(q3)
    if len_q1 % 2 == 0:
        m_q1 = (q1[len_q1//2 - 1] + q1[len_q1//2])/2
        m_q3 = (q3[len_q3//2 - 1] + q3[len_q3//2])/2
    else:
        if len_q1 % 2!= 0:
            m_q1 = q1[len_q1//2]
            m_q3 = q3[len_q3//2]
    print("{:.1f}".format(m_q3 - m_q1))
else:
    if n % 2 == 0:
        q1 = [s[i] for i in range(0, n//2)]
        q3 = [s[i] for i in range(n//2, n)]
        len_q1 = len(q1)
        len_q3 = len(q3)
        if len_q1 % 2 == 0:
            m_q1 = (q1[len_q1//2 - 1] + q1[len_q1//2])/2
            m_q3 = (q3[len_q3//2 - 1] + q3[len_q3//2])/2
        else:
            if len_q1 % 2!= 0:
                m_q1 = q1[len_q1//2]
                m_q3 = q3[len_q3//2]
        print("{:.1f}".format(m_q3 - m_q1))
