n = int(input())
x = list(map(int, input().split()))
x.sort()

if n % 2 != 0:
    q2 = x[n//2]
    q1 = [x[i] for i in range(0, n//2)]
    q3 = [x[i] for i in range(n//2 +1, n)]
    len_q1 = len(q1)
    len_q3 = len(q3)
    if len_q1 % 2 == 0:
        m_q1 = (q1[len_q1//2 - 1] + q1[len_q1//2])/2
        m_q3 = (q3[len_q3//2 - 1] + q3[len_q3//2])/2
    else:
        if len_q1 % 2!= 0:
            m_q1 = q1[len_q1//2]
            m_q3 = q3[len_q3//2]
    print(int(m_q1))
    print(q2)
    print(int(m_q3))
else:
    if n % 2 == 0:
        q2 = (x[n//2 - 1] + x[n//2])/2
        q1 = [x[i] for i in range(0, n//2)]
        q3 = [x[i] for i in range(n//2, n)]
        len_q1 = len(q1)
        len_q3 = len(q3)
        if len_q1 % 2 == 0:
            m_q1 = (q1[len_q1//2 - 1] + q1[len_q1//2])/2
            m_q3 = (q3[len_q3//2 - 1] + q3[len_q3//2])/2
        else:
            if len_q1 % 2!= 0:
                m_q1 = q1[len_q1//2]
                m_q3 = q3[len_q3//2]
        print(int(m_q1))
        print(int(q2))
        print(int(m_q3))
