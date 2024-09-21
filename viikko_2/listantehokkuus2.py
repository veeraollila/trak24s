import time

def add_and_remove(n):
    start = time.time()
    list = []
    for i in range(1, n+1):
        list.append(i)
    add_time = time.time() - start

    start = time.time()
    for i in range(n):
        del list[0]
    delete_time = time.time() - start

    return add_time, delete_time

if __name__ == "__main__":
    n = 10**5
    add_time, delete_time = add_and_remove(n)
    print(f"Luvun lisäämiseen meni aikaa: {add_time} sekuntia.")
    print(f"Luvun poistamiseen meni aikaa: {delete_time} sekuntia.")