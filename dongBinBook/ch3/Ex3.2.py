n, m, k = map(int, input().split())
data = list(map(int, input().split()))
# sortedNumbs = sorted(numbs, reverse=True)
# 그냥 sort로 해도 되는 것인가 보다 
data.sort(reverse=True)
# biggets = sortedNumbs[0]
# smaller = sortedNumbs[1]
first = data[0]
print(first)
second = data[1]
print(second)

count = int(m / (k+1)) 
namugj = m % (k+1)
print(count * (first*k + second) + first * namugj )
