def count_substring(string, sub_string):
    count = 0
    while sub_string in string:
        count += 1
        i = string.index(sub_string)
        new = string[i+1:]
        string = new
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
  
