def string_validatiors(string):
    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
     print (any(method(c) for c in s))
     
if __name__ == '__main__':
    s = input()
    string_validatiors(s)