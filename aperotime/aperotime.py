from datetime import datetime
import random

def is_this_apero_time():
    now = datetime.now()

    if now.hour > 17 and now.minute > 30:
        return True
    else:
        return False

cocktail_list = [
        "gin tonic",
        "vodka",
        "rhum",
        "beer",
        "tequila",
        "soda",
        ]

def randomize_cocktail():
    return random.choice(cocktail_list)


if __name__ == '__main__':
    is_this_aperotime()
