# Solution 1

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    print(sorted(set(arr))[-2])

# Solution 2

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = sorted(set(arr))
    print(arr[-2])
