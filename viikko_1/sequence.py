def generate(n):
    nykyinen = 1
    löydetyt = 0
    
    while True:
        string_nykyinen = str(nykyinen)
        if string_nykyinen[0] == string_nykyinen[-1]:
            löydetyt += 1 
            if löydetyt == n: 
                return nykyinen
        nykyinen += 1
        
if __name__ == "__main__":
    print(generate(1)) # 1
    print(generate(2)) # 2
    print(generate(3)) # 3
    print(generate(10)) # 11
    print(generate(123)) # 1141