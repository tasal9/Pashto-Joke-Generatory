"""Simple Pashto joke generator utility.

Usage:
    from generator import get_random_joke
    print(get_random_joke('jokes.json'))
"""
import json
import random
from typing import Dict, Any


def load_jokes(path: str = 'jokes.json') -> list:
    """Load jokes from a JSON file and return as a list.

    Args:
        path: path to a JSON file containing an array of joke objects.

    Returns:
        list: list of joke objects (dict or string).
    """
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_random_joke(path: str = 'jokes.json') -> Dict[str, Any]:
    """Return a random joke object from the given JSON file.

    The returned dictionary will contain at least a `type` key set to
    'single' or 'twopart'. For backward compatibility a string joke will
    be converted to `{"type": "single", "joke": <string>}`.
    """
    jokes = load_jokes(path)
    if not isinstance(jokes, list) or len(jokes) == 0:
        raise ValueError('No jokes available in %s' % path)
    j = random.choice(jokes)
    if isinstance(j, str):
        return {'type': 'single', 'joke': j}
    # ensure minimal contract
    if 'type' not in j:
        if 'setup' in j and 'delivery' in j:
            j['type'] = 'twopart'
        else:
            j['type'] = 'single'
    return j


if __name__ == '__main__':
    print(get_random_joke())
