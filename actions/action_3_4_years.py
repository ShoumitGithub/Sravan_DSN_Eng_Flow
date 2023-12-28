from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType, ActiveLoop, SlotSet, FollowupAction
from rasa_sdk.types import DomainDict

from actions.actions import AskForSlotDailyPillsAdvantage, AskForSlotDailyPillsDisadvantage
from actions.helper import *


class ActionAskDailyPillsAdvantage34(AskForSlotDailyPillsAdvantage):
    def name(self) -> Text:
        return "action_ask_daily_pills_advantage_3_4"


class AskForSlotDailyPillsDisadvantage34(AskForSlotDailyPillsDisadvantage):
    def name(self) -> Text:
        return "action_ask_daily_pills_disadvantage_3_4"


class ActionAsk3To4YearMethod(Action):
    def name(self) -> Text:
        return "action_ask_3_4_year_method"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = "You can still adopt the short-acting family planning methods or the barrier contraceptives " \
                  "if you don't want any device insertion into your body.\n" \
                  "  \nOk."
        dispatcher.utter_message(text=message)

        message=  "Long-acting reversible contraception, or LARC are:\n" \
                  "1. The Injectables.\n" \
                  "2. The Implants.\n" \
                  "3. The IUS.\n" \
                  "4. The IUD.\n" \
                  "  \nWhile the short-acting methods are:\n" \
                  "1. The daily contraceptive Pills.\n" \
                  "2. The emergency contraceptive pills.\n" \
                  "3. The barrier contraceptives\n" \
                  "  \nChoose any them from the options to get the full details about them."
        buttons = create_button(["Daily contraceptive pills", "Emergency contraceptive pills",
                                 "Injectable contraceptives", "Contraceptive implants", "IUS",
                                 "IUD"])
        dispatcher.utter_message(text=message, buttons=buttons, button_type='vertical')
        return []


class ActionAskIusHowWorks(Action):
    def name(self) -> Text:
        return "action_ask_ius_how_works"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = "Intrauterine system (IUS) are hormonal intrauterine device (IUD). They contain Levenorgestrel for " \
                  "the treatment of some gynecological conditions (endometriosis, adenomyosis, endometrial " \
                  "hyperplasia, etc.) and pregnancy prevention. It has contraceptive coverage for up to 5 years."
        dispatcher.utter_message(text=message)

        message = "Click to listen to a short explanation of IUS in Pidgin, if you want to.\n" \
                  f"{create_hyper_link(url_description='Audio embedding (Hormonal IUS)', url='https://drive.google.com/file/d/1xcG5r2T4nthgiNmIFi43dBb5xXetsJMP/view?usp=drive_link')} "

        dispatcher.utter_message(text=message)

        message=  "How they work is that\n"\
                  "  \nFor pregnancy prevention, it works by thickening the mucus in the cervix to " \
                  "stop sperm from fertilizing an egg. It also thins out the lining of the uterus and suppresses " \
                  "ovulation and for gynaecological conditions, it reduces the endometrial lining of the womb making " \
                  "the period lighter and less painful."
        dispatcher.utter_message(text=message)

        message=  "This means that you can use IUS for both gynecological matters and to prevent pregnancy."
        dispatcher.utter_message(text=message)

        message= "Do you understand"
        dispatcher.utter_message(text=message)
        return []


class ActionAskIusAdvantage(Action):
    def name(self) -> Text:
        return "action_ask_ius_advantage"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = "Now let me tell you some of the advantages and disadvantages of IUS.\n"\
                    "  \nAdvantages\n"\
                    "For pregnancy prevention:\n"\
                    "1. No daily use is required.\n"\
                    "2. Insertion and removal can be done at any time within the menstrual cycle.\n"\
                    "3. Do not require regular clinic visits.\n"\
                    "4. It has a quick return to fertility after removal.\n"\
                    "5. Safe for breastfeeding mothers from six weeks after delivery.\n"\
                    "6. Local release of the home ensures milder side effects.\n"\
                    "7. It maintains normal libido.\n"\
                    "8. Reduces the risk of ovarian cancer and endometrial cancer.\n"\
                    "9. Lower overall risk of ectopic pregnancy than women not on contraception.\n"\
                    "  \nFor gynecological use:\n"\
                    "1. Starts working within 24 hours after insertion.\n"\
                    "2. Highly effective for the treatment of abnormally heavy menstrual bleeding.\n"\
                    "3. Lowers the risk of anemia due to menstrual blood loss.\n"\
                    "4. Effective alternative to surgery especially for women who cannot afford to pay for surgery."
                    
        dispatcher.utter_message(text=message)

        message= "Do you understand"
        dispatcher.utter_message(text=message)
        return []


