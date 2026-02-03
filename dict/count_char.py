s = "hello world"
def usingList():
    count = 0
    for char in s:
        if char != " ":
            count+=1
    print(count)

def char_count():
    from collections import Counter
    result = Counter(ch for ch in s if not ch.isspace())
    for k,v in result.items():
        print(f"{k}-->{v}")
if __name__ == '__main__':
    usingList()
    char_count()
