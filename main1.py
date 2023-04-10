from pymongo import MongoClient
import pandas as pd
import yaml


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# client = MongoClient('mongodb://localhost:27017')
# db = client['dbchatbot']
# collection = db['utters_thuonggap']

# documents = collection.find()
# df = pd.DataFrame(list(documents))
# print(df)

# with open("utters.yml", "wt", encoding="utf-8") as f:
#     for index, row in df.iterrows():
#         f.write("{0}:\n  - text: {1}\n".format(row['utter_name'], row['utter']))

# with open("data/rules1.yml", "wt", encoding="utf-8") as f:
#     f.write('version: "3.1"\n\n')
#     f.write('rules: \n\n')
#     for i in range(1,68):
#         f.write("- rule: rule_cau_hoi_{0}\n".format(i))
#         f.write("  steps:\n")
#         f.write("  - intent: cau_hoi_{0}\n".format(i))
#         f.write("  - action: utter_cau_hoi_{0}\n\n".format(i))

client = MongoClient('mongodb://localhost:27017')
db = client['dbchatbot']
collection = db['AnswersMajor']
nganh = "Công Nghệ Thông Tin"
question = "co_hoi_viec_lam"
# query = {
#             'major': nganh,
#             'question': question
#         }
query = {
            'major': { "$regex": nganh, "$options": "i" },
            'question': question
        }
documents = collection.find(query)
listSinhVien = list(documents)
print(listSinhVien[0]['answer'])

        
        