number = input() 
answer = 0
for i in range(len(number)-1, -1, -1):
    now = number[i]
    if(number[i] == 'A'):
        now = '10'
    if(number[i] == 'B'):
        now = '11'
    if(number[i] == 'C'):
        now = '12'
    if(number[i] == 'D'):
        now = '13'
    if(number[i] == 'E'):
        now = '14'
    answer += int(now) * (16 ** (len(number)-1-i))
print(answer)