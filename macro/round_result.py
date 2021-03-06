import pyautogui
import time


def get_result():
    # Banker Win Anchor pixels
    banker_win_pixels = [((1200, 300), (219, 28, 28)), ((1235, 300), (189, 55, 55)), ((1300, 300), (219, 28, 28)), ((1335, 300), (219, 28, 28))]
    # Player Win Anchor pixels
    player_win_pixels = [((555, 300), (35, 169, 255)), ((590, 300), (59, 154, 232)), ((655, 300), (35, 169, 255)), ((690, 300), (35, 169, 255))]
    # Tie Anchor pixels
    tie_pixels = [((920, 300), (69, 191, 49)), ((965, 300), (69, 191, 49)), ((1000, 300), (70, 176, 52))]

    im = pyautogui.screenshot()

    temp_count = 0
    for i in banker_win_pixels:
        if im.getpixel(i[0]) != i[1]:
            break
        else:
            temp_count += 1
    if temp_count == len(banker_win_pixels):
        return 'B'

    temp_count = 0
    for i in player_win_pixels:
        if im.getpixel(i[0]) != i[1]:
            break
        else:
            temp_count += 1
    if temp_count == len(player_win_pixels):
        return 'P'

    temp_count = 0
    for i in tie_pixels:
        if im.getpixel(i[0]) != i[1]:
            break
        else:
            temp_count += 1
    if temp_count == len(tie_pixels):
        return 'T'


if __name__ == '__main__':
    try:
        while True:
            result = get_result()
            print(result)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('\n')
