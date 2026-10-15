class Tools:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    def run(self):
        return "Not implemented"
    def __str__(self):
        return (f"Tool: {self.name} - {self.description}")

if __name__ == "__main__":
    gaika = Tools("гайка", "её нужно закрутить")
    print(gaika)
    print(gaika.run())


