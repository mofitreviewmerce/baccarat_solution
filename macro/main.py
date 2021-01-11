import scoreboard_loader, turn_checker, clicker, bet_calculator, chatbot, round_result
import time
import os

status = ''
prev_status = ''
game_seq = []
result = ''
result_seq = []
side_to_bet = ''
relative_bet_size = 0
pre_relative_bet_size = 0
is_result = True
just_sat_down = True
bot_name = 'C3'
minimum_bet_size = clicker.minimum_bet_size
start_asset = int(input("Current Bankroll: "))
current_asset = start_asset

try:
    while True:
        status = turn_checker.status_check()

        if status != prev_status:
            print(status)
        time.sleep(0.1)
        prev_status = status

        if status == 'Bet':
            is_result = False

            game_seq = scoreboard_loader.load()
            print(game_seq)
            if not game_seq:
                data = str(result_seq) + '\n'
                f = open("../data/log.txt", 'a')
                f.write(data)
                f.close()

            relative_bet_size, side_to_bet, streak_side, streak_number = bet_calculator.calculate_action_141020(game_seq)
            print(relative_bet_size, side_to_bet, streak_side, streak_number)
            if just_sat_down:
                if relative_bet_size <= 1:
                    just_sat_down = False
                    clicker.do_click(side_to_bet, relative_bet_size, pre_relative_bet_size)
                    message = chatbot.make_message(bot_name, relative_bet_size, side_to_bet, streak_side,
                                                   streak_number, game_seq, minimum_bet_size)
                else:
                    clicker.do_click(side_to_bet, 0, pre_relative_bet_size)
                    message = chatbot.make_message(bot_name, 0, side_to_bet, streak_side,
                                                   streak_number, game_seq, minimum_bet_size)
            else:
                clicker.do_click(side_to_bet, relative_bet_size, pre_relative_bet_size)
                message = chatbot.make_message(bot_name, relative_bet_size, side_to_bet, streak_side, streak_number,
                                               game_seq, minimum_bet_size)

            print(message)
            chatbot.send(message)

            pre_relative_bet_size = relative_bet_size
            time.sleep(1)
        elif status == 'NE_Bet' or status == 'NE_CancelBet':
            if not is_result:
                while not is_result:
                    result = round_result.get_result()
                    if result == 'B' or result == 'P' or result == 'T':
                        if side_to_bet == 'T':
                            current_asset += 0
                        elif side_to_bet == result:
                            if side_to_bet == 'B':
                                current_asset += (relative_bet_size * minimum_bet_size) * 0.95
                            else:
                                current_asset += relative_bet_size * minimum_bet_size
                        elif side_to_bet != result:
                            current_asset -= relative_bet_size * minimum_bet_size
                        result_seq.append(result)
                        print(result, round(current_asset, 2), start_asset, round((current_asset - start_asset), 2))
                        is_result = True
            else:
                pass
        else:
            pass
except KeyboardInterrupt:
    print('Start Bankroll: ', start_asset)
    print('\n')
