import os
import json


class Entry:

    column_map = None
    map = None

    first = None
    last = None
    exten = None
    vm = None
    mac = None
    email = None
    cid_number = None
    endpoint = None
    label = None
    priority = None
    startrow = None
    did = None
    model = None
    group_dial = None
    site = None

    def __init__(self, column_map):
        if not os.path.exists(column_map):
            raise FileNotFoundError

        self.column_map = column_map
        self.load_column_map()

    def load_column_map(self):
        fp = open(self.column_map, 'r')
        self.map = json.load(fp)
        fp.close()

    def parse(self, row):

        for key in self.map:
            if not hasattr(self, key):
                print("{} was not found in the dialplan entry class".format(key))
                continue
            setattr(self, key, row[int(self.map[key])])

    def __str__(self):
        buffer = []
        for attr, value in self.__dict__.items():
            buffer.append("{}: {}".format(attr,value))
        return "\n".join(buffer)