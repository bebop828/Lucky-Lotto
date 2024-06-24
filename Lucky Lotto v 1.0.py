
import random

def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.sample(range(1, 27), 1)[0]
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Cut-off time to play is 10pm ET night of drawings. Drawings are held Mon. Wed. & Sat. 10:59pm ET." 
    pb_add = f"Available add ons- Power Play and Double Play each for $1 extra."
    pb_offical = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_offical)


def cash_4_life():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.sample(range(1, 5), 1)[0]
    numbers_main = f"Cash 4 Life Lucky Numbers: {cash_main}, Cash Ball: {cash_ball}."
    drawings_c4l = f"Base ticket price $2. Cut-off time to play is 8:30pm ET each night. Drawings are held Nightly 9pm ET."    
    rules_c4l = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/cash4life Good Luck!"    
    return (numbers_main, drawings_c4l, rules_c4l)


def florida_mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.sample(range(1, 26), 1)[0]
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $2. Cut-off time to play is 10pm ET night of drawings. Drawings are held Tues. Fri. 11pm ET."
    mm_add = f"Available add on- Megaplier $1 extra."
    mm_rules = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/mega-millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def florida_lotto_x():
    main = sorted(random.sample(range(1, 54), 6))
    fl_lotto_main = f"Florida Lotto X with Double Play Lucky Numbers: {main}"
    fl_lotto_drawings = f"Base ticket price $2. Cut-off time to play is 10:55pm ET night of drawings. Drawings are held Wed. Sat. 11:15pm ET."
    fl_lotto_add = f"Available add ons- Double Play and EZmatch each for $1 extra."
    fl_lotto_rules = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/florida-lotto Good Luck!"    
    return (fl_lotto_main, fl_lotto_drawings, fl_lotto_add,fl_lotto_rules)


def jackpot_triple_play():
    jackpot = sorted(random.sample(range(1, 47), 6))
    jack_main = f"Jackpot Triple Play with Combo Lucky Numbers: {jackpot}"
    jack_drawings = f"Base ticket price $1. Cut-off to play is 10:55pm ET night of drawings. Drawings held Tues. Fri. 11:15pm ET."
    jack_add = f"Available add on- Combo for $1 extra."
    jack_rules = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/jackpot-triple-play Good Luck!"    
    return (jack_main, jack_drawings, jack_add, jack_rules)


def fantasy_5_mid():
    fantasy_mid = sorted(random.sample(range(1, 37), 5))    
    fantasy_main = f"Fantasy 5 Mid-Day Lucky Numbers: {fantasy_mid}"
    fantasy_drawings = f"Base ticket price $1. Cut-off time to play is 12:45pm ET afternoons.Drawings held Daily 1:05pm ET."
    fantasy_add = f"Available add on- EZmatch $1 extra."
    fantasy_rules = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/fantasy5 Good Luck!"    
    return (fantasy_main, fantasy_drawings, fantasy_add, fantasy_rules)


def fantasy_5_eve():
    fantasy_eve = sorted(random.sample(range(1, 37), 5))
    fantasy_main_eve = f"Fantasy 5 Evening Lucky Numbers: {fantasy_eve}"
    fantasy_drawings_eve = f"Base ticket price $1. Cut-off time to play is 10:55pm nightly. Drawings held Nightly 11:15pm ET."
    fantasy_add_eve = f"Available add on- EZmatch $1 extra."
    fantasy_rules_eve = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/fantasy5 Good Luck!"    
    return (fantasy_main_eve, fantasy_drawings_eve, fantasy_add_eve, fantasy_rules_eve)


def pic_2_mid():
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)
    p2_main = f"Pick 2 plus Fireball Mid-Day Lucky Numbers: {set_1, set_2}"
    p2_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Front/Back"
    p2_drawings = f"Base ticket price $.50 or $1. Cut-off time to play is 1:17pm ET daily. Mid-Day Drawings are held Daily 1:30pm ET."
    p2_fire = f"Available add on- FIREBALL $1 extra."    
    p2_rules = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/pick-2 Good Luck!"    
    return (p2_main, p2_now, p2_drawings, p2_fire, p2_rules)


def pic_2_eve():
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)
    p2_main_eve = f"Pick 2 plus Fireball Mid-Day Lucky Numbers: {set_1, set_2}"
    p2_now_eve = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Front/Back"
    p2_drawings_eve = f"Base ticket prices are $.50 or $1. Cut-off time to play is 9:32pm ET nightly. Evening Drawings are held Nightly 9:45pm ET."
    p2_fire_eve = f"Available add on- FIREBALL $1 extra."    
    p2_rules_eve = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/pick-2 Good Luck!"    
    return (p2_main_eve, p2_now_eve, p2_drawings_eve, p2_fire_eve, p2_rules_eve)


def pic_3_mid():
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)
    set_3 = random.sample(range(0, 10), 1)
    p3_main = f"Pick 3 plus Fireball Mid-Day Lucky Numbers: {set_1, set_2, set_3}"
    p3_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo"
    p3_drawings = f"Base ticket prices are $.50 or $1. Cut-off time to play is 1:19pm ET each afternoon. Mid-Day Drawings are held Daily 1:30pm ET."
    p3_fire = f"Available add on- FIREBALL $1 extra."   
    p3_rules = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/pick-3 Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_fire, p3_rules)


