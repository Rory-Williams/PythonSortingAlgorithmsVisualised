import time

from DrawMethods import DrawInfo, draw_lst, draw
import winsound
from time import sleep

winsound_rng = [200, 600]  # lower and upper freq range for beeps
winsound_low_freq = winsound_rng[0]
winsound_freq_rng = winsound_rng[1] - winsound_rng[0]


def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst
    for i in range(len(lst)-1):
        for j in range(len(lst) - 1 - i):  # minus i so that it is optimised and the num of comparisons reduces
            num1 = lst[j]
            num2 = lst[j+1]

            # # for sounds
            # percent_height = num1 - draw_info.min_val / (draw_info.max_val - draw_info.min_val)
            # beep_freq = round(winsound_low_freq + percent_height * winsound_freq_rng / 100)
            # winsound.Beep(beep_freq, 100)

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j+1] = lst[j + 1], lst[j]  #swaps elements in array
                draw_lst(draw_info, {j: draw_info.GREEN, j+1: draw_info.RED}, True)
                yield True  #pause and hold current state of iterable loop
    return lst


def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst
    # drag elements back towards start if elements ahead are larger
    for i in range(1, len(lst)):
        num = lst[i]
        while True:
            acsend_sort = i>0 and lst[i-1] > num and ascending  # check sort and that numbers ahead are lower
            descend_sort = i>0 and lst[i-1] < num and not ascending # check sort and that numbers ahead are higher

            if not acsend_sort and not descend_sort:
                break

            # # for sounds
            # percent_height = lst[i] - draw_info.min_val / (draw_info.max_val - draw_info.min_val)
            # beep_freq = round(winsound_low_freq + percent_height * winsound_freq_rng / 100)
            # winsound.Beep(beep_freq, 200)

            lst[i] = lst[i-1]  # shift higher value element ahead of current
            i = i - 1
            lst[i] = num  # shift lower number back

            draw_lst(draw_info, {i-1:draw_info.GREEN, i:draw_info.RED}, True)
            yield True
    return lst


def selection_sort(draw_info, ascending=True):
    # finds the minimum value within a reducing array of numbers, and adds to end of sorted values
    lst = draw_info.lst
    for i in range(len(lst)):
        min_idx = i
        for j in range(i, len(lst)):
            draw_lst(draw_info, {j: draw_info.GREEN, min_idx: draw_info.RED}, True)
            if (lst[j] < lst[min_idx] and ascending) or (lst[j] > lst[min_idx] and not ascending):
                min_idx = j
            sleep(0.01)
        if i != min_idx:
            lst[min_idx], lst[i] = lst[i], lst[min_idx]
        draw_lst(draw_info, {i - 1: draw_info.GREEN, min_idx: draw_info.RED}, True)

        # # for sounds
        # percent_height = lst[i] - draw_info.min_val / (draw_info.max_val - draw_info.min_val)
        # beep_freq = round(winsound_low_freq + percent_height * winsound_freq_rng / 100)
        # winsound.Beep(beep_freq, 100)

        yield True  # pause and hold current state of iterable loop
    return lst


def merge_sort(draw_info, ascending=True, draw_info_temp=[], div=0, r_div=0, r=0, new_lst=[]):
    if type(draw_info) is not list:
        lst = draw_info.lst
        draw_info_temp = draw_info
        # yield True
    else:
        lst = draw_info
        draw_info_temp = draw_info_temp
    ascending = ascending

    if len(lst) > 1:
        # when divided list reaches single numbers, stops nesting functions
        print(f'lst: {lst}')
        div += 1
        mid_idx = len(lst)//2
        l_arr = lst[:mid_idx]  # halve lists
        r_arr = lst[mid_idx:]

        # print(f'l_arr: {l_arr}')
        # print(f'r_arr: {r_arr}')
        if r_div:
            r += 1
        # use r, r_div and div to find location of numbers being assessed in main array

        merge_sort(l_arr, ascending, draw_info_temp, div, r_div=0, r=r, new_lst=new_lst)
        merge_sort(r_arr, ascending, draw_info_temp, div, r_div=1, r=r, new_lst=new_lst)

        i = j = k = 0
        while i < len(l_arr) and j < len(r_arr):
            if (l_arr[i] <= r_arr[j] and ascending) or (l_arr[i] >= r_arr[j] and not ascending):
                # idx1 = draw_info_temp.lst.index(lst[k])
                # idx2 = draw_info_temp.lst.index(l_arr[i])
                # draw_info_temp.lst.insert(idx1, l_arr[i])
                # draw_info_temp.lst.pop(idx2+1)
                # draw_lst(draw_info_temp, {draw_info_temp.lst[idx1]: draw_info_temp.GREEN, draw_info_temp.lst[idx2]: draw_info_temp.RED}, True)
                # time.sleep(0.2)

                lst[k] = l_arr[i]
                i += 1
            else:
                # idx1 = draw_info_temp.lst.index(lst[k])
                # idx2 = draw_info_temp.lst.index(r_arr[j])
                # draw_info_temp.lst.insert(idx1, r_arr[j])
                # draw_info_temp.lst.pop(idx2 - 1)
                # draw_lst(draw_info_temp, {draw_info_temp.lst[idx1]: draw_info_temp.GREEN, draw_info_temp.lst[idx2]: draw_info_temp.RED}, True)
                # time.sleep(0.2)

                lst[k] = r_arr[j]
                j += 1
            k += 1

        while i < len(l_arr):
            # idx1 = draw_info_temp.lst.index(lst[k])
            # idx2 = draw_info_temp.lst.index(l_arr[i])
            # draw_info_temp.lst.insert(idx1, l_arr[i])
            # draw_info_temp.lst.pop(idx2 + 1)
            # draw_lst(draw_info_temp,
            #          {draw_info_temp.lst[idx1]: draw_info_temp.GREEN, draw_info_temp.lst[idx2]: draw_info_temp.RED},
            #          True)
            # time.sleep(0.2)

            lst[k] = l_arr[i]
            i += 1
            k += 1

        while j < len(r_arr):
            # idx1 = draw_info_temp.lst.index(lst[k])
            # idx2 = draw_info_temp.lst.index(r_arr[j])
            # draw_info_temp.lst.insert(idx1, r_arr[j])
            # draw_info_temp.lst.pop(idx2 - 1)
            # draw_lst(draw_info_temp,
            #          {draw_info_temp.lst[idx1]: draw_info_temp.GREEN, draw_info_temp.lst[idx2]: draw_info_temp.RED},
            #          True)
            # time.sleep(0.2)

            lst[k] = r_arr[j]
            j += 1
            k += 1
            # yield True


        print(f'i : {i}')
        print(f'j : {j}')
        print(f'k : {k}')
        print(f'ord lst: {lst}')
        # print(f'div : {div}')
        # print(f'r_div : {r_div}')
        # print(f'r : {r}')

        # draw_info_temp.lst()
        # for i in range(len(new_lst)):
        #     draw_info_temp.lst[i] = new_lst[i]
        # draw_lst(draw_info_temp, {len(lst)-j: draw_info_temp.GREEN, len(lst)-j-1: draw_info_temp.RED}, True)
        # sleep(0.2)
        print(f'temp lst: {draw_info_temp.lst}')

    return lst  # does nothing, just a return


