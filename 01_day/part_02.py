import json

def load_text(input:str)->str:
    token_texto = []
    with open (input, "r", encoding='utf-8') as f:
        texto = f.read()
        token_texto = texto.split()
        return token_texto

def load_dict(input):
    with open (input, "r", encoding='utf-8') as f:
        texto = f.read()
        return json.loads(texto)

if __name__ == "__main__":

    calibracion = load_text("calibracion.txt")
    numbers = load_dict("numbers.txt")


def nums_in_word_v2(word:str, num_dict)->int:
    """
    Receives a string and extracts the first and last concatenated number, returning a two-digit integer.
    """
    first_digit = None
    last_digit = None
    two_digit_number = None
    index = 0
    while index in range(len(word)):
        if first_digit == None:
            if word[index].isdigit():
                first_digit = word[index]

            else:
                for key,value in num_dict.items():
                    if key in word[index:index+len(key)]:
                        first_digit = num_dict[key]

        elif first_digit != None:
            if word[index].isdigit():
                last_digit = word[index]
            else:
                for key,value in num_dict.items():
                    if key in word[index:index+len(key)]:
                        last_digit = num_dict[key]

        index = index + 1
    
    else:
        if first_digit != None and last_digit == None:
            last_digit = first_digit
        elif first_digit == None and last_digit == None:
            first_digit = 0
            last_digit = 0

        index = index + 1
        two_digit_number = int(str(first_digit) + str(last_digit))
    

    return two_digit_number


def nums_in_list(mix_list, num_dict:dict):
    """
    Receives a list and iterates over it, extracting the two-digit integer from the strings using the nums_in_word function and adding them later. Returns an integer.
    """
    total = 0
    for word in mix_list:
            total = total + nums_in_word_v2(word, num_dict)
            print(nums_in_word_v2(word, num_dict))
    return total

print(nums_in_list(calibracion, numbers))

