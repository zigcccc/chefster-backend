from collections import OrderedDict
from typing import Dict


def get_sorted_dict(dict: Dict) -> Dict:
    """
    Returns given dict with sorted keys
    """
    return OrderedDict(sorted(dict.items()))
