import os
import json
from typing import Optional, List
from .base_searcher import Searcher


class JsonSearcher(Searcher):
    def __init__(self, db_dir: str) -> None:
        self._connect(db_dir)

    def _connect(self, db_dir: str):
        self._db = {}
        # reading all json-files to store them in-memory
        for root, _, files in os.walk(db_dir):
            for file in files:
                if file.endswith('.json'):
                    self._db[file[:-4]] = json.load(open(f"{root}/{file}"))

    def _match(self, item: dict, filter: dict) -> bool:
        res = True
        for k, v in filter:
            if item.get(k) != v:
                res = False
                break
        return res

    def _get_items_by_filter(self,
                             entity: str,
                             fields: list,
                             filter: dict) -> Optional[List[dict]]:
        result = []
        for item in self._db[entity]:
            if self._match(item, filter):
                result.append(self._trim_item(item, fields))
        return result

    def _trim_item(self, item: dict, fields: list) -> dict:
        trimed_item = {}
        for field in fields:
            trimed_item[field] = item[field]
        return trimed_item

    def _get_related(self, entity: str, item: dict, include: dict) -> dict:
        related_result = {}
        for related_entity, fields in include.items():
            related_result[related_entity] = list()
            related_items = None
            if entity == 'organizations':
                related_items = self._get_items_by_filter(
                    related_entity,
                    fields,
                    {
                        "organization_id": item['_id']
                    }
                )

            elif entity == 'tickets':
                if related_entity == 'organizations':
                    related_items = self._get_items_by_filter(
                        related_entity,
                        fields,
                        {
                            "_id": item['organization_id']
                        }
                    )

                elif related_entity == 'users':
                    submitters = self._get_items_by_filter(
                        related_entity,
                        fields,
                        {
                            "_id": item['submitter_id']
                        }
                    )
                    assignees = self._get_items_by_filter(
                        related_entity,
                        fields,
                        {
                            "_id": item['assignee_id']
                        }
                    )
                    related_items = {
                        'submitter': submitters[0],
                        'assignee': assignees[0]
                    }

            elif entity == 'users':
                if related_entity == 'organizations':
                    related_items = self._get_items_by_filter(
                        related_entity,
                        fields,
                        {
                            "_id": item['organization_id']
                        }
                    )
                elif related_entity == 'tickets':
                    submitted_tickets = self._get_items_by_filter(
                        related_entity,
                        fields,
                        {
                            "submitter_id": item['_id']
                        }
                    )
                    assigned_tickets = self._get_items_by_filter(
                        related_entity,
                        fields,
                        {
                            "assignee_id": item['_id']
                        }
                    )

                    related_items = {
                        'submitted_tickets': submitted_tickets,
                        'assigned_tickets': assigned_tickets
                    }

            if related_items:
                related_result[related_entity] = related_items

        return related_result

    def search(self, payload: dict) -> Optional[List[dict]]:
        entity = payload['entity']
        filter = payload['filter']
        fields = payload['fields']
        include = payload['include']

        search_results = self._get_items_by_filter(entity, fields, filter)
        if search_results:
            for item in search_results:
                item.update(self._get_related(entity, item, include))

        return search_results

