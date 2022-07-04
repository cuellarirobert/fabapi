import requests
import json
from fabapi.fabUrls import *

class ApiInstance:
    def __init__(self):
        self.url = Urls(response_format="json")

    #returns cards
    def get_cards(self, page, per_page):
        response = requests.request("GET", url=f"{self.url.cards_url()}?page={page}&per_page={per_page}", headers={'Accept': 'application/json'})
        return response.json()

    #returns cards
    def get_set_cards(self, page, per_page, set):
        response = requests.request("GET", url=f"{self.url.cards_url()}?page={page}&per_page={per_page}&set={set}", headers={'Accept': 'application/json'})
        return response.json()
    
    def decks(self, slug:str):
        response = requests.request("GET", url=f"{self.url.cards_url()}/{slug}", headers={'Accept': 'application/json'})
        return response.json()