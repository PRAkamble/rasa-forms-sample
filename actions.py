# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction,REQUESTED_SLOT


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message("Hello World!")

#         return []


class ActionRegisterUser(FormAction):

    def name(self):
        print("Inside name:")
        return "register_form"


    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        print("Inside required_slots:")    
        return ["first_name", "last_name"]



    def validate_first_name(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        print("Inside validate function")
        print("Inside validate function name ",value)

        name = value
        if isinstance(value,str):
            return {"first_name": value}
        else:
            dispatcher.utter_template("utter_wrong_first_name", tracker)
            return {"first_name": value}

        
        # if name == "alex@345":
        #     return {"first_name": value}
        # else:
        #     dispatcher.utter_template("utter_wrong_first_name", tracker)
        #     return {"first_name": value}

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        print("slot mapping")

        return {
            # "first_name": self.from_entity(entity="first_name", intent=["user_info", "register_request"]),
            # "last_name": self.from_entity(entity="last_name", intent=["user_info", "register_request"])
            "first_name": [
                self.from_entity(
                    entity="first_name"
                ),
                self.from_intent(intent="user_info", value=True)
            ],

            "last_name": self.from_text()
        }
    
    
    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker,domain: Dict[Text, Any]):
        dispatcher.utter_template("utter_submit", tracker)
        print("Inside submit:")
        return []


