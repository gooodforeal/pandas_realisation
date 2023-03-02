# FUNCS for Line
# generating string for output 1
def generate_line(line_size, max_len):
    res = ""
    for i in range(line_size):
        if i % (max_len + 2) == 0:
            res += "+"
        else:
            res += "-"
    res += "\n"
    return res


# generating string for output 2
def generate_value_in_line(max_len, data):
    res = ""
    i = 0
    for key in data.keys():
        if i == 0:
            res += f"| {key}{' ' * (max_len - len(key))}|"
        else:
            res += f" {key}{' ' * (max_len - len(key))}|"
        i += 1
    res += "\n"
    return res


# generating string for output 3
def generate_value_in_line_2(max_len, data):
    res = ""
    i = 0
    for value in data.values():
        if i == 0:
            res += f"| {value}{' ' * (max_len - len(str(value)))}|"
        else:
            res += f" {value}{' ' * (max_len - len(str(value)))}|"
        i += 1
    res += "\n"
    return res


# getting type of list (single or double)
def get_list_type(lst):
    count = 0
    for line in lst:
        if type(line) == list:
            count += 1
    if count == len(lst):
        return "type2"
    return "type1"


# reshaping data matrix after adding
def reshape(table, size):
    for line in table:
        line += [None] * (size - len(line))
    return table


# reshaping columns
def reshape_cols(table, size):
    for i in range(size - len(table)):
        table.append([None] * len(table[0]))
    return table


# Getting longest column in dict
def get_max_height(dct):
    max_h = 0
    for value in dct.values():
        if type(value) == list:
            max_h = max(len(value), max_h)
        else:
            max_h = max(1, max_h)
    return max_h


# Counting optimal cell size for table
def get_cell_size(l1, l2, l3):
    m0 = 0
    for line in l1:
        for el in line:
            m0 = max(m0, len(str(el)))
    m1 = max([len(str(el)) for el in l2])
    m2 = max([len(str(el)) for el in l3])
    return max(m0, m1, m2) + 2
