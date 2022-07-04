class Urls:
    def __init__(self, response_format="json"):
        self.format = response_format
        self.base_url = f"https://api.fabdb.net/"
        self.cards = "cards"
        self.decks = "decks"
        
    def base_url(self):
        return self.base_url
    
    def cards_url(self):
        return self.base_url + self.cards

    def decks_url(self):
        return self.base_url + self.decks