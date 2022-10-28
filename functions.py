"""Дополнительный модуль: вспомогательные функции."""

# импорт из стандартной библиотеки
import configparser

# импорт дополнительных модулей проекта
import data


def read_ini():
    # players.ini -> data.STATS
    players = configparser.ConfigParser()
    players.read(data.players_ini_path)
    for name in players.sections():
        dict_option = {}
        for option in players[name]:
            dict_option[option] = players[name][option]
        data.STATS[name] = dict_option
    # saves.ini -> data.SAVES
    saves = configparser.ConfigParser()
    saves.read(data.saves_ini_path)
    for name_players in saves.sections():
        dict_option = {}
        for option in saves[name_players]:
            dict_option[option] = saves[name_players][option]
        data.SAVES[name_players] = dict_option


def write_ini():
    # data.STATS -> players.ini
    players = configparser.ConfigParser()
    for player in data.STATS:
        players[player] = data.STATS[player]
    with open(data.players_ini_path, 'w', encoding='utf-8') as stats_files:
        players.write(stats_files)
    # data.SAVES -> saves.ini
    saves = configparser.ConfigParser()
    for name_players in data.SAVES:
        saves[name_players] = data.SAVES[name_players]
    with open(data.saves_ini_path, 'w', encoding='utf-8') as saves_files:
        saves.write(saves_files)


# тесты
if __name__ == '__main__':
    write_ini()

read_ini()
