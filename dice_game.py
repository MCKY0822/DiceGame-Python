import random
import argparse

def roll():
    results = []

    with open("log_file.txt", "a") as log_file: # "with" ensures the file is properly closed

        for attempt in range(3):
            first = random.randint(1, 6)
            second = random.randint(1, 6)
            results.append((first, second))
            
            log_file.write(f"Attempt {attempt + 1}: Roll = [{first}, {second}]\n")

            if first == 1 and second == 1:
                continue

            elif first == 6 and second == 6:
                continue

            log_file.write(f"Result: [{first}, {second}]\n\n")
            return [first, second]

        log_file.write(f"Results: [] \n\n") # return an empty list if no valid result

    return results


def main(number_of_rolls):
    for i in range(number_of_rolls):
        result = roll()
        print(f"Game {i + 1} result: {result}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dice roll")
    parser.add_argument("number_of_rolls", type=int, help="How many times should the dice roll? ")

    args = parser.parse_args()

    main(args.number_of_rolls)