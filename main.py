print("Ahoj, vitaj v programe, ktorý Ti po prihlásení umožni analyzovať texty!")

# registrovaní uživatelia
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# texty na analýzu
TEXTS = ['''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# prihlásenie
username = input("username: ")
password = input("password: ")

if username in users and users[username] == password:
    print(f"Vítej v aplikaci, {username}")
    print(f"Máme {len(TEXTS)} texty k dispozici.")

    choice = input(f"Zvol číslo mezi 1 a {len(TEXTS)}: ")

    if not choice.isdigit():
        print("Špatný vstup")
    else:
        choice = int(choice)

        if choice < 1 or choice > len(TEXTS):
            print("Číslo mimo rozsah")
        else:
            text = TEXTS[choice - 1]

            # rozdelenie textu na slová
            words = text.split()

            # očistenie slov od interpunkcie
            clean_words = [word.strip(".,!?") for word in words]

            # ------------------------
            # VÝPOČTY
            # ------------------------

            # dĺžky slov
            lengths = {}
            for word in clean_words:
                l = len(word)
                lengths[l] = lengths.get(l, 0) + 1

            # štatistiky slov
            title_words = sum(1 for w in clean_words if w.istitle())
            upper_words = sum(1 for w in clean_words if w.isupper())
            lower_words = sum(1 for w in clean_words if w.islower())

            # čísla v texte
            numbers = [int(w) for w in clean_words if w.isdigit()]

            # ------------------------
            # VÝSTUP
            # ------------------------

            print("\nSTATISTIKA:")
            print("Počet slov:", len(clean_words))
            print("Počet slov začínajících velkým písmenem:", title_words)
            print("Počet slov psaných VELKÝMI písmeny:", upper_words)
            print("Počet slov psaných malými písmeny:", lower_words)
            print("Počet čísel:", len(numbers))
            print("Součet všech čísel:", sum(numbers))

            print("\nDÉLKA | VÝSKYT")
            for l in sorted(lengths):
                print(f"{l:>3} | {'*' * lengths[l]:<20} | {lengths[l]:>3}")

else:
    print("Neregistrovaný uživatel, ukončuji program.")
