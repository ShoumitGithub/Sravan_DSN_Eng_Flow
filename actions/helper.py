from typing import List

# Constants
from rasa_sdk import Tracker
import requests


SOMETHING_IS_WRONG = "Something is Wrong"
VERTICAL_BUTTON_TYPE = 'vertical'


class ChatGPT(object):
    def __init__(self, api_key):
        self.url = "https://api.openai.com/v1/chat/completions"
        self.model = "gpt-3.5-turbo"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }

    def ask(self, question):
        body = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful bot."},
                {"role": "user", "content": question},
            ],
        }
        result = requests.post(
            url=self.url,
            headers=self.headers,
            json=body,
        )

        if result.status_code == 200:
            chatgpt_response = result.json()
            return chatgpt_response["choices"][0]["message"]["content"]
        else:
            return "Sorry, I couldn't generate a response at the moment. Please try again later."


chatGPT = ChatGPT("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")


def get_slot_value(tracker: Tracker, slot_name):
    return tracker.slots.get(slot_name)


def create_button(button_message_details: List):
    button_details = []
    for message in button_message_details:
        button_details.append({"title": message, "payload": message})
    return button_details


def create_hyper_link(url: str, url_description: str):
    return f'<a href="{url}">{url_description}</a>'


def create_yes_or_no_button():
    return create_button(["Yes", "No"])


def required_slots(slots: List, search_text: str):
    return [slot for slot in slots if slot.startswith(search_text)]


