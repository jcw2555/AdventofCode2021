# day 1 puzzle 2

def if_larger(num, prev_num):
    if int(num) > int(prev_num):
        return 1
    return 0

def compute_sum(one, two, three):
    return one + two + three

def obtain_values(filename, line_num):
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
    with open (filename) as file:
        count = 0
        line_count = 0
        prev_sum = 0
        for line in file:
            one, two, three = obtain_values(filename, line_count)
            # print(one, two, three)
            line_count += 1
            if one != 0 and two != 0:
                sum = compute_sum(one, two, three)
                # print(sum)
                count += if_larger(sum, prev_sum)
                prev_sum = sum
    return count - 1


            


def main():
    # print(big_boi("day1small.txt"))
    # print(compute_sum(1, 2, 3))
    print(big_boi("day1.txt"))
    

if __name__ == "__main__":
    main()