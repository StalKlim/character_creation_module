from random import randint

from graphic_arts.start_game_banner import run_screensaver


DEFAULT_ATTACK: int = 5
DEFAULT_DEFENCE: int = 10
DEFAULT_STAMINA: int = 80


class Character:
    BRIEF_DESC_CHAR_CLASS: str = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK: tuple[int] = (1, 3)
    RANGE_VALUE_DEFENCE: tuple[int] = (1, 5)
    SPECIAL_SKILL: str = 'Удача'
    SPECIAL_BUFF: int = 15

    def __init__(self, name) -> None:
        self.name = name

    def attack(self) -> str:
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')

    def defence(self) -> str:
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    def special(self) -> str:
        return (f'{self.name} применил специальное умение '
                f'{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}.')

    def __str__(self) -> str:
        return (f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}')


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' дерзкий воин ближнего боя. '
                                  'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK: tuple[int] = (3, 5)
    RANGE_VALUE_DEFENCE: tuple[int] = (5, 10)
    SPECIAL_BUFF: int = DEFAULT_STAMINA + 25
    SPECIAL_SKILL: str = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' находчивый воин дальнего боя. '
                                  'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK: tuple[int] = (5, 10)
    RANGE_VALUE_DEFENCE: tuple[int] = (-2, 2)
    SPECIAL_BUFF: int = DEFAULT_ATTACK + 40
    SPECIAL_SKILL: str = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' могущественный заклинатель. '
                                  'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK: tuple[int] = (-3, -1)
    RANGE_VALUE_DEFENCE: tuple[int] = (2, 5)
    SPECIAL_BUFF: int = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL: str = 'Защита'


def start_training(character):
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    commands = {'attack': character.attack,
                'defence': character.defence,
                'special': character.special}
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        # Замените блок условных операторов на словарь
        # и вынесите его из цикла. Здесь останется одно условие
        # принадлежности введённой команды словарю.
        # В функции print() будет вызываться метод класса,
        # который соответствует введённой команде.
        if cmd in commands:
            print(commands[cmd]())
    return 'Тренировка окончена.'


def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным
    классом персонажа.
    """
    game_classes: dict = {'warrior': Warrior,
                          'mage': Mage,
                          'healer': Healer}

    approve_choice: str = None

    while approve_choice != 'y':
        selected_class: str = input('Введи название персонажа, '
                                    'за которого хочешь играть: Воитель - '
                                    'warrior, Маг - mage, Лекарь - healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
