from datetime import datetime
class Tool:
    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value == "":
            raise ValueError("Неподходящий формат данных, нужна непустая строка.")
        self._name = value
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, value):
        if not isinstance(value, str) or value == "":
            raise ValueError("Неподходящий формат данных, нужна непустая строка.")
        self._description = value

    def run(self):
        return "Not implemented"
    def __str__(self):
        return (f"Tool: {self.name} - {self.description}")
    def __repr__(self):
        return (f"Tool(name={self.name!r}, description={self.description!r})")
    def __eq__(self, other):
        return self._name == other.name and self.description == other.description

class CalculatorTool(Tool):
    def __init__(self):
        super().__init__("Calculator","Складывает два числа")
    def run(self, a:float, b:float):
        return a + b

class TimeTool(Tool):
    def __init__(self):
        super().__init__("Time", "Возвращает текущее время")
    def run(self):
        return datetime.now().strftime("%H:%M:%S")

if __name__ == "__main__":
    t1 = Tool("calculator", "Складывает два числа")
    t2 = Tool("calculator", "Складывает два числа")
    t3 = Tool("time", "Возвращает текущее время")
    t1.name = ""
    print(t1._name)




