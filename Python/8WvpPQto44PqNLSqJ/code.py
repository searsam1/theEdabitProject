
def pad(message):
    length = len(message)
    if length >= 140: return message
    if length % 2 == 0: message += " "
    c = 'l'
    while length < 140:
        message += c
        c = ["o", "l"][c == "o"]
        length = len(message)
    return message


