n, m = map(int, input().split())

result = 0
# min과 max를 이용하는 방법 
# for i in range(n) :
#     input_list = list(map(int, input().split()))
#     min_value = min(input_list)
#     result = max(result, min_value)

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)        