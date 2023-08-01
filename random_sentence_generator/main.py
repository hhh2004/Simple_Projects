import random


def get_random_word(words):
    return random.choice(words)


names = ["Peter", "Michell", "Jane", "Steve", "Ivan", "Elena", "Ioanna"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas", "Bucharest", "Ruse", "Athens"]
verbs = ["eats", "holds", "sees", "plays with", "brings", "throws"]
nouns = ["stones", "cake", "apples", "laptops", "bikes", "candy"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly", "lazily"]
details = ["near the river", "at home", "in the park", "at his friend's house", "while at sea"]


print("Hello, this is your first random sequence:")
while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)

    print(f"{random_name} from {random_place} {random_verb} {random_noun} {random_adverb} {random_detail}")
    input("Press [Enter] to generate a new one.")
