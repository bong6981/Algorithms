n, k = map(int, input().split())
count = 0
# while n != 1 :
#     if (n % k) == 0 :
#         n /= k
#         count += 1
#     else :
#         n -= 1
#         count += 1

# 시간을 줄일 수 있는 방법 
while True:
    target = (n // k) * k
    count += n - target
    n = target

    if n < k:
        break

    n //= k     
    count += 1

count += (n - 1)
print(count)