import json

from allure_commons._allure import step
from constants import POST_BODY, UPDATE_BODY
from api.unicorns_api import UnicornsAPI


class TestUnicornsApi:
    def test_post_unicorn(self):
        with step('Create Unicorn'):
            unicorns_api = UnicornsAPI()
            response = unicorns_api.post_unicorn(body=POST_BODY).text
        with step('Check if unicorn was created'):
            response_to_dict = json.loads(response)
            assert response_to_dict["name"] == "Sparkle Angel"
            assert response_to_dict["age"] == 2
            assert response_to_dict["colour"] == "blue"
        with step('Delete unicorn'):
            unicorns_api.delete_unicorn(response_to_dict['_id'])

    def test_update_unicorn(self):
        with step('Create new unicorn'):
            unicorns_api = UnicornsAPI()
            new_unicorn = unicorns_api.post_unicorn(body=POST_BODY).text
        with step('Update Unicorn'):
            new_unicron_to_dict = json.loads(new_unicorn)
            unicorn_id = new_unicron_to_dict['_id']
            unicorns_api.update_unicorn(unicorn_id=unicorn_id, body=UPDATE_BODY)
        with step('Check if Unicorn data was updated'):
            response = unicorns_api.get_unicorn(unicorn_id)
            response_to_dict = json.loads(response.text)
            assert response_to_dict["name"] == "Star Angel"
            assert response_to_dict["age"] == 4
            assert response_to_dict["colour"] == "yellow"
        with step("Delete unicorn"):
            unicorns_api.delete_unicorn(unicorn_id)

    def test_delete_unicorn(self):
        with step('Create new unicorn'):
            unicorns_api = UnicornsAPI()
            new_unicorn = unicorns_api.post_unicorn(body=POST_BODY).text
        with step('Delete New Unicorn'):
            new_unicron_to_dict = json.loads(new_unicorn)
            unicorns_api.delete_unicorn(new_unicron_to_dict['_id'])
        with step('Check if unicorn was deleted'):
            assert unicorns_api.get_unicorn(new_unicron_to_dict['_id']).status_code == 404

    def test_get_unicorns(self):
        with step('Create unicrons'):
            for _ in range(2):
                UnicornsAPI().post_unicorn(body=POST_BODY)
        with step('Get all unicorns'):
            unicorns = json.loads(UnicornsAPI().get_unicorns().text)
        with step('Check if all unicorns were created'):
            assert len(unicorns) == 2
        with step('Delete all unicorns'):
            for _ in unicorns:
                UnicornsAPI().delete_unicorn(unicorn_id=_['_id'])
