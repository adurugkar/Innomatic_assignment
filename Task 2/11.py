# set.union()

# Enter your code here. Read input from STDIN. Print output to STDOUT
English_sub = int(input())
Eroll_num = set(map(int, input().split()))
French_sub = int(input())
Froll_num = set(map(int, input().split()))
union_value = Eroll_num.union(Froll_num)
print(len(union_value))
