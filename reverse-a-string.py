def reverse_while(s: str) -> str:
    length = len(s)
    i = 1
    reverse_string = ""
    while i < length+1:
        reverse_string += s[-i]
        i += 1
    return reverse_string

def reverse_for(s: str) -> str:
    reverse_string = ""
    for i in range(len(s)):
        reverse_string = s[i] + reverse_string
    return reverse_string

def reverse_foreach(s: str) -> str:
    reverse_string = ""
    for letter in s:
        reverse_string = letter + reverse_string
    return reverse_string

def main():
    s = "hello"
    r = reverse_while(s)
    print(r)
    r = reverse_for(s)
    print(r)
    r = reverse_foreach(s)
    print(r)

if __name__ == "__main__":
    main()
