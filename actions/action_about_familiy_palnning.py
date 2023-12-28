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
        print(f"{database[family_planning_method]().run(dispatcher, tracker, domain)}")
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
        if slot_value ==  "Miso-Fem":
            send_audio_to_telegram(tracker.sender_id,"miso_fem.mp3")
            dispatcher.utter_message(image="https://s3.typebot.io/public/workspaces/clk9ixvcx0005jt0fbmqw1kmk/typebots/cllwc05uj0009l80f5xsndtlz/blocks/rnibjxcqxalhj5bdya73t6de?v=1695033442476")
        if slot_value ==  "Mifepak":
            send_audio_to_telegram(tracker.sender_id,"mifepak.mp3")
            dispatcher.utter_message(image="https://s3.typebot.io/public/workspaces/clk9ixvcx0005jt0fbmqw1kmk/typebots/cllwc05uj0009l80f5xsndtlz/blocks/nyk51muabe30nnrh2brm1ann?v=1695038721346")
        if slot_value == "Fiesta intim gel":
            dispatcher.utter_message(image="https://s3.typebot.io/public/workspaces/clk9ixvcx0005jt0fbmqw1kmk/typebots/cllwc05uj0009l80f5xsndtlz/blocks/ve5s9r2zy5xql0w4xgwhz0h5?v=1695035450247")
        if slot_value == "KY Jelly":
            dispatcher.utter_message(image="https://s3.typebot.io/public/workspaces/clmis6ucm000il50gyvzllels/typebots/clmis9a0q000ol50gdavazp8y/blocks/rrkyravygai48dhokh93mewh?v=1695485135707")
        if slot_value == "Female condom":
            dispatcher.utter_message(image="https://s3.typebot.io/public/workspaces/clmis6ucm000il50gyvzllels/typebots/clmis9a0q000ol50gdavazp8y/blocks/jav5wf2tigjpmzhgbj9z0nxr?v=1698191892025")
        print(f"male_condom_database: {slot_value}")
        if slot_value == "Durex":
            dispatcher.utter_message(image="https://s3.typebot.io/public/workspaces/clk9ixvcx0005jt0fbmqw1kmk/typebots/cllwc05uj0009l80f5xsndtlz/blocks/u89m2yhtn2h4mwg1zrmc4vsu?v=1695046934183")
        if slot_value == "Trojan":
            dispatcher.utter_message(image="https://s3.typebot.io/public/workspaces/clk9ixvcx0005jt0fbmqw1kmk/typebots/cllwc05uj0009l80f5xsndtlz/blocks/jt1ntxpoa9s0k4aq3j8m1akj?v=1695046181629")
        if slot_value == "Kiss":
            dispatcher.utter_message(image="https://s3.typebot.io/public/workspaces/clk9ixvcx0005jt0fbmqw1kmk/typebots/cllwc05uj0009l80f5xsndtlz/blocks/jt1ntxpoa9s0k4aq3j8m1akj?v=1695046181629")
        if slot_value == "Gold Circle":
            dispatcher.utter_message(image="https://s3.typebot.io/public/workspaces/clk9ixvcx0005jt0fbmqw1kmk/typebots/cllwc05uj0009l80f5xsndtlz/blocks/r0x11v0us12fl25uzsps4u09?v=1695046576299")
        if slot_value == "Fiesta":
            dispatcher.utter_message(image="https://s3.typebot.io/public/workspaces/clk9ixvcx0005jt0fbmqw1kmk/typebots/cllwc05uj0009l80f5xsndtlz/blocks/khhlwsa9tt3xgoq2vh3yyhuv?v=1695046660975")

        return {"family_planning_method": slot_value}
    

    def validate_family_planning_method(self,
                                         slot_value: Any,
                                         dispatcher: CollectingDispatcher,
                                         tracker: Tracker,
                                         domain: DomainDict,
                                         ):

        if slot_value in ["Penegra", "HIV Self-test kit", "Diaphragm"]:
            dispatcher.utter_message(text=get_database_message(slot_value))
        if slot_value == "Penegra":
            dispatcher.utter_message(image="https://s3.typebot.io/public/workspaces/clk9ixvcx0005jt0fbmqw1kmk/typebots/cllwc05uj0009l80f5xsndtlz/blocks/siuf2nmqf64trpx21r9lcm5w?v=1695033735916")
            send_audio_to_telegram(tracker.sender_id,"Penegra.mp3")
        if slot_value == "HIV Self-test kit":
            dispatcher.utter_message(image="https://s3.typebot.io/public/workspaces/clk9ixvcx0005jt0fbmqw1kmk/typebots/cllwc05uj0009l80f5xsndtlz/blocks/welytc2vq8j6ty950xofaquj?v=1695034713635")
        return {"family_planning_method":slot_value}


    async def required_slots(
            self,
            domain_slots: List[Text],
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: "DomainDict",
    ) -> List[Text]:
        updated_slots = domain_slots.copy()
        print(f"slot_1{updated_slots}")
        if get_slot_value(tracker, 'family_planning_method') in ["Penegra", "HIV Self-test kit", "Diaphragm"]:
            updated_slots.remove('family_planning_product')
        print(f"slot_1{updated_slots}")    
            
        return updated_slots
 