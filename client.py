import json
import requests


if __name__ == '__main__':
    # what do we search?
    # how it must look like?
    # it is an example of the payload
    payload = {
        "entity": "users",
        "filter": {
            "_id": 1
        },
        "fields": ["_id", "name"],
        "include": {
            "organizations": ["_id", "name"],
            "tickets": ["subject", "description"]
        }
    }

    # search_machine server listens to port 4000
    search_url = 'http://127.0.0.1:4000/search'

    try:
        response = requests.post(search_url, json=payload, timeout=3)
        if response.status_code == 200:
            # output to the console a response in a pretty format
            resp_obj = json.loads(response.text)
            print(json.dumps(resp_obj, indent=2))
        else:
            print(f'Server answered with status_code = {response.status_code}')
    except Exception as exc:
        print(f'An error occurred during request to {search_url}. \nError message: {str(exc)}')
