import pyautogui
import time

# Banker Win Anchor pixels
banker_win_pixels = [((1200, 300), (219, 28, 28)), ((1235, 300), (189, 55, 55)), ((1300, 300), (219, 28, 28)), ((1335, 300), (219, 28, 28))]
# Player Win Anchor pixels
player_win_pixels = [((555, 300), (35, 169, 255)), ((590, 300), (59, 154, 232)), ((655, 300), (35, 169, 255)), ((690, 300), (35, 169, 255))]
# Tie Anchor pixels
tie_pixels = [((920, 300), (69, 191, 49)), ((965, 300), (69, 191, 49)), ((1000, 300), (70, 176, 52))]


# 순간 화면 캡쳐 후 뱅커, 플레이어, 타이 중 하나면 각 해당되는 길이 1 문자열 리턴, 그 외 리턴하지 않음
def get_result():
    im = pyautogui.screenshot()

    temp_count = 0
    for i in banker_win_pixels:
        if not pyautogui.pixelMatchesColor(i[0][0], i[0][1], i[1], tolerance=10):
            break
        else:
            temp_count += 1
    if temp_count == len(banker_win_pixels):
        return 'B'

    temp_count = 0
    for i in player_win_pixels:
        if not pyautogui.pixelMatchesColor(i[0][0], i[0][1], i[1], tolerance=10):
            break
        else:
            temp_count += 1
    if temp_count == len(player_win_pixels):
        return 'P'

    temp_count = 0
    for i in tie_pixels:
        if not pyautogui.pixelMatchesColor(i[0][0], i[0][1], i[1], tolerance=10):
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
            print("******************")
    except KeyboardInterrupt:
        print('\n')
