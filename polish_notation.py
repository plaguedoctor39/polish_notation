import datetime as dt


class TimeContextManager:
    def __init__(self):
        self.current_time = dt.datetime.today()

    def __enter__(self):
        print('Начало работы программы -', self.current_time.strftime('%H:%M:%S'))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = dt.datetime.today()
        print('Конец работы программы -', self.end_time.strftime('%H:%M:%S'))
        self.time_worked = self.end_time - self.current_time
        print('Время работы программы -', self.time_worked)


def list_to_calc(inp):
    tmp = []
    symbols = []
    digits = []
    for item in inp:
        try:
            if item.isalpha():
                raise AssertionError
        except AssertionError:
            return 'Зачем буквы?'
        if not item.isdigit():
            try:
                if len(digits) != 0:
                    raise AssertionError
            except AssertionError:
                return 'Формат ввода сначала оператор потом операнд'
            symbols.append(item)
        else:
            digits.append(item)
    try:
        if len(symbols) == 0:
            raise AssertionError
    except AssertionError:
        return 'Вы не ввели операторов'
    try:
        if not len(digits) > 1:
            raise AssertionError
    except AssertionError:
        return 'Для операции с числами нужно минимум два положительных числа :)'
    for digit in digits:
        if len(tmp) == 0:
            tmp.append(int(digit))
        else:
            if len(symbols) != 0:
                symbol = symbols.pop()
                if symbol == '+':
                    tmp[0] += int(digit)
                elif symbol == '-':
                    tmp[0] -= int(digit)
                elif symbol == '*':
                    tmp[0] *= int(digit)
                elif symbol == '/':
                    try:
                        tmp[0] /= int(digit)
                    except ZeroDivisionError:
                        return 'На ноль делить нельзя'
    res = tmp[0]
    return res


def runner():
    with TimeContextManager():
        print('Программа ожидает на ввод сначала операторы потом операнды')
        while True:
            inp = input('Ввод - ').split()
            if inp[0] == 'e':
                break
            list_to_calc(inp)
            print(list_to_calc(inp))


runner()
