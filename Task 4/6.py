#  Text Wrap

import textwrap

def wrap(string, width):
    wrapper = textwrap.TextWrapper(width=width)
    string = wrapper.fill(string)
    return (string)



if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)