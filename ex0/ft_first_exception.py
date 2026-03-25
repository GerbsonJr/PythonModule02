def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    # Valid input
    temp_str = "25"
    print(f"Input data is '{temp_str}'")
    temp = input_temperature(temp_str)
    print(f"Temperature is now {temp}°C\n")

    # Invalid input (program must not crash)
    temp_str = "abc"
    print(f"Input data is '{temp_str}'")
    try:
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
