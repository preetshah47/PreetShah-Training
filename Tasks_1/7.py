# Python Program to Check Prime Number
num = int(input("Enter a Number: "))
if (num > 1):
    for i in range(2,(num//2) + 1):
        if (num % i) == 0:
            print(f"{num} is not a prime number.")
            break
        # else:
        # print(f"The {num} is a prime number")

    else:
        print(f"{num} is a prime number")
        
else:
    print(f"{num} is not a prime number.")
