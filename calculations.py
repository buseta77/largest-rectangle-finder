import random


def get_random_array():
    array = []
    for _ in range(50):
        array.append(random.randint(1, 20))
    
    return array


def get_largest_chosen(heights_list, row, column):
    rectangle_data = 0
    for (i, height) in enumerate(heights_list):
        back_count, forth_count = 0, 0
        arms = 1
        if i == 0:
            for k in range(len(heights_list) - 1):
                forth_index = k + 1
                if heights_list[forth_index] >= height:
                    arms += 1
                    forth_count += 1
                else:
                    break
        elif i == len(heights_list):
            for j in range(i):
                back_index = i - 1 - j
                if heights_list[back_index] >= height:
                    arms += 1
                    back_count += 1
                else:
                    break
        else:
            for j in range(i):
                back_index = i - 1 - j
                if heights_list[back_index] >= height:
                    arms += 1
                    back_count += 1
                else:
                    break
            for k in range(len(heights_list) - i - 1):
                forth_index = i + 1 + k
                if heights_list[forth_index] >= height:
                    arms += 1
                    forth_count += 1
                else:
                    break
        rectangle = arms * height
        if rectangle > rectangle_data:
            start = i
            length = height
            back_last, forth_last = back_count, forth_count
            if start - back_last <= row and start + forth_last >= row:
                if heights_list[row] - column <= length:
                    rectangle_data = rectangle
                    startt = i
                    lengthh = height
                    back_lastt, forth_lastt = back_count, forth_count
                          
    return [rectangle_data, startt - back_lastt, startt + forth_lastt, lengthh]


def get_largest_rectangle(heights_list):
    rectangle_data = 0
    for (i, height) in enumerate(heights_list):
        back_count, forth_count = 0, 0
        arms = 1
        if i == 0:
            for k in range(len(heights_list) - 1):
                forth_index = k + 1
                if heights_list[forth_index] >= height:
                    arms += 1
                    forth_count += 1
                else:
                    break
        elif i == len(heights_list):
            for j in range(i):
                back_index = i - 1 - j
                if heights_list[back_index] >= height:
                    arms += 1
                    back_count += 1
                else:
                    break
        else:
            for j in range(i):
                back_index = i - 1 - j
                if heights_list[back_index] >= height:
                    arms += 1
                    back_count += 1
                else:
                    break
            for k in range(len(heights_list) - i - 1):
                forth_index = i + 1 + k
                if heights_list[forth_index] >= height:
                    arms += 1
                    forth_count += 1
                else:
                    break
        rectangle = arms * height
        if rectangle > rectangle_data:
            rectangle_data = rectangle
            start = i
            length = height
            back_last, forth_last = back_count, forth_count
    
    return [rectangle_data, start - back_last, start + forth_last, length]
