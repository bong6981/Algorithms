a = list(input()) 
result = 0
hap = len(a) - 1

for i in range(len(a)) :
    if a[i] == 'A' :
        number = 10 
    elif a[i] == 'B' :
        number = 11
    elif(a[i]) == 'C' :
        number = 12
    elif(a[i]) == 'D' :
        number = 13
    elif(a[i]) == 'E' :
        number = 14
    elif(a[i]) == 'F' :
        number = 15        
    else :
        number = int(a[i]) 
    number2 = hap - i 
    result += (16 ** number2) * number

print(result)  


