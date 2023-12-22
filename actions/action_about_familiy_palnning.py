from typing import Text, Any, Dict
from rasa_sdk import FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction, EventType
from rasa_sdk.types import DomainDict

from actions.action_1_2years import AskForSlotImplantsDatabase
from actions.actions import AskForSlotMaleCondomDatabase, AskForSlotFemaleCondomShow, \
    AskForSlotDailyContraceptiveDatabase, AskForSlotEmergencyContraceptiveDatabase, AskForSlotInjectableDatabase
from actions.helper import *


class ActionAskFamilyPlanningMethod(Action):
    def name(self) -> Text:
        return "action_ask_family_planning_method"

    async def run(self,
                  dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = 'Which of these family planning and reproductive health methods would ' \
                  'you like to know about their products?'
        button = create_button(["Male condom", "Female condom", "Lubricants and Gels", "Daily contraceptive pills",
                                "Emergency contraceptive pills", "Injectable contraceptives", "Contraceptive implants",
                                "IUCD/IUD", "Penegra", "HIV Self-test kit", "Diaphragm", "Misoprostol"])
        dispatcher.utter_message(text=message, buttons=button, button_type='vertical')
        return []


class ActionAskLubricantsAndGels(Action):
    def name(self) -> Text:
        return "action_lubricants_and_gels_database"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        hyper_link = create_hyper_link(url='https://drive.google.com/file/d/11HpoH3h5FBItO8nhjqOjMBOU6g9MiAVn/view?usp=drive_link',
                                       url_description='Audio embedding (Lubricants)')
        message = f"""Lubricants, also known as gels or lubes, are specially formulated fluids used during sexual 
activity. They help reduce friction, discomfort and vaginal dryness, enhancing pleasure and preventing condom breakage. Lubricants come in water-based, silicone-based, or oil-based varieties. 
Water-based lubes are safe to use with all condoms and sex toys. Water-based lubricants 
do not alter the pH of the vagina, does not stain clothings, and can be easily washed off with water, 
while silicone and oil-based lubes should only be used with certain condom materials.
                    
Click to listen to a short introduction of Lubricant in Pidgin, if you want."""

        dispatcher.utter_message(text=message)
        {hyper_link}
        #dispatcher.utter_message(text=message)
        message = "Here are some of the effective and available lubricants and gels.\n" \
                  "  \nClick on any of them to get their full details."
        buttons = create_button(["Fiesta intim gel", "KY Jelly"])
        dispatcher.utter_message(text=message, buttons=buttons, button_type='vertical')
        return []


class ActionIudDatabase(Action):
    def name(self) -> Text:
        return "action_iud_database"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        message = "Here are some of the effective and available lUDs.\n" \
                  "  \nClick on any of them to get their full details."
        buttons = create_button(["Lydia IUD", "Eliora"])
        dispatcher.utter_message(text=message, buttons=buttons, button_type='vertical')
        return []


class ActionMisoprostolDatabase(Action):
    def name(self) -> Text:
        return "action_misoprostol_database"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        message = """Misoprostol is a synthetic prostaglandin medication used to prevent and treat stomach and duodenal ulcers, induce labour, cause an abortion, and treat postpartum bleeding due to poor contraction of the uterus.
                    
It is an effective cervical ripening agent before first-trimester surgical abortion.\n"""

        dispatcher.utter_message(text=message)

        message="""It is recommended especially for women between 12 and 14 weeks of gestation, adolescents, and women in whom cervical dilation is expected to be difficult, either due to patient factors or provider inexperience."""
        dispatcher.utter_message(text=message)
        message = "Here are some of the effective and available misoprostol products.\n"\
                    "  \nClick on any of them to get their full details."
        buttons = create_button(["Miso-Fem", "Mifepak"])
        dispatcher.utter_message(text=message, buttons=buttons, button_type='vertical')
        return []


class ActionPenegraDatabase(Action):
    def name(self) -> Text:
        return "action_penegra_database"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        dispatcher.utter_message(text=get_database_message('Penegra'))
        return []


class ActionTestKitDatabase(Action):
    def name(self) -> Text:
        return "action_phiv_self_test_kit_database"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        dispatcher.utter_message(text=get_database_message('HIV Self-test kit'))
        return []


class ActionDiaphragmDatabase(Action):
    def name(self) -> Text:
        return "action_diaphragm_database"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        dispatcher.utter_message(text=get_database_message('Diaphragm'))
        return []


class ActionAskFamilyPlanningProduct(Action):
    def name(self) -> Text:
        return "action_ask_family_planning_product"

    async def run(self,
                  dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        database = {"Male condom": AskForSlotMaleCondomDatabase,
                    "Female condom": AskForSlotFemaleCondomShow,
                    "Lubricants and Gels": ActionAskLubricantsAndGels,
                    "Daily contraceptive pills": AskForSlotDailyContraceptiveDatabase,
                    "Emergency contraceptive pills": AskForSlotEmergencyContraceptiveDatabase,
                    "Injectable contraceptives": AskForSlotInjectableDatabase,
                    "Contraceptive implants": AskForSlotImplantsDatabase,
                    "IUCD/IUD": ActionIudDatabase,
                    "Penegra": ActionPenegraDatabase,
                    "HIV Self-test kit": ActionTestKitDatabase,
                    "Diaphragm": ActionDiaphragmDatabase,
                    "Misoprostol": ActionMisoprostolDatabase}
        family_planning_method = get_slot_value(tracker, 'family_planning_method')
        print(f"family_planning_method: {family_planning_method}")
        database[family_planning_method]().run(dispatcher, tracker, domain)
        return []


class ValidateSelectPlanningProduct(FormValidationAction):
    def name(self) -> Text:
        return "validate_request_select_planning_product"

    def validate_family_planning_product(self,
                                          slot_value: Any,
                                          dispatcher: CollectingDispatcher,
                                          tracker: Tracker,
                                          domain: DomainDict,
                                          ):

        if slot_value is not None:
            dispatcher.utter_message(text=get_database_message(slot_value))
        return {"family_planning_method": slot_value}
    

    def validate_family_planning_method(self,
                                         slot_value: Any,
                                         dispatcher: CollectingDispatcher,
                                         tracker: Tracker,
                                         domain: DomainDict,
                                         ):

        if slot_value in ["Penegra", "HIV Self-test kit", "Diaphragm"]:
            dispatcher.utter_message(text=get_database_message(slot_value))
        return {"family_planning_method":slot_value}


    async def required_slots(
            self,
            domain_slots: List[Text],
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: "DomainDict",
    ) -> List[Text]:
        updated_slots = domain_slots.copy()
        if get_slot_value(tracker, 'family_planning_method') in ["Penegra", "HIV Self-test kit", "Diaphragm"]:
            updated_slots.remove('family_planning_product')
        return updated_slots
