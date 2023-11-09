import allure
import requests
import json
from api.base_api import BaseRequest


class UnicornsAPI(BaseRequest):

    @allure.step('Get Unicorns')
    def get_unicorns(self):
        url = self.base_url + 'unicorns'
        return requests.get(url)

    @allure.step('Create Unicorn')
    def post_unicorn(self, body:dict):
        payload = json.dumps(body)
        url = self.base_url + 'unicorns'
        return requests.post(url=url, data=payload, headers=self.headers)

    @allure.step('Get Unicorn')
    def get_unicorn(self, unicorn_id:int):
        url = self.base_url +f'unicorns/{unicorn_id}'
        return requests.get(url)

    @allure.step('Update Unicorn')
    def update_unicorn(self, unicorn_id:int, body:dict):
        payload = json.dumps(body)
        url = self.base_url + f'unicorns/{unicorn_id}'
        return requests.put(url,data=payload, headers=self.headers)

    @allure.step('Delete unicorn')
    def delete_unicorn(self, unicorn_id:str):
        url = self.base_url + f'unicorns/{unicorn_id}'
        return requests.delete(url)






