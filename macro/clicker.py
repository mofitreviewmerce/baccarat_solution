import pyautogui
import time
import random


# if it is 2, 200M would be minimum size
minimum_bet_size = 2

left = (55, 1000)
right = (770, 1000)
# lr_button = ()

# 100k chip after aligning to leftest using left button
leftest_first_chip = (155, 1000)
# 100M chip after aligning to rightest using right button
rightest_third_chip = (415, 1000)
# 1B chip after aligning to rightest using right button
rightest_fourth_chip = (545, 1000)
# chip_button = ()

player_side = (540, 560)
banker_side = (1400, 560)
# side_button = ()

tie_side = (960, 560)
same_prev = (1135, 1000)
double_prev = (1435, 1000)
bet = (1740, 1000)
ground = (1800, 850)


def do_click(bet_side, relative_bet_size, pre_relative_bet_size):
    if relative_bet_size == 0:
        click_button(left)
        time.sleep(random.uniform(0.5, 0.7))
        click_button(leftest_first_chip)
        time.sleep(random.uniform(0.4, 0.6))
        click_button(tie_side)
        print("Bet to: tie ", tie_side)
    else:
        if relative_bet_size == 1:
            if pre_relative_bet_size == 1:
                click_button(same_prev)
                print("Bet to: same_prev ", same_prev)
            else:
                bet_amount(minimum_bet_size, relative_bet_size, bet_side)
        else:
            if pre_relative_bet_size * 2 == relative_bet_size:
                click_button(double_prev)
                print("Bet to: double_prev ", double_prev)
            else:
                bet_amount(minimum_bet_size, relative_bet_size, bet_side)

    time.sleep(random.uniform(0.7, 0.9))
    click_button(bet)


def bet_amount(minimum_bet_size, bet_num, bet_side):
    num = minimum_bet_size * bet_num
    num_1b = num // 10
    num_100m = num % 10

    if bet_side == 'P':
        side_button = player_side
    elif bet_side == 'B':
        side_button = banker_side

    if num_1b != 0:
        click_button(right)
        time.sleep(random.uniform(0.5, 0.7))
        click_button(rightest_fourth_chip)
        time.sleep(random.uniform(0.4, 0.6))
        for i in range(num_1b):
            click_button(side_button)
            time.sleep(random.uniform(0.1, 0.15))
    if num_100m != 0:
        click_button(right)
        time.sleep(random.uniform(0.5, 0.7))
        click_button(rightest_third_chip)
        time.sleep(random.uniform(0.5, 0.7))
        for i in range(num_100m):
            click_button(side_button)
            time.sleep(random.uniform(0.1, 0.15))

    print("Bet to: ", side_button)

    return num_1b, num_100m

"""
def bet_minimum(bet_side):
    if bet_side == 'P':
        side_button = player_side
    elif bet_side == 'B':
        side_button = banker_side

    if b_num != 0:
        click_button(right)
        time.sleep(random.uniform(0.5, 0.7))
        click_button(rightest_fourth_chip)
        time.sleep(random.uniform(0.4, 0.6))
        for i in range(b_num):
            click_button(side_button)
            time.sleep(random.uniform(0.3, 0.35))
    if m_num != 0:
        click_button(right)
        time.sleep(random.uniform(0.5, 0.7))
        click_button(rightest_third_chip)
        time.sleep(random.uniform(0.5, 0.7))
        for i in range(m_num):
            click_button(side_button)
            time.sleep(random.uniform(0.3, 0.35))

    print("Bet to: side_button ", side_button)
"""


def status_error_handle():
    click_button(ground)


def click_button(button):
    pyautogui.click(x=button[0], y=button[1])
