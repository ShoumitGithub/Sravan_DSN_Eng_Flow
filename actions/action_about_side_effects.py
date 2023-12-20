from typing import Text, Any, Dict
from rasa_sdk import FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from actions.helper import *


class ActionAskWhichMethodSideEffect(Action):
    def name(self) -> Text:
        return "action_ask_which_method_side_effect"

    async def run(self,
                  dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = 'Ok. Which of the methods do you want to know their side effects?'
        button = create_button(['Contraceptive implants', 'Daily contraceptive pills',
                                'Emergency contraceptive pills', 'Injectable contraceptives',
                                'IUD', 'IUS'])
        dispatcher.utter_message(text=message, buttons=button, button_type='vertical')
        return []


class ActionAskAreYouExperiencing(Action):
    def name(self) -> Text:
        return "action_ask_are_you_experiencing_side_effects"

    async def run(self,
                  dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = 'Are you experiencing any of these side effects?'
        button = create_yes_or_no_button()
        dispatcher.utter_message(text=message, buttons=button, button_type='vertical')
        return []


class ValidateRequestSideEffectExperience(FormValidationAction):
    def name(self) -> Text:
        return "validate_request_side_effect_experience"

    def validate_are_you_experiencing_side_effects(self,
                                          slot_value: Any,
                                          dispatcher: CollectingDispatcher,
                                          tracker: Tracker,
                                          domain: DomainDict,
                                          ):
        if slot_value == 'Yes':
            dispatcher.utter_message(text="Please, call 7790 to speak to an agent about it. Ok.")
        elif slot_value == 'No':
            dispatcher.utter_message(text="Ok, you can speak to an agent by calling 7790 for further "
                                          "questions and clarity on the side effects of family planning.")

        return {'are_you_experiencing_side_effects': slot_value}

    async def required_slots(
            self,
            domain_slots: List[Text],
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: "DomainDict",
    ) -> List[Text]:
        return domain_slots


class ActionResponseAboutSelectedSideEffect(Action):

    def name(self) -> Text:
        return "action_response_about_selected_side_effect"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        response = {"Contraceptive implants": """Here are some of the side effects associated with contraceptive implants.
                                                1. Headache.
                                                2. Nausea or vomiting.
                                                3. Dizziness.
                                                4. Breast tenderness.
                                                5. Weight gain.
                                                6. Menstrual changes.
                                                7. Spotting and irregular vaginal bleeding\n
                                                They usually go away after some weeks""",
                    "Daily contraceptive pills": """Here are some of the side effects associated with daily contraceptives
                                                    1. Mild headache.
                                                    2. Nausea or vomiting.
                                                    3. Spotting or bleeding at intervals.
                                                    4. Breast tenderness and soreness to touch.
                                                    5. Mood changes\n
                                                    They usually go away after some weeks""",
                    "Emergency contraceptive pills": """Here are some of the side effects associated with emergency contraceptives.
                                                        1. Mild headache.
                                                        2. Nausea or vomiting.
                                                        3. Dizziness.
                                                        4. Breast tenderness.
                                                        5. Lower abdominal discomfort.
                                                        6. Menstrual change (period may come early)\n
                                                        They usually go away after some days.""",
                    "Injectable contraceptives": """Here are some of the side effects associated with injectables contraceptives.
                                                    1. Weight changes.
                                                    2. Headache.
                                                    3. Dizziness.
                                                    4. Breast tenderness.
                                                    5. Mood changes.
                                                    6. Menstrual change.
                                                    7. Decreased libido\n
                                                    They usually go away after some weeks""",
                    "IUD": """Here are some of the side effects associated with IUD.
                                1. Irregular and heavy period or bleeding.
                                2. Menstrual cramps.
                                3. Abnormal vaginal discharge.\n
                                They usually go away after some weeks""",
                    "IUS": """Here are some of the side effects associated with contraceptive IUS.
                                1. Headache.
                                2. Nausea or vomiting.
                                3. Breast tenderness.
                                4. Lower abdominal cramps.
                                5. Irregular uterine/vaginal bleeding.\n
                                They usually go away after some weeks"""
                    }
        dispatcher.utter_message(text=response.get(get_slot_value(tracker=tracker, slot_name='which_method_side_effect')
                                                   , SOMETHING_IS_WRONG))
        return []
