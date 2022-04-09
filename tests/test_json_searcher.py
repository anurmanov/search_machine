import pytest
from typing import Optional, List, Dict
from searchers.json.json_searcher import JsonSearcher
from searchers.json.constants import USERS, TICKETS, ORGANIZATIONS


class MockJsonSearcher(JsonSearcher):

    def __init__(self, db: dict):
        self._db = db

    def _connect(self, db_dir: str):
        pass


@pytest.mark.parametrize(
    'payload, expected_result',
    [
        (
            {
                'entity': USERS,
                'filter': {
                    '_id': 1
                },
                'fields': ['url', 'name'],
                'include': {
                    TICKETS: ['subject', 'created_at'],
                    ORGANIZATIONS: ['name', 'details']
                }
            },
            {
                USERS: [
                    {
                        "url": "http://initech.aiworks.com/api/v2/users/1.json",
                        "name": "Francisca Rasmussen",
                        TICKETS: {
                            'submitted_tickets': [
                                {
                                    "created_at": "2016-04-28T11:19:34 -10:00",
                                    "subject": "A Catastrophe in Korea (North)"
                                },
                                {
                                    "created_at": "2016-04-14T08:32:31 -10:00",
                                    "subject": "A Catastrophe in Micronesia"
                                },
                            ],
                            'assigned_tickets': [
                                {
                                    "created_at": "2016-04-28T11:19:34 -10:00",
                                    "subject": "A Catastrophe in Korea (North)"
                                },
                                {
                                    "created_at": "2016-04-14T08:32:31 -10:00",
                                    "subject": "A Catastrophe in Micronesia"
                                },
                            ]
                        },
                        ORGANIZATIONS: [
                            {
                                "name": "Enthaze",
                                "details": "MegaCorp"
                            }
                        ]
                    }
                ]
            }
        )
    ]
)
def test_json_searcher(payload: dict,
                       expected_result: Optional[List[Dict]],
                       json_db: dict):
    json_searcher = MockJsonSearcher(json_db)

    result = json_searcher.search(payload)
    assert result == expected_result