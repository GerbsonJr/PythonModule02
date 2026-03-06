def check_temperature(temp_str: str) -> None:
    try:
        temp = int(temp_str)
        if temp >= 0 and temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!")
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        else:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test1: str = "25"
    test2: str = "abc"
    test3: str = "100"
    test4: str = "-50"
    print("")
    print(f"Testing temperature: {test1}")
    check_temperature(test1)
    print("")
    print(f"Testing temperature: {test2}")
    check_temperature(test2)
    print("")
    print(f"Testing temperature: {test3}")
    check_temperature(test3)
    print("")
    print(f"Testing temperature: {test4}")
    check_temperature(test4)
    print("")
    print("All tests completed - program didn't crash!")
