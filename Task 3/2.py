# find Angle MBC

import math
AB = int(input())
BC = int(input())
tan= AB/BC
rad=math.atan(tan)
print("{}\xb0".format(int(round(math.degrees(rad)))))
