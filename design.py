import PySimpleGUI as sg
import random
from work import play_guess_number

def main():
    sg.theme('BrownBlue')

    # Запрос количества попыток у пользователя
    attempts_limit_str = sg.popup_get_text('Введите количество попыток:', default_text='10')

    try:
        attempts_limit = int(attempts_limit_str)
    except ValueError:
        sg.popup_error('Введите корректное число для количества попыток.')
        return

    загадане_число = random.randint(1, 100)
    спроби = 0

    layout = [
        [sg.Text("Введіть число від 1 до 100:"), sg.Input(key='-INPUT-', size=(10, 1)), sg.Button('Відгадати')],
        [sg.Text("", size=(30, 1), key='-OUTPUT-')],
        [sg.Button('Вихід')]
    ]

    window = sg.Window('Гра "Відгадай число"', layout, finalize=True)

    while спроби < attempts_limit:  # Используйте цикл для ограничения количества попыток
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Вихід':
            break
        elif event == 'Відгадати':
            try:
                user_input = int(values['-INPUT-'])
                спроби += 1  # Увеличивайте количество попыток при каждой попытке
                result = play_guess_number(user_input, загадане_число, attempts_limit, спроби)
                window['-OUTPUT-'].update(result)
            except ValueError:
                window['-OUTPUT-'].update("Будь ласка, введіть число від 1 до 100.")

    window.close()
