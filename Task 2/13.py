#set.difference

English_sub = int(input())
Eroll_num = set(map(int, input().split()))
French_sub = int(input())
Froll_num = set(map(int, input().split()))
difference_value = Eroll_num.difference(Froll_num)
print(len(difference_value))
