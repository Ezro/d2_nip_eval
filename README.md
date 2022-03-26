# D2 nip-eval
D2 nip-eval is a package aimed to help in providing an API for converting nip expressions into python eval statements

- transpile_nip_expressions(expressions: list[str]) -> list[str]
- transpile_nip_expression(expression: str) -> str
- keep_item(expressions: list[str], item_data: HoveredItem)
## HoveredItem
```py
class HoveredItem:
    Name: str # e.g., DAGGER, SPIRIT, CHILLING GRAND CHARM OF VITA
    Quality: str # e.g., gray, normal, magic, rare, set, unique, runeword, rune
    Text: str
    BaseItem: dict
    Item: Union[dict, None]
    NTIPAliasType: int
    NTIPAliasClassID: int
    NTIPAliasClass: Union[int, None]
    NTIPAliasQuality: int
    NTIPAliasStat: Union[dict, None]
    NTIPAliasFlag: dict
```
## Usage
---
Python Example:
```py
import requests
from d2_nip_to_eval import lexer

data = requests.get(url='https://raw.githubusercontent.com/blizzhackers/kolbot/master/d2bs/kolbot/pickit/kolton.nip').text
expressions = lexer.transpile_nip_expressions(data.split('\n'))
for expression in expressions:
    print(expression)

hovered_item = {
    "Name": "War Traveler",
    "Quality": "unique",
    "Text": "WAR TRAVELER|BATTLE BOOTS|DEFENSE: 139|DURABILITY: 13 OF 48|REQUIRED STRENGTH: 95|REQUIRED LEVEL: 42|+25% FASTER RUN/WALK|ADDS 15-25 DAMAGE|+190% ENHANCED DEFENSE|+10 TO STRENGTH|+10 TO VITALITY|40% SLOWER STAMINA DRAIN|ATTACKER TAKES DAMAGE OF 10|50% BETTER CHANCE OF GETTING MAGIC ITEMS",
    "BaseItem":
    {
        "DisplayName": "Battle Boots",
        "NTIPAliasClassID": 388,
        "NTIPAliasType": 15,
        "NTIPAliasStatProps":
        {
            "72": 18,
            "73": 18,
            "31":
            {
                "min": 39,
                "max": 47
            },
            "0x400000":
            {
                "min": 0,
                "max": 1
            }
        },
        "dimensions": [2, 2],
        "sets": ["ALDURSADVANCE"],
        "uniques": ["WARTRAVELER"],
        "NTIPAliasClass": 1
    },
    "Item":
    {
        "DisplayName": "War Traveler",
        "NTIPAliasClassID": 388,
        "NTIPAliasType": 15,
        "NTIPAliasStatProps":
        {
            "3":
            {
                "min": 10,
                "max": 10
            },
            "0":
            {
                "min": 10,
                "max": 10
            },
            "80":
            {
                "min": 30,
                "max": 50
            },
            "72": 30,
            "73": 30,
            "96":
            {
                "min": 25,
                "max": 25
            },
            "16,0":
            {
                "min": 150,
                "max": 190
            },
            "21": 15,
            "22": 25,
            "78":
            {
                "min": 5,
                "max": 10
            },
            "154":
            {
                "min": 40,
                "max": 40
            }
        }
    },
    "NTIPAliasType": 15,
    "NTIPAliasClassID": 388,
    "NTIPAliasClass": None,
    "NTIPAliasQuality": 7,
    "NTIPAliasStat":
    {
        "21": 15,
        "22": 25,
        "78": 10,
        "31": 139,
        "72": 13,
        "73": 48,
        "80": 50,
        "0": 10,
        "3": 10,
        "16": 190,
        "96": 25,
        "154": 40
    },
    "NTIPAliasFlag":
    {
        "0x10": True,
        "0x400000": False,
        "0x4000000": False
    }
}
should_keep_item = lexer.keep_item(expressions, hovered_item)
print(should_keep_item)