def pic_3_eve():
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)
    set_3 = random.sample(range(0, 10), 1)
    p3_main_eve = f"Pick 3 plus Fireball Evening Lucky Numbers: {set_1, set_2, set_3}"
    p3_now_eve = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo"
    p3_drawings_eve = f"Base ticket prices are $.50 or $1. Cut-off time to play is 9:34pm nightly. Evening Drawings are held Nightly 9:45pm ET."
    p3_fire_eve = f"Available add on- FIREBALL $1 extra."  
    p3_rules_eve = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/pick-3 Good Luck!"    
    return (p3_main_eve, p3_now_eve, p3_drawings_eve, p3_fire_eve, p3_rules_eve)


def pick_4_mid():
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)
    set_3 = random.sample(range(0, 10), 1)
    set_4 = random.sample(range(0, 10), 1)
    p4_main = f"Pick 4 plus Fireball Mid-Day Lucky Numbers: {set_1, set_2, set_3, set_4}"
    p4_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo."
    p4_drawings = f"Base ticket prices are $.50 or $1. Cut-off time to play is 1:20pm ET daily. Mid-Day Drawings held Daily 1:30pm ET."
    p4_fire_mid = f"Available add on- FIREBALL $1 extra."    
    p4_rules = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/pick-4 Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_fire_mid, p4_rules)


def pick_4_eve():
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)
    set_3 = random.sample(range(0, 10), 1)
    set_4 = random.sample(range(0, 10), 1)
    p4_main_eve = f"Pick 4 with Fireball Evening Lucky Numbers: {set_1, set_2, set_3, set_4}"
    p4_now_eve = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo."
    p4_drawings_eve = f"Base ticket prices are $.50 or $1. Cut-off time to play is 9:35pm ET nightly. Evening Drawings held Daily 9:45pm ET."
    p4_fire_eve = f"Available add on- FIREBALL $1 extra."    
    p4_rules_eve = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/pick-4 Good Luck!"    
    return (p4_main_eve, p4_now_eve, p4_drawings_eve, p4_fire_eve, p4_rules_eve)


def pick_5_mid():
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)
    set_3 = random.sample(range(0, 10), 1)
    set_4 = random.sample(range(0, 10), 1)
    set_5 = random.sample(range(0, 10), 1)
    p5_main = f"Pick 5 with Fireball Mid-Day Lucky Numbers: {set_1, set_2, set_3, set_4, set_5}"
    p5_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo."
    p5_drawings = f"Base ticket prices are $.50 or $1. Cut-off time to play is 1:18pm ET. Mid-Day Drawings held Daily 1:30pm ET."
    p5_fire_mid = f"Available add on- FIREBALL $1 extra."    
    p5_rules = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/pick-5 Good Luck!"
    return (p5_main, p5_now, p5_drawings, p5_fire_mid, p5_rules)


def pick_5_eve():
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)
    set_3 = random.sample(range(0, 10), 1)
    set_4 = random.sample(range(0, 10), 1)
    set_5 = random.sample(range(0, 10), 1)
    p5_main_eve = f"Pick 5 with Fireball Evening Lucky Numbers: {set_1, set_2, set_3, set_4, set_5}"
    p5_now_eve = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo."
    p5_drawings_eve = f"Base ticket prices are $.50 or $1. Cut-off time to play is 9:33pm ET. Evening Drawings held Daily 9:45pm ET."
    p5_fire_eve = f"Available add on- FIREBALL $1 extra."     
    p5_rules_eve = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/pick-5 Good Luck!"    
    return (p5_main_eve, p5_now_eve, p5_drawings_eve, p5_fire_eve, p5_rules_eve)


fl_lotto_draw_games = {
    1: powerball,
    2: cash_4_life,
    3: florida_mega_millions,
    4: florida_lotto_x,
    5: jackpot_triple_play,
    6: fantasy_5_mid,
    7: fantasy_5_eve,
    8: pic_2_mid,
    9: pic_2_eve,
    10: pic_3_mid,
    11: pic_3_eve,
    12: pick_4_mid, 
    13: pick_4_eve,
    14: pick_5_mid,
    15: pick_5_eve,
}

def play_game():
    print("Choose Your Florida Lotto Draw Game:")
    print("1. Powerball")
    print("2. Cash 4 Life")
    print("3. Florida Mega Millions")
    print("4. Florida Lotto X")
    print("5. Jackpot Triple Play")
    print("6. Fantasy 5 (Mid-Day)")
    print("7. Fantasy 5 (Evening)")
    print("8. Pick 2 (Mid-Day)")
    print("9. Pick 2 (Evening)")
    print("10. Pick 3 (Mid-Day)")
    print("11. Pick 3 (Evening)")
    print("12. Pick 4 (Mid-Day)")
    print("13. Pick 4 (Evening)")
    print("14. Pick 5 (Mid-Day)")
    print("15. Pick 5 (Evening)")

    while True:
        try:
            fl_lotto_game_choice = int(input("Make your selection: "))
            if fl_lotto_game_choice in fl_lotto_draw_games:
                for result in fl_lotto_draw_games[fl_lotto_game_choice]():
                    print(result)
                break  # execute the program again
            else:
                print("Not a valid option. Please try again.")
        except ValueError:  #this helped fix invalid user input
            print("Not a valid option. Please try again.")

    print("Curious if your numbers have been drawn before? Visit https://floridalottery.com/games/winning-numbers/history and look for yourself!!!")

def main():
    while True:
        play_game()
        while True:
            play_again = input("\nWould you like to try another draw game? (y/n): ").strip().lower()
            if play_again == 'y':
                break  # Exit the inner loop and play the game again
            elif play_again == 'n':
                print("Ok! Good Luck!!!")
                return  # Exit 
            else:
                print("That is not an acceptable response. Please try again.")

if __name__ == "__main__":
    main()