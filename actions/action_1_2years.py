from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType, ActiveLoop, SlotSet, FollowupAction
from rasa_sdk.types import DomainDict

from actions.actions import AskForSlotDailyPillsAdvantage, AskForSlotDailyPillsDisadvantage
from actions.helper import *


class ActionAskDailyPillsAdvantage12(AskForSlotDailyPillsAdvantage):
    def name(self) -> Text:
        return "action_ask_daily_pills_advantage_1_2"
    

class AskForSlotDailyPillsDisadvantage12(AskForSlotDailyPillsDisadvantage):
    def name(self) -> Text:
        return "action_ask_daily_pills_disadvantage_1_2"


class AskForSlot12YearsMethod(Action):
    def name(self) -> Text:
        return "action_ask_1_2_years_method"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = "You can use either the daily pills, the emergency pills, the injectables or the implants.\n" \
                  "  \nChoose any them from the options to get the full details about them."
        buttons = create_button(['Daily contraceptive pills', 'Emergency contraceptive pills',
                                 'Injectable contraceptives', 'Contraceptive implants'])
        dispatcher.utter_message(text=message, buttons=buttons, button_type=VERTICAL_BUTTON_TYPE)
        return []


class AskForSlotImplantsAdvantage(Action):
    def name(self) -> Text:
        return "action_ask_implants_advantage"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = "Contraceptive implants are small, flexible rods inserted under the skin, " \
                  "typically in the arm. They release hormones (usually progestin) to prevent pregnancy.\n" \
                  "  \nThey are long-term birth control methods also called long-acting reversible contraception, " \
                  "or LARC. They provide contraception, lasting up to 3 - 5 years but can be removed at any time.\n" \
                  "  \nThey work by preventing the release of egg and thickening the cervical mucus making it " \
                  "difficult for sperm to reach the egg.\n" \

        dispatcher.utter_message(text=message)    

        message=  "Click to listen to a short explanation of implants in Pidgin, if you want to.\n" \
                  f"{create_hyper_link(url_description='Audio embedding (Implants)', url='https://drive.google.com/file/d/1_xdNkGpLTO-y3zWcJTMk7eRz7qTG-1a9/view?usp=drive_link')}\n" \
                  
        dispatcher.utter_message(text=message)
                  
        message=  "Now let me tell you some of the advantages and disadvantages of contraceptive implants.\n" \
                  "  \nAdvantages\n" \
                  "1. They can be used at any time in the menstrual cycle, are very effective, and are removed whenever you want to get pregnant.\n" \
                  "2. It gives total privacy, no one will know you have it and does not interfere with sex.\n" \
                  "3. No frequent clinical follow-up is needed after initial insertion.\n" \
                  "4. It is estrogen-free so many people can use it\n" \
                  "5. They are long-acting and may help prevent ectopic pregnancy.\n" \
                  "6. Does not disturb breast milk production.\n" \
                  "7. There is no delay in return to fertility when they are removed.\n" \
                  
        dispatcher.utter_message(text=message)

        message=  "Do you understand"
        dispatcher.utter_message(text=message)
        return []


class AskForSlotImplantsDisadvantage(Action):
    def name(self) -> Text:
        return "action_ask_implants_disadvantage"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = "Now to the disadvantages of contraceptive implants.\n" \
                  "  \nDisadvantages\n" \
                  "1. Insertion and removal involve minor surgery and must be performed by a trained professional.\n" \
                  "2. You cannot discontinue the method by yourself.\n" \
                  "3. They might have some side effects such as:\n" \
                  "a. Headache.\n" \
                  "b. Nausea or vomiting.\n" \
                  "c. Dizziness.\n" \
                  "d. Breast tenderness.\n" \
                  "e. Weight gain.\n" \
                  "f. Menstrual changes.\n" \
                  "g. Spotting and irregular vaginal bleeding." 
                  
        dispatcher.utter_message(text=message)

        message=  "Are you with me"
        dispatcher.utter_message(text=message, buttons=create_yes_or_no_button(), button_type='vertical')
        return []


class AskForSlotImplantsWhoCanAndCannotUse(Action):
    def name(self) -> Text:
        return "action_ask_implants_who_can_and_cannot_use"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = "On who can use and who cannot use implants.\n" \
                  "  \nWho can use\n" \
                  "1. You can use an implant if you want to prevent pregnancy for up to 1 to 3 years.\n" \
                  "2. If you are a breastfeeding mother (from 6 weeks after birth)\n" \
                  "3. If you cannot estrogen.\n" \
                  "4. If you don't have migrainous headaches.\n" \
                  "5. If you have endometrial or ovarian cancer, you can still use this method.\n"
        
        dispatcher.utter_message(text=message)          
        
        message=  "Do you get me"
        dispatcher.utter_message(text=message)
        return []


class AskForSlotImplantsMedicalCondition(Action):
    def name(self) -> Text:
        return "action_ask_implants_medical_condition"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = "So do you have any of the medical conditions listed?"
        buttons = create_button(["Yes", "No", "I don't know"])
        dispatcher.utter_message(text=message, buttons=buttons, button_type='vertical')
        return []


class AskForSlotImplantsDatabase(Action):
    def name(self) -> Text:
        return "action_ask_implants_database"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = "Let me tell you some of the effective and available contraceptive implants.\n" \
                  "  \nClick on any of them to get their full details."
        buttons = create_button(["Levoplant", "Jadelle", "Implanon NXT"])
        dispatcher.utter_message(text=message, buttons=buttons, button_type='vertical')
        return []


