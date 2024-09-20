def count(s):
    nollia = 0
    ykkosia = 0
 
    for merkki in range(0, len(s)):
 
        if s[merkki] == "0":
            nollia += 1
 
        elif s[merkki] == "1":
            ykkosia += 1
 
    if nollia >= ykkosia:
        return ykkosia
 
    else:
        return nollia
 
if __name__ == "__main__":
    print(count("01101")) # 2
    print(count("1111")) # 0
    print(count("101111")) # 1
    print(count("00001111")) # 4