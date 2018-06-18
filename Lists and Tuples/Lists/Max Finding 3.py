n = int(input())
arr = map(int, input().split(' '))
print(arr)
m1 = max(arr)
m2 = -9999999999
for i in range(n):
    if arr[i] != int(m1) and arr[i] > m2:
        m2 = int(arr[i])
print(m2)

