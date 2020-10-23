

def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) >1:
        if strs.pop(0) != strs.pop():
            return False

    return True
s = str(input("문자: "))
x = isPalindrome(s)
print(x)