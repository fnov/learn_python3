
num_d = int(input())
d = [input().lower() for _ in range(num_d)]
num_l = int(input())
l = []
for _ in range(num_d):
    l += input().lower().split()

for i in set(l):
    if d.count(i) >= 1:
        continue
    else:
        print(i)


