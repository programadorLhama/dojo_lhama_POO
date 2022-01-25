from template.calculator_template import CalculatorTemplate

class Calculator1(CalculatorTemplate):
    def calculate_second_factor(self, arg2: int) -> float:
        num_1 = arg2 ** 2
        num_2 = (num_1 + arg2) * 2
        num_3 = num_2 / 5
        second_factor = num_3 + self._constant_1
        return second_factor

class Calculator2(CalculatorTemplate):
    def __init__(self):
        super().__init__()
        self.__constant_3 = 1.2

    def calculate_second_factor(self, arg2: int) -> float:
        num_1 = arg2 ** 3
        num_2 = (num_1 - arg2) * 2
        second_factor = num_2 + self.__constant_3
        return second_factor