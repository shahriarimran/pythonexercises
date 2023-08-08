x = input('Input the unit you would like to convert (C or F):')

if x == 'C':
    C = int(input('Input Temperature in C:'))
    F = 1.8*C + 32
    myF = ("{} C is {} in Farenheight")
    print(myF.format(C,F))
elif x=='F':
    F = int(input('Input Temperature in F:'))
    C = 5*(F+32)/9
    myC = ("{} F is {} in Celcius")
    print(myC.format(F,C)) 
else:
    print('error')