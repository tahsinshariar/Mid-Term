N, M = map(int, input().split())
A = list(map(int, input().split()))

counts = [0] * (M + 1)

for number in A:
    counts[number] += 1

for i in range(1, M + 1):
    print(counts[i])