class ActionAskIusDisadvantage(Action):
    def name(self) -> Text:
        return "action_ask_ius_disadvantage"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = "Now to the disadvantages of IUS.\n"\
                    "  \nDisadvantages\n"\
                    "1. Your periods may become irregular or stop completely, which may not be suitable for some people.\n"\
                    "2. Self-limiting follicular cysts may develop in the first few cycles.\n"\
                    "3. If you get an infection when you have an IUS fitted, it could lead to a pelvic infection if it's not treated.\n"\
                    "4. In rare cases, an IUS can make a hole in the womb when it's put in.\n"\
                    "5. They might have some side effects such as:\n"\
                    "a. Headache.\n"\
                    "b. Nausea or vomiting.\n"\
                    "c. Breast tenderness.\n"\
                    "d. Lower abdominal cramps.\n"\
                    "e. Irregular uterine/vaginal bleeding."\
                    
        dispatcher.utter_message(text=message)

        message= "Are you with me"
        buttons = create_button(["Yes", "No"])
        dispatcher.utter_message(text=message, buttons=buttons, button_type='vertical')
        return []


class ActionAskIusWhoCanAndCannotUse(Action):

    def name(self) -> Text:
        return "action_ask_ius_who_can_and_cannot_use"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = "On who can use and who cannot use IUS.\n"\
                    "  \nWho can use\n"\
                    "1. You can use IUS if you cannot use combined contraceptives.\n"\
                    "2. If can use IUS even if you are HIV positive."
        dispatcher.utter_message(text=message)

        message=    "Do you get me?"
        dispatcher.utter_message(text=message)
        return []


class ActionAskIusMedicalCondition(Action):
    def name(self) -> Text:
        return "action_ask_ius_medical_condition"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = """So do you currently have or previously had any of the medical conditions listed?"""
        buttons = create_yes_or_no_button()
        dispatcher.utter_message(text=message, buttons=buttons, button_type='vertical')
        return []


class ActionAskIusShow(Action):
    def name(self) -> Text:
        return "action_ask_ius_show"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = """Ok, let me show you one of the effective IUS products that you can adopt."""
        dispatcher.utter_message(text=message)
        message=    "Eloira, which is an IUS different from an IUD due to the absence of copper. A hormone (Levonorgestrel) "\
                    "replaces the copper. It is used to treat gynecological conditions and pregnancy prevention."\
                    # "Eloira, which is an IUS different from an IUD due to the absence of copper." \
                    # "A hormone (Levonorgestrel) replaces the copper. It is used "\
                    # "to treat gynecological conditions and pregnancy prevention."
        dispatcher.utter_message(text=message)
        dispatcher.utter_message(image="https://s3.typebot.io/public/workspaces/clk9ixvcx0005jt0fbmqw1kmk/typebots/cllwc05uj0009l80f5xsndtlz/blocks/f41p5ei87ril6qassuiel2ul?v=1695034181128")

        return []


class ActionAskIudAdvantage(Action):
    def name(self) -> Text:
        return "action_ask_iud_advantage"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = "An IUD (Intrauterine Device) is a small T or Y-shaped contraceptive device inserted into the"\
                    "uterus to prevent pregnancy for up to 10 years. They are usually called Copper T or Copper Y.\n"\
                    "  \nThey are long-lasting, easily reversible, safe, and more than 99% effective in preventing unintended pregnancy.\n"\
                    "  \nThey work by providing an environment that is toxic and hostile for the sperm thereby preventing "\
                    "them from fertilizing an egg. \n"
        dispatcher.utter_message(text=message)

        message= "Click to listen to a short explanation of IUD in Pidgin, if you want to."
        dispatcher.utter_message(text=message)

        message= "Now let me tell you some of the advantages and disadvantages of IUD.\n"\
                    "  \nAdvantages"\
                    "1. IUDs are highly effective and safe for a majority of women."\
                    "2. They are 100% hormone-free, so no hormonal side effects."\
                    "3. Can be removed at any time with immediate return to fertility"\
                    "4. Can be used as an emergency contraceptive if inserted within 5 days of having unprotected sex."\
                    "5. They are private and independent of intercourse."\
                    "6. They are long-lasting and can prevent pregnancy for up to 10 years with no drug interaction."
        dispatcher.utter_message(text=message)

        message= "Do you understand"
        dispatcher.utter_message(text=message)
        return []


class ActionAskIudDisadvantage(Action):
    def name(self) -> Text:
        return "action_ask_iud_disadvantage"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = "Now to the disadvantages of IUD.\n"\
                    "  \nDisadvantages"\
                    "Complications are rare but may occur and they include;\n"\
                    "1. Expulsion of IUD, which may lead to pregnancy.\n"\
                    "2. Uterine perforation.\n"\
                    "3. They might cause some side effects such as:\n"\
                    "a. Irregular and heavy period or bleeding.\n"\
                    "b. Menstrual cramps.\n"\
                    "c. Abnormal vaginal discharge."
        
        dispatcher.utter_message(text=message)


        message= "Are you with me?"
        button = create_yes_or_no_button()
        dispatcher.utter_message(text=message, buttons=button)
        return []


