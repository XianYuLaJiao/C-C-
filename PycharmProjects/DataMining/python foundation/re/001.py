import re
m = re.findall(r'\d{3},\s(\w{5}$)', 'TA(L100F_07LY) = TOL/CORTOL, YAXIS, -0.913, INTOL')[0]

print(m)