import pandas as pd

numbers = {
    "one": 1,
    "two": 2,
    "three": 3, 
    "four": 4, 
    "five": 5, 
    "six": 6,
    "seven": 7, 
    "eight": 8, 
    "nine": 9,
}

# print([line for line in open("./inputs/puzz2_test_input.txt")])

def get_first_num(line):
    for idx, char in enumerate(line):
        if char.isdigit():
            break

    spelled_numbers = []
    for key in numbers.keys():
        spelled_num_idx = line.find(key)
        if spelled_num_idx != -1:
            spelled_numbers.append((key, spelled_num_idx))

    if spelled_numbers != []:
        spelled_nums = pd.DataFrame(spelled_numbers, columns=["spelled_num", "idx"])
        min_word_num_idx = spelled_nums.idx.min()
    else:
        min_word_num_idx = -1

    if (idx < min_word_num_idx) & (min_word_num_idx != -1):
        return int(line[idx])
    elif (idx > min_word_num_idx) & (min_word_num_idx != -1):
        return int(numbers[spelled_nums[spelled_nums.idx == min_word_num_idx].spelled_num.values[0]])
    elif min_word_num_idx == -1:
        return int(line[idx])
    else:
        return 0


def get_last_num(line):
    digit_idx = []
    for idx, char in enumerate(line):
        if char.isdigit():
            digit_idx.append(idx)

    if digit_idx != []:
        max_digit_idx = max(digit_idx)
    else:
        max_digit_idx = 0

    spelled_numbers = []
    for key in numbers.keys():
        spelled_num_idx = line.rfind(key)
        if spelled_num_idx != -1:
            spelled_numbers.append((key, spelled_num_idx))

    if spelled_numbers != []:
        spelled_nums = pd.DataFrame(spelled_numbers, columns=["spelled_num", "idx"])
        max_word_num_idx = spelled_nums.idx.max()
    else:
        max_word_num_idx = 0

    # print(spelled_nums)
    if max_digit_idx > max_word_num_idx:
        return int(line[max_digit_idx])
    elif max_digit_idx < max_word_num_idx:
        return int(numbers[spelled_nums[spelled_nums.idx == spelled_nums.idx.max()].spelled_num.values[0]])
    else:
        return 0

if __name__ == "__main__":
    sum = 0
    # for line in open("./inputs/puzz2_test_input.txt"):
    for line in open("./inputs/puzzel2_input.txt"):
    #     print(
    #         get_first_num(line),
    #         get_last_num(line)
    #     )
        first_digit = get_first_num(line)
        last_digit = get_last_num(line)
        if first_digit == 0:
            sum = sum + (last_digit * 10) + last_digit
        elif last_digit == 0:
            sum = sum + (first_digit * 10) + first_digit
        else:
            sum = sum + (first_digit * 10) + last_digit
    print(sum)
    # print(
    #     get_first_num("jrnf3"), 
    #     # get_last_num("jrnf3")
    # )
