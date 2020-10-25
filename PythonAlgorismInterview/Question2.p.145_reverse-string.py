
def reverseString(s: str) -> None:
    x = list(s)
    x.reverse()
    print(x)

s = str(input("문자입력: "))
reverseString(s)


