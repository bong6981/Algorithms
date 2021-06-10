n, m, k = map(int, input().split())

input_list = list(map(int, input().split()))

sorted_list = sorted(input_list, reverse=True)
result = 0
mok = m // (k+1)
namugi = m % (k+1)
result = (mok * 3 + namugi) * sorted_list[0] + mok * sorted_list[1]
print(result)