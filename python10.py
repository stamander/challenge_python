N, M = map(int, input().split())
passList = []
for i in range(0,N):
    tensuu, mainasu = map(int, input().split())
    total = tensuu - (5 * mainasu)
    if total >= 25:
        passList.append(i+1)