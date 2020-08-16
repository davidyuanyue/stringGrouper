

DELIMITER = '_'
DEFAULT_GROUP = 'default_group'
from collections import defaultdict

def _get_group_key(maybeNoGroupText :str):
    if DELIMITER in maybeNoGroupText:
        index_of_delimiter = maybeNoGroupText.index(DELIMITER)
        return maybeNoGroupText[:index_of_delimiter]
    else:
        return DEFAULT_GROUP

class StringGrouper:
    def __init__(self, list_of_string):
        self.list_of_string = list_of_string

    def divid_to_groups(self):
        string_group_by_prefix = defaultdict(list)
        for string in self.list_of_string:
            group_key = _get_group_key(string)
            string_group_by_prefix[group_key].append(string)
        return string_group_by_prefix



