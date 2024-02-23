def list_multiply_while(a: list[int], b: list[int]) -> list[int]:
    length = len(a)
    i = 0
    multiply_list = []
    while i < length:
        multiply_list.append(a[i] * b[i])
        i+=1
    return multiply_list

def list_multiply_for(a: list[int], b: list[int]) -> list[int]:
    multiply_list = []
    for i in range(len(a)):
        multiply_list.append(a[i] * b[i])
    return multiply_list


def list_multiply_foreach(a: list[int], b: list[int]) -> list[int]:
    multiply_list = []
    for ab_tuple in zip(a,b):
        multiply_list.append(ab_tuple[0]*ab_tuple[1])
    return multiply_list


def main():
    a = [1,2,3]
    b = [4,5,6]
    
    print(list_multiply_while(a,b))
    print(list_multiply_for(a,b))
    print(list_multiply_foreach(a,b))

if __name__ == "__main__":
   main()

