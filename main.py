# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

from pymongo import MongoClient
import pandas as pd
import yaml


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

client = MongoClient('mongodb://localhost:27017')
db = client['dbchatbot']
collection = db['intents_thuonggap']

documents = collection.find()
df = pd.DataFrame(list(documents))
print(df)
# data = {
#     "nlu": [
#         {
#             "intent": row['name'], 
#             "examples": row['example'] 
#         } for index, row in df.iterrows()
#     ]
# }

# data = {"version": "2.0", "nlu": []}

# for index, row in df.iterrows():
#     data["nlu"].append({
#         "intent": row['name'], 
#         "examples": row['example']
#     })

with open("data/nlu.yml", "wt", encoding="utf-8") as f:
    f.write('version: "3.1"\n')
    f.write('nlu: \n')
    for index, row in df.iterrows():
        f.write("\n- intent: {0}\n  examples: | \n".format(row['name']))
        print(len(row['example']))
        examples = row['example']
        for j in range(len(row['example'])):
            f.write(f"    - {examples[j]}\n")




# with open("data/nlu.yml", "w", encoding="utf-8") as outfile:
#     yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True, sort_keys = False)