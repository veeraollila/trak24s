def find(s):
    for i in range(1, len(s) // 2 + 1): 
        if s[:i] * (len(s) // i) == s and len(s) % i == 0:
            return i  
    return len(s)  
 
if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7