def get_database_message(key_value: str):
    messages = {"Levofem": "Levofem is a safe, low-dose, combined oral contraceptive used to prevent pregnancy. Each "\
                           "pack contains 21 active yellow tablets and 7 placebo(inactive) tablets which should be "\
                           "taken around the same time daily.\n"
                           "  \nHow to Use\n"
                           " 1. Take your first pill from the packet "
                           "marked with the correct day of the week, or the first pill of the first colour (phasic "
                           "pills)\n"
                           " 2. Continue to take a pill at the same time each day until the pack is finished. "
                           "Continue taking pills for seven days (during these seven days you will get a bleed).\n"
                           " 3. Start your next pack of pills on the eighth day, whether you are still bleeding or"
                           " not. This should be the same day of the week as when you took your first pill\n\n"
                           "You can buy Levofem at any pharmacy or health store around you.",

                "Desofem": "Desofem is a safe and effective daily pill used in the treatment of certain menstrual "\
                           "disorders as well as to prevent pregnancy.\n"\
                           "  \nHow to Use\n" \
                           "One pill is taken around the same "\
                           "time daily for 21 days followed by a 7-day break, then continue with the next pack.",

                "Dianofem": "Dianofem is a safe and effective pill that contains a combination of an antiandrogen ("\
                            "Cyprolerone Acetate 2mg) and estrogen (Ethinylestradiol 0.035mg) used for the treatment "\
                            "of dermatological and gynecological conditions in women. It also prevents pregnancy. It "\
                            "contains 21 tablets with no placebo (inactive pills).\n"\
                            "  \nHow to Use\n"
                            "Take one tablet daily "
                            "for 21 days, followed by a 7-day break where no tablets are taken. Start the next pack "
                            "after the 7-day break.",

                "Postpill": "Postpill is a one-dose emergency contraceptive pill by DKT. It contains 1.5 mg "\
                            "Levongestrel. POSTPILL should be taken orally as soon as possible within 24 hours but can "\
                            "still be taken within 5 days (120 hours) of unprotected\n\n"\
                            "You can click on the audio below to listen to a short introduction of Postpill "\
                            "in Pidgin if you want to.\n\n"
                            f"{create_hyper_link(url='https://drive.google.com/file/d/15O1QpDcxI9Zf1XvoR8REp788YVQcC-Hp/view?usp=drive_link', url_description='Audio embedding (Postpill)')}\n\n"
                            f"You can buy Postpill at any pharmacy or health store around you."\
                            f""    ,

                "Postinor 2": "POSTINOR is an Emergency Contraceptive Pill (ECP) that safely prevents unwanted "\
                              "accidental pregnancy within 72 hours after unprotected sexual intercourse.\n"\
                              "  \nIt doesn't work if you are already pregnant and will not harm an already established pregnancy. The sooner you take "\
                              "POSTINOR, the more effective it is.\n\n"\
                              "You can buy it at any pharmacy or health store around you.",

                "Progesta": "Progesta is an injectable contraceptive, a highly safe and effective contraceptive, "\
                            "injected intramuscularly and sometimes into the anus for 3 months continuously.\n "\
                            "  \nIts mechanism of action are\n"\
                            "• thicken cervical mucus.\n"\
                            "• inhibits ovulation.\n"\
                            "• thins uterus walls to prevent ovulation.\n\n"\
                            "Advantages of progesta include\n"\
                            "• Safe, highly effective, discontinued at will.\n"\
                            "• Long-acting,\n"\
                            "• Provided outside the clinic,\n"\
                            "• Reversible, easy to use, private, and non-contraceptive benefit.\n"\
                            "  \nUsers include heavy smokers, thyroid disorders, diabetes, those 18 years old or younger, "\
                            "breastfeeding mothers, and pelvic inflammatory diseases.\n\n"\
                            "How to use\n"\
                            "• Injected in the upper arm or buttocks, start at any time during the menstrual cycle.\n"\
                            "• 5 days after menstrual period, abstain from sex for the next 7 days.\n"\
                            "• It can be administered after abortion.\n"\
                            "• Start 6 weeks after delivery for a breastfeeding woman.\n\n"\
                            "You can click on the audio below to listen to a short introduction to Progesta in Pidgin "\
                            "if you want to.\n"
                            f"{create_hyper_link(url='https://drive.google.com/file/d/1rKNyg-etSIiFn1U-XwKNyNkRW8yw_ZSr/view?usp=drive_link', url_description='Audio embedding (Progesta)')}",

                "Sayana Press": """Sayana Press is indicated for long-term female contraception. Each subcutaneous injection prevents ovulation and provides contraception for at least 13 weeks\n
You can click on the audio below to listen to a short introduction of Sayana press in Pidgin, if you want to.
                    
<audio link>\n
<<<<<<< HEAD
You can also click to watch a video on how to inject a Sayana Press in Pidgin.
How to inject a Sayana Press\nhttps://youtu.be/bXi_6rbJhsk?si=86G6gnUmQaUCQ7t_\n""",
=======
You can also click to watch a video on how to inject a Sayana Press in Pidgin.""",
>>>>>>> origin/main

                "Kiss": """Kiss condoms are gently lubricated to provide you with a silky, natural feeling for increased pleasure and sensitivity.\n
You can buy the Kiss condom at any pharmacy or health store around you.
""",
                "Fiesta": """Fiesta is a premium condom brand that comes in 14 exciting variants of styles, colours, textures, flavors, shapes and sizes that increase the sensation for both partners.
                    
1. They provide great protection from both pregnancy and STIs/HIV
2. Exciting variants offer enhanced sexual pleasure for both partners.
3. Ensure STIs/HIV protection for women on other family planning methods.
4. Can be used for oral, anal and vaginal sex.
5. 100% electronically tested and manufactured to meet the highest international quality standards.\n
You can buy the Fiesta condom at any pharmacy or health store around you.""",
                "Durex": """Durex is a brand of condoms and personal lubricants owned by the British-Dutch company Reckitt Benckiser.\n
You can visit your nearest health shop to purchase
""",
                "Trojan": """Trojan brand latex condoms are made from premium quality latex to help reduce the risk of unintended pregnancy and sexually transmitted infections. Every condom is electronically tested to help ensure reliability. There are more than 30 varieties of Trojan brand condoms.\n
You can visit your nearest health shop to buy.
""",
                "Gold Circle": """Gold Circle (GC) Condom is SFH Nigeria's pinnacle product. They offer dual protection to encourage family planning and prevent sexually Transmitted Infections. Gold Circle Condoms are made of latex, well lubricated and shrinked-wrapped for maximum pleasure.\n
You can visit you nearest health shop to purchase.
""",
                "Levoplant": "LEVOPLANT which is a subdermal contraceptive implant, Levoplant has two small flexible "\
                             "rods about matchstick size. It is WHO-prequalified and highly effective for 3 years, "\
                             "it is suitable for most women except pregnant women.\n\n"\
                             "Advantages\n"\
                             "• Immediate return to fertility.\n"\
                             "• Fewer side effects.\n "\
                             "• Thinner trocar for the insertion process.\n"\
                             "• High quality and most affordable 3-year implant in Nigeria.\n"\
                             "  \nCommon side effects:\n"\
                             "• Menstrual changes.\n"\
                             "• Headaches.\n"\
                             "• Dizziness.\n"\
                             "• Weight changes (loss/Gain)- which is a buildup of water not fat.\n"\
                             "• Breast tenderness",

                "Jadelle": "Jadelle is a contraceptive implant that consists of two small flexible "\
                           "rods (as short as a match stick but thinner) that is inserted under the skin of "\
                           "a woman's upper arm. It contains 75mg of the hormone Levonorgestrel in each rod. "\
                           "Jadelle implants are over 99% effective and can prevent pregnancy "\
                           "for a period of 5 years.\n"\
                            "  \nThis method is completely and quickly reversible"\
                           " because it releases very low dose of hormone which leaves the body quickly when removed, "
                           "so the woman can get pregnant without delay.",

                "Implanon NXT": "Implanon NXT is a contraceptive implant that consists of one small "\
                                "flexible rod that is inserted under the skin of a woman's upper arm. "\
                                "It contains 65mg of the hormone Etonorgestrel in each rod.\n"\
                                "  \nImplanon NXT is over 99% effective and can prevent pregnancy for 3 years. "\
                                "Also, it can be stopped anytime the woman wants by asking a health provider "\
                                "to remove it.\n"\
                                "  \nThis method is completely and quickly reversible "\
                                "because it releases a very low dose of hormone, which leaves the body quickly "\
                                "when removed, so you woman can get pregnant without delay.\n\n"\
                                " Some of its common side effects are\n"\
                                "• Headaches.\n"\
                                "• Dizziness.\n"\
                                "• Breast tenderness.\n"\
                                "• Nausea\n"\
                                "• Stomach cramping/bloating.\n"\
                                "• Weight gain.\n"\
                                "• Vaginal irritation/discharge may occur.",
                                
                "Fiesta intim gel": """Fiesta Gels are classy and smooth, with a wet sensation for heightened sexual pleasure.
                    
How to Use
Pour a small amount of Fiesta Intim natural gel on your palm and apply directly on your erect penis. For extra pleasure, you can also apply on the woman's intimate area.\n
You can click to watch a video on how to use this lubricant in Pidgin.
                    
<<<<<<< HEAD
https://youtu.be/VtrXlRVaP-c?si=0HYn95zcGnXp6lBP\n
=======
<video_link>\n
>>>>>>> origin/main
You can purchase it at your nearest pharmacy or health shop.""",

                "KY Jelly": """KY Jelly is a water-based, fragrance-free, non-greasy formula that quickly prepares you for sexual intimacy & eases the discomfort of personal dryness.\n
You can click to watch a video on how to insert and remove a female condom in Pidgin.\n
<<<<<<< HEAD
How to insert a Diaphragm\nhttps://youtu.be/zw76siSZ2E4?si=cjaKJAvcHyWLobOR\n
How to remove a Diaphragm\nhttps://youtu.be/ettTJHL209w?si=Ojwf4Q1K2pircJjK\n
How to use a Diaphragm gel\nhttps://youtu.be/6VV1Wi67o4Y?si=KMsC2QkhQwr-WgGv\n
=======
<video link>\n
>>>>>>> origin/main
You can visit your nearest chemist/pharmacy to buy.
""",

                "Lydia IUD": """Lydia IUD devices are non-hormonal, long-lasting contraception (5-10 yrs.) DKT has 5 variants which can be T (the most common) or Y-shaped - made of plastic coat with copper. This device is inserted into the uterus and it is the most effective contraceptive according to WHO with about 99.9% efficacy. It can also serve as an emergency contraceptive if used within 5days of unprotected sexual intercourse.
                    
Its mechanism of action is to inhibit sperm penetration due to the toxicity of copper to sperm""",

                "Eliora": "Eloira, which is an IUS different from an IUD due to the absence of copper. A hormone (Levonorgestrel) replaces the copper. It is used to treat gynecological conditions and pregnancy prevention.",

                "Miso-Fem": """Miso-Fem is a tested and trusted high-quality brand of Misoprostol that is used in the management of obstetric, gynecological, and medical conditions. used for maternal mortality reduction. These conditions include postpartum haemorrhage (PPH) and peptic ulcer induced by Non-Steroidal Anti-Inflammatory Drugs (NSAIDs).
                    
How to Use 
Miso-Fem is to be taken under the tongue (dissolved under the tongue) and not to be swallowed, or through the vagina or rectal to be absolved. It is used for labor (pain) reduction by dilating the cervix.
                    
You can click on the audio below to listen to a full explanation of Miso-Fem and usage in Pidgin if you want to.""",

                "Mifepak": """Mifepak is used for intra-uterine fetal demise, therapeutic abortion, and conservative management of the placenta. Its mode of work includes blocking the progesterone, causing the contraction and expulsion of the detached embryo.
                    
How to Use 
Taken orally with water under healthcare supervision.
                    
You can click on the audio below to listen to a short introduction to Mifepak in Pidgin if you want to.
                    
<audio_link>""",

                "Penegra": """Penegra is a DKT product that contains Sidenafil Citrate. It is used to treat erectile dysfunction. Erectile Dysfunction refers to the consistent/recurrent inability of a man to obtain an erection sufficient for satisfactory sexual activities.
                    
Penegra helps to induce a hard erection which can last for an extended duration thereby enhancing confidence, well-being, and satisfaction in men. Penegra only induces a hard erection when the penis is stimulated.\n
You can click on the audio below to listen to a short introduction of Penegra in Pidgin, if you want to.
                    
<audio_link>\n
You can buy it at any pharmacy or health store around you.
""",

                "HIV Self-test kit": """OraQuick (by DKT) is an oral swab in-home test for HIV-1 and HIV-2. It is a private and accurate way to test for HIV without the use of needles or blood and in the convenience of your home with results in as little as 20 minutes. It is the first in-home oral HIV Self-Test to be approved by WHO, NAFDAC, FMOH, and US-FDA.\n
On who can use and cannot use HIV Self-Test kit
                    
Who can use
1. Adults 18 years and above
2. Mature minors - Adolescents under the age of 18 who are married, pregnant or sexually active.
3. Children - 12 and above with supervision of guardian.
                    
Individuals taking antiretroviral drugs for prevention or treatment of HIV cannot use this kit\n
You can click to watch a video on how to use a HIV Self-Test kit
                    
<<<<<<< HEAD
https://youtu.be/ap08kSitc1c?si=duUYyhpaS_TABv63\n
=======
<video link>\n
>>>>>>> origin/main
Please call 7790 if you would like to buy this HIV Self-Test kit.
""",

                "Diaphragm": """A diaphragm or cap is a barrier method of contraception. It fits inside your vagina and prevents sperm passing through the cervix (the entrance of your womb)\n
You can click to watch a video on how to insert and remove a diaphragm and how to use a diaphragm gel in pidgin.
                    
<video embedding>\n
You can visit your nearest pharmacy or health shop to purchase"""
}
    return messages.get(key_value, SOMETHING_IS_WRONG)

<<<<<<< HEAD
import time
=======

>>>>>>> origin/main

def send_audio_to_telegram(chat_id, audio_path):
    bot_token = "6981584077:AAGZIjltmtWJ5J_6Hr_SQ1TjYZRbLCzX75Y"
    api_url = f"https://api.telegram.org/bot{bot_token}/sendAudio"
    params = {"chat_id": chat_id}
    files = {"audio": (audio_path, open(audio_path, "rb"))}
    requests.post(api_url, params=params, files=files)
<<<<<<< HEAD
#    time.sleep(5)
    #self.check_response_status(response, "Audio")
=======
    #self.check_response_status(response, "Audio")
>>>>>>> origin/main
