import random

def play_guess_number(user_input, secret_number, attempts_limit, attempts):
    try:
        attempts += 1

        if user_input == secret_number:
            return f"Ви вгадали! Загадане число було {secret_number}. Кількість спроб: {attempts}"
        elif user_input < secret_number:
            return "Число більше."
        else:
            return "Число менше."

        if attempts == attempts_limit:
            return f"Кількість спроб вичерпана. Загадане число було {secret_number}."

    except ValueError:
        return "Будь ласка, введіть число від 1 до 100."
