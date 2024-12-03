import re
text_file = open("data.txt", "r")
data_file = text_file.read()
text_file.close()
regex = re.compile(r"don't\(\)|mul\(.{1,3},.{1,3}\)|do\(\)")
muls = regex.findall(data_file)

num_regex = re.compile(r'\d*')
check = 0
total = 0
for i in range(len(muls)):
    current_mul = muls[i]
    if current_mul == "don't()":
        print("DONT")
        check = 1
    elif current_mul == "do()":
        print("DO")
        check = 0
    else:
        if check == 1:
            pass
        else:
            temp_nums = num_regex.findall(current_mul)
            nums = list(filter(None, temp_nums))
            total += (int(nums[0]) * int(nums[1]))
            print(total)

print(f'Total is: {total}')
