start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
f1 = int(input("What factor are the numbers divisible by?: "))
f215 = int(input("What factor are the numbers divisible by?: "))

for x in range (start, end+1):
     if x % f1 == 0 and x % f2 == 0:
        print(x)

