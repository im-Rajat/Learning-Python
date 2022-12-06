# Basic Python


# # Lambda Functions
# def double(x):
#     return x * x
# # Both above and below fucntion do same thing
# double = lambda x: x * 2


# # *args and **kwargs (dictionary based)
# def var_args(name, *args):
#     print(name)
#     print(args)
#
# var_args("You", "Love Python", None, "Hello", True)


# name = "RAJAT"
# print("hello", name, ",", 26)


# tuple = (3, 5, 1, "RJ")
# print(tuple)


# #set and frozenset
# print(set([1, 2, 2, 4, 3, 5, 4]))


# # dictionary
# student = {"name": "RJ", "id": 1, "feedback": None}
#
# student["last_name"] = "K"
# try:
#     last_name = student["last_name"]
#     print(last_name)
#     num = 3 + last_name
# except KeyError:
#     print("Error finding last_name")
# except TypeError as error:
#     print("Can't add these two together")
#     print(error)
# except Exception:
#     print("Unknown Error")


# dic = {}
# students = [{"name": "S1", "id": 1}, {"name": "S2", "id": 2}, {"name": "S3", "id": 3}]
# print(students[0].keys())
# print(students[0].values())


# List = []


# name = "RAJAT"
# print("Hello {0}".format(name))
# print(f"Hello {name}")


# print("Hello,world,nice".split(","))
# print('Hello,world,nice'.split(","))


# print("Hello World")
