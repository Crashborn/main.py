class LogicCalc :
    ''' Логика калькулятора
    Все просто... Строку разбиваем в массив, а из массива
    через стек считываем и вычисляем выражение   '''
    def __init__(self):
        super(LogicCalc, self).__init__()
        #s = input()
        #mass = self.unpack(s)
        #print(self.turn(mass))


# Парсинг строки в массив из чисел типа float и математических операций
# и скобок типа str

    def unpack(self, s):
        mass, k = [], str()
        for i in s:
            if i in '1234567890.':
                k += i
            elif i == '-':
                if k != '-':
                    mass.append(float(k))
                    k = str()
                    k += i
                mass.append('+')
            elif i in '+*/()':
                if k != '':
                    mass.append(float(k))
                    k = str()
                mass.append(i)
        if k != '-' and k != '':
            mass.append(float(k))
        return mass

# Операция вычисления выражения без скобок

    def operation(self, mass):
        while len(mass) != 1:
            mass_it = mass
            for i in range(len(mass)):
                if mass[i] == '*' or mass[i] == '/':
                    if mass[i] == '*':
                        k = mass[i - 1] * mass[i + 1]
                        mass_it[i] = k
                        del mass_it[i - 1]
                        del mass_it[i]
                        break
                    if mass[i] == '/':
                        if mass[i + 1] != 0:
                            k = mass[i - 1] / mass[i + 1]
                            mass_it[i] = k
                            del mass_it[i - 1]
                            del mass_it[i]
                        else:
                            return 'Делить на 0 нельзя!'
                        break
            for i in range(len(mass)):
                if mass[i] == '+':
                    k = mass[i - 1] + mass[i + 1]
                    mass_it[i] = k
                    del mass_it[i - 1]
                    del mass_it[i]
                    break
            mass = mass_it
        return mass[0]

# Операция вычисления со скобочной структурой

    def turn(self, mass):
        it, k = [], []
        for i in mass:
            if i != ')':
                it.append(i)
            else:
                for j in range(len(it) - 1, -1, -1):
                    if it[j] != '(':
                        k.append(it.pop(j))
                    else:
                        p = self.operation(mass=k[::-1])
                        if type(p) == str:
                            return 'Делить на 0 нельзя!'
                        del it[j]
                        it.append(p)
                        k = []
                        break
        return self.operation(it)


if __name__ == '__main__':
    i = LogicCalc()
