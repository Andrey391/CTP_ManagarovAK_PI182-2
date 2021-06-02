l1, r1, l2, r2 = map(int,input().split())
for s in range(11,22) :
    if l1 + l2 <= s <= l1 + r2 :
        if s <= r2 :
            print(s, l1, s-l1)
        else :
            print(s, s - r2, r2)
    elif r1 + l2 <= s <= r1 + r2 :
        if s <= r2 :
            print(s, r1, s - r1)
        else :
            print(s, s - r2, r2)
    else :
        print(-1)