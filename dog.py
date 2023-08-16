human_years = int(input('input dog age in human years:'))

if human_years < 0:
    print('error')
elif human_years <= 2:
    dog_years = human_years*10.5
else:
    dog_years = 21 + ((human_years-2)*4)

mdog = "A dog's age in dog years is {}"
print(mdog.format(dog_years))