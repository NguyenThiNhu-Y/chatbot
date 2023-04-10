# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa.core.tracker_store import MongoTrackerStore
from pymongo import MongoClient
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted, SlotSet

# from rasa.core.trackers import DialogueStateTracker

client = MongoClient('mongodb://localhost:27017')
db = client['dbchatbot']

# khái niệm
class ActionDefineMajor(Action):
    def name(self) -> Text:
        return "action_define_major"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        collection = db['AnswersMajor']
        entities = tracker.latest_message['entities']
        for e in entities:
            if e['entity'] == "nganh":
                nganh = e['value']

        question = "khai_niem"
        query = {
            'major': { "$regex": nganh, "$options": "i" },
            'question': question
        }
        documents = collection.find(query)
        answers = list(documents)
        print(answers[0]['answer'])
        print(nganh)
        print(question)

        # answer = tracker.get_slot("nganh")
        # print(answer)

        dispatcher.utter_message(text = answers[0]['answer'])

# chỉ tiêu - học phí - cơ hội việc làm - điểm chuẩn - tiêu chí - mã - tổ hợp xét tuyển - chương trình đào tạo
class ActionDacDiemCuaNganh(Action):

    def name(self) -> Text: #tên action
        return "action_cau_tra_loi_chung"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        collection = db['AnswersMajor']

        user_question = tracker.latest_message['text']
        # answer = tracker.latest_message.get('text')
        # tracker.update(UserUtteranceReverted())
        # tracker.update(SlotSet("nganh", answer))
        
        entities = tracker.latest_message['entities']
        print(entities)
        print(user_question)

        for e in entities:
            if e['entity'] == "nganh":
                nganh = e['value']
            if e['entity'] == "chi_tieu":
                question = e['entity']
            if e['entity'] == "hoc_phi":
                question = e['entity']
            if e['entity'] == "co_hoi_viec_lam":
                question = e['entity']
            if e['entity'] == "diem_chuan":
                question = e['entity']
            if e['entity'] == "tieu_chi":
                question = e['entity']
            if e['entity'] == "ma":
                question = e['entity']
            if e['entity'] == "to_hop_xet_tuyen":
                question = e['entity']
            if e['entity'] == "chuong_trinh_dao_tao":
                question = e['entity']

        query = {
            'major': { "$regex": nganh, "$options": "i" },
            'question': question
        }
        documents = collection.find(query)
        answers = list(documents)
        print(answers[0]['answer'])
        print(nganh)
        print(question)
       

        dispatcher.utter_message(text = answers[0]['answer'])

# học ngành ... có khó không
class ActionDefficult(Action):
    def name(self) -> Text:
        return "action_defficult"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        collection = db['AnswersMajor']
        entities = tracker.latest_message['entities']
        for e in entities:
            if e['entity'] == "nganh":
                nganh = e['value']

        question = "co_kho_khong"
        query = {
            'major': { "$regex": nganh, "$options": "i" },
            'question': question
        }
        documents = collection.find(query)
        answers = list(documents)
        print(answers[0]['answer'])
        print(nganh)
        print(question)
        dispatcher.utter_message(text = answers[0]['answer'])

    