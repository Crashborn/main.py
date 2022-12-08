from logiccalc import *


s = input()
num, op, open_oper, close_oper = 0, 0, 0, 0
i = LogicCalc()
mass = i.unpack(s)
for el in mass:
    if type(el) == float:
        num += 1
    elif el in '+/*':
        op += 1
    elif el == '(':
        open_oper += 1
    elif el == ')':
        close_oper += 1
if num != (op + 1) or open_oper != close_oper:
    print('error')
else:
    print(str(round(i.turn(mass))))