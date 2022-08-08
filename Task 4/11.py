def solve(s):
   s = s.split(" ")
   return(" ".join(i.capitalize() for i in s))
    
if __name__ == '__main__':
    s = input()

    result = solve(s)
    print(result)