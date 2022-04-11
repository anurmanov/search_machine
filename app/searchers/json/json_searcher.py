import os
import json
from copy import copy
from typing import Optional, List
from app.searchers.base_searcher import Searcher
from .constants import USERS, TICKETS, ORGANIZATIONS


class JsonSearcher(Searcher):
    def __init__(self, db_dir: str) -> None:
        self._connect(db_dir)

    def _connect(self, db_dir: str):
        self._db = {}
        # reading all json-files to store them in-memory
        for root, _, files in os.walk(db_dir):
            for file in files:
                if file.endswith('.json'):
                    self._db[file[:-5]] = json.load(open(f"{root}/{file}"))

    def _match(self, item: dict, filter: dict) -> bool:
        """
        Matches item according to filter
        """
        res = True
        for k, v in filter.items():
            if item.get(k) != v:
                res = False
                break
        return res

    def _get_items_by_filter(self,
                             entity: str,
                             filter: dict,
                             fields: list = None) -> Optional[List[dict]]:
        """
        Matching items according to filter
        :param entity: an entity we search in
        :param filter: stores key-value pairs for filtering
        :param fields: a list of fields which items must have
        :return: a list of items matched on filter
        """
        result = []
        for item in self._db[entity]:
            if self._match(item, filter):
                result.append(self._get_trimmed_copy_of_item(item, fields) if fields else copy(item))
        return result

    def _get_trimmed_copy_of_item(self, item: dict, fields: list) -> dict:
        """
        Method copies an item and cut of all fields which is not in a list fields
        :param item: an item for trimming
        :param fields: a list of fields which must remain in copy of item
        :return: Trimmed copy
        """
        if fields:
            trimmed_item = {}
            for field in fields:
                trimmed_item[field] = item[field]
        else:
            trimmed_item = copy(item)

        return trimmed_item

    def _trim_item(self, item: dict, fields: list) -> None:
        """
        Method removes all redundant fields in the item
        :param item: an item for trimming
        :param fields: a list of fields which must remain in copy of item
        :return:
        """
        if fields:
            keys_of_item = item.keys()
            keys_to_remove = []
            for key_of_item in keys_of_item:
                if key_of_item not in fields:
                    keys_to_remove.append(key_of_item)

            for key_to_remove in keys_to_remove:
                del item[key_to_remove]

    def _get_related(self, entity: str, item: dict, include: Optional[dict]) -> dict:
        """
        Method gets all related items of the entity's item (users, tickets, organizations)
        :param entity:
        :param item: the item of the entity
        :param include: a dictionary of names of thr related
        :return:
        """
        related_result = {}

        if not include:
            return related_result

        for related_entity, fields in include.items():
            related_result[related_entity] = list()
            related_items = None
            if entity == ORGANIZATIONS:
                related_items = self._get_items_by_filter(
                    related_entity,
                    {
                        "organization_id": item['_id']
                    },
                    fields
                )

            elif entity == TICKETS:
                if related_entity == ORGANIZATIONS:
                    related_items = self._get_items_by_filter(
                        related_entity,
                        {
                            "_id": item['organization_id']
                        },
                        fields
                    )

                elif related_entity == USERS:
                    submitters = self._get_items_by_filter(
                        related_entity,
                        {
                            "_id": item['submitter_id']
                        },
                        fields
                    )
                    assignees = self._get_items_by_filter(
                        related_entity,
                        {
                            "_id": item['assignee_id']
                        },
                        fields
                    )
                    related_items = {
                        'submitter': submitters[0],
                        'assignee': assignees[0]
                    }

            elif entity == USERS:
                if related_entity == ORGANIZATIONS:
                    related_items = self._get_items_by_filter(
                        related_entity,
                        {
                            "_id": item['organization_id']
                        },
                        fields
                    )
                elif related_entity == TICKETS:
                    submitted_tickets = self._get_items_by_filter(
                        related_entity,
                        {
                            "submitter_id": item['_id']
                        },
                        fields
                    )
                    assigned_tickets = self._get_items_by_filter(
                        related_entity,
                        {
                            "assignee_id": item['_id']
                        },
                        fields
                    )

                    related_items = {
                        'submitted_tickets': submitted_tickets,
                        'assigned_tickets': assigned_tickets
                    }

            if related_items:
                related_result[related_entity] = related_items

        return related_result

    def get_record_by_index(self, entity: str, index: int = 0) -> dict:
        return self._db[entity][index]

    def search(self, payload: dict) -> dict:
        """
        The main method
        :param payload: a description of what we looking for
        :return: the search result
        """
        entity = payload['entity']
        filter = payload['filter']
        fields = payload.get('fields', [])
        include = payload.get('include', [])

        search_results = self._get_items_by_filter(entity, filter)
        if search_results:
            for item in search_results:
                related = self._get_related(entity, item, include)
                self._trim_item(item, fields)
                item.update(related)

        return {entity: search_results}

