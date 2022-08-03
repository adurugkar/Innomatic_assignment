# Nested Lists

record=[]
for i in range(int(input())):
    record.append([input(),float(input())])
highest=sorted(list(set([score for name, score in record ])))[1]
print('\n'.join([a for a, b in sorted(record) if b==highest]))
