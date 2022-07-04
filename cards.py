import json
from fabapi.fabendpoints import *

class Cards(object):
    def __init__(self, d):
        if type(d) is str:
            d = json.loads(d)

        self.from_dict(d)

    def from_dict(self, d):
        self.__dict__ = {}
        for key, value in d.items():
            if type(value) is dict:
                value = Cards(value)
            self.__dict__[key] = value

    def to_dict(self):
        d = {}
        for key, value in self.__dict__.items():
            if type(value) is Cards:
                value = value.to_dict()
            d[key] = value
        return d

    def __repr__(self):
        return str(self.to_dict())

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]

    """
	'identifier': 'absorb-in-aether-blue',
	'name': 'Absorb in Aether',
	'keywords': ['wizard', 'defense', 'reaction'],
	'stats': {'cost': '1', 'defense': '2', 'resource': '3'},
	'text': 'The next card you play this turn with an effect that deals arcane damage, instead deals that much arcane damage plus 2.',
	'rarity': 'R',
	'banned': False,
	'image': 'https://fabdb2.imgix.net/cards/printings/ARC125-RF.png?w=350&fit=clip&auto=compress',
	'totalSideboard': 0,

	"""
