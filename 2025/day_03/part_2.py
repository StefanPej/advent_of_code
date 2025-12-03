from aoc_utils import *

t = """987654321111111
811111111111119
234234234234278
818181911112111"""
t = t.split("\n")

inp = read_input(2025, 3)

count = 0
for line in inp:
    one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve = len(line)-12, len(line)-11, len(line)-10, len(line)-9, len(line)-8, len(line)-7, len(line)-6, len(line)-5, len(line)-4, len(line)-3, len(line)-2, len(line)-1
    
    one_ind = one
    while one > 0:
        new_one = one - 1
        if line[new_one] >= line[one_ind]:
            one_ind = new_one

        one = new_one

    two_ind = two
    while two > one_ind + 1:
        new_two = two - 1
        if line[new_two] >= line[two_ind]:
            two_ind = new_two

        two = new_two

    three_ind = three
    while three > two_ind + 1:
        new_three = three - 1
        if line[new_three] >= line[three_ind]:
            three_ind = new_three

        three = new_three

    four_ind = four
    while four > three_ind + 1:
        new_four = four - 1
        if line[new_four] >= line[four_ind]:
            four_ind = new_four

        four = new_four

    five_ind = five
    while five > four_ind + 1:
        new_five = five - 1
        if line[new_five] >= line[five_ind]:
            five_ind = new_five

        five = new_five

    six_ind = six
    while six > five_ind + 1:
        new_six = six - 1
        if line[new_six] >= line[six_ind]:
            six_ind = new_six

        six = new_six

    seven_ind = seven
    while seven > six_ind + 1:
        new_seven = seven - 1
        if line[new_seven] >= line[seven_ind]:
            seven_ind = new_seven

        seven = new_seven

    eight_ind = eight
    while eight > seven_ind + 1:
        new_eight = eight - 1
        if line[new_eight] >= line[eight_ind]:
            eight_ind = new_eight

        eight = new_eight

    nine_ind = nine
    while nine > eight_ind + 1:
        new_nine = nine - 1
        if line[new_nine] >= line[nine_ind]:
            nine_ind = new_nine

        nine = new_nine

    ten_ind = ten
    while ten > nine_ind + 1:
        new_ten = ten - 1
        if line[new_ten] >= line[ten_ind]:
            ten_ind = new_ten

        ten = new_ten

    eleven_ind = eleven
    while eleven > ten_ind + 1:
        new_eleven = eleven - 1
        if line[new_eleven] >= line[eleven_ind]:
            eleven_ind = new_eleven

        eleven = new_eleven

    twelve_ind = twelve
    while twelve > eleven_ind + 1:
        new_twelve = twelve - 1
        if line[new_twelve] >= line[twelve_ind]:
            twelve_ind = new_twelve

        twelve = new_twelve

    val = int(line[one_ind]+ line[two_ind]+ line[three_ind]+ line[four_ind]+ line[five_ind]+ line[six_ind]+ line[seven_ind]+ line[eight_ind]+ line[nine_ind]+ line[ten_ind]+ line[eleven_ind]+ line[twelve_ind])
    count += val

print(count)