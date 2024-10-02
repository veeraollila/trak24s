def count(s):
    count = 0
    chars = {"t": None, "i": None, "r": None, "a": None}
 
    def all_chars():
        return chars["t"] is not None and chars["i"] is not None and chars["r"] is not None and chars["a"] is not None
 
    def smallest():
        return min(chars["t"], chars["i"], chars["r"], chars["a"])
    
    for i, v in enumerate(s):
        if v in chars:
            chars[v] = i
 
        if all_chars():
            count += smallest() - (-1)
 
    return count
 
if __name__ == "__main__":
    print(count("aybabtu")) # 0
    print(count("tira")) # 1
    print(count("ritari")) # 6
    print(count("tiratiratira")) # 45
    print(count("xaxrxixtx")) # 4