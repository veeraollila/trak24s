import itertools
import string
 
def find(N):
    hash_values = {}
 
    for s in itertools.chain(string.ascii_lowercase, (''.join(p) for r in range(2, N+1) for p in itertools.product(string.ascii_lowercase, repeat=r))):
 
        h = hash(s) % N
        if h in hash_values:
            return (hash_values[h], s)
        else:
            hash_values[h] = s
            
if __name__ == "__main__":
    print(find(42)) # esim. ('abc', 'aybabtu')