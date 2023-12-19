from typing import Text, List, Any, Dict

from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from actions.helper import *


class ActionPermanentDisplayResponse(Action):

    def name(self):
        return "action_permanent_display_response"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        response = ""
        if get_slot_value(tracker, 'permanent_method') == 'Vasectomy':
            response = """Vasectomy is a form of male birth control that cuts the supply of sperm to your semen. 
                        It's done by cutting and sealing the tubes that carry sperm. 
                        Vasectomy has a low risk of problems and can usually be performed in an outpatient setting under local anesthesia.
                        You will need to consult a health care provider."""
        elif get_slot_value(tracker, 'permanent_method') == 'Tubal Litigation':
            response = """Tubal Litigation is surgery women can get to "tie" their fallopian tubes. 
            It's a type of female sterilization. The goal is to prevent eggs from travelling from the ovaries to 
            the uterus so you can't get pregnant.
                        "Some of its common side effects are:
                        a. Abdominal pain or cramping.
                        b. Fatigue.
                        c. Dizziness.
                        d. Gassiness or bloating.
                        e. Shoulder pain.
                        You will need to consult a health care provider."""
        dispatcher.utter_message(text=response)
        return []
        