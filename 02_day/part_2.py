

def load_text(input:str)->str:
    with open (input, "r", encoding='utf-8') as f:
        text = f.read()
        return text


def str_to_dict_v7(input_data):
    """
    It receives a chain, builds a dictionary with the maximum valuesfor each game of each color and 
    compares that dictionary with the cube_bag dictionary. If it is less than cube_bag add the game value to the accum. 
    Returns the complete summary of all valid games.
    """
    accum = 0
    for f_line in input_data.split("\n"):
        max_value_game = {} # Empty dictionary to collect the highest value dictionary of each game
        game_value = 1
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

         # Calculate the product of the values in max_value_game
        for single_color in max_value_game:
            game_value *= max_value_game[single_color]

        # Add the game_value to the accumulator
        accum += game_value

    return accum



if __name__ == "__main__":

    games = load_text("games.txt")

    print(str_to_dict_v7(games))

