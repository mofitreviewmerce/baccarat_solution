import pyautogui
import clicker


def status_check():
    # Designated pixel
    p1_x = 1850
    p1_y = 990

    pix = pyautogui.pixel(p1_x, p1_y)

    if (pix[0] == 123) and (pix[1] == 57) and (pix[2] == 158):
        status = 'Bet'
    elif (pix[0] == 250) and (pix[1] == 245) and (pix[2] == 253):
        status = 'CancelBet'
    elif (pix[0] == 79) and (pix[1] == 71) and (pix[2] == 83):
        status = 'NE_Bet'
    elif (pix[0] == 114) and (pix[1] == 94) and (pix[2] == 122):
        status = 'NE_CancelBet'
    else:
        print(pix)
        status = 'Status Error'
        clicker.status_error_handle()

    return status
