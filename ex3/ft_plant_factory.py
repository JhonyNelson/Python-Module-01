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


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")

    plants: list[Plant] = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]

    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