class ActionAskIudWhoCanAndCannotUse(Action):
    def name(self) -> Text:
        return "action_ask_iud_who_can_and_cannot_use"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = "On who can use and who cannot use IUD.\n"\
                    "  \nWho can use\n"\
                    "1. You can use an IUD if you are very sexually active.\n"\
                    "2. You can use an IUD even if you are a breastfeeding mother, a smoker, or have diabetes and hypertension.\n"\
                    "3. You can use an IUD if you have currently or history of certain health conditions like stroke, heart disease, liver disease, breast cancer, headaches, lupus, vein thrombosis, etc, and cannot use hormonal contraceptives.\n"\
                    "4. You can use an IUD even if you are taking drugs like anti-tuberculosis drugs, anti-convulsant drugs, or anti-retroviral agents, etc"
        
        dispatcher.utter_message(text=message)
        message= "Do you get me"
        dispatcher.utter_message(text=message)
        return []


class ActionAskIudMedicalCondition(Action):
    def name(self) -> Text:
        return "action_ask_iud_medical_condition"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = """So do you currently have or previously had any of the medical conditions listed?"""
        button = create_button(["Yes", "No", "I don't know"])
        dispatcher.utter_message(text=message, buttons=button)
        return []


class ActionAskIudShow(Action):
    def name(self) -> Text:
        return "action_ask_iud_show"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = "Ok, let me show you one of the effective IUD products that you can adopt.\n"
        dispatcher.utter_message(text=message)


        message=    "Lydia IUD devices are non-hormonal, long-lasting contraception (5-10 yrs.) DKT has 5 variants which can be T "\
                    "(the most common) or Y-shaped - made of plastic coat with copper. This device is inserted into the uterus and "\
                    "it is the most effective contraceptive according to WHO with about 99.9% efficacy. It can also "\
                    "serve as an emergency contraceptive if used within 5days of unprotected sexual intercourse.\n"\
                    "  \nIts mechanism of action is to inhibit sperm penetration due to the toxicity of copper to sperm"
        dispatcher.utter_message(text=message)
        dispatcher.utter_message(image="https://s3.typebot.io/public/workspaces/clk9ixvcx0005jt0fbmqw1kmk/typebots/cllwc05uj0009l80f5xsndtlz/blocks/hfzgb1qs4f2f7prnw7jxvzsq?v=1695034123315")
        return []


class ActionAskIusYes(Action):
    def name(self) -> Text:
        return "action_ask_ius_yes"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = "Ok, sorry about your medical condition but it is not advisable for you to use IUS.\n"\
                    "  \nPlease speak to your doctor before using this method of contraception."
        
        dispatcher.utter_message(text=message)
        message= "Do you understand? It is very important."

        dispatcher.utter_message(text=message)
        return []


class ActionAskIudYes(Action):
    def name(self) -> Text:
        return "action_ask_iud_yes"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = "Ok, sorry about your medical condition but it is not advisable for you to use IUS.\n"\
                    "  \nPlease speak to your doctor before using this method of contraception."
        
        dispatcher.utter_message(text=message)
        message= "Do you understand? It is very important."

        dispatcher.utter_message(text=message)
        return []


