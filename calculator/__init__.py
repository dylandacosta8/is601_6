from typing import List
from decimal import Decimal

class Calculation:
    def __init__(self, operation: str, operands: List[Decimal], result: Decimal):
        self.operation = operation
        self.operands = operands
        self.result = result

    def __str__(self) -> str:
        return f"{self.operation.capitalize()}: {self.operands} = {self.result}"

    def get_operands(self) -> List[Decimal]:
        return self.operands

    def get_result(self) -> Decimal:
        return self.result

class Calculator:
    history: List[Calculation] = []

    def __init__(self) -> None:
        pass

    def _add_to_history(self, operation: str, operands: List[Decimal], result: Decimal) -> None:
        calc = Calculation(operation, operands, result) #TODO
        Calculator.history.append(calc) #TODO

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history

    @classmethod
    def clear_history(cls) -> None:
        cls.history.clear()

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        if cls.history:
            return cls.history[-1]
        else:
            raise IndexError("No calculations in history.")

    @classmethod
    def get_calculations_by_type(cls, operation: str) -> List[Calculation]:
        return [calc for calc in cls.history if calc.operation == operation]
