
import sys
import time
import random



SLEEP_ACTION = 0.2
MAX_VALUE = 100
DICE_ROLL = 6
snake = {}
ladder = {}

player_trun_message = [
    "MY TURN.",
    "LET'S GO."
]


snake_bite_message = [
    "SNAKE BITE"
    "OH NO...."
]


ladder_jump_message = [
    "BOOM"
    "YAA I GOT IT"
]


def welcome_message():
    message = """
    WELCOME TO SNAKE AND LADDER GAME.
    VERSION 1.2.3.4
    DEVELOPED BY BooKMaKeR.LTD
    """
    print(message)
def artsnake():
    global snake
    s = int(input("Enter no of snakes: "))
    for i in range(s):
        temp = list(map(int, input("head&tail: ").split()))
        snake[temp[0]] = temp[1]

def artladder():
    global ladder
    s = int(input("Enter no of ladder: "))
    for i in range(s):
        temp = list(map(int, input("top&bottom: ").split()))
        ladder[temp[0]] = temp[1]



def total_player():
    ranking = ["1","2","3","4","5","6"]
    temp = int(input("Enter no of players: "))
    if temp < 7 and temp > 1:
        return temp

    elif temp > 6:
        print("No more than six players")
    elif temp <= 0:
        print("0 players entered")
    elif temp == 1:
        print("Enter more then one player") 
welcome_message()
artsnake()
artladder()
totalPlayer = total_player()


def player_names():
    players = []
    for i in range(totalPlayer):
        player_name = input("Please enter a valid name for player: ").strip()
        players.append(player_name)
    return players




def dice_value():
    time.sleep(SLEEP_ACTION)
    dice = random.randint(1, DICE_ROLL)
    print("Its a " + str(dice))
    return dice




def snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(snake_bite_message).upper() + " ~~~~~~~~>")
    print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))


def ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump_message).upper() + " ########")
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


def snake_ladder(player_name, current_value, dice_value):
    time.sleep(SLEEP_ACTION)
    old_value = current_value
    current_value = current_value + dice_value
    if current_value > MAX_VALUE:
        print("You need " + str(MAX_VALUE - old_value) + " to win this game. Keep trying.")
        return old_value
    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snake:
        final_value = snake.get(current_value)
        snake_bite(current_value, final_value, player_name)
    elif current_value in ladder:
        final_value = ladder.get(current_value)
        ladder_jump(current_value, final_value, player_name)
    else:
        final_value = current_value
    return final_value


def player_win(player_name, position):
    time.sleep(SLEEP_ACTION)
    if MAX_VALUE == position:
        print("\n\n\nFINALLY YOU GOT IT.\n\n" + player_name + "YOU GOT THE GAME")
        print("CONGRATULATION " + player_name)
        print("n\THANK YOU FOR PLAYING THE GAME AND BEING THE PART OF BooKMaKeR")
        sys.exit(1)


def start():
    welcome_message
    time.sleep(SLEEP_ACTION)
    players = player_names()
    time.sleep(SLEEP_ACTION)        

    players_position = {}
    for name in players:
        players_position[name] = 0

    while True:
        for name in players:
            time.sleep(SLEEP_ACTION)
            input_1 = input("\n" + name + ": " + random.choice(player_trun_message) + " Hit the enter to roll dice: ")
            print("\nRolling dice...")
            dice = dice_value()
            time.sleep(SLEEP_ACTION)
            print(name + " moving....")
            players_position[name] = snake_ladder(name, players_position[name], dice)
            player_win(name,players_position[name])



if __name__ == "__main__":
    start()

