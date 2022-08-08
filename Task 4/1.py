# string split and join

def split_and_join(line):
    modify  =line.replace(" ","-")
    return modify
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)