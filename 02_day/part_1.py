CUBE_BAG = {"red": 12 , "green": 13  , "blue": 14 }


def load_text(input:str)->str:
    with open (input, "r", encoding='utf-8') as f:
        text = f.read()
        return text


def str_to_dict_v7(input_data, CUBE_BAG):
    """
    It receives a chain, builds a dictionary with the maximum valuesfor each game of each color and 
    compares that dictionary with the cube_bag dictionary. If it is less than cube_bag add the game value to the accum. 
    Returns the complete summary of all valid games.
    """
    accum = 0
    for f_line in input_data.split("\n"):
        max_value_game = {} # Empty dictionary to collect the highest value dictionary of each game
        l_first = f_line.split("Game ")[1]
        game_numb = l_first.split(": ")
        l_second = game_numb[1]
        several_plays = l_second.split("; ") 
        for play in several_plays: 
            colors = play.split(", ")
            for single_color in colors:
                color_value = single_color.split()
                if color_value[1] not in max_value_game: # Build a dictionary with the maximum values ​​of each color for each game
                    max_value_game[color_value[1]] = int(color_value[0]) # If color not in diccionary, add color
                else:
                    max_value_game[color_value[1]] = max(max_value_game[color_value[1]], int(color_value[0])) # if color in dicctionary takes max value for that color

        accum += temp_dict_vs_dict_limit (max_value_game, CUBE_BAG, game_numb[0] ) 

    return accum



def temp_dict_vs_dict_limit(max_game, cube_bag, game_number):
    """
    Compare two dictionaries and in case max_game values are lower
    to those of cube bad, add 1 to the accum
    """
    accum_s = 0
    accum_game = 0
    for key, value in max_game.items():
        if value <= CUBE_BAG[key]: # For each color, if constructed dictionary value, less than or equal to dictionary cube_bag, add 1 to accum_game.
            accum_game = accum_game + 1
        else:
            break

    if accum_game == len(max_game): # Condition to avoid errors due to temporary dictionaries with less than 3 colors
        accum_s = int(game_number) # Example: game_number = 55 if "Game 55: 15 red, 1 blue, 6 green; 11 blue, 3 red; 9 blue, 3 red, 1 green"

    return accum_s




if __name__ == "__main__":

    games = load_text("games.txt")

    print(str_to_dict_v7(games, CUBE_BAG))

