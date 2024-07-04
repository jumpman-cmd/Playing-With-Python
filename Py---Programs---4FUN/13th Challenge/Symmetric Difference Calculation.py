def symmetric_difference(a, b):
    return sorted(list(a.symmetric_difference(b)))

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    m = int(data[0])
    set_a = set(map(int, data[1:m+1]))

    n = int(data[m+1])
    set_b = set(map(int, data[m+2:m+2+n]))

    result = symmetric_difference(set_a, set_b)
    
    for num in result:
        print(num)