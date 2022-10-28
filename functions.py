"""Дополнительный модуль: вспомогательные функции."""

# ИСПОЛЬЗОВАТЬ: для импорта из стандартной библиотеки мы стараемся использовать преимущественно инструкцию from...import... — это связано с тем, что модули стандартной библиотеки объёмные, но целиком нужны редко
# импорт из стандартной библиотеки
from configparser import ConfigParser

# ИСПОЛЬЗОВАТЬ: наоборот, импорт модулей текущего проекта мы чаще осуществляем с помощью инструкции import, для предупреждения закольцованности импортов
# импорт дополнительных модулей проекта
import data

def read_ini():
    # players.ini -> data.STATS
    players = ConfigParser()
    players.read(data.players_ini_path)
    for name in players.sections():
        dict_option = {}
        for option in players[name]:
            # ИСПРАВИТЬ: некоторые значения должны быть интерпретированы как числа, а ещё одно — как логическое значение
            # ИСПОЛЬЗОВАТЬ: в модуле configparser есть методы getint() и getboolean()
            dict_option[option] = players[name][option]
        data.STATS[name] = dict_option
    # saves.ini -> data.SAVES
    saves = ConfigParser()
    saves.read(data.saves_ini_path)
    for name_players in saves.sections():
        # УДАЛИТЬ: лишний словарь, работайте сразу с глобальной переменной
        dict_option = {}
        for option in saves[name_players]:
            # ИСПРАВИТЬ: название секции должны быть интерпретировано, как кортеж имён игроков, а значение по ключу turns — как список чисел
            dict_option[option] = saves[name_players][option]
        data.SAVES[name_players] = dict_option


def write_ini():
    # data.STATS -> players.ini
    players = ConfigParser()
    for player in data.STATS:
        players[player] = data.STATS[player]
    with open(data.players_ini_path, 'w', encoding='utf-8') as stats_files:
        players.write(stats_files)
    # data.SAVES -> saves.ini
    saves = ConfigParser()
    for name_players in data.SAVES:
        # ИСПРАВИТЬ: name_players — это кортеж, при записи у вас получится не предусмотренный формат названия секции, а строковое представление кортежа; аналогично со словарём data.SAVES[name_players]
        saves[name_players] = data.SAVES[name_players]
    with open(data.saves_ini_path, 'w', encoding='utf-8') as saves_files:
        saves.write(saves_files)


# КОММЕНТАРИЙ: а если бы у вас перед глазами был актуальный документ Архитектура, то вы бы видели из какой структуры данных в какую вы проводите преобразования


# тесты
if __name__ == '__main__':
    # ИСПОЛЬЗОВАТЬ: весь код, выполняемый для отладки и тестирования, должен входить в условный блок проверки импорта — иначе этот код будет выполняться не только во время выполнения только данного модуля, но и во время запуска всего проекта и импорта данного модуля

    read_ini()
    print(data.STATS)
    print(data.SAVES)
    # КОММЕНТАРИЙ: сравните получившиеся у вас типы значений в глобальных переменных с обозначенными в документе Архитектура
    # {'Player1': {'wins': '1', 'fails': '2', 'ties': '4', 'training': 'False'}, 'Player2': {'wins': '0', 'fails': '0', 'ties': '0', 'training': 'True'}}
    # {'Player1;Player2': {'turns': '4,8,2'}, '#2;Player2': {'turns': '3,7,4,9,5'}}

    # СДЕЛАТЬ: измените отсюда значения глобальных переменных data.STATS и data.SAVES, проверьте результат записи в файлы и сравните его со структурой хранения данных в обновлённом документе Архитектура

    write_ini()

