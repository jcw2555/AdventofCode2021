# day 2 puzzle 1

def get_location(filename):
    with open(filename) as file:
        horizonal = 0
        depth = 0
        for line in file:
            tokens = line.strip().split(" ")
            direction = tokens[0]
            amount = int(tokens[1])
            if direction == "forward":
                horizonal += amount
            elif direction == "down":
                depth += amount
            else:
                depth -= amount
        return horizonal * depth

def main():
    print(get_location("day2.txt"))

if __name__ == "__main__":
    main()