try:
    h1, m1 = map(int, input().split())
    if 0 <= h1 <= 23:
        raise ValueError()
    if 0 <= m1 <= 59:
        raise ValueError()
    h2, m2 = map(int, input().split())
    if 0 <= h2 <= 23:
        raise ValueError()
    if 0 <= m2 <= 59:
        raise ValueError()
except ValueError:
    print("Такого времени не сужествует")
if h1 == h2:
    if m2 <= (m1+15):
        print("Встреча состоится")
    else:
        print("встреча не состоится")
