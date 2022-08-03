#set.symmetric_difference

English_sub = int(input())
Eroll_num = set(map(int, input().split()))
French_sub = int(input())
Froll_num = set(map(int, input().split()))
sym_diff_value = Eroll_num.symmetric_difference(Froll_num)
print(len(sym_diff_value))
