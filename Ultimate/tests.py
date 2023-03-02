from line import Line
from table import Table


o1 = Line()
o1.create_from_list([1, 2, 3, 4, "abc", ["a", "c"]])
print(o1)
o2 = Line()
o2.create_from_text("First Second Third")
print("0 element =", o2.get(0))
print("Length =", o2.length)
o2[0] = None
print(o2)
o3 = Line()
o3.create_from_dict({"t1": 1, "t2": 2, "t3": 3})
print(o3)
o3.add(222)
print(o3)
o4 = Line()
o4.create_from_json('{"id":1,"father":"Mark","mother":"Charlotte","children":1}')
print(o4)


t1 = Table()
t1.create_table_from_list([["Helloooo", "I", "am", "her"], [1, 2, 3, 4]])
print(t1)
t2 = Table()
t2.create_table_from_dict({"First": [1, 2, 3], "Second": ["a", "b"]}, index=["First", "Last", "One more"])
print(t2)
t3 = Table()
t3.create_table_from_csv("data/test.csv")
print(t3)
t4 = Table()
t4.add_line([1, 2, 3])
t4.add_line([1])
print(t4)
print("Element 0, 1:", t4.get(0, 1))
t4.remove_line(0)
print(t4)
print("Shape of matrix id: ", t4.get_shape())
t4.remove_col(0)
print(t4)
print("Column with index 0 ->", t4.get_col(1))