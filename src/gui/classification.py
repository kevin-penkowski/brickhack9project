from enum import Enum

class Classification(Enum):
    UNCLASSIFIED = { "text": "Unclassified", "color":"black" }
    SAFE = { "text":"Maybe Safe to Consume", "color": "green" }
    DANGEROUS = { "text":"Potentially Dangerous!", "color": "red" }