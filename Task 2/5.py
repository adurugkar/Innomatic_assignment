# Tuple

def Hash_val(n,tpl):
    print(hash(tpl))

if __name__ =="__main__":
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    Hash_val(n,integer_list)
