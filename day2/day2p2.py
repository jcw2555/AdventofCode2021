# day 2 part 2

def get_location(filename):
    with open(filename) as file:
        aim = 0
        horizontal = 0
        depth = 0
        for line in file:
            tokens = line.strip().split(" ")
            direction = tokens[0]
            amount = int(tokens[1])
            if direction == "forward":
                horizontal += amount
                if aim != 0:
                    depth += (aim * amount)
            elif direction == "down":
                aim += amount
            else:
                aim -= amount
    return horizontal * depth

def main():
    print(get_location("day2.txt"))

if __name__ == "__main__":
    main()