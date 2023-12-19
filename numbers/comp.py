def sumofdigits(number):
    number = str(number)
    res = 0
    for i in number:
        res += int(i)
    return  res
       
sumofdigits(333)

def ispal(num):
    reversed_number = int(str(num)[::-1])
    if reversed_number == num :
        return True
    
print(ispal(6766))    