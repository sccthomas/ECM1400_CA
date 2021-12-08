"""[This is a function that handles the config file ie read/write commands ]
"""
import json
# open the config file
try:
    config_json = open('modules\config.json', 'r', encoding='UTF-8')
except:
    config_json = open('config.json', 'r', encoding='UTF-8')
contents = json.load(config_json)
key = contents["Profile"]['Key']  # API key
headlines = contents["Profile"]['News']  # the articles they dont want
schedule_config = contents['Profile']['Schedules']  # saved schedules
location = contents['Profile']['Location']  # local location
language = contents['Profile']['Language']  # langauge of the news
filters = contents['Profile']['Filters']  # what news should be returned
country = contents['Profile']['Country']  # the country they want


def schedule_update_remove(update_name: str) -> None:
    """[This function will remove a schedule from the config file]

    Args:
        update_name (str): [schedules title]
    """
    for sched in schedule_config:
        if sched['title'] == update_name:
            schedule_config.remove(sched)
            break
    write_json(contents)


def write_json(data: dict) -> None:
    """[a function that dumps data in the config file]

    Args:
        data (dict): [the new config files data]
    """    ''''''
    try:
        with open('modules\config.json', 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=2)  # overwrite the config file
    except:
        with open('config.json', 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=2)  # overwrite the config file
