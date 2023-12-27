from typing import Text

locationInfo = {
    "Abia": {"ABA SOUTH": ["Save  A Life Mission Hospital,43 Azikiwe Road by St. Joseph Catholic Church Aba",
                           "Jarnis Maternity & Clinic,303E PORT HARCOURT ROAD,OPPOSITE ORIE OHAMBIAM PORT HARCOURT ROAD"],

             "UMUAHIA NORTH": ["Amarajane Hospital Umuahia,Along Ikot Ekpene Road, After Opet Junction Umuahia.",
                               "Gojehs Hospital Umuahaia,Amakama Housing Estate Before Olokoro, Umuahia"],

             "OSISIOMA NGWA":["Mount Zion Hospital Limited ,12 mount zion avenue, off ukwu-apu junction umule road, ABA,Close to Scripture Union Center Umule, Aba",
                              "UC Golden Maternity and Home Services,49 Ihodimezie World Bank Housing Estate,By Umuocham Girls Sec School.Abayi",
                              "Floxyiyke Maternity,18b Umuodu Abayi Osisioma, Aba,3 Star Hotel",
                              "Divine Link Family Clinic/Maternity,7 UBA-OBASI STREET, WORLDBANK HOUSING ESTATE, ABAYI,MAINLAND FILLING STATION MCC ROAD",
                              "Nneoma Maternity,7 Assemblies Street, off Aloma road, Aba,Green Light Hotel",
                              "Divine Link Family Clinic,7 UBA-OBASI STREET, WORLDBANK HOUSING ESTATE, ABAYI,MAINLAND FILLING STATION MCC ROAD"],

              "OBI NGWA":["Juliet Paul Hospital And Maternity,OSUSU OMUEME, OFF GLASSFORCE,GLASSFORCE COMPANY"],

              "ISIALA-NGWA NORTH":["He Reigneth Medical Services,1 EBEYI ROAD, UMUNKPEYI NVOSI, ISI ALA,UMUNKPEYI PARK"],

              "ABA NORTH":["Isaac Okwuonu Memorial Hospital,127B Ikot-Ekpene Road, Ogbor Hill,Okwundu Bus Stop",
                           "Todac Specialist Clinic & Diagnostics,61 OKIGWE ROAD, ABA,TONIMAS FILLING STATION",
                           "Kharisma Clinic and Maternity,35 Omenazu Road, Off Faulks road ,Okigwe/Brass Junction"]
             },

    "Abuja":{"ABUJA MUNICIPAL (AMAC)": ["Life point Medical center,No 64, Moses Matokodinmi, crescent Utako,Beside Big Joe Motors",
                                        "Ngozi Ben clinic,Before Alhaji Bello, Giwa,N/A",
                                        "Gem of Hope medical center,House 5 Daki Biyu Jabi",
                                        "Mayday specialist hospital and Maternity,No 1, May day hospital road opposite skye bank mararaba Abuja,N/A",
                                        "Gibonna womens hospital,No 1 Joshua madaki close Apo,N/A",
                                        "Well- life hospital limited,No 12b Arbara street, Wuse 2,N/A",
                                        "Accolade Medical Clinic,House 1D road opposite DFD pharmacy &Store before fidelity bank, sector F,FHA-Lugbe.",
                                        "Peace care clinic LTD,No 46, 3rd Avenue opposite Skye bank Gwanrinpa,Opposite Skye bank And Union Bank",
                                        "Prime care hospital,Plot 75, road 321 off 3rd Avenue, Gwarinpa, Abuja",
                                        "Garki Hospital,Garki Area 8",
                                        "Diff Hospital Abuja,Plot 1195 Cadatral Zone, Oladipo Diya  Street, Apo-Gudu Area,Gudu FCT High court",
                                        "Anointed Hospital,Behind Abdul-Abdul Fueling Station, Mararaba",
                                        "May Day Hospital,No. 1 Mayday Hospitall Road,Opposite Skye Bank Mararaba,Opposite Skye Bank",
                                        "Alliance Hospital,5, Malumfashi Close, Off Emeka Anyaoku Street, (Beside Fedex), Area 11, Garki, Abuja ,Beside Fedex",
                                        "Bepo's Clinic,10,Faskari Crescent, Garki",
                                        "Fort Ella Specialist Hospital,New site Lugbe behind Overcomer Secondary school Lubge Abuja.",
                                        "Medimax Hospital,Plot 555 Cadastral Zone, Durumi, Abuja ,Old Dunamis Church, after Garki Area 1 round-about",
                                        "Mararaba Charity Hospital,No 1, May day hospital road opposite Polaris bank mararaba Abuja",
                                        "Total care Hospital,4 Umar baza close mararaba Abuja,by melcuzebeth academy",
                                        "Freedomscan Medical Centre,Area B last Nyanya Abuja",
                                        "Cedar Crest Hospital,No. 2 Sam Mbakwe Street, District, Abuja",
                                        "Excel Specialist Hospital ,PLOT 154 Kaura District, the blue building behind Glowing Ages Academy before Human Right radio, Kaura,APO Legislative quarters",
                                        "QUEENS SPECIALIST HOSPITAL,Plot 224, Martin Ejembi Crescent, Apo - Dutse, Gudu District AMAC,Cleverfield Schools",
                                        "Thomas David Hospital,House 14, 1(K)9 Crescent,  Federal Housing Area, Sector F Junction, Lugbe,O2-Fit Gym",
                                        "Tolbert Specialist Hospital,No 17, Democracy Crescent Gaduwa Estate, Abuja, Ibeto Hotel",
                                        "Olive Green Hospital,Jikwoyi Phase 2, Opposite All Christian Fellowship Mission, Abuja,Phase 2 Junction, Jikwoyi",
                                        "Divine And Reign Ultimate Clinic,Behind Living Faith Church, Sauka Village, Along Airport Road, Abuja.,Living Faith Church, Sauka",
                                        "Trust Charitos Hospital,Mrs. Njoku Josphine,8036901261"],

             "BWARI":["Bwari Medical Center,Behind The Capital Nursery and Primary school, Zango,The Capital Nursery and Primary school, Zango",
                      "Divine Winners medical and maternity,Duste second gate Bwari area council Abuja",
                      "Medford Hospital,plot A144 mpape by katape junction Abuja",
                      "Wrisberg Hospital,Behind Amada Plaza, Angwa-Gede, Jikwoyi Phase 2, Abuja",
                      "Anglican Hospital,Gado Nasko Road 2/1 Federal Housing Kubwa Abuja,ECOBANK Kubwa"],

             "GWAGWALADA":["Well care hospital,Adjacent Abattoir gate, new Kutunku, FRCN road, Gwagwalada, FCT,N/A",
                           "Minat Hospital and maternity ,Alowa Old Zuba road Timaje Abuja FCT,Adjacent primary health centre",
                           "Jerab Hospital,Plot 145 Jeremiah Abutu Close, off FRCN Road Kutunku, Gwagwalada"]
             },

    "Adamawa":{"YOLA North":["Da'ama Specialist Hospital, Gimba Road,Shopping Complex",
                             "Peace Hospital, 2 upper lugere jimeta,BESIDE GATE 3 KASOWA"],
                             
                "DEMSA":["LCCN Health Centre,P.O.Box 21,Numan road"]
                },

    "Akwa Ibom":{"UYO":["Premier Medical services,No 3 high tension, Uyo, Akwa Ibom,Close to Monty Suites",
                        "Save  A Life Mission Hospital,60 Aka Road, Uyo, Akwa Ibom",
                        "Ark of Noah Hospital, 29 Ebong Umoitung Strt,LIVING FAITH CHURCH IKOT EBIDO",
                        "Fulcare Specialist Hospital, 15B Ekpayang Strt Uyo,IKOT EKPENE ROADIkot",
                        "Shelter'd specialist hospital,467 Oron Road Uyo, Before Shlter Afrique Junction",
                        "Mediques Plus Uyo,Plot H22 Ewet Housing Estate Uyo, Akwaibom State",
                        "Firstline Clinics and Surgery,101 Akaa Road Uyo, Akwaibom",
                        "Ubong Abasi Specialist Hospital Uyo, Aks,5 Clement Isiong Street, Uyo,UBA Bank"],
                        
                 "ESSIEN UDIM":["Good Health Specialist Hospital Uyo,30 Akpa Ube Lane, Uyo"],

                 "EKET":["Romivic Specialist Hospital, 18 Ibong Udoito Street Eket,Immernuel General Hospital Eket"]
                 },

    "Anambra":{"IDEMILI NORTH":["Divine Healing Specialist Hospital  ,10, Ezinnaya street, awada off Oriafiti Obosi, Anambra,First white house from Nkpor",
                                "Somto convalescence clinic and Maternity,Moso compound along Sardon West Avenue Ogidi Ani Ukwu, Anambra State,Moso Compound",
                                "Life Value Hospital and Maternity,No 89 Ezeiweka Road, Awada, Obosi, Anambra state",
                                "Cimac Clinics,12 Okpalikeo Str, Eziowelle",
                                "Christabel Maternity,1, Afroigwe Str Eziowelle"],
                                
                "ANAOCHA":["Chibuikem Maternity Home,Godwin Anazodo Compound, Ifiteani Village, Agulu"],
                
                "AWKA SOUTH":["Harmony Specialist Hospital,5, Orogbu street, behind Nipost HQ"],
                
                "NNEWI NORTH":["Chidera Hospital and Maternity,12 Metuh Road Nnewi,NAUTH"],
                
                "NJIKOKA":["Victory Maternity,Umudumu Village, Abagana"],
                
                "ONITSHA SOUTH":["Mexgloria Maternity, 17 Ziks Avenue Fegge, Onitsha"],
                
                "ONITSHA NORTH":["Kanayo Specialist hospital,17 Enugu road onitsha, near Onitsha high court, Anambra state,Near Onitsha high court, very close to All Cathedral Church",
                                 "Gozie Specialist Hospital,No 10 new cementery road onisha, anambra",
                                 "All Hallows Hospital,11,Ekwerekwu Close Osha,Police Area Command Office, Osha",
                                 "Save  A Life Mission Hospital,Otigba Street  Off Niger Drive, Onitsha"],
                                 
                "AWKA NORTH":["Lancet Hospitals,Odogwu Mgbakwu Complex, Isuaniocha, Awka"]
                },

    "Bauchi":{"Bauchi":["Specialist Hospital,Adamu Ajiya Road, Bauchi,GGSS Bauchi",
                        "Almanzoor Hospital,10 Rijiyan Bauchi Street, Igbo Qtrs, Bauchi,Igbo Quarters"],

              "Katagun":["Queen Amina Medical Integration,No. 1 Market road, Azaare, Bauchi state.,mir's Drive, Opposite Central Mosque Main Market, Azare",
                         "Godiya Medical Centre ,55 Old Kano road, Azare,Old Kano road",
                         "Extreme Hospital,No,403 State Low Cost Bye-pass Azare,State Low Cost",
                         "Urban Maternity PHC Centre ,Kasuwar Kaji Azare,Katagum college of health sciences/ First Bank plc."]
                },

    "Bayelsa":{"YENEGOA":["FRANK-WEST Specialist Hospital,No 21 Igbim Road, Amarata, Yenegoa, Bayelsa State.,Besides Salvation Ministries Church.",
                          "Meniscus Clinic and Maternity,No 59, Old Azikoro Road, Okaka,Mountain of Fire Junction, Okaka.",
                          "Save  A Life Mission Hospital,0 Osiri Road, Ekeki, Yenagoa",
                          "Pallen Clinic and Maternity,22 OSIRI ROAD, EKEKI, Yenegoa,EKEKI MOTOR PARK",
                          "Metrixmed Clinics, 49 Customs Road, Biogbolo, Yenagoa,Customs Road",
                          "Godly Shepherd Specialist Hospital ,14 Akoi Str, Yenezue-gene,Akoi Junction",
                          "Hilem Medical Center,Opposite Christ Embassy Church, Off Okolobiri Rd, Igbogene, Bayelsa,Okolobiri Round About"]
                },

    "Benue":{"MARKURDI":["Sandra Hospital,24 J.S Janna road,Makurdi",
                         "First Fertility Hospital,Samuel Rufus Street,Ankpa Ward,Makurdi"]
            },

    "Cross River":{"CALABAR-MUNICIPAL":["Hope Spring Clinic,79 Eta Agbor road by Orok Orok Calabar Cross river state,By Orok roundabout, close to Tutttle Bay phamarcy at Unical maingate.",
                                        "Victoria Medical Center Calabar,23 Marian Road Calabar,Atekom Junction",
                                        "Mary Mother Of Mercy Hospital Calabar,54 Spring Road, Ekorinium Calabar,House Of Assembly Head Quaters"],
                    },

    "Delta":{"ETHIOPE WEST":["St Gere Hospital,KM 4 AJAGBODUDU ROAD,  OGHARA",
                             "Enofes Medicals and Health Limited,NO 25 Otorho Road Oghara"],
                             
             "UVWIE":["West End Hospital,1,25th Street DDPA, Off Old Airport Road, Warri, Delta State."],
             
             "IKA NORTH EAST":["Somtochi Specialist clinic,42 Memeh Street Boji Boji Owa"],
             
             "OSHIMILI SOUTH":["Life Value Hospital and Maternity,No, 19 onochie Lane, off nnebisi road, Asaba, Delta state",
                               "Komfort Consult and Surgeries Hospital,No 12 Uche anianwa street, Okpanam road, Asaba, Delta state,Okpanam road",
                               "Jombo Maternity and Gynaecological Clinic, CRESCENT DIAGNOSIS BUILDING, OPPOSITE FMC ASABA BY GOOD FEKONS",
                               "Icon Clinic And Maternity, 303 Nnebisi road Asaba",
                               "Kanayo specialist Hospital and Maternity,No 10, Achina Street,Umuchu, Asaba,Asaba SCAN centre",
                               "El comfort hospital,No 1 fear God street Bonsaac Asaba, Delta state,By Bonsaac junction",
                               "Holy Cross Clinic,70 Umejei road, Ibusa"],
                               
             "BOMADI":["Amazing Grace of God Clinic,NO 10 TUOMO ROAD, AFTER SETRACO"]
             },

    "Ebonyi":{"ABAKALIKI":["Bethel Hospital , 1b Ugodan Street, off convent road, off afikpo road Abakaliki"],
              "EBONYI":["EVIDENCE SPECIALIST HOSPITAL,Odomoke Ishioke, Ebonyi LGA, Ebonyi,Ebonyi State University (Permanent site)",
                        "Doctors Specialist Hospital And Maternity,No 1 Liberty Street, Off Water Works Road, Abakaliki, Ebonyi State"]
             },

    "Edo":{"IKPOBA-OKHA":["Benin Medical Care LTD,53, Adesuwa grammar school road, Benin City Edo state",
                          "Royal Crown Hospital ,NO 7 OKHUMARUYI STREET OFF LUCKY WAY, UPPER MISSION",
                          "Supreme Clinic and Maternity ,NO 15 ROLAND OBASUYI STREET OFF LUCKY IGBINEDION WAY, BENIN"],
                          
            "OREDO":["Nicholas Brown Maternity,No 1 Anointed way KM 8 ekee sapele road",
                     "Bethel faith Medical Centre and Maternity,Plot 11 & 12 Jo's Bazuaye layout, Erediawa street off Ekewan road, Benin City, Edo state.",
                     "Emose Memorial Medical centre,23b iheya street off new lagos road Benin City, Edo state.",
                     "St Mathias Anglican Hospital,NO 35, AWO STREET OFF OMORUYI STREET OFF FIRST EAST CIRCULAR ROAD",
                     "Jonos Medical Centre,35 Second East Circular Road,Benin City",
                     "Gims Medical Center,12 Edebiri Street Off Joromi Road, Benin City Edo State",
                     "Asriel Medical Center,11 iduh Street, off college Road , off ekewan Road benin city",
                     "Devine Trinity Hospital,2 Ukponmwam Avenue off, Patrick Ehimen Street off first Ugbor GRA Benin city"],
                     
            "EGOR":["DE' Passover Clinic,171 Uwelu Road Opposite Uwasota Junction Benin City"]
            },

    "Ekiti":{"ADO EKITI":["Oguntoye Hospital,Opposite Ola-Oluwa grammar school. 136, Ilawe road, Ado Ekiti,Ola-Oluwa grammar school.",
                          "St Gregory Hospital,Km 2, Iyin road, Fajuyi park, Basiri, Ado Ekiti,Fajuyi park",
                          "Queen's Care Hospital,1, Unity Avenue, behind Falgo filling station, Iyin road, Ado Ekiti.,Falgo filling station",
                          "Unique Consulting Hospital, 1 Bawa Road, Similoluwa, Ado Ekiti"]
            },

    "Enugu":{"NSUKKA":["Divine Mercy And Maternity Hospital,32, Orba Road, Nsukka ,UAW",
                       "Divine Intervention Hospital And Maternity,59 Bernard Eze Str, Opp Addmore Filling Station, Nsukka"],
                       
             "ENUGU EAST":["St. Leo's Hospital,57, Nikelake road, Trans Ekulu, Nowas Junction Enugu",
                           "Julius Ezenyirioha Memorial Hospital &Maternity,39, Atani street, Abakpa Nike, Enugu,Peace Mass Transit, Liberty Bustop",
                           "Renoks Alpha and Maternity Hospital,Ugwogo-Nike, Enugu East, Enugu,Oye Ngwogo Market",
                           "Uchechukwu Maternity,13, Obiagu Road, Off NNPC, Emene",
                           "Ogechukwu Hospital and Maternity,No 6, Davis Umealu Street, New GRA Enugu,Mater Dei Cathoiic Church, after Nowa's filling station",
                           "Kenechukwu Specialist Hospital, 1, Thinkers Estate. Thinkers Corner, Emene. Enugu",
                           "Divine Grace Hospital And Maternity,No, 2 Anike Ugwu Street, Ifoh Layout, Abakpa Nike, Enugu State,Abakpa Nike, Enugu State",
                           "ST Gianna Specialist Hospital and Maternity,No, 6 Road 18, Upper North, Trans Ekulu-Enugu State,Trans Ekulu, Enugu State",
                           "Redeemer Maternity,2, Edible Str, Coperative Layout, Abakpa Nike, Enugu"],
                           
             "ENUGU NORTH": ["Livingston specialist Hospital.,34, Brown and Brown Crescent, Independence Layout, Enugu.,WAEC Junction",
                             "Ekwomibe Memorial Hospital.,Uno Akwa Bustop, Ngwo,9th Mile and New Market",
                             "Upper North Junction Hospital and Maternity,Road 18 House 6,Upper North 5th Trans Ekulu,Micktery Schools"],
                             
                             
             "ENUGU SOUTH":["Mercyland maternity,53 Igbariam street achara layout Enugu,Mayor Market Bus/stop",
                            "Redemption Hospital ,200c Amechi Road, off Ikenwatu Road",
                            "ST CAMILLUS Clinic And Maternity,75 New Town Layout, New Haven Extension",
                            "Emmanuel and Grace Maternity, 12 Okonkwo Ede street,Topland"],
                            
             "AMECHI":["Palms Medical Consultants,No 2 Umuchu Lane, Agbani Road,Union Boys Secondary School"]
             
             },

    "Gombe":{"Akko":["Shifa Medical Clinic,Kalshingi, Kumo Road, Beside Police Children School, Kumo",
                     "Salama Hospital,Tarsan Magarya, close to G H Kumo temporary site, Kumo",
                     "Ahajas Memorial Hospital ,Behind Hammadu Kafi Primary School, Bypass Road"]
             },

    "Imo":{"MBAITOLI":["Suncel Health Foundation,7 Ohii Street,by Ohii Junction, Off Orlu Road"],
           
           "OWERRI NORTH":["Save A Life Mission Hospital,Eli Johnson Sirleaf Road, Amakohia, IMO State.",
                           "Juliet Obi Memorial Hospital,1, Juliet Obi Hospital Road, Ubah, Mbaoma, Emii. Owerri.",
                           "God's Gift Maternity,Area 2 off Abraham Road, Egbu",
                           "Humility Specialist Hospital , Plot 35 Akwakuma Extension, Opp Akwakuma Girls School, Owerri.",
                           "Gennycare Maternity Home,Umovum Ulakwo"],
                           
            "OKIGWE":["Eve Specialist Women Hospital,Behind Road Safety Office, Opp Kelex Bread Okigwe",
                      "Ivory Clinic,13, Reverend Mann Avenue, Okigwe, Imo State,St. Mary Catholic Cathedral"],
                      
            "OWERRI-MUNICIPAL":["Eve Specialist Women Hospital,Behind Road Safety Office, Opp Kelex Bread Okigwe",
                                "Ivory Clinic,13, Reverend Mann Avenue, Okigwe, Imo State,St. Mary Catholic Cathedral"],
                                
            "OWERRI WEST":["Pool of Bethsaida Maternity,Umuanunu Junction, Obinze, Owerri"]
            },

    "Jigawa":{"Dutse":["Sambo Hospital, No 19 OFF MAIMALARI WAY TAKUR ADU'A DUTSE"]
              },

    "Kaduna":{"KADUNA SOUTH":["Nasara Specialist Hospital,No 1, Area D Ilorin Road, Marafa Estate, Kaduna,Kaduna prison and Kaduna polytechnic"],
              
              "ZARIA":["St.Luke Anglican Hospital Wusasa Zaria,Hospital Road Wusasa Zaria,Danmagaji Flyover/Kaduna Bypass"],
              
              "CHIKUN":["Mafnaz Clinic,No.5 Sultan Saad Abubakar Road, Millennium city,AA Shema Filling station"],
              
              "KADUNA NORTH":["Garden city specialist hospital,No 2 Sultan road, Ungwan Rimi GRA Kaduna,General Buhari house",
                              "Chasel Hospital,No 15, Isa Kaita Road. Ungwan Sarki GRA. Kaduna,Adjacent to Dialogue pharmacy and next to KSTLEA OFFICE."]
                },

    "Kano":{"NASARAWA": [
                "Prime Alliance multicare specialist hospital, Plot No 183 Hotoro GRA Kwanar Maggi, Nasarawa LGA, Kano state",
                "Nablus Clinic, Hotoro, Kawo giginyu, Kano",
                "Copperstone Hospital, No 5, court House close off miller road, Kano",
                "Family Clinic, Hadejia Road, yankaba, Kano"
            ],

            "DALA": [
                "Zumunci Hospital, Kofar ruwa, katsina road, Opposite Alaj filling station, Kofar ruwa"
            ],

            "KANO MUNICIPAL": [
                "International clinic and hospital ltd, 40, Niger street/2A airport Rd, kano",
                "Hajara Specialist Hospital, Plot 6&7 Yahaya Gusau Road Kano",
                "Sabon Bakin Zumo Maternity Hospital Jakara, Jakara",
                "Bamalli Nuhu Maternity Hospital, Kofar Nasarawa Kofar"
            ],

            "GWALE": [
                "UMC Zahir Hospital, Janbulo, buk road, Kano"
            ],

            "TARAUNI": [
                "AKTH, Zaria road, Kano",
                "Barewa clinic, Zaria road, Kano",
                "EHA Clinics, Lamido Crescent, Kano, Along Swiss cottage school.",
                "City Clinics and Maternity, No 149 DAURAWA QATERS KANO STATE.",
                "Triumph Clinic And Maternity, 106 New Hospital Road Kano State",
                "Dr AA7 Clinic and Maternity, Daurawa, Farin Gida Street kano."
            ],

            "GWARZO": [
                "Get well Women and Children Hospital, Kabuga road, kano, behind AA Rani filling station",
                "UMC Zahir Hospital, Kabuga road, Kano"
            ],

            "FAGGE": [
                "Good Pasture Clinic, Nomaansland, sabongari, Kano",
                "Zoputa Clinic, Nomansland, Kano",
                "Maria Ville Hospital, Jaba Estate, Kano",
                "Overcomers clinic, Sarkin yaki, Sabongari, Kano",
                "New Greenland Specialist Hospital, Sarkin yaki, Sabongari, Kano",
                "Naz Clinic and Maternity, 118 Zungeru road Nomansland",
                "Maternal and Child Health Care Center, No 9 Middle Road Sabon Gari Kano"
            ]

            },

    "Kastina":{"Katsina":["OKMOS CLINICS,IBB WAY KOFAR KAURA BY GATE ",
                          "Sauki Clinic and maternity,KIMARUSA KATSINA",
                          "K-DARA SPECIALIST CLINIC,GIDAN DAWA KATSINA STATE."]
                          
                },

    "Kebbi": {
                "Birnin Kebbi": [
                    "D.D.G Medical Center, No. 28 MECHANIC VILLAGE, BEHIND OLD MOTOR PARK, BIRNIN KEBBI",
                    "Equity Hospital, Plot 788 LP 04 Atiku Ilijo Close Off Adamum Auge Street GRA Birnin Kebbi",
                    "Taimako Clinic and Maternity, No 32 Emir Usman Road, Between Gesse Hotel and Sha'aban Supper Market, Gesse Hotel, Sha'aban Supper Market"
                ],

                "Jega": [
                    "Fauziyatu Clinic And Maternity, Yauri Road Jega, Jega Motor Park, Yauri Road"
                ]
            },

    "Kogi": {
                "DEKINA": [
                    "Good Shepherd Hospital, No 10, Ankpa road Anyimgba, Between Igala Unity square and Kogi State University"
                ],

                "LOKOJA": [
                    "Niger Hospital, 12B IBB Road, Adankolo, Lokoja , Niger, Opposite GTBank",
                    "Fisayo Hospital, Obajana Behind Anglican Church, Beside High Court, Behind the Anglican Church",
                    "LOKOJA CITY CLINIC AND MATERNITY, 2, Makira Junction beside Holy Trinity church cantonment, Lokoja",
                    "REHOBOTH SPECIALIST HOSPITAL, 2nd Gate, Phase 2 Estate, Lokoja, Opposite Harmony Secondary School",
                    "Helping Hands Women Hospital, Before T-square Hotel, near zone 8 roundabout army barracks road, Lokoja STATE: KOGI, Zone 8 roundabout"
                ],

                "YAGBA WEST": [
                    "Ecwa Hospital, 5, Hospital Road, Egbe, ECWA School of Nursing"
                ]
            },

    "Kwara": {
                "ILORIN SOUTH": [
                    "Yusjib Hospital, Opp Oando filling station, Offa Garage, Ilorin, Rohemichs school",
                    "Ola Olu Hospital, Opp Stella Obasanjo Hall, Ilorin, Stella Obasanjo hall",
                    "Premier Hospital, 1, Panat Street Old Jebba Road, Behind Kwasu Contact Office",
                    "Anchormed Hospital, 2 Niyi Aniyikaiye street off University road, University road"
                ],

                "ILORIN EAST": [
                    "Leah Medical centre, 12, Abdulkareem Adisa street, GRA Ilorin, Kwara hotels",
                    "Olanrewaju Hospital, 5, Oroago close, Sabo oke Ilorin, Sabo",
                    "Temitope Hospital, 3B, Amilegbe Sabo line, Ilorin, Sabo"
                ]
                },

    "Lagos": {
                "ALIMOSHO": [
                    "Subol hospital, 16/17 Oba Amusa Avenue, Idimu Lagos state, Subol bus-stop",
                    "Lifefount Medical center, 103 Moshalashi road, Egan Igado, Shima bus stop",
                    "Light Hospital and maternity, 15 Olumide Onanubi street, Alimosho bus stop Alimosho, Lagos, Alimosho Bus Stop",
                    "Precious gift hospital, No 1B Isolo road cele bus stop Egbe Lagos, Cele bus stop",
                    "Glad Tidings Medical center, 1 Amusa Alabi Street, Off Gbadamosi, Opesa street, Opeki Bus stop. Ipaja, Opeki Bus stop",
                    "Do- Alar Medical clinic, 15, Aliu street, Oja b/stop, Liasu Road Egbe, N/A",
                    "Solad Hospital, 16, Maria street, Baruwa Ipaja, Solad junction",
                    "Broad hospital, 13, Feyintola street, Ikotun, N/A",
                    "Doalar Hospital, 15, Aliu off liasu road Egbe., N/A",
                    "Mojol hospital, 20, Church street Shasha Bameke Moshalashi Bus stop beside mobil Egbeda., N/A",
                    "Quickcare Health center, 60 Egbeda Idimu road, Egbeda., Jendol Supermarket",
                    "Talent specialist hospital, Plot 440, 4th Avenue Gowan estate Egbeda, N/A",
                    "El-Dunamis Medical center, 17, King Solomon street Araromi bus stop off Lasu-Isheri road Akesan Lagos, N/A",
                    "Primex Hospital, 58 Unity Bus stop Igando road, Ikotun, N/A",
                    "P and G Medical center, 29, Sanni fabode street off social club road, N/A",
                    "ST Bernidith medical center, 44, Franzaki street Bucknor isolo ijegun road, Transformer from Jakande gate",
                    "Hamkad Hospital, 39, Olawale Cole Street, Abule Egba, N/A",
                    "Crystal Specialist Hospital, Akowonjo Road, Dopemu Agege, Akowonjo road",
                    "BlueSky hospital, 263 Idimu Road, Egbeda, pipeline bus stop",
                    "B-Rock Hospital, 3, Olaiya Street Ikotun, N/A",
                    "Blessing Clinic, 1, Council Street Council bustop Ikotun, N/A",
                    "CarePoint Hospital Egbeda, 7 - 9 Ogunlana street, Egbeda, Lagos, Egbeda Bus stop / Egbeda Central Mall / GTB E-centre",
                    "Krown hospital, 11 Alhaji Sekoni street, off Alimosho road, Regia Luxuria hotel send suites",
                    "Evangel Hospital, 16 Adeaga street, Awori B/stop, Abule Egba, Lagos, Awori bus stop",
                    "Blessed Hands of God Maternity centre, 1 Prosper Mukoro Street, off Adexson Vulcaniser, Akesan, Vulcanizer bus stop",
                    "Mediservices Community Hospital, 28 David Ogundele Street, Ipaja, Rosebol Petrol station",
                    "Santa Maria Hospital, 10, Santa Maria Street, Egan",
                    "Dr Express Clinics, No 5, Idimu Road, Ikotun, Opposite Ikotun Market Round About",
                    "Maciland Medical Center, 1 Lafunke street, Papa Major bus stop, Ijegun, Praise Bus stop",
                    "Bien Sante Medical Centre, 9 Alaka Street, off Bameke Shasha, Akowonjo",
                    "New Alpha Medical Centre, No. 26 Oshundairo street off Lagos Abeokuta Exp. Way Araromi B/Stop Iyana Ipaja Lagos., Iyana Ipaja B/stop",
                    "Alalade Memorial Hospital, 67 Abeokuta Expressway, Idi Mangoro, Lagos, Forte Oil filling station",
                    "Agape Medical Center, 16 Ogunbiyi Ilo Street, Olude Bus stop, Ipaja Lagos, Ayobo Round-about",
                    "Mercygate Hospital, 24 - 32 Ogunlana Street, Egbeda., Egbeda Roundabout.",
                    "Peaceful Health Hospital, 60, Ijagemo Street, Ijegun, Ijegun Roundabout."
                ],

                "AJEROMI-IFELODUN": [
                    "Jibol Medical Center, Jibol Medical center 119, Toli Road, Olodi Apapa, N/A",
                    "Hilton Hospital, 1 Itohan omo close Olodi- Apapa, Berger suya",
                    "Sonnex Hospital, 3, Emordi street, Olodi-Apapa Lagos, N/A",
                    "City Of Hope Hospital, 80, Bale Ayetoro Street, Ajegunle, N/A",
                    "Emmanuel Pauda Hospital, 8, Arumo Street, Ajegunle, N/A",
                    "Dr Express Clinics, 3, Orodu Street Ajegunle, In front of Ajegunle Market or Boundry Market",
                    "City of Hope Hospital , 80, Bale street Ajegunle"
                ],

                "Kosofe": [
                    "Gifted hands hospital, 25 Old Olowora road Isheri, N/A",
                    "Dafe Medical center, 34 Dairo street Ketu Lagos, N/A",
                    "Barbinton Medical center, No 9, Samuel Ali baba street Iyan school Ketu, N/A",
                    "Delta crown hospital and maternity, 14 Ajayi street Ketu, N/A",
                    "Sparkview hospital, 20A, Wilmer Road, Isheri-Oke, Olowora, Ojodu Berger, berger bus stop",
                    "St Patrick Hospital, 19, Adams street olojojo bus stop Oworonshoki, N/A",
                    "Strategic Insight Healthcare, 21, Raji Oladimeji Crescent, By PML Filling Station, Magodo, Lagos, PML Filling station",
                    "Queens Specialist Hospital, 3, CMD Road, Magodo, Ikosi Ketu, N/A",
                    "Magodo Specialist Hospital, 10, Jaiye Oyedotun Street, Magodo GRA, Phase 2, Shangisha, N/A",
                    "Dr Express Clinics, 2, Jimoh Balogun, Off CMD Road Ketu, Caleb Secondary School",
                    "Pink Clinic, 149 Ogudu road Ojota ogudu roundabout opp fcmb, Ogudu Roundabout",
                    "Afolabi Medcial Center, 78 Oworro link. Labule bus stop, Labule bus stop",
                    "Chion Family Medical Center, 3, Oki Lane, Mende, Maryland Lagos.",
                    "Elam Hospital, 48, Ofenbi Ogidan Street, Owode Onirin, Kosofe, Owode Bus Stop",
                    "KRYSTAL MEDICAL CENTRE, 15, Emmanuel Keshi Street, Magodo Phase II, Emmanuel Keshi Street",
                    "Lade Hospital, 17, Olatunji Ige Street Ikosi, Ketu, Ketu Market",
                    "Al-Afiat Clinic, 27, Aina Road, Agility Mile 12, Mile 12 Market",
                    "AL- Sadiq Memorial Hospital, 21, Asiyat Street, Mile 12, Mile 12 Market",
                    "Stefnita Maternity Centre, 17/18 Fatai Ayinde STreet, Irawo, Irawo, Just after the popular Mile 12 market, Lagos-Ikorodu express road.",
                    "Azir HealthCare, 47, Oduntan Street, Off Ikorodu Road Kosofe, Bus stop, Kosofe, Lagos, Kosofe bu bus stop"
                ],

                "Mushin": [
                    "Ade Jimmy Convalescent Home, 24 Wuraola bus stop Itire, N/A",
                    "Labake Clinic, 20, Alfanda street Ilasa Akanro, N/A",
                    "Kaaf Medical center, Akinpelu Adesola Road, University of Lagos (Unilag) Akoka., Unilag Medical Center, Off Unilag Business School",
                    "Able God Clinic, 52, Ijesha road, Opposite Mobil Petrol station by Adedeji Bus stop, N/A",
                    "Dr Express Clinics, 288 Agege motor road, Mushin branch., In Front Of Ojuwoye Market",
                    "Abisat Convalescent, 51 Martins street, mushin, Mushin market",
                    "Halifat Convalescent Home, 63 Iyilara Street, Isolo Rd, Mushin, General Hospital Mushin.",
                    "Royaland Trinity Healthcare, 14, Olanusi Street, Off Daleko Bus Stop"
                ],

                "Oshodi-Isolo": [
                    "FaithCity Hospital, 16, Asa Afariogun Street off Osolo way Ajao Estate, N/A",
                    "Siloan Medical center, 14/16 Mohammed Akije street Ejigbo Lagos, Iyanna Ejigbo market",
                    "Dolu Hospital, 7, Sunmola Abayomi street Mafoluku, Oshodi Lagos, Mosolasi bus stop",
                    "St Raphael hospital, No 114 Lateef Adegboyega grandmate bus stop Okota, N/A",
                    "Sentinel Hospital, 1 Benson Akinyele street Oke-Ara Isolo, N/A",
                    "Living spring hospital and maternity home, 49 Alafia Avenue Ori-Oke bus stop Ejigbo, Ori-Oke bus stop",
                    "Sentinel hospital, 1 Benson Akinyele street Oke-Ara Isolo, Jankande's Gate",
                    "Forte care hospital, 162, Ago Palace way by Gks bus stop after Forte oil filling station Ago Palace, Okota., N/A",
                    "Godscare maternity center, 36, Dosunmu street Mafoluku, N/A",
                    "Outreach Mother and Child Hospital, Cele Bustop Isolo, 125 Okota Road, N/A",
                    "Divine Grace Hospital, 3, Sobogun Rofa Mafoluku, N/A",
                    "Dr Express Clinics, 8 Suwebatu Ajala street Oshodi Apapa Express way Oshodi, Opposite Former NAFDAC Office",
                    "Syd Monic Hospital, 6, Moshobalaje Street, Ago, Okota Lagos, Ali-Dada Bustop",
                    "Kupa Medical Center, 6, Olabode Street, Ajao Estate",
                    "Unique Care Hospital, 53 Temitope St, Ilasamaja, Lagos, Dream Land Electronics",
                    "Edmac Hospital, 31 Ayodele St, Mafoluku Oshodi, Jericho Hospital",
                    "Good Health Medical Centre, 19 Oludegun Street, Ire-Akari Rd Isolo, St Mary's Catholic Church Isolo",
                    "Glory of God Maternity Home, 4, Bello Street, Off Makinde Street, Mafoluku, Oshodi., Makinde Street",
                    "Plato Hospital, 641, Agege Motor Road, Shogunle Lagos, NAF Barracks Ikeja",
                    "Kings and Queens Multi-Specialist Hospital",
                    "Long Life Hospital, 22, Owoseni Street Oshodi, Oshodi Market"
                ],

                "Ojo": [
                    "El Shaddai Hospital, K/m 4 Lasu-Isheri road, Ojo, Iyanna School",
                    "Med-Inn Specialist Hospital, 1&3 Oshogbo, off celestial way Ogudu, N/A",
                    "Ilogbo Central Hospital, 175, Ilogbo Road, Tope, Itire Bustop, Ajangbadi, N/A",
                    "CarePoint Hospital Ojo, 9, Abbi Street, (Muskat Hospital, Off Shibiri Road, Rasaki Bus stop, Ilemba Awori, Ojo, LAGOS, Shibiri Bus stop / Rasaq Bus stop",
                    "CarePoint Clinic Alaba, Shop 24, Cornerstone Plaza, Beside Zenith Alaba Phone Village., Zenith Bank / Phone Village Alaba International Market",
                    "Bonne Sante Hospital, 12, Alhaji Suleman opposite Ojo cantonment Ojo.",
                    "VIC-D Maternity Home, 1, Adebisi Arandun Street, Iba New Town, Ojo",
                    "Graceland Hospital, 147, Badagry expressway Ojo, Igbede Road Ojo or Iba Housing Estate",
                    "Ibijola Hospital Agbara, Km31, Lagos-Badagry expressway Jidah Agbara., Palatable complex beside Odo Eran Agbara.",
                    "Goodness Medical Center Iba, 151 Shibiri road Ajangbadi, opp Isashi police station",
                    "Safe Healing Hospital, 16, Summit street Victory Estate Iyana School Bstop, Lasu Isheri Expressway, Iba Lagos., Victory Estate gate, beside El Shaddai Hospital building Iba",
                    "Life Heritage Maternity and Child Center, 5, Micky street Okolo off Oreofe street Okoko, International bus stop",
                    "Healing Land Hospital, 35 Oke-Agbo Rd, Ojo, Lagos, God’s Blessing Pri School",
                    "Ancop Hospital, 10 Ahmed Street Off Emodi Street Chemist Bus Stop Alaba International Market Ojo, Alaba International Market",
                    "New Alpha Medical Centre",
                    "Treasure Hospital, No. 7 Ariyo Close, Iba, Iyana-School"
                ],

                "Ikorodu": [
                    "Barbinton Medical Center, No 3, Ade Adenaike street, Ojomo Area Ajegunle Ikorodu Lagos, N/A",
                    "Oak Hospital, 191, Lagos road, N/A",
                    "HOLY Fill HOSPITAL, 1 ONOFOWOKAN STREET OWUTU AGRIC, IKORODU",
                    "COSAN HOSPITAL, Behind LG primary school igbe Laara off Ijede",
                    "Bronk Premiere Hospital, IJEDE ROAD IKORODU, DIVINE MERCY SPECIALIST HOSPITAL",
                    "Hamaab Medical Centre, 1 Unity Avenue, Komina Crescent, Divine Mercy Catholic church",
                    "Shalom Convalescent Home, 10, Kingsley Omorhuyi Street, Morekete, Off Bayeku Road, Igbogbo, Morekete Junction",
                    "Uzopean Specialist Hospital, 3, Fatimah Bintu Street, Sholebo Estate off Ebute/Igbogbo Expressway Ikorodu, Sholebo Estate",
                    "Alifort Medical Clinic, 76, TOS Benson Road, Ebute, Ikorodu, TOS Benson Road",
                    "Lifeshade Hospital and Medical Facilities LTD, 3, Osholigbehin street off Awolowo way Ota-Ona Ikorodu, Mobil filling station by grammar school",
                    "Shola Medical Centre, 108, OBA OMOLAJA OGUNLEWE ROAD, IGBOGBO-IKORODU, OJOTA BUS STOP AFTER IGBE JUNCTION. IGBOGBO",
                    "Dasochris Hospital, 2nd Avenue Poboyeyo estate, Odogunyan Ikorodu, Odogunyan Market",
                    "Jay Kay Nursing Home, 53, Oduyebo Street, Odogunyan-Ikorodu, Odogunyan Market",
                    "The Excellence Hospital, 5, Alogba street, off Ibeshe Road, Ebute, Ikorodu, Lagos., Alogba Estate",
                    "Landmark Hospital, 46, Ikorodu-Epe Road, Akasolori Ikorodu., Sabo Market",
                    "Life Guard Hospital, 32, Babatunde Adegboyega street, Ibeshe, Ikorodu, Ibeshe market",
                    "Living Hope Clinic and Maternity, 41B, Boundary Road, Off Ita-Oluwo Ikorodu, Ita-Oluwo Bus stop",
                    "Ayo Classical Medical Center, 33, Ijesha Road Itire, Adedeji Junction or Karohunwi Bus Stop"
                ],

                "Surulere": [
                    "Uwemedimo Hospital, 5, Thanni street, Ijesha Off Ijesha Road surulere, Ijesha Police Station",
                    "His Mercy Hospital, 17, Adeyemi Street, Orile Iganmu, Off Abu Street",
                    "Peculiar Hospital, 62, Coker Road, Orile Iganmu, N/A",
                    "Angel Hospital, 20, ECWA church road, Coker Village, N/A",
                    "Dr Express Clinic, 171B Akerele road, Surulere, Opposite Havana Hospital",
                    "Iwalewa Nursing and Maternity Home, 20, erelu danisa, ijesatedo surulere lagos, Checking Point",
                    "His Glory Hospital, 59 Coker road, Orile, Coker Bustop",
                    "Boot Hospital, 47B James Robertson street, Surulere",
                    "Avon Medical Practice Ltd, 8 Adedamola Ojomo Close, off Bode Thomas St, Surulere, RCCG - Kingdom Life Chapel",
                    "Oxford Healthplus Hospital, 164 Ogunlana Drive, Surulere, Mr Biggs Masha",
                    "Primus Hospital, 272, IJESHA ROAD IJESHATEDO ITIRE, IKATE., IJESHA POLICE STATION",
                    "The Comforter Hospital, 17 Ajana Street, off Ogunlana Dr, Ijesha, Ijesha Market"
                ],

                "Agege": [
                    "Promise Medical Center, 132 Dopemu road, Dopemu, Agege Lagos, N/A",
                    "Dunia Hospital, 45, Old Oko Oba road (Abattoir), Abbatoir",
                    "May Fair Medical Center, 30, 32, Adene Street, Off Oke-Koto Agege, Oke-Koto Bustop, N/A",
                    "Good Family Hospital, 18, Oluwaseun Street, Odoeran, Ekore B/stop, Oworonshoki, N/A",
                    "Mobonike Hospital, 42 Surulere street, Bale Bus stop, Dopemu Agege., Bale Bustop",
                    "Habibat Memorial Convalescent Home, 31 Omodehinde street, Marcaz, Agege, Marcaz",
                    "All Souls Infirmary, Hospital and Maternity Centre., 8, Church Street, Agege, Pencinima Flyover"
                ],

                "Ifako-Ijaye": [
                    "Pacific Hospital, 4 Shoboyejo Street, off Iju Waterworks Road, Elliott bus stop, Iju, Lagos, Methodist Church and Oando Filling Station.",
                    "Ayodele Medical Center, 25, Jonathan Coker Road, Abule -Egba, Ifako Ijaiye, Lagos, Nigeria, N/A",
                    "AB10 Specialist Hospital, 3, Ola Street, Karaole Estate off Estate Bus Stop along College Road Ifako Ijaye, N/A",
                    "Matador Hospital, 26/28 Runsewe Estate, Lagos Abeokuta Expressway, Ahmadiya, Ifako Ijaiye, Lagos, Ahamadiya Bus Stop",
                    "Osuntuyi Hospital, 255, Iju Road, Iju Ishaga, Ifako Ijaiye, Lagos, Nigeria, Balogun Bus Stop",
                    "Longing Medical Centre, 1A Josepha Close, off Oguntona Ogundejiu Street Ajala Bustop Ojokoro, N/A",
                    "Josek Hospital, 3 Ifesowapo Street, off Muibi Street, Ajayi Road, Ogba, Ajayi Road junction.",
                    "Bayo Medical Centre, 1 Akinyele Close, off Oeemeji Street, Obawole, Omonile",
                    "Longe Hospital, No126 Olusegun Oshoba Rd, Oremote Bus Stop, Agbado, Toyin Bus Stop",
                    "Springhill Hospital, 7 Adisa Coker Street, off Yusuf Jimoh St, Obawole, Ndike Market",
                    "First Mainland Hospital, 66, Sanusi Balogun Street, Abule Egba, Ifako-Ijaye, Sani Balogun Street",
                    "Marie Claire Hospital, 1b Victory Close, Off Jibowu Estate Road U Turn Bus Stop, Abule Egba, UBA Bank"
                ],

                "Shomolu": [
                    "Ladi-lak Medical Center, 53 Igi Olugbin Street, Bariga, Lagos State, N/A",
                    "Oneness Hospital, 9 Fakorede Street, Shomolu",
                    "Maycentral Healthcare, 22 St. Finbers Road, Akoka, Beolah Diagnostic Centre, and Zenith Bank",
                    "Medol Consultant Clinic, Famous B/Stop, 54 Adaranijo St, Somolu, Pedro Primary School"
                ],

                "Lagos Mainland": [
                    "Marian Hospital, 7 Montgomery Road, Off Muritala Mohammed way, Yaba, N/A",
                    "Action Health Incorporated Lagos (AHI), 17 Lawal Street, Off Oweh Street, Fadeyi, Yaba, N/A",
                    "Total Victory Hospital, 2 Ogayemi Street, Oko Agbon Makoko, N/A",
                    "Nigeria Army Reference Hospital, 68 NIGERIA ARMY REFERENCE HOSPITAL, ALONG WAEC ROAD, YABA, LAGOS., N/A",
                    "Cottage Hospital, 18 Iwaya Road, Yaba, Onike Primary School",
                    "Theo Convalescent Centre, 78 Iwaya Road, Onike. Yaba, Oando Filling Station, Iwaya",
                    "D-Lawrence Hospital, 50 Ikorodu Road Fadeyi, Yaba Lagos, Healthcare Practitioners Association of Nigeria Office",
                    "Alpine Integrated Health Services, 15 Aje Road Sabo, Sabo-roundabout"
                ],

                "Amuwo-Odofin": [
                    "Onyems B Hospital, 16 Oba Dauda street, Ojo, Transformer bus stop(Ojo) and GRA(amuwo odofin)",
                    "Maycentral healthcare, 200 ROAD SECOND AVENUE, HOUSE 7 FESTAC, BEHIND ZENITH BANK, Zenith Bank",
                    "Outreach Mother and Child Hospital, Head Office. Festac, 4th Avenue by 3rd Avenue Junction. Festac Town., Opposite Paramount LifeCare (Diagnostic Center)",
                    "Outreach Mother and Child Hospital, No 23 Community Road by First bank, Abule Ado Satellite Town, Lagos Nigeria, N/A",
                    "Ituah Hospital, 512 Road J close Festac close to Slot complex",
                    "Safehands Medical Center, 26, Akin Mateola street Amuwo, Raji Rasaq Estate"
                ],

                "Ikeja": [
                    "Solid Rock hospital, No 6. Akinsanya street off ogunmusi ojodu, Lagos state, N/A",
                    "Motayo hospital, 3, Owodunni street off Amore street off toyin street Ikeja, St. Leo Catholic Church",
                    "Apex Care Hospital, 20, Adeniyi Jones, Avenue, Ikeja Lagos",
                    "Soteria Hospital, 2B CLAM AVENUE COME IN THROUGH CLOSE OPP NNPC FILLING STATION INSIDE THE COMPOUND OF CLAM CHURCH, NNPC filling Station",
                    "IFPF, 5 oki Lane,  Maryland, N/A",
                    "NAF Hospital (Nigerian Airforce Hospital), 661 NAAF Hospital, Sam Ethnan Airforce Base Ikeja, N/A",
                    "God's Apple City Hospital, 32 Isheri Holiday Inn, off Olaleke Taiwo, Ojodu Berger, Grammar School Police Station",
                    "Eko hospitals., 31, Mobolaji Bank Anthony Way, Ikeja., N/A",
                    "Ikeja Medical Centre, 11, Ogunmodede Street, Behind Alade Market, Off Allen Avenue Ikeja, Alade Market",
                    "Pureheart Wellness Solution Clinic, 48 Oluwaleimu Street, off Amore and off Toyin St Ikeja, beside Calabar kitchen. 1st floor Washaman building.",
                    "G and S Hospital, 15, Muyibi street Okeira, Aguda Ogba, Excellence Hotel",
                    "661 Nigerian Airforce Hospital, Idi Maina street, Shogunle, Ikeja., MMA2",
                    "J. A. Lashman Hospital, 10, Adedosu Street, Off Akilo Road, Ogba, Lagos., Akilo Road"
                ],

                "Eti-Osa": [
                    "Critical rescue international (CRI), CRI Health Centre @ VGC-Lekki, 2nd Avenue, VGC Shopping complex, VGC Estate, VGC-Lekki, Lekki, Lagos., VGC Roundabout",
                    "Q-Life Hospital, 155A, Prince Ade Odedina Street V.I, N/A",
                    "Maycentral healthcare, 132 AWOLOWO ROAD, IKOYI LAGOS. BEHIND HESS PHARMACY, OPPOSITE SPAR SUPER MARKET, BEHIND HESS PHARMACY",
                    "Vedic LifeCare Hospital, BLOCK 105, PLOT 6, OLABANJI OLAJIDE STREET, LEKKI PHASE 1, N/A",
                    "First Consultant Medical Center, 24 Ikoyi road Obalende",
                    "Klienburg Hospital Victoria Island, 6b, Abimbola Awoniyi street victoria island lagos.",
                    "Eti Osa Maternal and Child Center, 10, Abraham Adesanya Road, Ogombo Town, Ajah",
                    "Ifeoluwa Hospital, Block 380, Flat 2 Jakande Estate, Ilasan Lekki Lagos, St Kizito Clinic, Jakande",
                    "Precious and Praise Clinic and Maternity, 3 Afariogu close off lord's way, marshy hill estate, Akins Bus stop, Addo road, Genesis Event Centre",
                    "Ifeoluwani Convalescence Health Centre, 1, Noibi street, Igando, Ibeju Lekki, Igando Bus-stop"
                ],

                "Badagry": [
                    "The Great Physician hospital, 3, Niyi Adebule Street, Former Nepa office, Alakija, Badagry",
                    "Era Medical Centre, 72, afromedia road, odan_era, lagos, Afromedia",
                    "Iwalewa Hospital Nursing and Maternity (Annex), Address: No 10 Hassan Iwalewa str, checking point bustop. Ibiye badagry express road.",
                    "God's Kingdom of Life Hospital (Popularly known as GODZOF), 9, Ogundipe street, off check point bus stop, Badagry",
                    "A-Harmony Hospital Badagry, 10, Ekundayo Road Badagry",
                    "Everlife hospital Ijanikin, 3, Peter Edojo street Ijanikin, Ijanikin busstop.",
                    "Ademola Hospital Ijanikin, 1, omowale street Ijanikin, opposite Cele bustop ijanikin"
                ],

                "Lagos Island": [
                    "Fuja hospital, 22, Elegbata street, Apongbon Lagos Island Lagos state",
                    "Fehintola Hospital, No 2, Olushi Street Lagos Isaland, Opposite Forte Filling Station",
                    "Awoliyi Memorial Hospital And Maternity, 183, Massey Bamgbose Street, Lagos Island, ST. Nicholas Hospital"
                ],

                "Apapa": [
                    "Ifeoluwa hospital, 12, Turner Eradiri, Ojo Road, Apapa, Lagos, Pcn bus stop",
                    "Bayo Ogunro Memorial Hospital, 160, kirikiri road olodi Apapa, Church of latter day saint, close to 2nd Benue bustop."
                ],

                "Epe": ["Soneli hospital, KM 10 Freezone way magbon Ibeju lekki"],

                "Ibeju/Lekki": [
                    "Clearview Hospital, 14B, Taiye Olowu street off victoria Arobieke lekki, N/A",
                    "Lagos Reproductive Health center, 17, Osapa Road, Osapa London Jakande, Lekki Epe Road., Beside First City Hospital",
                    "Assalam Hospital, KM 34, Lekki Epe Express Way, Lakowe, Ibeju Leki, Lakowe Golf",
                    "Awoyaya Hospital, Akinyemi Close off Ogunlana crescent Awoyaya, N/A",
                    "Arubah Hospital Family medical center, No 9, Kudirat Salami Street Lekki",
                    "Landmark Hospital, Ikorodu, 17, Alh Kamadeen Oriola Drive, Amala City Restaurant",
                    "The Pearls Specialist Medical Centre, 9, Olawale Onitiri cole avenue, off Admiralty Road, Lekki Phase 1, Evercare Hospital"
                ]

             },

    "Nasarawa": {
                "Lafia": [
                    "Police Clinic Lafia - Jos Road, Lafia Nassarawa State, Taal Conference Hotel",
                    "Dalhatu Araf Special Hospital, Lafia - Shendam Road Lafia, Hospital Management Board",
                    "Kowa Hospital - Shendam Road Lafia, Opposite Dalhatu Araf Specialist Hospital, Lafia",
                    "Diamond Clinic and Maternity - Opposite Emmanuel Baptist Church. Tudun Gwandara, Lafia, Opposite Emmanuel Baptist Church"
                ],

                "Karu": [
                    "Alhery Clinic - Alheri ifeoluwa medical Centre up market jankawan road Masaka Karu LGA, Up Market Jankawan",
                    "Mojilla Hospital LTD - No. 60 Aso District, Nassarawa, Maria Asumpta School",
                    "Primary Healthcare Centre (PHC) Mararaba - Old Karu Road, Mararaba Nasarawa State, Mararaba Market",
                    "Blessed Trinity Hospital Mararaba - Criss Park Road, Mararaba Nasarawa State, Young Shall Grow Park",
                    "Accordia Hospitals - Opp, Tipper Garage, Ruga Juli Off Mararaba, Ruga Market",
                    "Special Care Hospital, Kabayi - Kabayi Before Bridge, Off Sharp Corner, Mararaba, Sharp Corner Mararaba",
                    "Vicar Hospital - Near Deeper Life Church, Kabayi Off Maraba, Deeper Life Church Karu",
                    "Healthclone Consult Limited - No. 1 Ali Amodu Close Opp Sky Bank CBN Junction karu., CBN Junction"
                ],

                "Nasarawa": [
                    "Kuana Clinic and Maternity. - Opposite Ruga market Mararaba, Ruga Market"
                ],
                "Doma": [
                    "Aida Hospital - No. 2 Hospital Road, Doma, General Hospital Doma"
                ],
                "Keffi": [
                    "Nagari Aliah Magani Hospital - No 10 Alh Burga road, Adjacent high court keffi nasarawa state, First Bank",
                    "Destiny clinic New Nyanya - Behind Amasco filling station, Karu New Nyayan, Amasco Filling station (there are bike men at the junction beside the filling station ask them to lead you to the clinic)",
                    "Masaka Central Hospital & Maternity - 100 Royal College Road, Masaka Nasarawa State, Royal College",
                    "Mayday specialist hospital and Maternity - No 1, May day hospital road opposite skye bank mararaba Abuja, N/A",
                    "Woore Hospital - No 1 Tafawa Balewa Street Opposite GTBank Maraba beside Jaiz bank, Jaiz Bank",
                    "Kauna Clinic - Ruga market Mararaba, Karu LGA: Keffi",
                    "Kauna Hospital - Behind Winners Church Keffi, Winners Church Keffi"
                ]
                },

    "Niger": {
                "Suleja": [
                    "Suzan Memorial Clinic And Maternity - Uphill, Near Suleja Club, GRA, Old NTA Suleja Club"
                ],
                "Chanchaga": [
                    "Divine Faith Medical Clinic - No. 26, OFF NITECO ROAD, BESIDE BANANA HOUSE, CLOSE TO GIDAN IBETO, TUNGA LOW-COST, MINNA, Banana House",
                    "MCH Minna - Old Airport Road, Niger State, Government House"
                ],
                "Bida": [
                    "Yebosoko Specialist hospital - Near former musain guesthouse, Bida, Niger, Emir's palace"
                ],
                "Bosso": [
                    "Charles Hospital - GRA Road, Suleja Between Union Bank & NTA, GRA",
                    "Olives Hospital - Beside Kingdom Heritage Gbaiko close to st. clement sec school",
                    "Top Medical Hospital - 4 Top medical road minna",
                    "Blossom Specialist Hospital - Besides MJ Wushishi estate Minna"
                ],
                "Tafa": [
                    "PHC Chachi - OPPOSITE CHACHI PRIMARY SCHOOL, BEHIND NANA OIL, ALONG KADUNA ROAD, CHACHI PRIMARY SCHOOL BEHIND NANA OIL."
                ]
                },

    "Ogun" : {
                "IFO": [
                    "Sam Steve Hospital, 8 Omotosho Close, Abule Ojo Bus stop. Ogun State.",
                    "Heritage Hospital, 102 Opeoluwa Rd, Ita-Oshin, Abeokuta, Ogun State., Ita-Oshin Garage",
                    "DABFEK CLINIC AND MATERNITY, Olodo Igbala Gasline, Itoki Lemode, Tiper Garage, Gasline.",
                    "AL HASSAN CLINIC AND MATERNITY, 9 Ajisefini Street, Itoki, Gasline Bus stop",
                    "As Images Clinic and Maternity Home, 12 Abiodun Funmilayo street, Ifesowapo Estate, Moricas Akute, Ogun State, Jolasco bus stop, Akute.",
                    "Mapro Lifespring Hospital, 6 Ogunjobi Olota Off Ojusango Street Vespa Bus Stop, Vespa Bus Stop"
                ],

                "ADO-ODO/OTA": [
                    "St Shiloh Hospital, No2, Popoola Street, Igbala, Sango, Igbala Bus stop",
                    "Ace Medicare Clinics Limited, Km 4, Idiroko road, Ota, Justrite/Jehovah Witness",
                    "Rubee medical center LTD, Km 38 Abeokuta Express way Igbala bus stop, Igbala Bus stop",
                    "Kaytuns clinics, 2 Ahmed Kayode street, Arinko Housing Estate, Sango",
                    "Sure Mercy Hospital, 1 Anuoluwapo street off coca cola road, oju-ore, Ota"
                ],

                "IJEBU NORTH": [
                    "Great Dominion Clinic and Maternity, 1/3 Botu st, Off Molusi College rd, Okesopin, Ijebu Igbo, Ogun State., Balogun South area",
                    "Dairo Hospital, 3 Ogunaike close, Cele Ibadan bus stop, Adiyan, Agbado junction",
                    "Olabisi Onabanjo University Teaching Hospital (Annex)",
                    "Blessed clinics and maternity home,5, Aiyegbami-Ikansi quarters, Oru-Ijebu"
                ],

                "ABEOKUTA SOUTH": [
                    "Besh Life Care, 3 Rotimi Koleosho st, Motef Sch Rd, Gbonagun, Abeokuta., N/A",
                    "Olabisi Onabanjo University Teaching Hospital (Annex), Olabisi Onabanjo University Teaching Hospital Anne, Shage, Shage",
                    "FMC ABEOKUTA FAMILY PLANNING UNIT, BISI ONABANJO WAY, IDI ABA, ABEOKUTA, OGUN STATE",
                    "Emiloju Crystal Clinic & Maternity, 6 Abanise St, Adikuta, Oke Aregba, Carwash, iyana cele",
                    "ACCESS MEDICAL CENTRE, Lukosi estate, Leme Abiola way, Abeokuta, IBDEC OFFICE",
                    "Redwood Clinics, 9 Gani Egbeyemi Street, Opposite Car wash, Agbeloba",
                    "Atoke Medcial Center, EWANG EXTENSION, TEKOBO ROAD, IDI ABA, ABEOKUTA",
                    "Egba Medical Centre, 67B, nawardeen road, Oke yeke",
                    "Apata Iye Clinic and Maternity, 29 Moshalasi Jimoh road, Odo Oyo, Abeokuta",
                    "Health hood clinic and maternity, 2 Jide Taiwo close, Olohunda community, Idi Aba",
                    "Holy Micheal Clinic, 96 NUD ROAD, OKE YEKEN, ABEOKUTA",
                    "Praise Clinic and Maternity Centre, 36 EKUNDAYO STREET, IJEUN TITUN",
                    "E-care Clinic and wellness Center, KM 91, ABEOKUTA IBADAN EXPRESS ROAD, ASERO, ABEOKUTA, MUDA LAWAL STADIUM",
                    "Olufunmi Specialist Hospital, 16 Adegboyega street, Asero Housing Estate, Abeokuta",
                    "State Hospital Ijaye, Ogun state general hospital, Ijaye, Abeokuta",
                    "Itunu Hospital, 48 Tinubu Street, Ita Eko, Abeokuta, Adjacent Super foods",
                    "ATS Clinic and Maternity, 1 Baba Oja Building, Aregbesola, Obantoko, Abekuta"
                ],

                "SAGAMU": [
                    "Olabisi Onabanjo University Teaching Hospital, Olabisi Onabanjo University Teaching Hospital Sagamu",
                    "Twin Specialist Clinic, 11 Gunwa Ola street, GRA quarters off Paddy Arikawe Avenue, Sagamu, Paddy Arikawe Avenue Sagamu",
                    "MEDYTOP SPECIALIST HOSPITAL, 3 Ejimo Alibiosu Street off Isale-Ojumele Junction, Isale-Ojumele Junction.",
                    "Owokoniran Memorial Hospital, 3 Owokoniran Street Hospital Road, Sagamu, Ogun State, Makun Bustop",
                    "Omapas Clinic, 30 Unity Street, Off Escoba, Ogijo, Sagamu, Escoba",
                    "Idera Hospital, Ajaka Power Line, Sagamu, Power Line",
                    "Azores Clinic and Maternity Home Ogijo, 12 Aina Street Ori-Okuta, Ogijo, Ori-Okuta"
                ],

                "OBAFEMI-OWODE": [
                    "Medic Plus Hospital, 3 Omu Arogun Junction, Mowe/Ofada road Mowe, Total Fueling Station",
                    "Beachland Hospital, plot 16 Al Firdaus Estate, Off Lagos Ibadan Express Way, Arepo, Ogun State.",
                    "Iyaniwura Specialist Hospital, Olujobi Falana close, Mowe., Mowe bus stop",
                    "Redeemed Christian Church of God Health Centre, Redeemed Christian Church of God Health Centre, Camp Premises, Camp Ground",
                    "TOBILOBA CLINIC AND MATERNITY CENTRE, 1 TOBILOBA ROAD, KUFORIJI, OLUBI ADIGBE",
                    "Riverside Medical Center, Ibafo, Omolaja Odunmaku street, off Oremeji Bus stop Ibafo, Obafemi-Owode LG, Ogun, Ibafo market"
                ],

                "ABEOKUTA NORTH": [
                    "Daverose Hospital, Federal Housing Estate, Opposite Dr Anjorin group of school Olomoore, Dr Anjorin group of school Olomoore"
                ],

                "YEWA SOUTH": [
                    "Ore Ofe Clinic and Maternity home, Tunde Ibikunle road, adjacent Federal Polytechnic, Ilaro, Ogun state",
                    "Queens Hospital, 2 Ilupeju street, Oke Ola, Ilaro",
                    "Biolak Clinic and Maternity, AKINNIKU QUARTERS, OFF UDOJI ROAD, POWER LINE JUNCTION",
                    "Hossanah specialist hospital, Federal Polytechnic express road, Ilaro"
                ],

                "IJEBU ODE": [
                    "El Shadai Specialist Hospital, Beside MRS Filling Station Ijebu-Ode Town, MRS Filling Station Ijebu-Ode Town",
                    "Halajor Memorial Specilislist Hospital, 24 Tayo Sonoiki street, Golden estate off Ibadan road, Irewon, Ijebu Ode, Ibadan Garage road"
                ],

                "IPOKIA": [
                    "God's Time Clinic and Maternity, Idi Iroko, BESIDE DEEPER LIFE CHURCH, OJUREKO, IDI IROKO"
                ],

                "ODEDA": [
                    "Alless Trinity Hospital, 8 Taiwo Ogundeyi Street, Bode Olude Junction, Elega",
                    "Omo Arewa Health Care Foundation, opposite Odeda local government secretariat, Odeda",
                    "Samdok clinics and maternity, Abeokuta/ Ibadan road",
                    "Awolola Memorial Hospital, KM 9 Abeokuta/Ibadan road, Camp junction before Osiele, Abeokuta"
                ],

                "IMEKO-AFON": [
                    "Otobi Quality Health Care, SANKA ROAD, IMEKO, OGUN STATE"
                ],

                "REMO NORTH": [
                    "Healing Spring Medical Centre, 23 Ilisan Rd, Iperu Remo, Remo LGA Office"
                ],

                "MOWE": [
                    "Lotto central Hospital, 7 Aminu Kolade Street, Lotto, Mowe, Ogun state, Lotto junction"
                ]
             },

    "Ondo": {
                "AKURE SOUTH": [
                    "New day Medical Services, N0 9 Owo Avenue, Ijapo Estate"
                ],
                "AKURE NORTH": [
                    "Key of David Hospital and Fertility Center, 10 hospital lane, Beside state specialist hospital, Akure",
                    "Tim Unity Specialist Hospital, Olukayode House Opp FCMB, Akure"
                ]
             }


}





def get_clinic_info(state, lga) -> Text:

    try:
        return "\n\n".join(locationInfo[state][lga])
    except KeyError:
        return "State or LGA not defined"