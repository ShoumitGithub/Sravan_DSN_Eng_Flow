from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, Action, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType, ActiveLoop, SlotSet, FollowupAction
from rasa_sdk.types import DomainDict

from actions.action_3_4_years import ActionAskIudAdvantage, ActionAskIudDisadvantage, ActionAskIudWhoCanAndCannotUse, \
    ActionAskIudMedicalCondition, ActionAskIudShow, ActionAskIusYes, ActionAskIudYes, ActionAskIusHowWorks, \
    ActionAskIusAdvantage, ActionAskIusDisadvantage, ActionAskIusWhoCanAndCannotUse, ActionAskIusMedicalCondition, \
    ActionAskIusShow
from actions.helper import *


class ActionAsk5To10YearMethod(Action):
    def name(self) -> Text:
        return "action_ask_5_10_year_method"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = """The long-acting reversible contraception, or LARC method ideal for 5 to 10 pregnancy prevention are 
1. The IUS
2. The IUD

Click on any of them to get the full details about them."""
        buttons = create_button(["IUS", "IUD"])
        dispatcher.utter_message(text=message, buttons=buttons, button_type='vertical')
        return []


class ActionAskIusHowWorks5To10(ActionAskIusHowWorks):
    def name(self) -> Text:
        return "action_ask_ius_how_works_5_10"


class ActionAskIusAdvantage5To10(ActionAskIusAdvantage):
    def name(self) -> Text:
        return "action_ask_ius_advantage_5_10"


class ActionAskIusDisadvantage5To10(ActionAskIusDisadvantage):
    def name(self) -> Text:
        return "action_ask_ius_disadvantage_5_10"


class ActionAskIusWhoCanAndCannotUse5To10(ActionAskIusWhoCanAndCannotUse):

    def name(self) -> Text:
        return "action_ask_ius_who_can_and_cannot_use_5_10"


class ActionAskIusMedicalCondition5To10(ActionAskIusMedicalCondition):
    def name(self) -> Text:
        return "action_ask_ius_medical_condition_5_10"


class ActionAskIusShow5To10(ActionAskIusShow):
    def name(self) -> Text:
        return "action_ask_ius_show_5_10"


class ActionAskIudAdvantage510(ActionAskIudAdvantage):
    def name(self) -> Text:
        return "action_ask_iud_advantage_5_10"


class ActionAskIudDisadvantage510(ActionAskIudDisadvantage):
    def name(self) -> Text:
        return "action_ask_iud_disadvantage_5_10"


class ActionAskIudWhoCanAndCannotUse510(ActionAskIudWhoCanAndCannotUse):
    def name(self) -> Text:
        return "action_ask_iud_who_can_and_cannot_use_5_10"


class ActionAskIudMedicalCondition510(ActionAskIudMedicalCondition):
    def name(self) -> Text:
        return "action_ask_iud_medical_condition_5_10"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = """So do you currently have or previously had any of the medical conditions listed?"""
        button = create_button(["Yes", "No", "I don’t know"])
        dispatcher.utter_message(text=message, buttons=button)
        return []


class ActionAskIudShow510(ActionAskIudShow):
    def name(self) -> Text:
        return "action_ask_iud_show_5_10"


class ActionAskIusYes510(ActionAskIusYes):
    def name(self) -> Text:
        return "action_ask_ius_yes_5_10"


class ActionAskIudYes510(ActionAskIudYes):
    def name(self) -> Text:
        return "action_ask_iud_yes_5_10"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = """OK, sorry about your medical condition but it is not advisable for you to use IUD. 
        Please speak to your doctor before using this method of contraception.\n
        Do you understand? It is very important."""

        dispatcher.utter_message(text=message)
        return []


class ValidateRequest5To10YearsForm(FormValidationAction):

    def name(self):
        return 'validate_request_5_10_years_form'

    def validate_ius_who_can_and_cannot_use_5_10(self,
                                            slot_value: Any,
                                            dispatcher: CollectingDispatcher,
                                            tracker: Tracker,
                                            domain: DomainDict,
                                            ):
        if slot_value is not None:
            message = """Who cannot use
                        You cannot use IUS if you have any of the following medical conditions.
                        a. Uncontrolled hypertension.
                        b. Stroke.
                        c. Heart Disease.
                        d. Liver Disease.
                        e. Breast Cancer.
                        f. Cervical cancer.
                        g. Kidney infection.
                        h. Unexplained vaginal bleeding"""
            dispatcher.utter_message(text=message)

        return {'ius_who_can_and_cannot_use_5_10': slot_value}

    async def required_slots(
            self,
            domain_slots: List[Text],
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: "DomainDict",
    ) -> List[Text]:
        slot_mappings = {"IUS": "ius",
                         "IUD": "iud"
                         }
        slots = domain_slots.copy()
        print(f"Before calling required in 5_10 years: {slots}")

        if get_slot_value(tracker, '5_10_year_method') and get_slot_value(tracker, '5_10_year_method') == 'IUD':
            print(f"inside if")
            return ["iud_advantage_5_10"]
        if get_slot_value(tracker, '5_10_year_method'):
            # print(f"Slot Mapping: {slot_mappings.get(get_slot_value(tracker, '5_10_year_method'), 'Dummy')}")
            slots = required_slots(slots, slot_mappings.get(get_slot_value(tracker, '5_10_year_method'), "Dummy"))

        if get_slot_value(tracker, 'ius_medical_condition_5_10') == 'No':
            slots.remove('ius_yes_5_10')

        if get_slot_value(tracker, 'iud_medical_condition_5_10') == 'No':
            slots.remove('iud_yes_5_10')

        print(f"After calling required slots in 5_10 years: {slots}")
        return slots
