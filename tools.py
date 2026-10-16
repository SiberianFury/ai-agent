from datetime import datetime
class Tool:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    def run(self):
        return "Not implemented"
    def __str__(self):
        return (f"Tool: {self.name} - {self.description}")

class CalculatorTool(Tool):
    def __init__(self):
        super().__init__("Calculator","Складывает два числа")
    def run(self, a:float, b:float):
        return  a + b

class TimeTool(Tool):
    def __init__(self):
        super().__init__("Time", "Возвращает текущее время")
    def run(self):
        return datetime.now().strftime("%H:%M:%S")

if __name__ == "__main__":
    print(CalculatorTool().run(2, 3))



