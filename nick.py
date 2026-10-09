import random

print("==Генератор ников==")

while True:
    word = input("Введи слово: ")

    prefixes = ["xX_", "Pro_", "Dark"]
    suffixes = ["_Master", "228", "Mr"]

    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)

    nick = prefix + word + suffix

    print("Твой ник:", nick)

    answer = input("Хочешь ещё? (да/нет): ")
    if answer.lower() != "да":
        print("Пока!")
        break
