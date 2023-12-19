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
                  "if you don't want any device insertion into your body. \n" \
                  "Ok. \n" \
                  "Long-acting reversible contraception, or LARC are:\n" \
                  "1. The Injectables.\n" \
                  "2. The Implants.\n" \
                  "3. The IUS.\n" \
                  "4. The IUD.\n" \
                  "While the short-acting methods are:\n" \
                  "1. The daily contraceptive Pills.\n" \
                  "2. The emergency contraceptive pills.\n" \
                  "3. The barrier contraceptives\n" \
                  "Choose any them from the options to get the full details about them."
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

        message = "How they work is that For pregnancy prevention, it works by thickening the mucus in the cervix to " \
                  "stop sperm from fertilizing an egg. It also thins out the lining of the uterus and suppresses " \
                  "ovulation and for gynaecological conditions, it reduces the endometrial lining of the womb making " \
                  "the period lighter and less painful. \n" \
                  "This means that you can use IUS for both gynecological matters and to prevent pregnancy.\n" \
                  "Do you understand" \
                  ""
        dispatcher.utter_message(text=message)
        return []


class ActionAskIusAdvantage(Action):
    def name(self) -> Text:
        return "action_ask_ius_advantage"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = """Now let me tell you some of the advantages and disadvantages of IUS.

                    Advantages
                    For pregnancy prevention:
                    1. No daily use is required.
                    2. Insertion and removal can be done at any time within the menstrual cycle.
                    3. Do not require regular clinic visits. 
                    4. It has a quick return to fertility after removal.
                    5. Safe for breastfeeding mothers from six weeks after delivery.
                    6. Local release of the home ensures milder side effects.
                    7. It maintains normal libido.
                    8. Reduces the risk of ovarian cancer and endometrial cancer.
                    9. Lower overall risk of ectopic pregnancy than women not on contraception.
                    
                    For gynecological use:
                    1. Starts working within 24 hours after insertion.
                    2. Highly effective for the treatment of abnormally heavy menstrual bleeding.
                    3. Lowers the risk of anemia due to menstrual blood loss.
                    4. Effective alternative to surgery especially for women who cannot afford to pay for surgery.\n
                    Do you understand"""
        dispatcher.utter_message(text=message)
        return []


class ActionAskIusDisadvantage(Action):
    def name(self) -> Text:
        return "action_ask_ius_disadvantage"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = """Now to the disadvantages of IUS.

Disadvantages
1. Your periods may become irregular or stop completely, which may not be suitable for some people.
2. Self-limiting follicular cysts may develop in the first few cycles.
3. If you get an infection when you have an IUS fitted, it could lead to a pelvic infection if it's not treated.
4. In rare cases, an IUS can make a hole in the womb when it's put in.
5. They might have some side effects such as:
a. Headache.
b. Nausea or vomiting.
c. Breast tenderness.
d. Lower abdominal cramps.
e. Irregular uterine/vaginal bleeding.\n
Are you with me"""
        buttons = create_button(["Yes", "No"])
        dispatcher.utter_message(text=message, buttons=buttons, button_type='vertical')
        return []


class ActionAskIusWhoCanAndCannotUse(Action):

    def name(self) -> Text:
        return "action_ask_ius_who_can_and_cannot_use"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = """On who can use and who cannot use IUS.

Who can use
1. You can use IUS if you cannot use combined contraceptives.
2. If can use IUS even if you are HIV positive.\n
Do you get me?"""
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
        message = """Ok, let me show you one of the effective IUS products that you can adopt.\n
        Eloira, which is an IUS different from an IUD due to the absence of copper. A hormone (Levonorgestrel) 
        replaces the copper. It is used to treat gynecological conditions and pregnancy prevention. 
        Eloira, which is an IUS different from an IUD due to the absence of copper. 
        A hormone (Levonorgestrel) replaces the copper. It is used 
        to treat gynecological conditions and pregnancy prevention. """
        dispatcher.utter_message(text=message)
        return []


class ActionAskIudAdvantage(Action):
    def name(self) -> Text:
        return "action_ask_iud_advantage"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = """An IUD (Intrauterine Device) is a small T or Y-shaped contraceptive device inserted into the 
        uterus to prevent pregnancy for up to 10 years. They are usually called Copper T or Copper Y. 
        They are long-lasting, easily reversible, safe, and more than 99% effective in preventing unintended pregnancy. 
        They work by providing an environment that is toxic and hostile for the sperm thereby preventing 
        them from fertilizing an egg. \n
        Click to listen to a short explanation of IUD in Pidgin, if you want to. 
        Now let me tell you some of the advantages and disadvantages of IUD.
Advantages
1. IUDs are highly effective and safe for a majority of women.
2. They are 100% hormone-free, so no hormonal side effects.
3. Can be removed at any time with immediate return to fertility.
4. Can be used as an emergency contraceptive if inserted within 5 days of having unprotected sex.
5. They are private and independent of intercourse.
6. They are long-lasting and can prevent pregnancy for up to 10 years with no drug interaction. \n
Do you understand"""
        dispatcher.utter_message(text=message)
        return []


