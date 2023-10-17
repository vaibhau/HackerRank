# Solution 1

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# Solution 2

import textwrap

def wrap(string, max_width):
    paragraph = ''
    n = 0
    for i in string:
        paragraph += ''.join(i)
        n += 1
        if n == max_width:
            paragraph +='\n'
            n = 0
    return paragraph

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
