def count(s):
    not_a_counter = 0
    length = 0
 
    for char in s:
        if char != "a":
            length += 1
            not_a_counter += length
        else:
            length = 0
 
    return not_a_counter
 
 
if __name__ == "__main__":
    print(count("aaa")) # 0
    print(count("saippuakauppias")) # 23
    print(count("x")) # 1
    print(count("aybabtu")) # 9