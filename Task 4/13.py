def merge_the_tools(string, k):
    from collections import OrderedDict
    split = [string[i:i+k] for i in range(0, len(string), k)]
    for i in split:
        print ("".join(OrderedDict.fromkeys(i)))
        
if __name__ == '__main__':
 string, k = input(), int(input())
 merge_the_tools(string, k)