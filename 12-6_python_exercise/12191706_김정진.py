'''
학번 : 12191706
이름 : 김정진
'''
from mymod import Calculator

class Upgrad_claculator(Calculator):
    def div(self, f_num, s_num):
        try:
            result = f_num/s_num
        except ZeroDivisionError as e:
            print('0으로 나눌 수 없습니다.')
        else:
            print('{} / {} = {}'.format(f_num, s_num, result))

    def pow(self, f_num, s_num):
        result = f_num ** s_num
        print('{} ** {} = {}'.format(f_num, s_num, result))
        return result

    def fac(self, num):
        result = 1
        if num > 1:
            for x in range(1, num+1):
                result *= x
        print('{}! = {}'.format(num, result))           
        return result 


class New_calculator:
    def __init__(self):
        self.save = []
        
    def add (self, f_num, s_num):
        result = f_num + s_num
        str_save = '{} + {} = {}'.format(f_num, s_num, result)
        self.save.append(str_save)
        print(str_save)
        return result

    def sub (self, f_num, s_num):
        result = f_num - s_num
        str_save = '{} - {} = {}'.format(f_num, s_num, result)
        self.save.append(str_save)
        print(str_save)
        return result

    def mul (self, f_num, s_num):
        result = f_num * s_num
        str_save = '{} * {} = {}'.format(f_num, s_num, result)
        self.save.append(str_save)
        print(str_save)
        return result

    def div (self, f_num, s_num):
        try:
            result = f_num/s_num
        except ZeroDivisionError as e:
            print('0으로 나눌 수 없습니다.')
        else:
            str_save = '{} / {} = {}'.format(f_num, s_num, result)
            self.save.append(str_save)
            print(str_save)
            return result

    def printHistory(self):
        print(self.save)


if __name__ == '__main__':
    print('-'*20)
    print('Calculator 테스트')
    a = Calculator()
    a.add(2, 5)
    a.sub(2, 5)
    a.mul(2, 5)
    a.div(2, 5)
    print('-' * 20)

    print('-' * 20)
    print('Upgrad_claculator 테스트')
    b = Upgrad_claculator()
    b.add(2, 5)
    b.sub(2, 5)
    b.mul(2, 5)
    b.div(2, 5)
    b.div(2, 0)
    b.pow(2, 5)
    b.fac(5)
    print('-' * 20)

    print('-' * 20)
    print('New_calculator 테스트 1')
    c = New_calculator()
    c.add(2, 5)
    c.sub(2, 5)
    c.mul(2, 5)
    c.div(2, 5)
    c.div(2, 0)
    c.printHistory()
    print('-' * 20)
    print('New_calculator 테스트 2')
    d = New_calculator()
    d.add(3, 5)
    d.sub(3, 5)
    d.mul(3, 5)
    d.div(3, 5)
    d.printHistory()
    print('-' * 20)
