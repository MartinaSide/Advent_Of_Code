import regex as re

def main():
    with open("2024/Day 3/input.txt") as file:
        data = file.readlines()
    data = [x.strip() for x in data]
    data = [x.replace("\n", "") for x in data]
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    matches = [pattern.findall(x) for x in data]
    values = []
    for match in matches:
        values+=(match)
    values = [list(map(int, x)) for x in values]
    print("****Part 1****")
    print(sum([x[0] * x[1] for x in values]))
    print("****Part 2****")
    data = "".join(data)
    pattern_new = re.compile(r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))")
    matches = re.findall(pattern_new,data)
    output = []
    for match in matches:
        temp = []
        for element in match:
            if element != "" and "mul" not in element:
                if element == "do()":
                    element = True
                elif element == "don't()":
                    element = False
                else:
                    element = int(element)
                temp.append(element)
        output.append(temp) 
    should_I_sum = True
    my_sum = 0               
    for element in output:
        if element[0] == True:
            should_I_sum = True
        elif element[0] == False:
            should_I_sum = False
        else:
            if should_I_sum:
                my_sum += element[0] * element[1]
    print(my_sum)
if __name__ == "__main__":
    main()