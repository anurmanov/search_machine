import pytest
from app.searchers.json.constants import USERS, TICKETS, ORGANIZATIONS


@pytest.fixture()
def json_db() -> dict:
    return {
        ORGANIZATIONS: [
            {
                "_id": 1,
                "url": "http://initech.aiworks.com/api/v2/organizations/101.json",
                "external_id": "9270ed79-35eb-4a38-a46f-35725197ea8d",
                "name": "Enthaze",
                "domain_names": [
                    "kage.com",
                    "ecratic.com",
                    "endipin.com",
                    "zentix.com"
                ],
                "created_at": "2016-05-21T11:10:28 -10:00",
                "details": "MegaCorp",
                "shared_tickets": False,
                "tags": [
                    "Fulton",
                    "West",
                    "Rodriguez",
                    "Farley"
                ]
            },
            {
                "_id": 2,
                "url": "http://initech.aiworks.com/api/v2/organizations/102.json",
                "external_id": "7cd6b8d4-2999-4ff2-8cfd-44d05b449226",
                "name": "Nutralab",
                "domain_names": [
                    "trollery.com",
                    "datagen.com",
                    "bluegrain.com",
                    "dadabase.com"
                ],
                "created_at": "2016-04-07T08:21:44 -10:00",
                "details": "Non profit",
                "shared_tickets": False,
                "tags": [
                    "Cherry",
                    "Collier",
                    "Fuentes",
                    "Trevino"
                ]
            },
        ],
        TICKETS: [
            {
                "_id": "436bf9b0-1147-4c0a-8439-6f79833bff5b",
                "url": "http://initech.aiworks.com/api/v2/tickets/436bf9b0-1147-4c0a-8439-6f79833bff5b.json",
                "external_id": "9210cdc9-4bee-485f-a078-35396cd74063",
                "created_at": "2016-04-28T11:19:34 -10:00",
                "type": "incident",
                "subject": "A Catastrophe in Korea (North)",
                "description": "Nostrud ad sit velit cupidatat laboris ipsum nisi amet laboris ex exercitation amet et proident. Ipsum fugiat aute dolore tempor nostrud velit ipsum.",
                "priority": "high",
                "status": "pending",
                "submitter_id": 1,
                "assignee_id": 1,
                "organization_id": 1,
                "tags": [
                    "Ohio",
                    "Pennsylvania",
                    "American Samoa",
                    "Northern Mariana Islands"
                ],
                "has_incidents": False,
                "due_at": "2016-07-31T02:37:50 -10:00",
                "via": "web"
            },
            {
                "_id": "1a227508-9f39-427c-8f57-1b72f3fab87c",
                "url": "http://initech.aiworks.com/api/v2/tickets/1a227508-9f39-427c-8f57-1b72f3fab87c.json",
                "external_id": "3e5ca820-cd1f-4a02-a18f-11b18e7bb49a",
                "created_at": "2016-04-14T08:32:31 -10:00",
                "type": "incident",
                "subject": "A Catastrophe in Micronesia",
                "description": "Aliquip excepteur fugiat ex minim ea aute eu labore. Sunt eiusmod esse eu non commodo est veniam consequat.",
                "priority": "low",
                "status": "hold",
                "submitter_id": 1,
                "assignee_id": 1,
                "organization_id": 1,
                "tags": [
                    "Puerto Rico",
                    "Idaho",
                    "Oklahoma",
                    "Louisiana"
                ],
                "has_incidents": False,
                "due_at": "2016-08-15T05:37:32 -10:00",
                "via": "chat"
            },
            {
                "_id": "2217c7dc-7371-4401-8738-0a8a8aedc08d",
                "url": "http://initech.aiworks.com/api/v2/tickets/2217c7dc-7371-4401-8738-0a8a8aedc08d.json",
                "external_id": "3db2c1e6-559d-4015-b7a4-6248464a6bf0",
                "created_at": "2016-07-16T12:05:12 -10:00",
                "type": "problem",
                "subject": "A Catastrophe in Hungary",
                "description": "Ipsum fugiat voluptate reprehenderit cupidatat aliqua dolore consequat. Consequat ullamco minim laboris veniam ea id laborum et eiusmod excepteur sint laborum dolore qui.",
                "priority": "normal",
                "status": "closed",
                "submitter_id": 2,
                "assignee_id": 2,
                "organization_id": 2,
                "tags": [
                    "Massachusetts",
                    "New York",
                    "Minnesota",
                    "New Jersey"
                ],
                "has_incidents": True,
                "due_at": "2016-08-06T04:16:06 -10:00",
                "via": "web"
            },
            {
                "_id": "87db32c5-76a3-4069-954c-7d59c6c21de0",
                "url": "http://initech.aiworks.com/api/v2/tickets/87db32c5-76a3-4069-954c-7d59c6c21de0.json",
                "external_id": "1c61056c-a5ad-478a-9fd6-38889c3cd728",
                "created_at": "2016-07-06T11:16:50 -10:00",
                "type": "problem",
                "subject": "A Problem in Morocco",
                "description": "Sit culpa non magna anim. Ea velit qui nostrud eiusmod laboris dolor adipisicing quis deserunt elit amet.",
                "priority": "urgent",
                "status": "solved",
                "submitter_id": 2,
                "assignee_id": 2,
                "organization_id": 2,
                "tags": [
                    "Texas",
                    "Nevada",
                    "Oregon",
                    "Arizona"
                ],
                "has_incidents": True,
                "due_at": "2016-08-19T07:40:17 -10:00",
                "via": "voice"
            }
        ],
        USERS: [
            {
                "_id": 1,
                "url": "http://initech.aiworks.com/api/v2/users/1.json",
                "external_id": "74341f74-9c79-49d5-9611-87ef9b6eb75f",
                "name": "Francisca Rasmussen",
                "alias": "Miss Coffey",
                "created_at": "2016-04-15T05:19:46 -10:00",
                "active": True,
                "verified": True,
                "shared": False,
                "locale": "en-AU",
                "timezone": "Sri Lanka",
                "last_login_at": "2013-08-04T01:03:27 -10:00",
                "email": "coffeyrasmussen@flotonic.com",
                "phone": "8335-422-718",
                "signature": "Don't Worry Be Happy!",
                "organization_id": 1,
                "tags": [
                    "Springville",
                    "Sutton",
                    "Hartsville/Hartley",
                    "Diaperville"
                ],
                "suspended": True,
                "role": "admin"
            },
            {
                "_id": 2,
                "url": "http://initech.aiworks.com/api/v2/users/2.json",
                "external_id": "c9995ea4-ff72-46e0-ab77-dfe0ae1ef6c2",
                "name": "Cross Barlow",
                "alias": "Miss Joni",
                "created_at": "2016-06-23T10:31:39 -10:00",
                "active": True,
                "verified": True,
                "shared": False,
                "locale": "zh-CN",
                "timezone": "Armenia",
                "last_login_at": "2012-04-12T04:03:28 -10:00",
                "email": "jonibarlow@flotonic.com",
                "phone": "9575-552-585",
                "signature": "Don't Worry Be Happy!",
                "organization_id": 2,
                "tags": [
                    "Foxworth",
                    "Woodlands",
                    "Herlong",
                    "Henrietta"
                ],
                "suspended": False,
                "role": "admin"
            }
        ],
    }
