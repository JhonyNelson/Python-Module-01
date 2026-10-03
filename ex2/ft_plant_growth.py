class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        growth_rate: float = 0.8,
    ) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days
        self.growth_rate: float = growth_rate

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")


def main() -> None:
    plant: Plant = Plant("Rose", 25.0, 30, 0.8)
    initial_height: float = plant.height

    print("=== Garden Plant Growth ===")
    plant.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age()
        plant.show()

    growth: float = round(plant.height - initial_height, 1)
    print(f"Growth this week: {growth:.1f}cm")


if __name__ == "__main__":
    main()
