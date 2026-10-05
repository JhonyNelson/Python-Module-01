class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float = 0.8,
    ) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self._growth_rate: float = growth_rate

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age = age

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age

    def grow(self, amount: float = 0.8) -> None:
        if amount < 0:
            print(f"{self._name}: Error, height can't be negative")
            return
        self._height = round(self._height + amount, 1)

    def age(self, days: int = 1) -> None:
        if days < 0:
            print(f"{self._name}: Error, age can't be negative")
            return
        self._age += days

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant: Plant = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    plant.show()
    print()

    plant.set_height(25.0)
    print(f"Height updated: {int(plant.get_height())}cm")
    plant.set_age(30)
    print(f"Age updated: {plant.get_age()} days")
    print()

    plant.set_height(-5.0)
    plant.set_age(-10)
    print()

    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    ft_garden_security()