class ActionAskIudDisadvantage(Action):
    def name(self) -> Text:
        return "action_ask_iud_disadvantage"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = """Now to the disadvantages of IUD.
Disadvantages
Complications are rare but may occur and they include;
1. Expulsion of IUD, which may lead to pregnancy.
2. Uterine perforation.
3. They might cause some side effects such as:
a. Irregular and heavy period or bleeding.
b. Menstrual cramps.
c. Abnormal vaginal discharge.\n
Are you with me?"""
        button = create_yes_or_no_button()
        dispatcher.utter_message(text=message, buttons=button)
        return []


class ActionAskIudWhoCanAndCannotUse(Action):
    def name(self) -> Text:
        return "action_ask_iud_who_can_and_cannot_use"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = """On who can use and who cannot use IUD.
Who can use
1. You can use an IUD if you are very sexually active.
2. You can use an IUD even if you are a breastfeeding mother, a smoker, or have diabetes and hypertension.
3. You can use an IUD if you have currently or history of certain health conditions like stroke, heart disease, liver disease, breast cancer, headaches, lupus, vein thrombosis, etc, and cannot use hormonal contraceptives.
4. You can use an IUD even if you are taking drugs like anti-tuberculosis drugs, anti-convulsant drugs, or anti-retroviral agents, etc\n
Do you get me"""
        dispatcher.utter_message(text=message)
        return []


class ActionAskIudMedicalCondition(Action):
    def name(self) -> Text:
        return "action_ask_iud_medical_condition"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = """So do you currently have or previously had any of the medical conditions listed?"""
        button = create_button(["Yes", "No", "I don’t know"])
        dispatcher.utter_message(text=message, buttons=button)
        return []


class ActionAskIudShow(Action):
    def name(self) -> Text:
        return "action_ask_iud_show"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = """Ok, let me show you one of the effective IUD products that you can adopt.\n
        Lydia IUD devices are non-hormonal, long-lasting contraception (5-10 yrs.) DKT has 5 variants which can be T 
        (the most common) or Y-shaped - made of plastic coat with copper. This device is inserted into the uterus and 
        it is the most effective contraceptive according to WHO with about 99.9% efficacy. It can also 
        serve as an emergency contraceptive if used within 5days of unprotected sexual intercourse. 
Its mechanism of action is to inhibit sperm penetration due to the toxicity of copper to sperm"""
        dispatcher.utter_message(text=message)
        return []


class ActionAskIusYes(Action):
    def name(self) -> Text:
        return "action_ask_ius_yes"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = """Ok, sorry about your medical condition but it is not advisable for you to use IUS. 
        Please speak to your doctor before using this method of contraception.\n
        Do you understand? It is very important."""

        dispatcher.utter_message(text=message)
        return []


class ActionAskIudYes(Action):
    def name(self) -> Text:
        return "action_ask_iud_yes"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        message = """OK, sorry about your medical condition but it is not advisable for you to use IUD. 
        Please speak to your doctor before using this method of contraception.\n
        Do you understand? It is very important."""

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

        return {'ius_who_can_and_cannot_use': slot_value}

    def validate_ius_medical_condition(self,
                                     slot_value: Any,
                                     dispatcher: CollectingDispatcher,
                                     tracker: Tracker,
                                     domain: DomainDict,
                                     ):

        if slot_value and slot_value.upper() == "YES":
            message = """Ok, sorry about your medical condition but it is not advisable for you to use IUS. 
            Please speak to your doctor before using this method of contraception.\n
            Do you understand? It is very important."""
            dispatcher.utter_message(text=message)

        return {'ius_medical_condition': slot_value}


    def validate_iud_who_can_and_cannot_use( self,
                                             slot_value: Any,
                                             dispatcher: CollectingDispatcher,
                                             tracker: Tracker,
                                             domain: DomainDict,
                                     ):
        if slot_value is not None:
            message = """Who cannot use
                        You cannot use an IUD if you have any of the following medical conditions.
                        a. Cervical cancer.
                        b. Endometrial disease.
                        c. Unexplained vaginal bleeding.
                        d. Uterine fibroid with cavity distortion.
                        e. Pelvic tuberculosis.
                        f. Untreated vaginal infection.
                        g. STIs like gonorrhoea and chlamydia."""
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