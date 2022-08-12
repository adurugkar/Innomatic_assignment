# Regex Substitution

import re

regex1 = r' &&(?= )'
regex2 = r' \|\|(?= )'

n = int(input())

for i in range(n):
    line = str(input())
    matches1 = re.finditer(regex1, line)
    line = re.sub(regex1, ' and', line)
    line = re.sub(regex2, ' or', line)
    print(line)
