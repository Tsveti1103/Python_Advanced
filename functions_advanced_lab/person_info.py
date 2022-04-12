def get_info(**kwargs):
    return f"This is {kwargs.get('name')} from {kwargs.get('town')} and he is {kwargs.get('age')} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))  # разопакова речник
# print(get_info(name="George", town="Sofia", age=20)) е същото като ред 5
