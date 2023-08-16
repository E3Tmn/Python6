import urwid


def has_digit(password):
    return any(symbol.isdigit() for symbol in password)


def has_alpha(password):
    return any(symbol.isalpha() for symbol in password)


def has_symbols(password):
    return any(not symbol.isalpha() and not symbol.isdigit() for symbol in password)


def is_very_long(password):
    return len(password) > 12


def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)


def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)


def raiting_of_password(password):
    score = 0
    list_of_functions = [has_digit, is_very_long, has_alpha, has_upper_letters, has_lower_letters, has_symbols]
    for function in list_of_functions:
        score += function(password)
    return score * 2


def on_ask_change(edit, password):
    reply.set_text("Рейтинг этого пароля %s" % raiting_of_password(password))


if __name__ == '__main__':
    ask = urwid.Edit('Тайный ввод: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()
