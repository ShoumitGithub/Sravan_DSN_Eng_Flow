from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType, ActiveLoop, SlotSet, Restarted, SlotSet
from rasa_sdk.types import DomainDict
from actions.helper import *


class ActionPreviousContraceptionUsage(Action):
    def name(self) -> Text:
        return "action_previous_contraception_usage"

    async def run(self,
                  dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet(key='is_planned_family_planning_before', value='Yes'),
                SlotSet(key='satisfied_last_method', value='Yes')]


class ActionAskSwitchAnotherReason(Action):
    def name(self) -> Text:
        return "action_ask_switch_another_reason"

    async def run(self,
                  dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = "Can you tell me why you don't want to use your previous method"
        dispatcher.utter_message(text=message)
        # SlotSet(key='is_planned_family_planning_before', value='No')
        return []


class ValidateRequestSwitchingAnotherReason(FormValidationAction):
    def name(self) -> Text:
        return "validate_request_switching_another_reason"

    async def required_slots(
            self,
            domain_slots: List[Text],
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: "DomainDict",
    ) -> List[Text]:
        return domain_slots
