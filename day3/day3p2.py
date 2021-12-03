"""
day 3 part 2
@author Jenna Weinman
"""

def get_popular_bit_file(filename, bit_index):
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

def get_popular_bit_list(list, bit_index):
    """
    gets the most popular bit from the index specified for each
    value in a list
    """
    ones = 0
    zeros = 0
    for index in list:
        bit = int(index[bit_index])
        if bit == 0:
            zeros += 1
        elif bit == 1:
            ones += 1
    if ones >= zeros:
        return 1
    return 0

def get_least_popular_bit_list(list, bit_index):
    """
    gets the least popular bit from the index specified for each
    value in a list
    """
    ones = 0
    zeros = 0
    for index in list:
        bit = int(index[bit_index])
        if bit == 0:
            zeros += 1
        elif bit == 1:
            ones += 1
    if ones >= zeros:
        return 0
    return 1

    
def binary_to_decimal(binary_str):
    """
    Converts binary strings to decimal
    """
    return int(binary_str, 2)

def get_possible_values(filename, bit_str):
    """
    Creates a returns of all the possible lists from the 
    given bit string
    """
    possible_strings = []
    with open(filename) as file:
        for line in file:
            if line.strip()[:len(bit_str)] == bit_str:
                possible_strings.append(line.strip())
    return possible_strings

def oxygen_generator_rating(filename):
    """
    Calculates the oxygen generator rating
    """
    bit_str = ""
    bit_index = 0
    bit = get_popular_bit_file(filename, bit_index)
    bit_str += str(bit)
    bit_index += 1
    possible_values = get_possible_values(filename, bit_str)
    while len(possible_values) != 1:
        bit = get_popular_bit_list(possible_values, bit_index)
        bit_str += str(bit)
        bit_index += 1
        possible_values = get_possible_values(filename, bit_str)
    return possible_values[0]

def co2_scrubber_rating(filename):
    """
    Calculates the CO2 scrubber rating
    """
    bit_str = ""
    bit_index = 0
    bit = 0
    if get_popular_bit_file(filename, bit_index) == 0:
        bit = 1
    bit_str += str(bit)
    bit_index += 1

    possible_values = get_possible_values(filename, bit_str)
    while len(possible_values) != 1:
        bit = get_least_popular_bit_list(possible_values, bit_index)
        bit_str += str(bit)
        bit_index += 1
        possible_values = get_possible_values(filename, bit_str)
    return possible_values[0]

def life_support_rating(filename):
    """
    Determines the life support rating after converting the 
    oxygen rating and CO2 scrubber rating from binary to 
    decimal and returns it
    """
    oxygen_rating = binary_to_decimal(oxygen_generator_rating(filename))
    co2_rating = binary_to_decimal(co2_scrubber_rating(filename))
    return oxygen_rating * co2_rating

def main():
    # print(get_popular_bit("day3small.txt", 1)) 
    # print(get_gamma_binary("day3small.txt"))
    # print(get_epsilon_binary("day3small.txt"))
    # print(binary_to_decimal('10110'))
    # print(binary_to_decimal('01001'))
    # print(power_consumption("day3small.txt"))
    # print(power_consumption("day3.txt"))
    # print(get_possible_values("day3small.txt", "10111"))
    # print(oxygen_generator_rating("day3small.txt"))
    # print(co2_scrubber_rating("day3small.txt"))
    print(life_support_rating("day3.txt"))

if __name__ == "__main__":
    main()