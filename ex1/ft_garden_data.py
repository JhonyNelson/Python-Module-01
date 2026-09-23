class Plant:
    name: str
    height: int
    age: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")
    rose = Plant()
    