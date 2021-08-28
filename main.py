bits = input()
final = ''

for i in bits:
    if(i == '1'):
        final += '0'
    else:
        final += '1'

if(final[-1] == '0'):
    final = final[:-1] + '1'

else:
    temp = ''
    carry = 0
    finished = False

    for i in range(len(final)-1, -1, -1):
        if(final[i] == '0' and carry == 1 and not finished):
            temp += '1'
            carry = 0
            finished = True
        elif(final[i] == '1' and not finished):
            temp += '0'
            carry = 1
        else:
            temp += final[i]
        
    if(carry == 1):
        temp += '1'

    final = temp[::-1]



print('twos complement --> ', final)