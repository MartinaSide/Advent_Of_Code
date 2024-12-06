def check_rules(rules, page):
    for rule in rules:
        if rule[0] in page:
            coordinate = page.index(rule[0])
            if rule[1] in page:
                if page.index(rule[1]) - coordinate < 1:
                    return False
        if rule[1] in page:
            coordinate = page.index(rule[1])
            if rule[0] in page:
                if page.index(rule[0]) - coordinate > 1:
                    return False
    return True


def apply_rules(rules, page):
    for rule in rules:
        if rule[0] in page:
            coordinate = page.index(rule[0])
            if rule[1] in page:
                if page.index(rule[1]) - coordinate < 1:
                    page[coordinate], page[page.index(rule[1])] = rule[1], rule[0]
        if rule[1] in page:
            coordinate = page.index(rule[1])
            if rule[0] in page:
                if page.index(rule[0]) - coordinate > 1:
                    page[coordinate], page[page.index(rule[1])] = rule[0], rule[1]
    return page


def main():
    with open("2024/Day 5/input.txt") as file:
        data = file.readlines()
    rules = []
    pages = []


    for line in data:
        if "|" in line:
            rules.append(line.strip().split("|"))
        elif "," in line:
            pages.append(line.strip().split(","))
    valid_pages = []
    invalid_pages = []
    for page in pages:
        if check_rules(rules, page):
            valid_pages.append(page)
        else:
            invalid_pages.append(page)

    print("****Part 1****")
    print(sum(int(x[len(x)//2]) for x in valid_pages))
    fixed_pages = []

    for invalid_page in invalid_pages:
        temp = invalid_page
        i = 0
        while not check_rules(rules, invalid_page) and i < 100:
            temp = apply_rules(rules, temp)
            i+=1
        fixed_pages.append(temp)
        

    print("****Part 2****")
    print(sum(int(x[len(x)//2]) for x in fixed_pages))
            

if __name__ == "__main__":
    main()