class ValidateRequest3To4YearsForm(FormValidationAction):

    def name(self):
        return 'validate_request_3_4_years_form'

    def validate_ius_who_can_and_cannot_use( self,
                                             slot_value: Any,
                                             dispatcher: CollectingDispatcher,
                                             tracker: Tracker,
                                             domain: DomainDict,
                                     ):
        if slot_value is not None:
            message = "Who cannot use\n"\
                        "You cannot use IUS if you have any of the following medical conditions.\n"\
                        "a. Uncontrolled hypertension.\n"\
                        "b. Stroke.\n"\
                        "c. Heart Disease.\n"\
                        "d. Liver Disease.\n"\
                        "e. Breast Cancer.\n"\
                        "f. Cervical cancer.\n"\
                        "g. Kidney infection.\n"\
                        "h. Unexplained vaginal bleeding"
            dispatcher.utter_message(text=message)

        return {'ius_who_can_and_cannot_use': slot_value}

    def validate_injectable_database(self,
                                     slot_value: Any,
                                     dispatcher: CollectingDispatcher,
                                     tracker: Tracker,
                                     domain: DomainDict,
                                     ):
        if slot_value is not None:
            dispatcher.utter_message(text=get_database_message(slot_value))
        print(f"------------------------------------ {slot_value}")
        if slot_value == "Progesta":
            dispatcher.utter_message(image="https://s3.typebot.io/public/workspaces/clmis6ucm000il50gyvzllels/typebots/clmis9a0q000ol50gdavazp8y/blocks/fwty6spob6fvmzy7d6kigsbv?v=1699596361639")
        if slot_value == "Sayana Press":
            dispatcher.utter_message(image="https://s3.typebot.io/public/workspaces/clmis6ucm000il50gyvzllels/typebots/clmis9a0q000ol50gdavazp8y/blocks/fwty6spob6fvmzy7d6kigsbv?v=1699596361639")
    

        return {'injectable_database': slot_value} 
     
    def validate_daily_contraceptive_database(self, 
                                              slot_value: Any,
                                              dispatcher: CollectingDispatcher,
                                              tracker: Tracker,
                                              domain: DomainDict,
                                              ):

        print(f"in solt validate daily contraceptive database: {slot_value}")
        dispatcher.utter_message(text=get_database_message(slot_value))
        if slot_value =="Levofem":
            dispatcher.utter_message(image="https://s3.typebot.io/public/workspaces/clk9ixvcx0005jt0fbmqw1kmk/typebots/cllwc05uj0009l80f5xsndtlz/blocks/me84zjejcyqsy5bn0j1kag6x?v=1695032418409")
        if slot_value =="Desofem":
            dispatcher.utter_message(image="https://s3.typebot.io/public/workspaces/clk9ixvcx0005jt0fbmqw1kmk/typebots/cllwc05uj0009l80f5xsndtlz/blocks/jt5uf3v5zbns3z9ahg6g1yt7?v=1695033075331")
        if slot_value =="Dianofem":
            dispatcher.utter_message(image="https://s3.typebot.io/public/workspaces/clk9ixvcx0005jt0fbmqw1kmk/typebots/cllwc05uj0009l80f5xsndtlz/blocks/me84zjejcyqsy5bn0j1kag6x?v=1695032418409")
        
        return {'daily_contraceptive_database': slot_value}
    
    def validate_ius_medical_condition(self,
                                     slot_value: Any,
                                     dispatcher: CollectingDispatcher,
                                     tracker: Tracker,
                                     domain: DomainDict,
                                     ):

        if slot_value and slot_value.upper() == "YES":
            message = "Ok, sorry about your medical condition but it is not advisable for you to use IUS.\n"\
                        "  \nPlease speak to your doctor before using this method of contraception."
            
            dispatcher.utter_message(text=message)
            message= "Do you understand? It is very important."

            dispatcher.utter_message(text=message)

        return {'ius_medical_condition': slot_value}


    def validate_implants_database(self,
                                              slot_value: Any,
                                              dispatcher: CollectingDispatcher,
                                              tracker: Tracker,
                                              domain: DomainDict,
                                              ):

        print(f"in solt validate daily contraceptive database: {slot_value}")
        dispatcher.utter_message(text=get_database_message(slot_value))
        return {'implants_database': slot_value}
    
    def validate_iud_who_can_and_cannot_use( self,
                                             slot_value: Any,
                                             dispatcher: CollectingDispatcher,
                                             tracker: Tracker,
                                             domain: DomainDict,
                                     ):
        if slot_value is not None:
            message = "Who cannot use\n"\
                        "You cannot use an IUD if you have any of the following medical conditions.\n"\
                        "a. Cervical cancer.\n"\
                        "b. Endometrial disease.\n"\
                        "c. Unexplained vaginal bleeding.\n"\
                        "d. Uterine fibroid with cavity distortion.\n"\
                        "e. Pelvic tuberculosis.\n"\
                        "f. Untreated vaginal infection.\n"\
                        "g. STIs like gonorrhoea and chlamydia."
            dispatcher.utter_message(text=message)

        return {'iud_who_can_and_cannot_use': slot_value}


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
                         "IUS": "ius",
                         "IUD": "iud"
                         }
        slots = domain_slots.copy()
        print(f"Before calling required in 3_4 years: {slots}")
        print(f"Value is: {get_slot_value(tracker, '3_4_year_method')}")
        if get_slot_value(tracker, '3_4_year_method'):
            print(f"Slot Mapping: {slot_mappings.get(get_slot_value(tracker, '3_4_year_method'), 'Dummy')}")
            slots = required_slots(slots, slot_mappings.get(get_slot_value(tracker, '3_4_year_method'), "Dummy"))
        if get_slot_value(tracker, 'ius_medical_condition') == 'No':
            slots.remove('ius_yes')

        if get_slot_value(tracker, 'iud_medical_condition') == 'No':
            slots.remove('iud_yes')

        print(f"After calling required in 3_4 years: {slots}")
        return slots