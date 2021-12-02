"""
day 1 puzzle 2
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

def compute_sum(one, two, three):
    """
    computes the sum of the three values given and
    returns it
    """
    return one + two + three

def obtain_values(filename, line_num):
    """
    gets the values for 'one', 'two', and 'three' by iterating through
    the file until the two lines before the current line_num and inputs
    the values from there until line_num as 'one', 'two', 'three'
    """
    with open(filename) as file:
        if line_num < 2:
            return 0, 0, 0
        
        count = 0
        for line in file:
            if count == line_num - 2:
                one = int(line)
            elif count == line_num - 1:
                two = int(line)
            elif count == line_num:
                three = int(line)            
            count += 1
        
    return one, two, three

def big_boi(filename):
    """
    opens file, gets the sum of the three lines that it needs to,
    computes the sum for the three lines, and then compares it 
    with the next sequence of three lines to determine if the 
    next sequence increases, and if so adds to count and returns
    count at the end
    """
    with open (filename) as file:
        count = 0
        line_count = 0
        prev_sum = 0
        for line in file:
            one, two, three = obtain_values(filename, line_count)
            line_count += 1
            if one != 0 and two != 0:
                sum = compute_sum(one, two, three)
                count += if_larger(sum, prev_sum)
                prev_sum = sum
    return count - 1


def main():
    # print(big_boi("day1small.txt"))
    print(big_boi("day1.txt"))
    
if __name__ == "__main__":
    main()