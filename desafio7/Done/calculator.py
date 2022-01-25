import math

class Calculator:

    def __init__(self) -> None:
        self.__constant_1 = 5.7
        self.__constant_2 = 4.2
    
    def calculate(self, arg1: int, arg2: int) -> float:
        first_factor = self.__calculate_first_factor(arg1)
        second_factor = self.__calculate_second_factor(arg2)
        final_value = self.__calculate_final_value(first_factor, second_factor)
        return final_value
    
    def __calculate_first_factor(self, arg1: int) -> float:
        num_1 = (arg1 * 5)/8
        num_2 = math.sqrt(num_1)
        first_factor = num_2 ** 3
        return first_factor
        
    def __calculate_second_factor(self, arg2: int) -> float:
        num_1 = arg2 ** 2
        num_2 = (num_1 + arg2)
        num_3 = (num_2 * 2) / 5
        second_factor = num_3 + self.__constant_1
        return second_factor
    
    def __calculate_final_value(self, first_factor: int, second_factor: int) -> float:
        final_value = (first_factor + second_factor) * self.__constant_2
        return final_value
