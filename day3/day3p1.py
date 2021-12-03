"""
day 3 part 1
@author Jenna Weinman
"""

def get_popular_bit(filename, bit_index):
    """
    Determines the most popular bit in a column
    and returns it
    """
    with open(filename) as file:
        ones = 0
        zeros = 0
        for row in file:
            bit = int(row[bit_index])
            if bit == 0:
                zeros += 1
            elif bit == 1:
                ones += 1
        if ones > zeros:
            return 1 # if 1 is most popular
        return 0 # if 0 is most popular

def get_gamma_binary(filename):
    """
    Calculates binary string for gamma ray
    """
    binary = ""
    with open(filename) as file:
        for line in file:
            line_len = len(line)
            break
    for bit_index in range(line_len - 1):
        binary += str(get_popular_bit(filename, bit_index))
    
    return binary

def get_epsilon_binary(filename):
    """
    Calculates binary string for epsilon ray
    """
    binary = ""
    gamma_binary = str(get_gamma_binary(filename))
    for bit in gamma_binary:
        if bit == '0':
            binary += '1'
        else:
            binary += '0'
    return binary
    
def binary_to_decimal(binary_str):
    """
    Converts binary strings to decimal
    """
    return int(binary_str, 2)

def power_consumption(filename):
    """
    Gets both gamma and epsilon rates, and returns them
    multiplied together to get power consumption
    """
    gamma = binary_to_decimal(get_gamma_binary(filename))
    epsilon = binary_to_decimal(get_epsilon_binary(filename))
    return gamma * epsilon

def main():
    # print(get_popular_bit("day3small.txt", 1)) 
    # print(get_gamma_binary("day3small.txt"))
    # print(get_epsilon_binary("day3small.txt"))
    # print(binary_to_decimal('10110'))
    # print(binary_to_decimal('01001'))
    # print(power_consumption("day3small.txt"))
    print(power_consumption("day3.txt"))

if __name__ == "__main__":
    main()