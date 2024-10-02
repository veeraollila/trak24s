def count(s):
    total = 0
    counter = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            counter += 1
        else:
            total += counter * (counter + 1) // 2
            counter = 1
 
    total += counter * (counter + 1) // 2
 
    return total
 
if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5