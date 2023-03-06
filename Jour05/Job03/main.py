def str_length(str):
    try:
        str[0]
        return 1 + str_length(str[1:])

    except IndexError:
        return 0

str = input("Entrer une chaine de caractères: ")
print("La longueur de votre chaine de caractères est: ", str_length(str))