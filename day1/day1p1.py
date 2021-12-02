# day 1 puzzle 1

def if_larger(num, prev_num):
    if int(num) > int(prev_num):
        return 1
    return 0

def big_boi(filename):
    with open (filename) as file:
        count = 0
        prev_line = 0
        for line in file:
            count += if_larger(line, prev_line)
            # print(count, line)
            prev_line = line
    return count - 1


def main():
    print(big_boi("day1.txt"))
    # print(big_boi("day1small.txt"))

    

if __name__ == "__main__":
    main()