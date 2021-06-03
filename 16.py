k = int(input())
tic = []

for _ in range(k):

    tic = input()
    if tic.startswith('a') and tic.endswith('55661'):
        tic.append(ticket)

if len(tic) == 0:
    print(-1)
else:
    print(' '.join(tic))