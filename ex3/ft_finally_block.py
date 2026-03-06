class PlantError(Exception):
    pass


def water_plants(plant_list: list, water_amount: float) -> None:
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise PlantError("Cannot water none - invalid plant!")
            if water_amount <= 0:
                raise PlantError(f"Invalid water amount: {water_amount}L")
            print(f"Watering {plant}")
    except PlantError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"], 2.5)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    water_plants(["tomato", None, "carrots"], 2.5)
    print("")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
