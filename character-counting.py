def char_count_while(target: str, c: str):
    length = len(target)
    i = 0
    counter = 0
    while i < length:
        if c == target[i]:
            counter +=1
        i += 1
    return counter

def char_count_for(target: str, c: str):
    counter = 0
    for i in range(len(target)):
        if target[i] == c:
            counter += 1
    return counter

def char_count_foreach(target: str, c: str):
    counter = 0
    for letter in target:
        if letter == c:
            counter += 1
    return counter

def main():
    s = "hello"
    c = "l"
    
    num_times_c_in_s = char_count_while(s, c)
    print(num_times_c_in_s)
    num_times_c_in_s = char_count_for(s, c)
    print(num_times_c_in_s)
    num_times_c_in_s = char_count_foreach(s, c)
    print(num_times_c_in_s)

if __name__ == "__main__":
    main()
    
