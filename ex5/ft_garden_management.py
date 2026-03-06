class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager():
    def __init__(self) -> None:
        self.plants = []
        self.water_tank = 100.0
        self.system_open = False

    def add_plant(self, name: str, water_level: float,
                  sunlight_hours: int) -> None:
        if not name:
            raise ValueError("Plant name cannot be empty!")
        if not isinstance(name, str):
            raise TypeError(
                f"Plant name must be a string, got {type(name).__name__}"
            )
        if not isinstance(water_level, (float, int)):
            raise TypeError(
                "Water level must be a number, got "
                f"{type(water_level).__name__}"
            )
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if not isinstance(sunlight_hours, int):
            raise TypeError(
                "Sunlight hours must be a number, got "
                f"{type(sunlight_hours).__name__}"
            )
        if sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        if sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )
        plant = {
            "name": name,
            "water": water_level,
            "sun": sunlight_hours
        }
        self.plants.append(plant)

    def water_plants(self) -> None:
        try:
            print("Opening watering system")
            self.system_open = True
            for plant in self.plants:
                print(f"Watering {plant['name']} - success")
        finally:
            print("Closing watering system (cleanup)")
            self.system_open = False

    def check_plant_health(self, name: str) -> str:
        plant = None
        for p in self.plants:
            if p["name"] == name:
                plant = p
                break
        if plant is None:
            raise PlantError(f"Plant '{name}' not found in garden")
        if plant["water"] < 1:
            raise ValueError(
                f"Water level {plant['water']} is too low (min 1)"
            )
        if plant["water"] > 10:
            raise ValueError(
                f"Water level {plant['water']} is too high (max 10)"
            )
        if plant["sun"] < 2:
            raise ValueError(
                f"Sunlight hours {plant['sun']} is too low (min 2)"
            )
        if plant["sun"] > 12:
            raise ValueError(
                f"Sunlight hours {plant['sun']} is too high (max 12)"
            )
        return (
            f"{name}: healthy (water: {plant['water']}, sun: {plant['sun']})"
        )


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    garden = GardenManager()
    print("\nAdding plants to garden...")
    try:
        garden.add_plant("tomato", 5, 8)
        print("Added tomato successfully")
    except (ValueError, TypeError, PlantError) as e:
        print(f"Error adding plant: {e}")
    try:
        garden.add_plant("lettuce", 3, 6)
        print("Added lettuce successfully")
    except (ValueError, TypeError, PlantError) as e:
        print(f"Error adding plant: {e}")
    try:
        garden.add_plant("", 8, 10)
        print("Added plant successfully")
    except (ValueError, TypeError, PlantError) as e:
        print(f"Error adding plant: {e}")
    print("\nWatering plants...")
    for plant in garden.plants:
        if plant["name"] == "lettuce":
            plant["water"] = 15  # ← AGORA muda para 15!
            break
    garden.water_plants()
    garden.plants.append({"name": "tomato", "water": 5, "sun": 8})
    print("\nChecking plant health...")
    try:
        result = garden.check_plant_health("tomato")
        print(result)
    except (ValueError, PlantError) as e:
        print(f"Error checking tomato: {e}")
    try:
        result = garden.check_plant_health("lettuce")
        print(result)
    except (ValueError, PlantError) as e:
        print(f"Error checking lettuce: {e}")
    print("\nTesting error recovery...")
    try:
        if garden.water_tank < 1000:
            raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
