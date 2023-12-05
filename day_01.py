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
    Recibe una cadena y devuelve el primer y último numero concatenado devolviendo un entero de dos cifras.
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
    Recibe una lista e itera sobre ella extrayendo de las cadenas el entero de dos cifras mediante la funcion nums_in_word y sumandolos posteriormente. Devuelve un entero.
    """
    total = 0
    for word in mix_list:
            total = total + nums_in_word(word)
    return total

print(nums_in_list(calibracion))
