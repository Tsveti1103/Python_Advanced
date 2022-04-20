def start_spring(**kwargs):
    final_collection = {}
    a = ""
    for key, value in kwargs.items():
        if value not in final_collection:
            final_collection[value] = []
        final_collection[value].append(key)
    final_collection = sorted(final_collection.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    result = ""
    for name, quantities in final_collection:
        sort = sorted(quantities)
        result += name + ":" + "\n"
        result += "\n".join(["-" + el for el in sort]) + "\n"
    return result


example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))


