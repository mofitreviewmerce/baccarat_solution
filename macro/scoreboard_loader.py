import pyautogui


# 화면 위 스코어보드에서 픽셀 색으로 구분 후 결과 읽어옴: 결과는 플레이어, 뱅커, 타이만 계산, 페어는 계산하지 않음
def load():
    # Column pixel location
    col_pix_loc = [753, 779, 805, 830, 856, 881, 907, 932, 958, 983, 1009, 1034, 1060, 1085, 1111, 1136, 1162]
    # Row pixel location
    row_pix_loc = [11, 31, 50, 70, 89, 109]
    seq = []

    is_clean = False

    # to assure that scoreboard is clean from the notice image and the dealer image
    while not is_clean:
        im = pyautogui.screenshot()
        notice_check_pix_1 = im.getpixel((737, 3))
        notice_check_pix_2 = im.getpixel((737, 13))
        notice_check_pix_3 = im.getpixel((737, 23))
        dealer_check_pix = im.getpixel((860, 122))
        if ((notice_check_pix_1 == (162, 130, 101)) and (notice_check_pix_2 == (162, 130, 101)) and \
           (notice_check_pix_3 == (162, 130, 101)) and (dealer_check_pix == (162, 130, 101))):
            is_clean = True
        else:
            is_clean = False

    for i in range(len(col_pix_loc)):
        for j in range(len(row_pix_loc)):
            pix = im.getpixel((col_pix_loc[i], row_pix_loc[j]))

            # Blue - Player Won
            if pix == (12, 119, 207):
                seq.append('P')
            # Red - Banker Won
            elif pix == (184, 0, 0):
                seq.append('B')
            # Tie
            elif pix == (38, 132, 38):
                seq.append('T')
            # Implement this part as exception handling later
            else:
                pass

    return seq
