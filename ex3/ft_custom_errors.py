class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def test_plant_error(plant_health: int) -> None:
    print("Testing PlantError...")
    try:
        if plant_health < 30:
            raise PlantError("The tomato plant is wilting!")
        elif plant_health < 60:
            raise PlantError("The tomato plant needs attention!")
        else:
            raise PlantError("Plant is healthy")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_water_error(water_level: int) -> None:
    print("Testing WaterError...")
    try:
        if water_level < 10:
            raise WaterError("Not enough water in the tank!")
        elif water_level < 50:
            raise WaterError("Warning: Water level is low")
        else:
            raise WaterError("Water level is adequate")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_catch_all_garden_errors(plant_health: int, water_level: int) -> None:
    print("Testing catching all garden errors...")
    try:
        if plant_health < 30:
            raise PlantError("The tomato plant is wilting!")
        elif plant_health < 60:
            raise PlantError("The tomato plant needs attention!")
        else:
            raise PlantError("Plant is healthy")
    except GardenError as e:
        print(f"Caught PlantError: {e}")
    try:
        if water_level < 10:
            raise WaterError("Not enough water in the tank!")
        elif water_level < 50:
            raise WaterError("Warning: Water level is low")
        else:
            raise WaterError("Water level is adequate")
    except GardenError as e:
        print(f"Caught WaterError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print("")
    test_plant_error(29)
    print("")
    test_water_error(9)
    print("")
    test_catch_all_garden_errors(29, 9)
    print("")
    print("All custom error types work correctly!")
