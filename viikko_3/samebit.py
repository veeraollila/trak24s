def count(s):
    zeros = s.count("0")
    ones = s.count("1")
 
    zero_pairs = zeros * (zeros - 1) // 2
    
    one_pairs = ones * (ones - 1) // 2
 
    return zero_pairs + one_pairs
 
if __name__ == "__main__":
    print(count("0101")) # 2
    print(count("000000")) # 15
    print(count("000111")) # 6
    print(count("00100001101100")) # 46