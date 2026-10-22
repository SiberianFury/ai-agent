from datetime import datetime
from typing import Any, Union
class Tool:
    def __init__(self, name: str, description: str) -> None:
        self._name: str = name
        self._description: str = description
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value == "":
            raise ValueError("Неподходящий формат данных, нужна непустая строка.")
        self._name = value
    @property
    def description(self) -> str:
        return self._description
    @description.setter
    def description(self, value):
        if not isinstance(value, str) or value == "":
            raise ValueError("Неподходящий формат данных, нужна непустая строка.")
        self._description = value

    def run(self, *args: Any, **kwargs: Any) -> Any:
        return "Not implemented"
    def __str__(self) -> str:
        return (f"Tool: {self.name} - {self.description}")
    def __repr__(self) -> str:
        return (f"Tool(name={self.name!r}, description={self.description!r})")
    def __eq__(self, other) -> bool:
        return self.name == other.name and self.description == other.description

class CalculatorTool(Tool):
    def __init__(self):
        super().__init__("Calculator","Складывает два числа")
    def run(self, a: Union[float, int], b: Union[float, int]) -> Union[float, int]:
        return a + b

class TimeTool(Tool):
    def __init__(self):
        super().__init__("Time", "Возвращает текущее время")
    def run(self) -> str:
        return datetime.now().strftime("%H:%M:%S")

class EchoTool(Tool):
    def __init__(self):
        super().__init__("echo", "Повторяет введённый текст")
    def run(self, text: str) -> str:
        return f"Эхо: {text}"
        
        

if __name__ == "__main__":

    e = EchoTool()
    print(e)
    print(e.run("привет"))