class ValidateRequest02YearsForm(FormValidationAction):

    def name(self):
        return 'validate_request_1_2_years_form'

    def validate_daily_medical_conditions(self,
                                          slot_value: Any,
                                          dispatcher: CollectingDispatcher,
                                          tracker: Tracker,
                                          domain: DomainDict,
                                          ):
        print("in validate medical condition")
        print(slot_value)
        if slot_value.lower() == 'yes':
            dispatcher.utter_message(text="Ok, it is not advisable for you to take daily pills. "
                                          "Please speak to your doctor before using this method of contraceptive.")

        return {'daily_medical_conditions': slot_value}

    def validate_daily_implants_database(self,
                                              slot_value: Any,
                                              dispatcher: CollectingDispatcher,
                                              tracker: Tracker,
                                              domain: DomainDict,
                                              ):

        print(f"in solt validate daily contraceptive database: {slot_value}")
        dispatcher.utter_message(text=get_database_message(slot_value))
        return {'daily_implants_database': slot_value}


    def validate_daily_contraceptive_database(self,
                                              slot_value: Any,
                                              dispatcher: CollectingDispatcher,
                                              tracker: Tracker,
                                              domain: DomainDict,
                                              ):

        print(f"in solt validate daily contraceptive database: {slot_value}")
        dispatcher.utter_message(text=get_database_message(slot_value))
        return {'daily_contraceptive_database': slot_value}

    def validate_emergency_contraceptive_database(self,
                                                  slot_value: Any,
                                                  dispatcher: CollectingDispatcher,
                                                  tracker: Tracker,
                                                  domain: DomainDict,
                                                  ):
        
        print(f"in solt validate emergency_contraceptive_database: {slot_value}")
        dispatcher.utter_message(text=get_database_message(slot_value))
        return {'emergency_contraceptive_database': slot_value}

    def validate_injectable_who_can_and_cannot_use_injectables(self,
                                                               slot_value: Any,
                                                               dispatcher: CollectingDispatcher,
                                                               tracker: Tracker,
                                                               domain: DomainDict,
                                                               ):
        if slot_value is not None:
            dispatcher.utter_message(text="Who cannot use\n"
                                          "1. If you are a breastfeeding mother from 6 weeks to 6 months postpartum.\n"
                                          "2. If you are a smoker and over 35 years old.\n"
                                          "3. If you have any of the following medical conditions, it is not advisable to take daily piils:\n"
                                          "a. Blood Pressure.\n"
                                          "b. Venous thromboembolism.\n"
                                          "c. Stroke.\n"
                                          "d. Heart Disease.\n"
                                          "e. Liver Disease.\n"
                                          "f. Breast Cancer.\n"
                                          "g. Diabetes.\n"
                                          "h. Vascular Disease.\n"
                                          "i. Vaginal bleeding")
            return {'injectable_who_can_and_cannot_use_injectables': slot_value}

    def validate_injectable_database(self,
                                     slot_value: Any,
                                     dispatcher: CollectingDispatcher,
                                     tracker: Tracker,
                                     domain: DomainDict,
                                     ):
        if slot_value is not None:
            dispatcher.utter_message(text=get_database_message(slot_value))
        print(f"-------injectable_database--------- {slot_value}")
            

        return {'injectable_database': slot_value}    
    def validate_implants_who_can_and_cannot_use(self,
                                                 slot_value: Any,
                                                 dispatcher: CollectingDispatcher,
                                                 tracker: Tracker,
                                                 domain: DomainDict,
                                                 ):
        if slot_value is not None:
            dispatcher.utter_message(text="Who cannot use\n"
                                          "You cannot use implants if you have any of the following medical "
                                          "conditions.\n "
                                          "a. Uncontrolled hypertension.\n"
                                          "b. Venous thromboembolism.\n"
                                          "c. Stroke.\n"
                                          "d. Heart Disease.\n"
                                          "e. Liver Disease.\n"
                                          "f. Breast Cancer.\n"
                                          "g. Kidney infection.\n"
                                          "h. Vaginal bleeding.")
        return {'implants_who_can_and_cannot_use': slot_value}
    

    def validate_implants_medical_condition(self,
                                            slot_value: Any,
                                            dispatcher: CollectingDispatcher,
                                            tracker: Tracker,
                                            domain: DomainDict,
                                            ):
        if slot_value and slot_value.lower() == 'yes':
            dispatcher.utter_message(text="Ok, sorry about your medical condition but it is not advisable "
                                          "for you to use contraceptive implants."
                                          " Please speak to your doctor before using this method of contraception.\n")
            

            dispatcher.utter_message(text="Do you understand? It is very important.")

        return {'implants_medical_condition': slot_value}

    async def required_slots(
            self,
            domain_slots: List[Text],
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: "DomainDict",
    ) -> List[Text]:
        slot_mappings = {"Daily contraceptive pills": "daily",
                         "Emergency contraceptive pills": "emergency",
                         "Injectable contraceptives": "injectable",
                         "Contraceptive implants": "implants",
                         }
        slots = domain_slots.copy()
        print(f"Before slots: {slots}")
        print(f"Slot value: {get_slot_value(tracker, '1_2_years_method')}")
        if get_slot_value(tracker, '1_2_years_method'):
            print("inside if")
            slots = required_slots(slots, slot_mappings.get(get_slot_value(tracker, '1_2_years_method'), "Dummy"))
        print(f"After slots: {slots}")
        return slots