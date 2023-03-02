from funcs import *


class Table:
    data = []
    lines_count = 0
    cols_count = 0
    cols = []
    index = []
    shape = []

    # creating table from list
    def create_table_from_list(self, lst, cols=[], index=[]):
        if not lst:
            self.data = None
            return
        self.data = []
        if get_list_type(lst) == "type1":
            for el in lst:
                self.data.append(el)
        elif get_list_type(lst) == "type2":
            line_size = max([len(el) for el in lst])
            for i in range(len(lst)):
                self.data.append([None] * line_size)
                for j in range(len(lst[i])):
                    self.data[i][j] = lst[i][j]
        self.lines_count = len(self.data)
        self.cols_count = len(self.data[0])
        if len(cols) < self.cols_count:
            self.cols = [i for i in range(self.cols_count)]
        else:
            self.cols = cols
        if len(index) < self.lines_count:
            self.index = [i for i in range(self.lines_count)]
        else:
            self.index = index
        self.shape = [self.lines_count, self.cols_count]

    # creating table from dict
    def create_table_from_dict(self, dct, index=[]):
        if not dct:
            self.data = None
            return
        self.data = []
        self.cols = list(dct.keys())
        self.lines_count = get_max_height(dct)
        self.cols_count = len(self.cols)
        if len(index) < self.lines_count:
            self.index = [i for i in range(self.lines_count)]
        else:
            self.index = index
        for row in range(self.lines_count):
            self.data.append([])
            for col in range(self.cols_count):
                self.data[row].append(None)
        cl = 0
        for key in self.cols:
            if type(dct[key]) == list:
                for j in range(len(dct[key])):
                    self.data[j][cl] = dct[key][j]
            else:
                self.data[0][cl] = dct[key]
            cl += 1
        self.shape = [self.lines_count, self.cols_count]\


    # creating table from csv file
    def create_table_from_csv(self, filename, sep=","):
        index = []
        lst = []
        lines = open(filename, "r").read().split("\n")
        cols = lines[0].split(sep)
        if type(cols) != list:
            cols = [cols]
        for line in lines[1:]:
            lst.append(line.split(sep))
        if not lst:
            self.data = None
            return
        self.data = []
        if get_list_type(lst) == "type1":
            for el in lst:
                self.data.append(el)
        elif get_list_type(lst) == "type2":
            line_size = max([len(el) for el in lst])
            for i in range(len(lst)):
                self.data.append([None] * line_size)
                for j in range(len(lst[i])):
                    self.data[i][j] = lst[i][j]
        self.lines_count = len(self.data)
        self.cols_count = len(self.data[0])
        if len(cols) < self.cols_count:
            self.cols = [i for i in range(self.cols_count)]
        elif len(cols) > self.cols_count:
            for line in self.data:
                while len(line) != len(cols):
                    line.append(None)
            self.cols_count = len(cols)
            self.cols = cols
        else:
            self.cols = cols
        if len(index) < self.lines_count:
            self.index = [i for i in range(self.lines_count)]
        else:
            self.index = index
        self.shape = [self.lines_count, self.cols_count]

    # setting columns
    def set_cols(self, cols):
        if len(cols) == self.cols_count:
            self.cols = cols

    # getting columns
    def get_cols(self):
        return self.cols

    # setting indexes
    def set_index(self, index):
        if len(index) == self.lines_count:
            self.index = index

    # getting index
    def get_index(self):
        return self.index

    # getting shape
    def get_shape(self):
        return self.shape

    # adding new line to table
    def add_line(self, lst, index=0):
        if index == 0:
            self.index.append(len(self.index))
        else:
            self.index.append(index)
        if len(lst) < self.cols_count:
            lst += [None] * (self.cols_count - len(lst))
        elif len(lst) > self.cols_count:
            self.data = reshape(self.data, len(lst))
            for i in range(self.cols_count, len(lst)):
                self.cols.append(i)
            self.cols_count += len(lst) - self.cols_count
        self.data.append(lst)
        self.lines_count += 1
        self.shape = [self.lines_count, self.cols_count]

    # adding column
    def add_column(self, lst, index=0):
        if index == 0:
            self.cols.append(len(self.cols))
        else:
            self.cols.append(index)
        if len(lst) < self.lines_count:
            lst += [None] * (self.lines_count - len(lst))
        elif len(lst) > self.lines_count:
            for i in range(len(lst) - len(self.data)):
                self.data.append([None] * len(self.data[0]))
            self.lines_count += len(lst) - self.lines_count
        for i in range(len(lst)):
            self.data[i].append(lst[i])
        self.cols_count += 1
        self.shape = [self.lines_count, self.cols_count]

    # removing line by index
    def remove_line(self, index):
        if index >= self.lines_count:
            raise IndexError
        self.data.pop(index)
        self.lines_count -= 1
        self.shape = [self.lines_count, self.cols_count]

    def remove_col(self, key):
        if key not in self.cols:
            raise KeyError
        ind = self.cols.index(key)
        self.cols.pop(ind)
        self.cols_count -= 1
        for line in self.data:
            line.pop(ind)
        self.shape = [self.lines_count, self.cols_count]

    # getting element
    def get(self, row, col):
        if row >= self.lines_count or col >= self.cols_count:
            raise IndexError
        return self.data[row][col]

    # getting line by index
    def get_line(self, key):
        if key not in self.index:
            raise KeyError
        i = self.index.index(key)
        return self.data[i]

    # getting col by key
    def get_col(self, key):
        if key not in self.cols:
            raise KeyError
        i = self.cols.index(key)
        return [self.data[i][key] for i in range(len(self.data))]

    # getting shape
    def get_shape(self):
        return self.shape

    # convert to string
    def __str__(self):
        # Consts and variables
        res = ""
        cell_size = get_cell_size(self.data, self.cols, self.index) + 1
        line_size = 2 + self.cols_count + cell_size * self.cols_count + cell_size
        # Printing header
        res += " " + " " * (cell_size + 2)
        for i in range(self.cols_count):
            if i == 0:
                res += "+" + "-" * (cell_size + 2) + "+"
            else:
                res += "-" * (cell_size + 2) + "+"
        res += "\n"
        # Printing cols names
        res += " " + " " * (cell_size + 2)
        for i in range(len(self.cols)):
            if i == 0:
                res += f"| {self.cols[i]}{' ' * (cell_size - len(str(self.cols[i])))} |"
            else:
                res += f" {self.cols[i]}{' ' * (cell_size - len(str(self.cols[i])))} |"
        res += "\n"
        res += "+" + "-" * (cell_size + 2)
        for i in range(self.cols_count):
            if i == 0:
                res += "+" + "-" * (cell_size + 2) + "+"
            else:
                res += "-" * (cell_size + 2) + "+"
        res += "\n"
        # Printing table
        for i in range(self.lines_count):
            for j in range(self.cols_count):
                if j == 0:
                    res += f"| {self.index[i]}{' ' * (cell_size - len(str(self.index[i])))} |"
                    res += f" {self.data[i][j]}{' ' * (cell_size - len(str(self.data[i][j])))} |"
                else:
                    res += f" {self.data[i][j]}{' ' * (cell_size - len(str(self.data[i][j])))} |"
            res += "\n"
            res += "+" + "-" * (cell_size + 2)
            for k in range(self.cols_count):
                if k == 0:
                    res += "+" + "-" * (cell_size + 2) + "+"
                else:
                    res += "-" * (cell_size + 2) + "+"
            res += "\n"
        return res
