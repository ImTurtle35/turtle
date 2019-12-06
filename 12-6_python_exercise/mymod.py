class Calculator:
    def add(self, f_num, s_num):
        result = f_num + s_num
        print('{} + {} = {}'.format(f_num, s_num, result))
        return result

    def sub(self, f_num, s_num):
        result = f_num - s_num
        print('{} - {} = {}'.format(f_num, s_num, result))
        return result

    def mul(self, f_num, s_num):
        result = f_num * s_num
        print('{} * {} = {}'.format(f_num, s_num, result))
        return result

    def div(self, f_num, s_num):
        result = f_num / s_num
        print('{} / {} = {}'.format(f_num, s_num, result))
        return result