from collections import Counter

def count(s: str):
    return Counter(s)


s = 'aba'

print(count(s))