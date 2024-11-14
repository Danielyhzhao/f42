from smart_contract.vulnerabilities import check_with_slither, contract, result


def check_reentrancy_with_slither(result_path) -> str:
    print(f"Checking for reentrancy vulnerabilities in {result_path} with Slither...")
    try:
        with open(result_path, "r", encoding="utf-8") as f:
            content = f.read()
        start_string = "Reentrancy in"
        end_string = "INFO"
        start = content.find(start_string)
        end = -1
        if start != -1:
            detection = content[start:]
            end = detection.find(end_string)
            print("Potential reentrancy vulnerability found!")
            print(detection[:end])
            return detection[:end]
        else:
            print("No reentrancy vulnerability found.")
            return "No reentrancy vulnerability found."
    except Exception as e:
        print(f"An error occurred while running Slither: {e}")


if __name__ == "__main__":
    check_with_slither(contract)
    check_reentrancy_with_slither(result)
