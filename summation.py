def summation_while(n: int) -> int:
    sum = n
    while n != 0:
        sum += n - 1
        n -= 1
    return sum

def summation_for(n: int) -> int:
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

def main():
    print("While loop:")
    print(summation_while(1))
    print(summation_while(2))
    print(summation_while(3))
    print(summation_while(4))
    print(summation_while(5))
    print("\nFor Loop:")
    print(summation_for(1))
    print(summation_for(2))
    print(summation_for(3))
    print(summation_for(4))
    print(summation_for(5))

if __name__ == "__main__":
    main()
