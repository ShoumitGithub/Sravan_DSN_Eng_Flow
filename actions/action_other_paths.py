from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType, ActiveLoop, SlotSet, Restarted
from rasa_sdk.types import DomainDict
from actions.helper import *


class ActionAskEnterFaq(Action):

    def name(self) -> Text:
        return "action_ask_enter_faq"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ok, what is your question?\n"
                                      "  \nPlease note that I am a family planning bot and can only respond "
                                      "to questions relating to family planning.")
        return []


class ActionAskSelectReproductiveIssue(Action):

    def name(self) -> Text:
        return "action_ask_select_reproductive_issue"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        message = "What other issue would you like to know about?"
        buttons = create_button(["HIV", "Abortion", "Sexually Transmitted Disease (STI)", "Menstruation",
                                 "Sex"])
        dispatcher.utter_message(text=message, buttons=buttons, button_type='vertical')
        return []


class AboutReproductiveProblem(Action):

    def name(self) -> Text:
        return "action_ask_about_reproductive_problem"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Great, Please ask your question in full.")
        return []


class ActionAskIsLocalInfoCorrect(Action):

    def name(self) -> Text:
        return "action_ask_is_local_info_correct"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        message = f"Ok, Please can you confirm that your current state is {get_slot_value(tracker, 'state')} " \
                  f"and your Local government is {get_slot_value(tracker, 'lga')}"
        buttons = create_yes_or_no_button()
        dispatcher.utter_message(text=message, buttons=buttons, button_type='vertical')
        return []


class ActionIsLocalInformationCorrect(Action):

    def name(self) -> Text:
        return "action_is_local_information_correct"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        if get_slot_value(tracker, 'is_local_info_correct') == 'No':
            return [SlotSet('state', None), SlotSet('lga', None)]


class ActionAskClinicInformation(Action):

    def name(self) -> Text:
        return "action_ask_clinic_information"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Drop down of clinic")
        return []


class ActionCallMessage(Action):

    def name(self) -> Text:
        return "action_call_message"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        message = "Before you visit the clinic, call 7790 to speak to an agent for more guidance and direction. Ok."
        dispatcher.utter_message(text=message)
        return []


class RequestReproductiveHealthIssue(FormValidationAction):

    def name(self) -> Text:
        return "validate_request_reproductive_health_issue_form"

    def validate_about_reproductive_problem(self,
                                          slot_value: Any,
                                          dispatcher: CollectingDispatcher,
                                          tracker: Tracker,
                                          domain: DomainDict,
                                          ):

        if slot_value is not None:
            dispatcher.utter_message("We need to implement CHATGPT API")
        return {'about_reproductive_problem': slot_value}

    async def required_slots(
        self,
        domain_slots: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> List[Text]:
        return domain_slots


class RequestFaqForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_request_faq_form"

    def validate_enter_faq(self,
                                          slot_value: Any,
                                          dispatcher: CollectingDispatcher,
                                          tracker: Tracker,
                                          domain: DomainDict,
                                          ):

        if slot_value is not None:
            faq_response = chatGPT.ask(slot_value)
            dispatcher.utter_message(text=faq_response)
        return {'enter_faq': slot_value}

    async def required_slots(
        self,
        domain_slots: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> List[Text]:
        return domain_slots
