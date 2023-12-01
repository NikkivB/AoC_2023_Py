import re

def part1():
    # read input_dag1.txt as input file
    with open('input_dag1.txt', 'r') as f:
        input = f.readlines()
        input = [x.strip() for x in input]

    # get only the numbers and delete the letters
    number_array = []
    for i in range(len(input)):
        new_number = int(''.join(filter(str.isdigit, input[i])))
        new_number = str(new_number)
        temp = new_number[0]
        temp = temp + new_number[len(new_number) - 1]
        temp = int(temp)
        number_array.append(temp)

    print(sum(number_array))


def part2():
    my_dict = {"one": "1", "two": "2", "three": "3",
               "four": "4", "five": "5", "six": "6",
               "seven": "7", "eight": "8", "nine": "9"}

    with open('input_dag1.txt', 'r') as f:
        input_data = f.readlines()
        input_data = [x.strip() for x in input_data]

    new_array = []
    for line in input_data:

        temp = []
        current_index = 0

        for char in line:
            if char.isdigit():
                temp.append(char)

            else:
                for key, value in my_dict.items():
                    if key.startswith(char):
                        if key in line[current_index:current_index+len(key)]:

                            temp.append(value)

            current_index += 1
        new_array.append(temp)

    number_array = [int(num[0] + num[-1]) for num in new_array]

    print(number_array)
    print(sum(number_array))

part2()

