def check_plant_health(plant_name: str, water_level: float,
                       sunlight_hours: int) -> str:
    if not isinstance(plant_name, str):
        raise TypeError(
            f"Plant name must be a string,got {type(plant_name).__name__}"
        )
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if not isinstance(water_level, (int, float)):
        raise TypeError(
            f"Water level must be a number, got {type(water_level).__name__}"
        )
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if not isinstance(sunlight_hours, int):
        raise TypeError(
            "Sunlight hours must be a number, got "
            f"{type(sunlight_hours).__name__}"
        )
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)"
        )
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    plant_list = [
        ("good values", "tomato", 5, 8),
        ("empty plant name", "", 5, 8),
        ("bad water level", "tomato", 15, 8),
        ("bad sunlight hours", "tomato", 5, 0),
    ]
    for test_name, name, water, sun in plant_list:
        print(f"Testing {test_name}...")
        try:
            result = check_plant_health(name, water, sun)
            print(result)
            print("")
        except (ValueError, TypeError) as e:
            print(f"Error: {e}")
            print("")
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
