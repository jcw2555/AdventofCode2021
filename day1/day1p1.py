"""
day 1 puzzle 1
@author Jenna Weinman
"""

def if_larger(num, prev_num):
    """
    determines if num is greater than previous num,
    returns 1 is True, 0 if False
    """
    if int(num) > int(prev_num):
        return 1
    return 0

def big_boi(filename):
    """
    opens file and iterates through each line checking if
    the value of the current is greater than the last
    """
    with open (filename) as file:
        count = 0
        prev_line = 0
        for line in file:
            count += if_larger(line, prev_line)
            prev_line = line
    return count - 1 # to account for the first line always being > 0


def main():
    # print(big_boi("day1small.txt"))
    print(big_boi("day1.txt"))

if __name__ == "__main__":
    main()