import json
import requests
from typing import Tuple, Optional


# search_machine server listens to port 4000
search_url = 'http://127.0.0.1:4000/search'
show_fields_template_url = 'http://127.0.0.1:4000/show_fields/{}'


def interrogate_user() -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """
    The boring function for extraction an entity
    and its pair of field-value via interrogation user =)
    :return: tuple of entity, field and its value
    """

    entity = None
    field = None
    value = None
    # picking up an entity to work with
    print(
        "There are three entities we can work with: \n1) users \n2) tickets \n3) organizations"
    )
    print()

    answer = ''
    while answer not in ('1', '2', '3', 'quit'):
        answer = input("Select an entity number or 'quit' to exit:").lower().strip()

    print()

    if answer == 'quit':
        return None, None, None

    if answer == '1':
        entity = 'users'
    elif answer == '2':
        entity = 'tickets'
    elif answer == '3':
        entity = 'organizations'

    # fetching a list of fields of the selected entity
    response = requests.get(show_fields_template_url.format(entity))
    if response.status_code == 200:
        fields_of_entity = response.text
        fields_of_entity = fields_of_entity.replace('[', '')\
            .replace(']', '')\
            .replace('"', '')\
            .split(',')
        print(f"Available fields of the entity '{entity}':")
        print(fields_of_entity)
        print()

        # picking up the one of the available fields
        field = ''
        while field not in (fields_of_entity + ['quit']):
            field = input("Please, enter one of them or 'quit' to exit app:").lower()

        if field == 'quit':
            return None, None, None

        # entering value of the field
        print()
        value = ''
        while not value:
            value = input(
                f"Please, enter '{field}' field's a value or 'quit' to exit app:").lower()

        if value == 'quit':
            return None, None, None

    else:
        print(
            f'Server answered with status_code = {response.status_code}. Message: {response.text}'
        )
        return None, None, None

    return entity, field, value


def build_a_payload(entity: str, field: str, value: str) -> dict:
    include = None
    if entity == 'users':
        include = {
            "organizations": [],
            "tickets": []
        }
    elif entity == 'tickets':
        include = {
            "users": [],
            "organizations": []
        }
    else:
        include = {
            "users": [],
            "tickets": []
        }

    # what do we search?
    # how it must look like?
    # it is an example of the payload
    payload = {
        "entity": entity,
        "filter": {
            field: value if field != '_id' else int(value)
        },
        "fields": [],
        "include": include
    }
    return payload


def search(payload: dict):
    try:
        response = requests.post(search_url, json=payload, timeout=3)
        if response.status_code == 200:
            # output the result in a pretty format to the console
            resp_obj = json.loads(response.text)
            print('The result is: ')
            print(json.dumps(resp_obj, indent=2))
        else:
            print(
                f'Server answered with status_code = {response.status_code}. Message: {response.text}')
    except Exception as exc:
        print(
            f'An error occurred during request to {search_url}. \nError message: {str(exc)}')


if __name__ == '__main__':
    entity, field, value = interrogate_user()
    if entity and field and value:
        search(build_a_payload(entity, field, value))
    else:
        print('App exited!')
