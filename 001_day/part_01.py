def load_text(book:str)->str:
    token_texto = []
    with open (book, "r", encoding='utf-8') as f:
        texto = f.read()
        token_texto = texto.split()
        return token_texto

if __name__ == "__main__":

    calibracion = load_text("calibracion.txt")

def nums_in_word(word:str)->int:
    """
    Receives a string and extracts the first and last concatenated number, returning a two-digit integer.
    """
    tow_digit_number = 0
    index = 0
    first_num = None
    last_num = None
    for index in range(len(word)):
        if word[index].isdigit() and first_num == None:
            first_num = int(word[index])
        if word[index].isdigit():
            last_num = int(word[index])
            tow_digit_number = int(str(first_num )+str(last_num))

        index = index + 1

    return tow_digit_number


def nums_in_list(mix_list):
    """
    Receives a list and iterates over it, extracting the two-digit integer from the strings using the nums_in_word function and adding them later. Returns an integer.
    """
    total = 0
    for word in mix_list:
            total = total + nums_in_word(word)
    return total

print(nums_in_list(calibracion))
