from funcs import *
import json


class Line:
    # dist with data
    __data = {}
    # length of dict
    length = 0

    def __int__(self):
        self.__data = {}
        self.length = 0

    # takes list -> returns None
    def create_from_list(self, lst):
        self.__data = {}
        self.length = 0
        for i in range(len(lst)):
            self.__data[f"{i}"] = lst[i]
            self.length += 1

    # takes string -> returns None
    def create_from_text(self, string, sep=" "):
        self.length = 0
        self.__data = {}
        tmp = string.split(sep)
        for i in range(len(tmp)):
            self.__data[f"{i}"] = tmp[i]
            self.length += 1

    # takes dict -> returns None
    def create_from_dict(self, dct):
        self.length = 0
        self.__data = {}
        for key in dct.keys():
            self.__data[f"{key}"] = dct[key]
            self.length += 1

    # takes csv string -> returns None
    def create_from_csv(self, string, sep=","):
        self.length = 0
        self.__data = {}
        tmp = string.split(sep)
        for i in range(len(tmp)):
            self.__data[f"{i}"] = tmp[i]
            self.length += 1

    # takes json single string
    def create_from_json(self, string):
        self.length = 0
        self.__data = {}
        self.__data = json.loads(string)
        self.length = len(self.__data)

    # 1) get element by key (rewriting)
    def __getitem__(self, item):
        if item >= self.length:
            raise IndexError
        return self.__data[f"{item}"]

    # 2) get element by key
    def get(self, key):
        if key >= self.length:
            raise IndexError
        return self.__data[f"{key}"]

    # 1) set item by key (rewriting)
    def __setitem__(self, key, value):
        self.__data[f"{key}"] = value

    # 2) set item by key
    def set(self, key, value):
        self.__data[f"{key}"] = value

    # 1) returns size of line (rewriting)
    def __len__(self):
        return self.length

    # 2) returns size of line
    def size(self):
        return self.length

    # adding element to line
    def add(self, value, key=None):
        if key is None:
            key = self.length
        if not(key in self.__data.keys()):
            self.__data[f"{key}"] = value
        else:
            raise KeyError
        self.length += 1

    # converts line to string (rewriting)
    def __str__(self):
        max_len = max([len(str(self.__data[key])) for key in self.__data.keys()]) + 1
        line_size = (max_len + 1) * self.length + self.length + 1
        res = ""
        res += generate_line(line_size, max_len)
        res += generate_value_in_line(max_len, self.__data)
        res += generate_line(line_size, max_len)
        res += generate_value_in_line_2(max_len, self.__data)
        res += generate_line(line_size, max_len)
        return res
