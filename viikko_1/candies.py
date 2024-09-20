def count(a, b, c):
    max_nalle = c // a
    max_karkit = max_nalle

    for i in range(max_nalle + 1):
        jaljella = c - (a * i)
        max_suklaa = jaljella // b
        max_karkit = max(max_karkit, i + max_suklaa)
 
    return max_karkit
 
if __name__ == "__main__":
    print(count(3, 4, 11)) # 3
    print(count(5, 1, 100)) # 100
    print(count(2, 3, 1)) # 0
    print(count(2, 3, 9)) # 4