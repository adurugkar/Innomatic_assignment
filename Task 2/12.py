# set.intersection

English_sub = int(input())
Eroll_num = set(map(int, input().split()))
French_sub = int(input())
Froll_num = set(map(int, input().split()))
intersect_value = Eroll_num.intersection(Froll_num)
print(len(intersect_value))
