import ast
import os
import random

from faker import Faker

import file_operations

FAKE = Faker('ru_RU')
HERO_SKILLS = file_operations.read_file('skills.txt').split('\n')
LETTERS_MAPPING = ast.literal_eval(
    file_operations.read_file('letters_mapping.txt')
)


def change_skill_format() -> list[str]:
    runic_skills = [
        ''.join(LETTERS_MAPPING.get(char, char) for char in skill)
        for skill in HERO_SKILLS
    ]
    return runic_skills


def generate_character_attributes() -> dict[str, int]:
    character_attribute = {atr: random.randint(3, 18) for atr in [
        "strength",
        "agility",
        "endurance",
        "intelligence",
        "luck",
        ]
    }
    return character_attribute


def cards_attributes() -> tuple[list[str], int, int, int, int, int, list[str]]:
    people_characteristic = [
        FAKE.first_name(),
        FAKE.last_name(),
        FAKE.job(),
        FAKE.city(),
    ]
    attributes = generate_character_attributes()
    skills = random.sample(change_skill_format(), 3)
    return (
        people_characteristic,
        attributes['strength'],
        attributes['agility'],
        attributes['endurance'],
        attributes['intelligence'],
        attributes['luck'],
        skills,
    )


def main() -> None:
    os.makedirs('Card_players', exist_ok=True)
    for i in range(1, 11):
        card_info = cards_attributes()
        card_player = {
            'first_name': card_info[0][0],
            'last_name': card_info[0][1],
            'job': card_info[0][2],
            'town': card_info[0][3],
            'strength': card_info[1],
            'agility': card_info[2],
            'endurance': card_info[3],
            'intelligence': card_info[4],
            'luck': card_info[5],
            'skill_1': card_info[6][0],
            'skill_2': card_info[6][1],
            'skill_3': card_info[6][2],
        }
        card_name = f'Card_players_{i}.svg'
        file_operations.render_template(
            'charsheet.svg', f'Card_players/{card_name}', card_player
        )


if __name__ == '__main__':
    main()
