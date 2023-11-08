class TwoFacedJanus:

    def __init__(self, face='future'):
        self.face = face

    def __call__(self, number):
        result_line = ''
        if self.face == 'future':  # смотрит в будущее
            for x in range(number, number + 10):
                if x != 0:
                    result_line += str(x) + " "
                else:
                    result_line += str(x) + " "
                    break
        else:  # смотрим в прошлое
            for x in range(number, number - 10, -1):
                if x != 0:
                    result_line += str(x) + " "
                else:
                    result_line += str(x) + " "
                    break

        result_line = result_line[:-1:]
        print(result_line)


tfj = TwoFacedJanus('past')
tfj(5)
