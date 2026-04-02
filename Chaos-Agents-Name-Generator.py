import streamlit as st
from wonderwords import RandomWord
import random
import names

r = RandomWord()
st.title("Chaos Agents Name Generator")

clausius_names = [
    # A
    "Aeloria","Aenira","Aeshala","Aevyra","Aelthira","Ariqen","Aravelle","Arisyn","Alyndra","Avarine",
    "Ashalyn","Ashyra","Azerai","Azerelle","Aeluna","Aelvara","Aelthys","Arielleth","Arivana","Ariselle",
    "Avenya","Avyssia","Aylindra","Aylira","Aylith","Ayshera","Aysira","Azerith","Azhalia","Azmira",
    "Azrynn","Aeloriah","Aenalyth","Aerysha","Aerynna","Aerythia","Ariqessa","Arilyth","Arivessa","Arlyndra",
    "Ashalithe","Ashyelle","Ashyvana","Avelynne","Averessa","Avyrith","Ayliss","Ayshera","Aysylia","Azhalyn",
    "Azmirae","Azryelle","Aelthirae","Aenalyra","Aeryssia","Arivelle","Averyn",

    # B
    "Baelira","Baeshyn","Balyra","Barithia","Belassa","Belthira","Benalyth","Beressa","Bethyra","Beylira",
    "Bhalira","Bharissa","Bhelaya","Bhenira","Bhyssara","Biashara","Bilynne","Birassa","Birelle","Bisarya",
    "Bivessa","Biyara","Blaeryn","Blaessia","Blayra","Blenira","Blyssara","Boressa","Borynthia","Bralynne",
    "Brayessa","Brelith","Brenyra","Brisaya","Brithara","Bryelle","Brylassa","Bryssira","Bynessa","Byrithia",
    "Byssara","Baelissa","Belanyra","Bharaya","Bhelissa","Bhyrella","Biasharae","Biralyth","Bivara","Blyrissa",
    "Boressyn","Braylith","Bryssaya","Byrassa","Byrelle","Byssira","Bhalynne",

    # C
    "Caelira","Caeryn","Calessa","Calynra","Camyra","Caralyth","Carissael","Carynthia","Cashera","Casyra",
    "Cavessa","Caylira","Cazmira","Cazrynn","Celaira","Celessa","Celithra","Celyra","Ceralyth","Cerissa",
    "Cerynthia","Ceshalyn","Cevyra","Ceylissa","Cezhara","Chaelyra","Chalessa","Chalyth","Charissa","Chavira",
    "Chaylith","Chellara","Chenyra","Cheryssa","Cheshalia","Chivara","Chyressa","Cilaira","Cinessa","Cinythra",
    "Cisarya","Civessa","Ciyara","Claeryn","Clalessa","Clanyra","Clerissa","Cleyra","Clyssara","Coressa",
    "Coralyth","Coryssa","Cressaya","Crylissa","Cyshera","Cyzmira","Cylassa",

    # D
    "Daelira","Daessyn","Dalyra","Danessa","Danythra","Daralyth","Darissa","Darynthia","Dashera","Dasyra",
    "Davessa","Daylira","Dazmira","Dazrynn","Delaira","Delessa","Delithra","Delyra","Deralyth","Derissa",
    "Derynthia","Deshalyn","Devyra","Deylissa","Dezhara","Dhaelyra","Dhalessa","Dhalynra","Dharissa","Dhavira",
    "Dhaylith","Dhellara","Dhenyra","Dheryssa","Dheshalia","Dhivara","Dhyressa","Dilaira","Dinessa","Dinythra",
    "Disarya","Divessa","Diyara","Dlaeryn","Dlalyssa","Dlanyra","Dlerissa","Dleyra","Dlyssara","Doressa",
    "Doralyth","Doryssa","Dressaya","Drylissa","Dyshera","Dyzmira","Dylassa",

    # E
    "Eaelira","Ealynra","Eanessa","Earynthia","Eashira","Easylia","Eavessa","Eaylira","Eazmira","Eazrynn",
    "Ecelira","Ecessa","Ecelith","Ecelyra","Ecerissa","Ecynra","Ecythia","Ecyssa","Edalyra","Edanessa",
    "Edaryth","Edeshara","Edevyra","Edeylia","Edezhara","Efaelyra","Efalyssa","Efanyra","Eferissa","Efivara",
    "Efressa","Efyra","Egalyth","Egenyra","Egerissa","Eglyssa","Ehalira","Ehalyssa","Ehanira","Eharyth",
    "Eheshalia","Ehivara","Ehressa","Eilaira","Eilessa","Eilithra","Eilyra","Einara","Eiralyth","Eirissa",
    "Eiryssa","Eisarya","Eivessa","Eiyara","Ejalyth","Ejaryssa","Ejylassa",

    # F
    "Faelira","Faelyss","Falynra","Fanessa","Fanythra","Faralyth","Farissa","Farynthia","Fashera","Fasyra",
    "Favessa","Faylira","Fazmira","Fazrynn","Felaira","Felessa","Felithra","Felyra","Feralyth","Ferissa",
    "Ferynthia","Feshalyn","Fevyra","Feylissa","Fezhara","Fhaelyra","Fhalessa","Fhalynra","Fharissa","Fhavira",
    "Fhaylith","Fhellara","Fhenyra","Fheryssa","Fheshalia","Fhivara","Fhyressa","Filaira","Finessa","Finythra",
    "Fisarya","Fivessa","Fiyara","Flaeryn","Flalessa","Flanyra","Flerissa","Fleyra","Flyssara","Foressa",
    "Foralyth","Foryssa","Fressaya","Frylissa","Fyshera","Fyzmira","Fylassa",

    # G
    "Gaelira","Gaelyss","Galynra","Ganessa","Ganythra","Garalyth","Garissa","Garynthia","Gashera","Gasyra",
    "Gavessa","Gaylira","Gazmira","Gazrynn","Gelaira","Gelessa","Gelithra","Gelyra","Geralyth","Gerissa",
    "Gerynthia","Geshalyn","Gevyra","Geylissa","Gezhara","Ghaelyra","Ghalessa","Ghalynra","Gharissa","Ghavira",
    "Ghaylith","Ghellara","Ghenyra","Gheryssa","Gheshalia","Ghivara","Ghyressa","Gilaira","Ginessa","Ginythra",
    "Gisarya","Givessa","Giyara","Glaeryn","Glalessa","Glanyra","Glerissa","Gleyra","Glyssara","Goressa",
    "Goralyth","Goryssa","Gressaya","Grylissa","Gyshera","Gyzmira","Gylassa",

    # H
    "Haelira","Haelyss","Halynra","Hanessa","Hanythra","Haralyth","Harissa","Harynthia","Hashera","Hasyra",
    "Havessa","Haylira","Hazmira","Hazrynn","Helaira","Helessa","Helithra","Helyra","Heralyth","Herissa",
    "Herynthia","Heshalyn","Hevyra","Heylissa","Hezhara","Hhaelyra","Hhalessa","Hhalynra","Hharissa","Hhavira",
    "Hhaylith","Hhellara","Hhenyra","Hheryssa","Hheshalia","Hhivara","Hhyressa","Hilaira","Hinessa","Hinythra",
    "Hisarya","Hivessa","Hiyara","Hlaeryn","Hlalyssa","Hlanyra","Hlerissa","Hleyra","Hlyssara","Horessa",
    "Horalyth","Horyssa","Hressaya","Hrylissa","Hyshera","Hyzmira","Hylassa",

    # I
    "Iaelira","Iaelyss","Ialynra","Ianessa","Ianythra","Iaralyth","Iarissa","Iarynthia","Iashera","Iasyra",
    "Iavessa","Iaylira","Iazmira","Iazrynn","Ielaira","Ielessa","Ielithra","Ielyra","Ieralyth","Ierissa",
    "Ierynthia","Ieshalyn","Ievyra","Ieylissa","Iezhara","Ihaelyra","Ihalessa","Ihalynra","Iharissa","Ihavira",
    "Ihaylith","Ihellara","Ihenyra","Iheryssa","Iheshalia","Ihivara","Ihyressa","Ilaira","Ilessa","Ilythra",
    "Isarya","Ivessa","Iyara","Ilaeryn","Ilalessa","Ilanyra","Ilerissa","Ileyra","Ilyssara","Ioressa",
    "Ioralyth","Ioryssa","Iressaya","Irylissa","Iyshera","Iyzmira","Iylassa",

    # J
    "Jaelira","Jaelyss","Jalynra","Janessa","Janythra","Jaralyth","Jarissa","Jarynthia","Jashera","Jasyra",
    "Javessa","Jaylira","Jazmira","Jazrynn","Jelaira","Jelessa","Jelithra","Jelyra","Jeralyth","Jerissa",
    "Jerynthia","Jeshalyn","Jevyra","Jeylissa","Jezhara","Jhaelyra","Jhalessa","Jhalynra","Jharissa","Jhavira",
    "Jhaylith","Jhellara","Jhenyra","Jheryssa","Jheshalia","Jhivara","Jhyressa","Jilaira","Jinessa","Jinythra",
    "Jisarya","Jivessa","Jiyara","Jlaeryn","Jlalyssa","Jlanyra","Jlerissa","Jleyra","Jlyssara","Joressa",
    "Joralyth","Joryssa","Jressaya","Jrylissa","Jyshera","Jyzmira","Jylassa",

    # K
    "Kaelira","Kaelyss","Kalynra","Kanessa","Kanythra","Karalyth","Karissa","Karynthia","Kashera","Kasyra",
    "Kavessa","Kaylira","Kazmira","Kazrynn","Kelaira","Kelessa","Kelithra","Kelyra","Keralyth","Kerissa",
    "Kerynthia","Keshalyn","Kevyra","Keylissa","Kezhara","Khaelyra","Khalessa","Khalynra","Kharissa","Khavira",
    "Khaylith","Khellara","Khenyra","Kheryssa","Kheshalia","Khivara","Khyressa","Kilaira","Kinessa","Kinythra",
    "Kisarya","Kivessa","Kiyara","Klaeryn","Klalyssa","Klanyra","Klerissa","Kleyra","Klyssara","Koressa",
    "Koralyth","Koryssa","Kressaya","Krylissa","Kyshera","Kyzmira","Kylassa",

    # L
    "Laelira","Laelyss","Lalynra","Lanessa","Lanythra","Laralyth","Larissa","Larynthia","Lashera","Lasyra",
    "Lavessa","Laylira","Lazmira","Lazrynn","Lelaira","Lelessa","Lelithra","Lelyra","Leralyth","Lerissa",
    "Lerynthia","Leshalyn","Levyra","Leylissa","Lezhara","Lhaelyra","Lhalessa","Lhalynra","Lharissa","Lhavira",
    "Lhaylith","Lhellara","Lhenyra","Lheryssa","Lheshalia","Lhivara","Lhyressa","Lilaira","Linessa","Linythra",
    "Lisarya","Livessa","Liyara","Llaeryn","Llalyssa","Llanyra","Llerissa","Lleyra","Llyssara","Loressa",
    "Loralyth","Loryssa","Lressaya","Lrylissa","Lyshera","Lyzmira","Lylassa",

    # M
    "Maelira","Maelyss","Malynra","Manessa","Manythra","Maralyth","Marissa","Marynthia","Mashera","Masyra",
    "Mavessa","Maylira","Mazmira","Mazrynn","Melaira","Melessa","Melithra","Melyra","Meralyth","Merissa",
    "Merynthia","Meshalyn","Mevyra","Meylissa","Mezhara","Mhaelyra","Mhalessa","Mhalynra","Mharissa","Mhavira",
    "Mhaylith","Mhellara","Mhenyra","Mheryssa","Mheshalia","Mhivara","Mhyressa","Milaira","Minessa","Minythra",
    "Misarya","Mivessa","Miyara","Mlaeryn","Mlalyssa","Mlanyra","Mlerissa","Mleyra","Mlyssara","Moressa",
    "Moralyth","Moryssa","Mressaya","Mrylissa","Myshera","Myzmira","Mylassa",

    # N
    "Naelira","Naelyss","Nalynra","Nanessa","Nanythra","Naralyth","Narissa","Narynthia","Nashera","Nasyra",
    "Navessa","Naylira","Nazmira","Nazrynn","Nelaira","Nelessa","Nelithra","Nelyra","Neralyth","Nerissa",
    "Nerynthia","Neshalyn","Nevyra","Neylissa","Nezhara","Nhaelyra","Nhalessa","Nhalynra","Nharissa","Nhavira",
    "Nhaylith","Nhellara","Nhenyra","Nheryssa","Nheshalia","Nhivara","Nhyressa","Nilaira","Ninessa","Ninythra",
    "Nisarya","Nivessa","Niyara","Nlaeryn","Nlalyssa","Nlanyra","Nlerissa","Nleyra","Nlyssara","Noressa",
    "Noralyth","Noryssa","Nressaya","Nrylissa","Nyshera","Nyzmira","Nylassa",

    # O
    "Oaelira","Oaelyss","Oalynra","Oanessa","Oanythra","Oaralyth","Oarissa","Oarynthia","Oashera","Oasyra",
    "Oavessa","Oaylira","Oazmira","Oazrynn","Oelaira","Oelessa","Oelithra","Oelyra","Oeralyth","Oerissa",
    "Oerynthia","Oeshalyn","Oevyra","Oeylissa","Oezhara","Ohaelyra","Ohalessa","Ohalynra","Oharissa","Ohavira",
    "Ohaylith","Ohellara","Ohenyra","Oheryssa","Oheshalia","Ohivara","Ohyressa","Oilaira","Oinessa","Oinythra",
    "Oisarya","Oivessa","Oiyara","Olaeryn","Olalyssa","Olanyra","Olerissa","Oleyra","Olyssara","Oressa",
    "Oralyth","Oryssa","Oressaya","Orylissa","Oyshera","Oyzmira","Oylassa",

    # P
    "Paelira","Paelyss","Palynra","Panessa","Panythra","Paralyth","Parissa","Parynthia","Pashera","Pasyra",
    "Pavessa","Paylira","Pazmira","Pazrynn","Pelaira","Pelessa","Pelithra","Pelyra", "Qaelira","Qaelyss","Qalynra","Qanessa","Qanythra","Qaralyth","Qarissa","Qarynthia","Qashera","Qasyra",
    "Qavessa","Qaylira","Qazmira","Qazrynn","Qelaira","Qelessa","Qelithra","Qelyra","Qeralyth","Qerissa",
    "Qerynthia","Qeshalyn","Qevyra","Qeylissa","Qezhara","Qhaelyra","Qhalessa","Qhalynra","Qharissa","Qhavira",
    "Qhaylith","Qhellara","Qhenyra","Qheryssa","Qheshalia","Qhivara","Qhyressa","Qilaira","Qinessa","Qinythra",
    "Qisarya","Qivessa","Qiyara","Qlaeryn","Qlalyssa","Qlanyra","Qlerissa","Qleyra","Qlyssara","Qoressa",
    "Qoralyth","Qoryssa","Qressaya","Qrylissa","Qyshera","Qyzmira","Qylassa",

    # R (57)
    "Raelira","Raelyss","Ralynra","Ranessa","Ranythra","Raralyth","Rarissa","Rarynthia","Rashera","Rasyra",
    "Ravessa","Raylira","Razmira","Razrynn","Relaira","Relessa","Relithra","Relyra","Reralyth","Rerissa",
    "Rerynthia","Reshalyn","Revyra","Reylissa","Rezhara","Rhaelyra","Rhalessa","Rhalynra","Rharissa","Rhavira",
    "Rhaylith","Rhellara","Rhenyra","Rheryssa","Rheshalia","Rhivara","Rhyressa","Rilaira","Rinessa","Rinythra",
    "Risarya","Rivessa","Riyara","Rlaeryn","Rlalyssa","Rlanyra","Rlerissa","Rleyra","Rlyssara","Roressa",
    "Roralyth","Roryssa","Rressaya","Rrylissa","Ryshera","Ryzmira","Rylassa",

    # S (57)
    "Saelira","Saelyss","Salynra","Sanessa","Sanythra","Saralyth","Sarissa","Sarynthia","Sashera","Sasyra",
    "Savessa","Saylira","Sazmira","Sazrynn","Selaira","Selessa","Selithra","Selyra","Seralyth","Serissa",
    "Serynthia","Seshalyn","Sevyra","Seylissa","Sezhara","Shaelyra","Shalessa","Shalynra","Sharissa","Shavira",
    "Shaylith","Shellara","Shenyra","Sheryssa","Sheshalia","Shivara","Shyressa","Silaira","Sinessa","Sinythra",
    "Sisarya","Sivessa","Siyara","Slaeryn","Slalyssa","Slanyra","Slerissa","Sleyra","Slyssara","Soressa",
    "Soralyth","Soryssa","Sressaya","Srylissa","Syshera","Syzmira","Sylassa",

    # T (57)
    "Taelira","Taelyss","Talynra","Tanessa","Tanythra","Taralyth","Tarissa","Tarynthia","Tashera","Tasyra",
    "Tavessa","Taylira","Tazmira","Tazrynn","Telaira","Telessa","Telithra","Telyra","Teralyth","Terissa",
    "Terynthia","Teshalyn","Tevyra","Teylissa","Tezhara","Thaelyra","Thalessa","Thalynra","Tharissa","Thavira",
    "Thaylith","Thellara","Thenyra","Theryssa","Theshalia","Thivara","Thyressa","Tilaira","Tinessa","Tinythra",
    "Tisarya","Tivessa","Tiyara","Tlaeryn","Tlalyssa","Tlanyra","Tlerissa","Tleyra","Tlyssara","Toressa",
    "Toralyth","Toryssa","Tressaya","Trylissa","Tyshera","Tyzmira","Tylassa",

    # U (57)
    "Uaelira","Uaelyss","Ualynra","Uanessa","Uanythra","Uaralyth","Uarissa","Uarynthia","Uashera","Uasyra",
    "Uavessa","Uaylira","Uazmira","Uazrynn","Uelaira","Uelessa","Uelithra","Uelyra","Ueralyth","Uerissa",
    "Uerynthia","Ueshalyn","Uevyra","Ueylissa","Uezhara","Uhaelyra","Uhalessa","Uhalynra","Uharissa","Uhavira",
    "Uhaylith","Uhellara","Uhenyra","Uheryssa","Uheshalia","Uhivara","Uhyressa","Uilaira","Uinessa","Uinythra",
    "Uisarya","Uivessa","Uiyara","Ulaeryn","Ulalyssa","Ulanyra","Ulerissa","Uleyra","Ulyssara","Uoressa",
    "Uoralyth","Uoryssa","Uressaya","Urylissa","Uyshera","Uyzmira","Uylassa",

    # V (57)
    "Vaelira","Vaelyss","Valynra","Vanessa","Vanythra","Varalyth","Varissa","Varynthia","Vashera","Vasyra",
    "Vavessa","Vaylira","Vazmira","Vazrynn","Velaira","Velessa","Velithra","Velyra","Veralyth","Verissa",
    "Verynthia","Veshalyn","Vevyra","Veylissa","Vezhara","Vhaelyra","Vhalessa","Vhalynra","Vharissa","Vhavira",
    "Vhaylith","Vhellara","Vhenyra","Vheryssa","Vheshalia","Vhivara","Vhyressa","Vilaira","Vinessa","Vinythra",
    "Visarya","Vivessa","Viyara","Vlaeryn","Vlalyssa","Vlanyra","Vlerissa","Vleyra","Vlyssara","Voressa",
    "Voralyth","Voryssa","Vressaya","Vrylissa","Vyshera","Vyzmira","Vylassa",

    # W (57)
    "Waelira","Waelyss","Walynra","Wanessa","Wanythra","Waralyth","Warissa","Warynthia","Washera","Wasyra",
    "Wavessa","Waylira","Wazmira","Wazrynn","Welaira","Welessa","Welithra","Welyra","Weralyth","Werissa",
    "Werynthia","Weshalyn","Wevyra","Weylissa","Wezhara","Whaelyra","Whalessa","Whalynra","Wharissa","Whavira",
    "Whaylith","Whellara","Whenyra","Wheryssa","Wheshalia","Whivara","Whyressa","Wilaira","Winessa","Winythra",
    "Wisarya","Wivessa","Wiyara","Wlaeryn","Wlalyssa","Wlanyra","Wlerissa","Wleyra","Wlyssara","Woressa",
    "Woralyth","Woryssa","Wressaya","Wrylissa","Wyshera","Wyzmira","Wylassa",

    # X (57)
    "Xaelira","Xaelyss","Xalynra","Xanessa","Xanythra","Xaralyth","Xarissa","Xarynthia","Xashera","Xasyra",
    "Xavessa","Xaylira","Xazmira","Xazrynn","Xelaira","Xelessa","Xelithra","Xelyra","Xeralyth","Xerissa",
    "Xerynthia","Xeshalyn","Xevyra","Xeylissa","Xezhara","Xhaelyra","Xhalessa","Xhalynra","Xharissa","Xhavira",
    "Xhaylith","Xhellara","Xhenyra","Xheryssa","Xheshalia","Xhivara","Xhyressa","Xilaira","Xinessa","Xinythra",
    "Xisarya","Xivessa","Xiyara","Xlaeryn","Xlalyssa","Xlanyra","Xlerissa","Xleyra","Xlyssara","Xoressa",
    "Xoralyth","Xoryssa","Xressaya","Xrylissa","Xyshera","Xyzmira","Xylassa",

    # Y (57)
    "Yaelira","Yaelyss","Yalynra","Yanessa","Yanythra","Yaralyth","Yarissa","Yarynthia","Yashera","Yasyra",
    "Yavessa","Yaylira","Yazmira","Yazrynn","Yelaira","Yelessa","Yelithra","Yelyra","Yeralyth","Yerissa",
    "Yerynthia","Yeshalyn","Yevyra","Yeylissa","Yezhara","Yhaelyra","Yhalessa","Yhalynra","Yharissa","Yhavira",
    "Yhaylith","Yhellara","Yhenyra","Yheryssa","Yheshalia","Yhivara","Yhyressa","Yilaira","Yinessa","Yinythra",
    "Yisarya","Yivessa","Yiyara","Ylaeryn","Ylalyssa","Ylanyra","Ylerissa","Yleyra","Ylyssara","Yoressa",
    "Yoralyth","Yoryssa","Yressaya","Yrylissa","Yyshera","Yyzmira","Yylassa",

    # Z (57)
    "Zaelira","Zaelyss","Zalynra","Zanessa","Zanythra","Zaralyth","Zarissa","Zarynthia","Zashera","Zasyra",
    "Zavessa","Zaylira","Zazmira","Zazrynn","Zelaira","Zelessa","Zelithra","Zelyra","Zeralyth","Zerissa",
    "Zerynthia","Zeshalyn","Zevyra","Zeylissa","Zezhara","Zhaelyra","Zhalessa","Zhalynra","Zharissa","Zhavira",
    "Zhaylith","Zhellara","Zhenyra","Zheryssa","Zheshalia","Zhivara","Zhyressa","Zilaira","Zinessa","Zinythra",
    "Zisarya","Zivessa","Ziyara","Zlaeryn","Zlalyssa","Zlanyra","Zlerissa","Zleyra","Zlyssara","Zoressa",
    "Zoralyth","Zoryssa","Zressaya","Zrylissa","Zyshera","Zyzmira","Zylassa"]
clausius_names1 = [
    # A
    "Aeloria","Aenira","Aeshala","Aevyra","Aelthira","Ariqen","Aravelle","Arisyn","Alyndra","Avarine",
    "Ashalyn","Ashyra","Azerai","Azerelle","Aeluna","Aelvara","Aelthys","Arielleth","Arivana","Ariselle",
    "Avenya","Avyssia","Aylindra","Aylira","Aylith","Ayshera","Aysira","Azerith","Azhalia","Azmira",
    "Azrynn","Aeloriah","Aenalyth","Aerysha","Aerynna","Aerythia","Ariqessa","Arilyth","Arivessa","Arlyndra",
    "Ashalithe","Ashyelle","Ashyvana","Avelynne","Averessa","Avyrith","Ayliss","Ayshera","Aysylia","Azhalyn",
    "Azmirae","Azryelle","Aelthirae","Aenalyra","Aeryssia","Arivelle","Averyn",

    # B
    "Baelira","Baeshyn","Balyra","Barithia","Belassa","Belthira","Benalyth","Beressa","Bethyra","Beylira",
    "Bhalira","Bharissa","Bhelaya","Bhenira","Bhyssara","Biashara","Bilynne","Birassa","Birelle","Bisarya",
    "Bivessa","Biyara","Blaeryn","Blaessia","Blayra","Blenira","Blyssara","Boressa","Borynthia","Bralynne",
    "Brayessa","Brelith","Brenyra","Brisaya","Brithara","Bryelle","Brylassa","Bryssira","Bynessa","Byrithia",
    "Byssara","Baelissa","Belanyra","Bharaya","Bhelissa","Bhyrella","Biasharae","Biralyth","Bivara","Blyrissa",
    "Boressyn","Braylith","Bryssaya","Byrassa","Byrelle","Byssira","Bhalynne",

    # C
    "Caelira","Caeryn","Calessa","Calynra","Camyra","Caralyth","Carissael","Carynthia","Cashera","Casyra",
    "Cavessa","Caylira","Cazmira","Cazrynn","Celaira","Celessa","Celithra","Celyra","Ceralyth","Cerissa",
    "Cerynthia","Ceshalyn","Cevyra","Ceylissa","Cezhara","Chaelyra","Chalessa","Chalyth","Charissa","Chavira",
    "Chaylith","Chellara","Chenyra","Cheryssa","Cheshalia","Chivara","Chyressa","Cilaira","Cinessa","Cinythra",
    "Cisarya","Civessa","Ciyara","Claeryn","Clalessa","Clanyra","Clerissa","Cleyra","Clyssara","Coressa",
    "Coralyth","Coryssa","Cressaya","Crylissa","Cyshera","Cyzmira","Cylassa",

    # D
    "Daelira","Daessyn","Dalyra","Danessa","Danythra","Daralyth","Darissa","Darynthia","Dashera","Dasyra",
    "Davessa","Daylira","Dazmira","Dazrynn","Delaira","Delessa","Delithra","Delyra","Deralyth","Derissa",
    "Derynthia","Deshalyn","Devyra","Deylissa","Dezhara","Dhaelyra","Dhalessa","Dhalynra","Dharissa","Dhavira",
    "Dhaylith","Dhellara","Dhenyra","Dheryssa","Dheshalia","Dhivara","Dhyressa","Dilaira","Dinessa","Dinythra",
    "Disarya","Divessa","Diyara","Dlaeryn","Dlalyssa","Dlanyra","Dlerissa","Dleyra","Dlyssara","Doressa",
    "Doralyth","Doryssa","Dressaya","Drylissa","Dyshera","Dyzmira","Dylassa",

    # E
    "Eaelira","Ealynra","Eanessa","Earynthia","Eashira","Easylia","Eavessa","Eaylira","Eazmira","Eazrynn",
    "Ecelira","Ecessa","Ecelith","Ecelyra","Ecerissa","Ecynra","Ecythia","Ecyssa","Edalyra","Edanessa",
    "Edaryth","Edeshara","Edevyra","Edeylia","Edezhara","Efaelyra","Efalyssa","Efanyra","Eferissa","Efivara",
    "Efressa","Efyra","Egalyth","Egenyra","Egerissa","Eglyssa","Ehalira","Ehalyssa","Ehanira","Eharyth",
    "Eheshalia","Ehivara","Ehressa","Eilaira","Eilessa","Eilithra","Eilyra","Einara","Eiralyth","Eirissa",
    "Eiryssa","Eisarya","Eivessa","Eiyara","Ejalyth","Ejaryssa","Ejylassa",

    # F
    "Faelira","Faelyss","Falynra","Fanessa","Fanythra","Faralyth","Farissa","Farynthia","Fashera","Fasyra",
    "Favessa","Faylira","Fazmira","Fazrynn","Felaira","Felessa","Felithra","Felyra","Feralyth","Ferissa",
    "Ferynthia","Feshalyn","Fevyra","Feylissa","Fezhara","Fhaelyra","Fhalessa","Fhalynra","Fharissa","Fhavira",
    "Fhaylith","Fhellara","Fhenyra","Fheryssa","Fheshalia","Fhivara","Fhyressa","Filaira","Finessa","Finythra",
    "Fisarya","Fivessa","Fiyara","Flaeryn","Flalessa","Flanyra","Flerissa","Fleyra","Flyssara","Foressa",
    "Foralyth","Foryssa","Fressaya","Frylissa","Fyshera","Fyzmira","Fylassa",

    # G
    "Gaelira","Gaelyss","Galynra","Ganessa","Ganythra","Garalyth","Garissa","Garynthia","Gashera","Gasyra",
    "Gavessa","Gaylira","Gazmira","Gazrynn","Gelaira","Gelessa","Gelithra","Gelyra","Geralyth","Gerissa",
    "Gerynthia","Geshalyn","Gevyra","Geylissa","Gezhara","Ghaelyra","Ghalessa","Ghalynra","Gharissa","Ghavira",
    "Ghaylith","Ghellara","Ghenyra","Gheryssa","Gheshalia","Ghivara","Ghyressa","Gilaira","Ginessa","Ginythra",
    "Gisarya","Givessa","Giyara","Glaeryn","Glalessa","Glanyra","Glerissa","Gleyra","Glyssara","Goressa",
    "Goralyth","Goryssa","Gressaya","Grylissa","Gyshera","Gyzmira","Gylassa",

    # H
    "Haelira","Haelyss","Halynra","Hanessa","Hanythra","Haralyth","Harissa","Harynthia","Hashera","Hasyra",
    "Havessa","Haylira","Hazmira","Hazrynn","Helaira","Helessa","Helithra","Helyra","Heralyth","Herissa",
    "Herynthia","Heshalyn","Hevyra","Heylissa","Hezhara","Hhaelyra","Hhalessa","Hhalynra","Hharissa","Hhavira",
    "Hhaylith","Hhellara","Hhenyra","Hheryssa","Hheshalia","Hhivara","Hhyressa","Hilaira","Hinessa","Hinythra",
    "Hisarya","Hivessa","Hiyara","Hlaeryn","Hlalyssa","Hlanyra","Hlerissa","Hleyra","Hlyssara","Horessa",
    "Horalyth","Horyssa","Hressaya","Hrylissa","Hyshera","Hyzmira","Hylassa",

    # I
    "Iaelira","Iaelyss","Ialynra","Ianessa","Ianythra","Iaralyth","Iarissa","Iarynthia","Iashera","Iasyra",
    "Iavessa","Iaylira","Iazmira","Iazrynn","Ielaira","Ielessa","Ielithra","Ielyra","Ieralyth","Ierissa",
    "Ierynthia","Ieshalyn","Ievyra","Ieylissa","Iezhara","Ihaelyra","Ihalessa","Ihalynra","Iharissa","Ihavira",
    "Ihaylith","Ihellara","Ihenyra","Iheryssa","Iheshalia","Ihivara","Ihyressa","Ilaira","Ilessa","Ilythra",
    "Isarya","Ivessa","Iyara","Ilaeryn","Ilalessa","Ilanyra","Ilerissa","Ileyra","Ilyssara","Ioressa",
    "Ioralyth","Ioryssa","Iressaya","Irylissa","Iyshera","Iyzmira","Iylassa",

    # J
    "Jaelira","Jaelyss","Jalynra","Janessa","Janythra","Jaralyth","Jarissa","Jarynthia","Jashera","Jasyra",
    "Javessa","Jaylira","Jazmira","Jazrynn","Jelaira","Jelessa","Jelithra","Jelyra","Jeralyth","Jerissa",
    "Jerynthia","Jeshalyn","Jevyra","Jeylissa","Jezhara","Jhaelyra","Jhalessa","Jhalynra","Jharissa","Jhavira",
    "Jhaylith","Jhellara","Jhenyra","Jheryssa","Jheshalia","Jhivara","Jhyressa","Jilaira","Jinessa","Jinythra",
    "Jisarya","Jivessa","Jiyara","Jlaeryn","Jlalyssa","Jlanyra","Jlerissa","Jleyra","Jlyssara","Joressa",
    "Joralyth","Joryssa","Jressaya","Jrylissa","Jyshera","Jyzmira","Jylassa",

    # K
    "Kaelira","Kaelyss","Kalynra","Kanessa","Kanythra","Karalyth","Karissa","Karynthia","Kashera","Kasyra",
    "Kavessa","Kaylira","Kazmira","Kazrynn","Kelaira","Kelessa","Kelithra","Kelyra","Keralyth","Kerissa",
    "Kerynthia","Keshalyn","Kevyra","Keylissa","Kezhara","Khaelyra","Khalessa","Khalynra","Kharissa","Khavira",
    "Khaylith","Khellara","Khenyra","Kheryssa","Kheshalia","Khivara","Khyressa","Kilaira","Kinessa","Kinythra",
    "Kisarya","Kivessa","Kiyara","Klaeryn","Klalyssa","Klanyra","Klerissa","Kleyra","Klyssara","Koressa",
    "Koralyth","Koryssa","Kressaya","Krylissa","Kyshera","Kyzmira","Kylassa",

    # L
    "Laelira","Laelyss","Lalynra","Lanessa","Lanythra","Laralyth","Larissa","Larynthia","Lashera","Lasyra",
    "Lavessa","Laylira","Lazmira","Lazrynn","Lelaira","Lelessa","Lelithra","Lelyra","Leralyth","Lerissa",
    "Lerynthia","Leshalyn","Levyra","Leylissa","Lezhara","Lhaelyra","Lhalessa","Lhalynra","Lharissa","Lhavira",
    "Lhaylith","Lhellara","Lhenyra","Lheryssa","Lheshalia","Lhivara","Lhyressa","Lilaira","Linessa","Linythra",
    "Lisarya","Livessa","Liyara","Llaeryn","Llalyssa","Llanyra","Llerissa","Lleyra","Llyssara","Loressa",
    "Loralyth","Loryssa","Lressaya","Lrylissa","Lyshera","Lyzmira","Lylassa",

    # M
    "Maelira","Maelyss","Malynra","Manessa","Manythra","Maralyth","Marissa","Marynthia","Mashera","Masyra",
    "Mavessa","Maylira","Mazmira","Mazrynn","Melaira","Melessa","Melithra","Melyra","Meralyth","Merissa",
    "Merynthia","Meshalyn","Mevyra","Meylissa","Mezhara","Mhaelyra","Mhalessa","Mhalynra","Mharissa","Mhavira",
    "Mhaylith","Mhellara","Mhenyra","Mheryssa","Mheshalia","Mhivara","Mhyressa","Milaira","Minessa","Minythra",
    "Misarya","Mivessa","Miyara","Mlaeryn","Mlalyssa","Mlanyra","Mlerissa","Mleyra","Mlyssara","Moressa",
    "Moralyth","Moryssa","Mressaya","Mrylissa","Myshera","Myzmira","Mylassa",

    # N
    "Naelira","Naelyss","Nalynra","Nanessa","Nanythra","Naralyth","Narissa","Narynthia","Nashera","Nasyra",
    "Navessa","Naylira","Nazmira","Nazrynn","Nelaira","Nelessa","Nelithra","Nelyra","Neralyth","Nerissa",
    "Nerynthia","Neshalyn","Nevyra","Neylissa","Nezhara","Nhaelyra","Nhalessa","Nhalynra","Nharissa","Nhavira",
    "Nhaylith","Nhellara","Nhenyra","Nheryssa","Nheshalia","Nhivara","Nhyressa","Nilaira","Ninessa","Ninythra",
    "Nisarya","Nivessa","Niyara","Nlaeryn","Nlalyssa","Nlanyra","Nlerissa","Nleyra","Nlyssara","Noressa",
    "Noralyth","Noryssa","Nressaya","Nrylissa","Nyshera","Nyzmira","Nylassa",

    # O
    "Oaelira","Oaelyss","Oalynra","Oanessa","Oanythra","Oaralyth","Oarissa","Oarynthia","Oashera","Oasyra",
    "Oavessa","Oaylira","Oazmira","Oazrynn","Oelaira","Oelessa","Oelithra","Oelyra","Oeralyth","Oerissa",
    "Oerynthia","Oeshalyn","Oevyra","Oeylissa","Oezhara","Ohaelyra","Ohalessa","Ohalynra","Oharissa","Ohavira",
    "Ohaylith","Ohellara","Ohenyra","Oheryssa","Oheshalia","Ohivara","Ohyressa","Oilaira","Oinessa","Oinythra",
    "Oisarya","Oivessa","Oiyara","Olaeryn","Olalyssa","Olanyra","Olerissa","Oleyra","Olyssara","Oressa",
    "Oralyth","Oryssa","Oressaya","Orylissa","Oyshera","Oyzmira","Oylassa",

    # P
    "Paelira","Paelyss","Palynra","Panessa","Panythra","Paralyth","Parissa","Parynthia","Pashera","Pasyra",
    "Pavessa","Paylira","Pazmira","Pazrynn","Pelaira","Pelessa","Pelithra","Pelyra", "Qaelira","Qaelyss","Qalynra","Qanessa","Qanythra","Qaralyth","Qarissa","Qarynthia","Qashera","Qasyra",
    "Qavessa","Qaylira","Qazmira","Qazrynn","Qelaira","Qelessa","Qelithra","Qelyra","Qeralyth","Qerissa",
    "Qerynthia","Qeshalyn","Qevyra","Qeylissa","Qezhara","Qhaelyra","Qhalessa","Qhalynra","Qharissa","Qhavira",
    "Qhaylith","Qhellara","Qhenyra","Qheryssa","Qheshalia","Qhivara","Qhyressa","Qilaira","Qinessa","Qinythra",
    "Qisarya","Qivessa","Qiyara","Qlaeryn","Qlalyssa","Qlanyra","Qlerissa","Qleyra","Qlyssara","Qoressa",
    "Qoralyth","Qoryssa","Qressaya","Qrylissa","Qyshera","Qyzmira","Qylassa",

    # R (57)
    "Raelira","Raelyss","Ralynra","Ranessa","Ranythra","Raralyth","Rarissa","Rarynthia","Rashera","Rasyra",
    "Ravessa","Raylira","Razmira","Razrynn","Relaira","Relessa","Relithra","Relyra","Reralyth","Rerissa",
    "Rerynthia","Reshalyn","Revyra","Reylissa","Rezhara","Rhaelyra","Rhalessa","Rhalynra","Rharissa","Rhavira",
    "Rhaylith","Rhellara","Rhenyra","Rheryssa","Rheshalia","Rhivara","Rhyressa","Rilaira","Rinessa","Rinythra",
    "Risarya","Rivessa","Riyara","Rlaeryn","Rlalyssa","Rlanyra","Rlerissa","Rleyra","Rlyssara","Roressa",
    "Roralyth","Roryssa","Rressaya","Rrylissa","Ryshera","Ryzmira","Rylassa",

    # S (57)
    "Saelira","Saelyss","Salynra","Sanessa","Sanythra","Saralyth","Sarissa","Sarynthia","Sashera","Sasyra",
    "Savessa","Saylira","Sazmira","Sazrynn","Selaira","Selessa","Selithra","Selyra","Seralyth","Serissa",
    "Serynthia","Seshalyn","Sevyra","Seylissa","Sezhara","Shaelyra","Shalessa","Shalynra","Sharissa","Shavira",
    "Shaylith","Shellara","Shenyra","Sheryssa","Sheshalia","Shivara","Shyressa","Silaira","Sinessa","Sinythra",
    "Sisarya","Sivessa","Siyara","Slaeryn","Slalyssa","Slanyra","Slerissa","Sleyra","Slyssara","Soressa",
    "Soralyth","Soryssa","Sressaya","Srylissa","Syshera","Syzmira","Sylassa",

    # T (57)
    "Taelira","Taelyss","Talynra","Tanessa","Tanythra","Taralyth","Tarissa","Tarynthia","Tashera","Tasyra",
    "Tavessa","Taylira","Tazmira","Tazrynn","Telaira","Telessa","Telithra","Telyra","Teralyth","Terissa",
    "Terynthia","Teshalyn","Tevyra","Teylissa","Tezhara","Thaelyra","Thalessa","Thalynra","Tharissa","Thavira",
    "Thaylith","Thellara","Thenyra","Theryssa","Theshalia","Thivara","Thyressa","Tilaira","Tinessa","Tinythra",
    "Tisarya","Tivessa","Tiyara","Tlaeryn","Tlalyssa","Tlanyra","Tlerissa","Tleyra","Tlyssara","Toressa",
    "Toralyth","Toryssa","Tressaya","Trylissa","Tyshera","Tyzmira","Tylassa",

    # U (57)
    "Uaelira","Uaelyss","Ualynra","Uanessa","Uanythra","Uaralyth","Uarissa","Uarynthia","Uashera","Uasyra",
    "Uavessa","Uaylira","Uazmira","Uazrynn","Uelaira","Uelessa","Uelithra","Uelyra","Ueralyth","Uerissa",
    "Uerynthia","Ueshalyn","Uevyra","Ueylissa","Uezhara","Uhaelyra","Uhalessa","Uhalynra","Uharissa","Uhavira",
    "Uhaylith","Uhellara","Uhenyra","Uheryssa","Uheshalia","Uhivara","Uhyressa","Uilaira","Uinessa","Uinythra",
    "Uisarya","Uivessa","Uiyara","Ulaeryn","Ulalyssa","Ulanyra","Ulerissa","Uleyra","Ulyssara","Uoressa",
    "Uoralyth","Uoryssa","Uressaya","Urylissa","Uyshera","Uyzmira","Uylassa",

    # V (57)
    "Vaelira","Vaelyss","Valynra","Vanessa","Vanythra","Varalyth","Varissa","Varynthia","Vashera","Vasyra",
    "Vavessa","Vaylira","Vazmira","Vazrynn","Velaira","Velessa","Velithra","Velyra","Veralyth","Verissa",
    "Verynthia","Veshalyn","Vevyra","Veylissa","Vezhara","Vhaelyra","Vhalessa","Vhalynra","Vharissa","Vhavira",
    "Vhaylith","Vhellara","Vhenyra","Vheryssa","Vheshalia","Vhivara","Vhyressa","Vilaira","Vinessa","Vinythra",
    "Visarya","Vivessa","Viyara","Vlaeryn","Vlalyssa","Vlanyra","Vlerissa","Vleyra","Vlyssara","Voressa",
    "Voralyth","Voryssa","Vressaya","Vrylissa","Vyshera","Vyzmira","Vylassa",

    # W (57)
    "Waelira","Waelyss","Walynra","Wanessa","Wanythra","Waralyth","Warissa","Warynthia","Washera","Wasyra",
    "Wavessa","Waylira","Wazmira","Wazrynn","Welaira","Welessa","Welithra","Welyra","Weralyth","Werissa",
    "Werynthia","Weshalyn","Wevyra","Weylissa","Wezhara","Whaelyra","Whalessa","Whalynra","Wharissa","Whavira",
    "Whaylith","Whellara","Whenyra","Wheryssa","Wheshalia","Whivara","Whyressa","Wilaira","Winessa","Winythra",
    "Wisarya","Wivessa","Wiyara","Wlaeryn","Wlalyssa","Wlanyra","Wlerissa","Wleyra","Wlyssara","Woressa",
    "Woralyth","Woryssa","Wressaya","Wrylissa","Wyshera","Wyzmira","Wylassa",

    # X (57)
    "Xaelira","Xaelyss","Xalynra","Xanessa","Xanythra","Xaralyth","Xarissa","Xarynthia","Xashera","Xasyra",
    "Xavessa","Xaylira","Xazmira","Xazrynn","Xelaira","Xelessa","Xelithra","Xelyra","Xeralyth","Xerissa",
    "Xerynthia","Xeshalyn","Xevyra","Xeylissa","Xezhara","Xhaelyra","Xhalessa","Xhalynra","Xharissa","Xhavira",
    "Xhaylith","Xhellara","Xhenyra","Xheryssa","Xheshalia","Xhivara","Xhyressa","Xilaira","Xinessa","Xinythra",
    "Xisarya","Xivessa","Xiyara","Xlaeryn","Xlalyssa","Xlanyra","Xlerissa","Xleyra","Xlyssara","Xoressa",
    "Xoralyth","Xoryssa","Xressaya","Xrylissa","Xyshera","Xyzmira","Xylassa",

    # Y (57)
    "Yaelira","Yaelyss","Yalynra","Yanessa","Yanythra","Yaralyth","Yarissa","Yarynthia","Yashera","Yasyra",
    "Yavessa","Yaylira","Yazmira","Yazrynn","Yelaira","Yelessa","Yelithra","Yelyra","Yeralyth","Yerissa",
    "Yerynthia","Yeshalyn","Yevyra","Yeylissa","Yezhara","Yhaelyra","Yhalessa","Yhalynra","Yharissa","Yhavira",
    "Yhaylith","Yhellara","Yhenyra","Yheryssa","Yheshalia","Yhivara","Yhyressa","Yilaira","Yinessa","Yinythra",
    "Yisarya","Yivessa","Yiyara","Ylaeryn","Ylalyssa","Ylanyra","Ylerissa","Yleyra","Ylyssara","Yoressa",
    "Yoralyth","Yoryssa","Yressaya","Yrylissa","Yyshera","Yyzmira","Yylassa",

    # Z (57)
    "Zaelira","Zaelyss","Zalynra","Zanessa","Zanythra","Zaralyth","Zarissa","Zarynthia","Zashera","Zasyra",
    "Zavessa","Zaylira","Zazmira","Zazrynn","Zelaira","Zelessa","Zelithra","Zelyra","Zeralyth","Zerissa",
    "Zerynthia","Zeshalyn","Zevyra","Zeylissa","Zezhara","Zhaelyra","Zhalessa","Zhalynra","Zharissa","Zhavira",
    "Zhaylith","Zhellara","Zhenyra","Zheryssa","Zheshalia","Zhivara","Zhyressa","Zilaira","Zinessa","Zinythra",
    "Zisarya","Zivessa","Ziyara","Zlaeryn","Zlalyssa","Zlanyra","Zlerissa","Zleyra","Zlyssara","Zoressa",
    "Zoralyth","Zoryssa","Zressaya","Zrylissa","Zyshera","Zyzmira","Zylassa"]
clausius_names2 = [
    # A
    "Aeloria","Aenira","Aeshala","Aevyra","Aelthira","Ariqen","Aravelle","Arisyn","Alyndra","Avarine",
    "Ashalyn","Ashyra","Azerai","Azerelle","Aeluna","Aelvara","Aelthys","Arielleth","Arivana","Ariselle",
    "Avenya","Avyssia","Aylindra","Aylira","Aylith","Ayshera","Aysira","Azerith","Azhalia","Azmira",
    "Azrynn","Aeloriah","Aenalyth","Aerysha","Aerynna","Aerythia","Ariqessa","Arilyth","Arivessa","Arlyndra",
    "Ashalithe","Ashyelle","Ashyvana","Avelynne","Averessa","Avyrith","Ayliss","Ayshera","Aysylia","Azhalyn",
    "Azmirae","Azryelle","Aelthirae","Aenalyra","Aeryssia","Arivelle","Averyn",

    # B
    "Baelira","Baeshyn","Balyra","Barithia","Belassa","Belthira","Benalyth","Beressa","Bethyra","Beylira",
    "Bhalira","Bharissa","Bhelaya","Bhenira","Bhyssara","Biashara","Bilynne","Birassa","Birelle","Bisarya",
    "Bivessa","Biyara","Blaeryn","Blaessia","Blayra","Blenira","Blyssara","Boressa","Borynthia","Bralynne",
    "Brayessa","Brelith","Brenyra","Brisaya","Brithara","Bryelle","Brylassa","Bryssira","Bynessa","Byrithia",
    "Byssara","Baelissa","Belanyra","Bharaya","Bhelissa","Bhyrella","Biasharae","Biralyth","Bivara","Blyrissa",
    "Boressyn","Braylith","Bryssaya","Byrassa","Byrelle","Byssira","Bhalynne",

    # C
    "Caelira","Caeryn","Calessa","Calynra","Camyra","Caralyth","Carissael","Carynthia","Cashera","Casyra",
    "Cavessa","Caylira","Cazmira","Cazrynn","Celaira","Celessa","Celithra","Celyra","Ceralyth","Cerissa",
    "Cerynthia","Ceshalyn","Cevyra","Ceylissa","Cezhara","Chaelyra","Chalessa","Chalyth","Charissa","Chavira",
    "Chaylith","Chellara","Chenyra","Cheryssa","Cheshalia","Chivara","Chyressa","Cilaira","Cinessa","Cinythra",
    "Cisarya","Civessa","Ciyara","Claeryn","Clalessa","Clanyra","Clerissa","Cleyra","Clyssara","Coressa",
    "Coralyth","Coryssa","Cressaya","Crylissa","Cyshera","Cyzmira","Cylassa",

    # D
    "Daelira","Daessyn","Dalyra","Danessa","Danythra","Daralyth","Darissa","Darynthia","Dashera","Dasyra",
    "Davessa","Daylira","Dazmira","Dazrynn","Delaira","Delessa","Delithra","Delyra","Deralyth","Derissa",
    "Derynthia","Deshalyn","Devyra","Deylissa","Dezhara","Dhaelyra","Dhalessa","Dhalynra","Dharissa","Dhavira",
    "Dhaylith","Dhellara","Dhenyra","Dheryssa","Dheshalia","Dhivara","Dhyressa","Dilaira","Dinessa","Dinythra",
    "Disarya","Divessa","Diyara","Dlaeryn","Dlalyssa","Dlanyra","Dlerissa","Dleyra","Dlyssara","Doressa",
    "Doralyth","Doryssa","Dressaya","Drylissa","Dyshera","Dyzmira","Dylassa",

    # E
    "Eaelira","Ealynra","Eanessa","Earynthia","Eashira","Easylia","Eavessa","Eaylira","Eazmira","Eazrynn",
    "Ecelira","Ecessa","Ecelith","Ecelyra","Ecerissa","Ecynra","Ecythia","Ecyssa","Edalyra","Edanessa",
    "Edaryth","Edeshara","Edevyra","Edeylia","Edezhara","Efaelyra","Efalyssa","Efanyra","Eferissa","Efivara",
    "Efressa","Efyra","Egalyth","Egenyra","Egerissa","Eglyssa","Ehalira","Ehalyssa","Ehanira","Eharyth",
    "Eheshalia","Ehivara","Ehressa","Eilaira","Eilessa","Eilithra","Eilyra","Einara","Eiralyth","Eirissa",
    "Eiryssa","Eisarya","Eivessa","Eiyara","Ejalyth","Ejaryssa","Ejylassa",

    # F
    "Faelira","Faelyss","Falynra","Fanessa","Fanythra","Faralyth","Farissa","Farynthia","Fashera","Fasyra",
    "Favessa","Faylira","Fazmira","Fazrynn","Felaira","Felessa","Felithra","Felyra","Feralyth","Ferissa",
    "Ferynthia","Feshalyn","Fevyra","Feylissa","Fezhara","Fhaelyra","Fhalessa","Fhalynra","Fharissa","Fhavira",
    "Fhaylith","Fhellara","Fhenyra","Fheryssa","Fheshalia","Fhivara","Fhyressa","Filaira","Finessa","Finythra",
    "Fisarya","Fivessa","Fiyara","Flaeryn","Flalessa","Flanyra","Flerissa","Fleyra","Flyssara","Foressa",
    "Foralyth","Foryssa","Fressaya","Frylissa","Fyshera","Fyzmira","Fylassa",

    # G
    "Gaelira","Gaelyss","Galynra","Ganessa","Ganythra","Garalyth","Garissa","Garynthia","Gashera","Gasyra",
    "Gavessa","Gaylira","Gazmira","Gazrynn","Gelaira","Gelessa","Gelithra","Gelyra","Geralyth","Gerissa",
    "Gerynthia","Geshalyn","Gevyra","Geylissa","Gezhara","Ghaelyra","Ghalessa","Ghalynra","Gharissa","Ghavira",
    "Ghaylith","Ghellara","Ghenyra","Gheryssa","Gheshalia","Ghivara","Ghyressa","Gilaira","Ginessa","Ginythra",
    "Gisarya","Givessa","Giyara","Glaeryn","Glalessa","Glanyra","Glerissa","Gleyra","Glyssara","Goressa",
    "Goralyth","Goryssa","Gressaya","Grylissa","Gyshera","Gyzmira","Gylassa",

    # H
    "Haelira","Haelyss","Halynra","Hanessa","Hanythra","Haralyth","Harissa","Harynthia","Hashera","Hasyra",
    "Havessa","Haylira","Hazmira","Hazrynn","Helaira","Helessa","Helithra","Helyra","Heralyth","Herissa",
    "Herynthia","Heshalyn","Hevyra","Heylissa","Hezhara","Hhaelyra","Hhalessa","Hhalynra","Hharissa","Hhavira",
    "Hhaylith","Hhellara","Hhenyra","Hheryssa","Hheshalia","Hhivara","Hhyressa","Hilaira","Hinessa","Hinythra",
    "Hisarya","Hivessa","Hiyara","Hlaeryn","Hlalyssa","Hlanyra","Hlerissa","Hleyra","Hlyssara","Horessa",
    "Horalyth","Horyssa","Hressaya","Hrylissa","Hyshera","Hyzmira","Hylassa",

    # I
    "Iaelira","Iaelyss","Ialynra","Ianessa","Ianythra","Iaralyth","Iarissa","Iarynthia","Iashera","Iasyra",
    "Iavessa","Iaylira","Iazmira","Iazrynn","Ielaira","Ielessa","Ielithra","Ielyra","Ieralyth","Ierissa",
    "Ierynthia","Ieshalyn","Ievyra","Ieylissa","Iezhara","Ihaelyra","Ihalessa","Ihalynra","Iharissa","Ihavira",
    "Ihaylith","Ihellara","Ihenyra","Iheryssa","Iheshalia","Ihivara","Ihyressa","Ilaira","Ilessa","Ilythra",
    "Isarya","Ivessa","Iyara","Ilaeryn","Ilalessa","Ilanyra","Ilerissa","Ileyra","Ilyssara","Ioressa",
    "Ioralyth","Ioryssa","Iressaya","Irylissa","Iyshera","Iyzmira","Iylassa",

    # J
    "Jaelira","Jaelyss","Jalynra","Janessa","Janythra","Jaralyth","Jarissa","Jarynthia","Jashera","Jasyra",
    "Javessa","Jaylira","Jazmira","Jazrynn","Jelaira","Jelessa","Jelithra","Jelyra","Jeralyth","Jerissa",
    "Jerynthia","Jeshalyn","Jevyra","Jeylissa","Jezhara","Jhaelyra","Jhalessa","Jhalynra","Jharissa","Jhavira",
    "Jhaylith","Jhellara","Jhenyra","Jheryssa","Jheshalia","Jhivara","Jhyressa","Jilaira","Jinessa","Jinythra",
    "Jisarya","Jivessa","Jiyara","Jlaeryn","Jlalyssa","Jlanyra","Jlerissa","Jleyra","Jlyssara","Joressa",
    "Joralyth","Joryssa","Jressaya","Jrylissa","Jyshera","Jyzmira","Jylassa",

    # K
    "Kaelira","Kaelyss","Kalynra","Kanessa","Kanythra","Karalyth","Karissa","Karynthia","Kashera","Kasyra",
    "Kavessa","Kaylira","Kazmira","Kazrynn","Kelaira","Kelessa","Kelithra","Kelyra","Keralyth","Kerissa",
    "Kerynthia","Keshalyn","Kevyra","Keylissa","Kezhara","Khaelyra","Khalessa","Khalynra","Kharissa","Khavira",
    "Khaylith","Khellara","Khenyra","Kheryssa","Kheshalia","Khivara","Khyressa","Kilaira","Kinessa","Kinythra",
    "Kisarya","Kivessa","Kiyara","Klaeryn","Klalyssa","Klanyra","Klerissa","Kleyra","Klyssara","Koressa",
    "Koralyth","Koryssa","Kressaya","Krylissa","Kyshera","Kyzmira","Kylassa",

    # L
    "Laelira","Laelyss","Lalynra","Lanessa","Lanythra","Laralyth","Larissa","Larynthia","Lashera","Lasyra",
    "Lavessa","Laylira","Lazmira","Lazrynn","Lelaira","Lelessa","Lelithra","Lelyra","Leralyth","Lerissa",
    "Lerynthia","Leshalyn","Levyra","Leylissa","Lezhara","Lhaelyra","Lhalessa","Lhalynra","Lharissa","Lhavira",
    "Lhaylith","Lhellara","Lhenyra","Lheryssa","Lheshalia","Lhivara","Lhyressa","Lilaira","Linessa","Linythra",
    "Lisarya","Livessa","Liyara","Llaeryn","Llalyssa","Llanyra","Llerissa","Lleyra","Llyssara","Loressa",
    "Loralyth","Loryssa","Lressaya","Lrylissa","Lyshera","Lyzmira","Lylassa",

    # M
    "Maelira","Maelyss","Malynra","Manessa","Manythra","Maralyth","Marissa","Marynthia","Mashera","Masyra",
    "Mavessa","Maylira","Mazmira","Mazrynn","Melaira","Melessa","Melithra","Melyra","Meralyth","Merissa",
    "Merynthia","Meshalyn","Mevyra","Meylissa","Mezhara","Mhaelyra","Mhalessa","Mhalynra","Mharissa","Mhavira",
    "Mhaylith","Mhellara","Mhenyra","Mheryssa","Mheshalia","Mhivara","Mhyressa","Milaira","Minessa","Minythra",
    "Misarya","Mivessa","Miyara","Mlaeryn","Mlalyssa","Mlanyra","Mlerissa","Mleyra","Mlyssara","Moressa",
    "Moralyth","Moryssa","Mressaya","Mrylissa","Myshera","Myzmira","Mylassa",

    # N
    "Naelira","Naelyss","Nalynra","Nanessa","Nanythra","Naralyth","Narissa","Narynthia","Nashera","Nasyra",
    "Navessa","Naylira","Nazmira","Nazrynn","Nelaira","Nelessa","Nelithra","Nelyra","Neralyth","Nerissa",
    "Nerynthia","Neshalyn","Nevyra","Neylissa","Nezhara","Nhaelyra","Nhalessa","Nhalynra","Nharissa","Nhavira",
    "Nhaylith","Nhellara","Nhenyra","Nheryssa","Nheshalia","Nhivara","Nhyressa","Nilaira","Ninessa","Ninythra",
    "Nisarya","Nivessa","Niyara","Nlaeryn","Nlalyssa","Nlanyra","Nlerissa","Nleyra","Nlyssara","Noressa",
    "Noralyth","Noryssa","Nressaya","Nrylissa","Nyshera","Nyzmira","Nylassa",

    # O
    "Oaelira","Oaelyss","Oalynra","Oanessa","Oanythra","Oaralyth","Oarissa","Oarynthia","Oashera","Oasyra",
    "Oavessa","Oaylira","Oazmira","Oazrynn","Oelaira","Oelessa","Oelithra","Oelyra","Oeralyth","Oerissa",
    "Oerynthia","Oeshalyn","Oevyra","Oeylissa","Oezhara","Ohaelyra","Ohalessa","Ohalynra","Oharissa","Ohavira",
    "Ohaylith","Ohellara","Ohenyra","Oheryssa","Oheshalia","Ohivara","Ohyressa","Oilaira","Oinessa","Oinythra",
    "Oisarya","Oivessa","Oiyara","Olaeryn","Olalyssa","Olanyra","Olerissa","Oleyra","Olyssara","Oressa",
    "Oralyth","Oryssa","Oressaya","Orylissa","Oyshera","Oyzmira","Oylassa",

    # P
    "Paelira","Paelyss","Palynra","Panessa","Panythra","Paralyth","Parissa","Parynthia","Pashera","Pasyra",
    "Pavessa","Paylira","Pazmira","Pazrynn","Pelaira","Pelessa","Pelithra","Pelyra", "Qaelira","Qaelyss","Qalynra","Qanessa","Qanythra","Qaralyth","Qarissa","Qarynthia","Qashera","Qasyra",
    "Qavessa","Qaylira","Qazmira","Qazrynn","Qelaira","Qelessa","Qelithra","Qelyra","Qeralyth","Qerissa",
    "Qerynthia","Qeshalyn","Qevyra","Qeylissa","Qezhara","Qhaelyra","Qhalessa","Qhalynra","Qharissa","Qhavira",
    "Qhaylith","Qhellara","Qhenyra","Qheryssa","Qheshalia","Qhivara","Qhyressa","Qilaira","Qinessa","Qinythra",
    "Qisarya","Qivessa","Qiyara","Qlaeryn","Qlalyssa","Qlanyra","Qlerissa","Qleyra","Qlyssara","Qoressa",
    "Qoralyth","Qoryssa","Qressaya","Qrylissa","Qyshera","Qyzmira","Qylassa",

    # R (57)
    "Raelira","Raelyss","Ralynra","Ranessa","Ranythra","Raralyth","Rarissa","Rarynthia","Rashera","Rasyra",
    "Ravessa","Raylira","Razmira","Razrynn","Relaira","Relessa","Relithra","Relyra","Reralyth","Rerissa",
    "Rerynthia","Reshalyn","Revyra","Reylissa","Rezhara","Rhaelyra","Rhalessa","Rhalynra","Rharissa","Rhavira",
    "Rhaylith","Rhellara","Rhenyra","Rheryssa","Rheshalia","Rhivara","Rhyressa","Rilaira","Rinessa","Rinythra",
    "Risarya","Rivessa","Riyara","Rlaeryn","Rlalyssa","Rlanyra","Rlerissa","Rleyra","Rlyssara","Roressa",
    "Roralyth","Roryssa","Rressaya","Rrylissa","Ryshera","Ryzmira","Rylassa",

    # S (57)
    "Saelira","Saelyss","Salynra","Sanessa","Sanythra","Saralyth","Sarissa","Sarynthia","Sashera","Sasyra",
    "Savessa","Saylira","Sazmira","Sazrynn","Selaira","Selessa","Selithra","Selyra","Seralyth","Serissa",
    "Serynthia","Seshalyn","Sevyra","Seylissa","Sezhara","Shaelyra","Shalessa","Shalynra","Sharissa","Shavira",
    "Shaylith","Shellara","Shenyra","Sheryssa","Sheshalia","Shivara","Shyressa","Silaira","Sinessa","Sinythra",
    "Sisarya","Sivessa","Siyara","Slaeryn","Slalyssa","Slanyra","Slerissa","Sleyra","Slyssara","Soressa",
    "Soralyth","Soryssa","Sressaya","Srylissa","Syshera","Syzmira","Sylassa",

    # T (57)
    "Taelira","Taelyss","Talynra","Tanessa","Tanythra","Taralyth","Tarissa","Tarynthia","Tashera","Tasyra",
    "Tavessa","Taylira","Tazmira","Tazrynn","Telaira","Telessa","Telithra","Telyra","Teralyth","Terissa",
    "Terynthia","Teshalyn","Tevyra","Teylissa","Tezhara","Thaelyra","Thalessa","Thalynra","Tharissa","Thavira",
    "Thaylith","Thellara","Thenyra","Theryssa","Theshalia","Thivara","Thyressa","Tilaira","Tinessa","Tinythra",
    "Tisarya","Tivessa","Tiyara","Tlaeryn","Tlalyssa","Tlanyra","Tlerissa","Tleyra","Tlyssara","Toressa",
    "Toralyth","Toryssa","Tressaya","Trylissa","Tyshera","Tyzmira","Tylassa",

    # U (57)
    "Uaelira","Uaelyss","Ualynra","Uanessa","Uanythra","Uaralyth","Uarissa","Uarynthia","Uashera","Uasyra",
    "Uavessa","Uaylira","Uazmira","Uazrynn","Uelaira","Uelessa","Uelithra","Uelyra","Ueralyth","Uerissa",
    "Uerynthia","Ueshalyn","Uevyra","Ueylissa","Uezhara","Uhaelyra","Uhalessa","Uhalynra","Uharissa","Uhavira",
    "Uhaylith","Uhellara","Uhenyra","Uheryssa","Uheshalia","Uhivara","Uhyressa","Uilaira","Uinessa","Uinythra",
    "Uisarya","Uivessa","Uiyara","Ulaeryn","Ulalyssa","Ulanyra","Ulerissa","Uleyra","Ulyssara","Uoressa",
    "Uoralyth","Uoryssa","Uressaya","Urylissa","Uyshera","Uyzmira","Uylassa",

    # V (57)
    "Vaelira","Vaelyss","Valynra","Vanessa","Vanythra","Varalyth","Varissa","Varynthia","Vashera","Vasyra",
    "Vavessa","Vaylira","Vazmira","Vazrynn","Velaira","Velessa","Velithra","Velyra","Veralyth","Verissa",
    "Verynthia","Veshalyn","Vevyra","Veylissa","Vezhara","Vhaelyra","Vhalessa","Vhalynra","Vharissa","Vhavira",
    "Vhaylith","Vhellara","Vhenyra","Vheryssa","Vheshalia","Vhivara","Vhyressa","Vilaira","Vinessa","Vinythra",
    "Visarya","Vivessa","Viyara","Vlaeryn","Vlalyssa","Vlanyra","Vlerissa","Vleyra","Vlyssara","Voressa",
    "Voralyth","Voryssa","Vressaya","Vrylissa","Vyshera","Vyzmira","Vylassa",

    # W (57)
    "Waelira","Waelyss","Walynra","Wanessa","Wanythra","Waralyth","Warissa","Warynthia","Washera","Wasyra",
    "Wavessa","Waylira","Wazmira","Wazrynn","Welaira","Welessa","Welithra","Welyra","Weralyth","Werissa",
    "Werynthia","Weshalyn","Wevyra","Weylissa","Wezhara","Whaelyra","Whalessa","Whalynra","Wharissa","Whavira",
    "Whaylith","Whellara","Whenyra","Wheryssa","Wheshalia","Whivara","Whyressa","Wilaira","Winessa","Winythra",
    "Wisarya","Wivessa","Wiyara","Wlaeryn","Wlalyssa","Wlanyra","Wlerissa","Wleyra","Wlyssara","Woressa",
    "Woralyth","Woryssa","Wressaya","Wrylissa","Wyshera","Wyzmira","Wylassa",

    # X (57)
    "Xaelira","Xaelyss","Xalynra","Xanessa","Xanythra","Xaralyth","Xarissa","Xarynthia","Xashera","Xasyra",
    "Xavessa","Xaylira","Xazmira","Xazrynn","Xelaira","Xelessa","Xelithra","Xelyra","Xeralyth","Xerissa",
    "Xerynthia","Xeshalyn","Xevyra","Xeylissa","Xezhara","Xhaelyra","Xhalessa","Xhalynra","Xharissa","Xhavira",
    "Xhaylith","Xhellara","Xhenyra","Xheryssa","Xheshalia","Xhivara","Xhyressa","Xilaira","Xinessa","Xinythra",
    "Xisarya","Xivessa","Xiyara","Xlaeryn","Xlalyssa","Xlanyra","Xlerissa","Xleyra","Xlyssara","Xoressa",
    "Xoralyth","Xoryssa","Xressaya","Xrylissa","Xyshera","Xyzmira","Xylassa",

    # Y (57)
    "Yaelira","Yaelyss","Yalynra","Yanessa","Yanythra","Yaralyth","Yarissa","Yarynthia","Yashera","Yasyra",
    "Yavessa","Yaylira","Yazmira","Yazrynn","Yelaira","Yelessa","Yelithra","Yelyra","Yeralyth","Yerissa",
    "Yerynthia","Yeshalyn","Yevyra","Yeylissa","Yezhara","Yhaelyra","Yhalessa","Yhalynra","Yharissa","Yhavira",
    "Yhaylith","Yhellara","Yhenyra","Yheryssa","Yheshalia","Yhivara","Yhyressa","Yilaira","Yinessa","Yinythra",
    "Yisarya","Yivessa","Yiyara","Ylaeryn","Ylalyssa","Ylanyra","Ylerissa","Yleyra","Ylyssara","Yoressa",
    "Yoralyth","Yoryssa","Yressaya","Yrylissa","Yyshera","Yyzmira","Yylassa",

    # Z (57)
    "Zaelira","Zaelyss","Zalynra","Zanessa","Zanythra","Zaralyth","Zarissa","Zarynthia","Zashera","Zasyra",
    "Zavessa","Zaylira","Zazmira","Zazrynn","Zelaira","Zelessa","Zelithra","Zelyra","Zeralyth","Zerissa",
    "Zerynthia","Zeshalyn","Zevyra","Zeylissa","Zezhara","Zhaelyra","Zhalessa","Zhalynra","Zharissa","Zhavira",
    "Zhaylith","Zhellara","Zhenyra","Zheryssa","Zheshalia","Zhivara","Zhyressa","Zilaira","Zinessa","Zinythra",
    "Zisarya","Zivessa","Ziyara","Zlaeryn","Zlalyssa","Zlanyra","Zlerissa","Zleyra","Zlyssara","Zoressa",
    "Zoralyth","Zoryssa","Zressaya","Zrylissa","Zyshera","Zyzmira","Zylassa"]
tsallis_madhi_names = ["Aeron", "Aelric", "Aethor", "Avaron", "Aldric", "Arvyn", "Arenlor", "Astarin", "Atheron", "Alyndar",
"Arenith", "Arkos", "Azeron", "Aldros", "Aethyn", "Arvoss", "Alyrion", "Avaric", "Arenvar", "Ashron",
"Aelthor", "Arenos", "Arthyn", "Avarn", "Alythos", "Azerith", "Aldran", "Aethros", "Arvandar", "Alyrith",
"Astaros", "Arenmar", "Aldyn", "Avaros", "Aethorin", "Arvyr", "Alyndaros", "Azeronyn", "Aldevor", "Arenlorin",
"Aethorin", "Arkosyn", "Avarith", "Alyrath", "Aldevyn", "Arenvoss", "Aetharion", "Arveth", "Astarion", "Alyrionis",
"Azerath", "Aldrynn", "Arenvaros", "Aethyros", "Arvandaros", "Alythorin", "Avarion",

# B (57)
"Baelor", "Baedran", "Baryn", "Belthor", "Bastor", "Brenvar", "Baldric", "Barvyn", "Beryn", "Bastyr",
"Beldros", "Brenlor", "Baryneth", "Bastorin", "Belvoss", "Baldros", "Baranth", "Beryth", "Brenvaros", "Bastorin",
"Baelthor", "Barynlor", "Belmar", "Bastyn", "Brenvoss", "Baldyn", "Barathor", "Berynth", "Belvyr", "Bastros",
"Brenmar", "Baelvyn", "Baryndar", "Belthos", "Bastarin", "Brenvyr", "Baldrosyn", "Barvoss", "Berynor", "Belvarin",
"Bastyrin", "Brenlorin", "Baelvar", "Barynoss", "Belthorin", "Bastyrion", "Brenvath", "Baldrynn", "Baranthos", "Beryndar",
"Belvath", "Bastorinyn", "Brenvarin", "Baelthos", "Baryndor", "Belmaros", "Bastyrionis",

# C (57)
"Caelor", "Caedros", "Caryn", "Calthor", "Castor", "Crenvar", "Caldric", "Carvyn", "Ceryn", "Calthos",
"Celdros", "Crenlor", "Caryneth", "Castorin", "Celvoss", "Caldros", "Caranth", "Ceryth", "Crenvaros", "Castorin",
"Caelthor", "Carynlor", "Celmar", "Castyn", "Crenvoss", "Caldyn", "Carathor", "Cerynth", "Celvyr", "Castros",
"Crenmar", "Caelvyn", "Caryndar", "Celthos", "Castarin", "Crenvyr", "Caldrosyn", "Carvoss", "Cerynor", "Celvarin",
"Castyros", "Crenlorin", "Caelvar", "Carynoss", "Celthorin", "Castyrion", "Crenvath", "Caldrynn", "Caranthos", "Ceryndar",
"Celvath", "Castorinyn", "Crenvarin", "Caelthos", "Caryndor", "Celmaros", "Castyrionis", "Cerberus"

# D (57)
"Daelor", "Daedran", "Daryn", "Dalthor", "Dastor", "Drenvar", "Daldric", "Darvyn", "Deryn", "Dalthos",
"Deldros", "Drenlor", "Daryneth", "Dastorin", "Delvoss", "Daldros", "Daranth", "Deryth", "Drenvaros", "Dastorin",
"Daelthor", "Darynlor", "Delmar", "Dastyn", "Drenvoss", "Daldyn", "Darathor", "Derynth", "Delvyr", "Dastros",
"Drenmar", "Daelvyn", "Daryndar", "Delthos", "Dastarin", "Drenvyr", "Daldrosyn", "Darvoss", "Derynor", "Delvarin",
"Dastyros", "Drenlorin", "Daelvar", "Darynoss", "Delthorin", "Dastyrion", "Drenvath", "Daldrynn", "Daranthos", "Deryndar",
"Delvath", "Dastorinyn", "Drenvarin", "Daelthos", "Daryndor", "Delmaros", "Dastyrionis",

# E (57)
"Eaelor", "Eaethor", "Earyn", "Elthor", "Estor", "Erenvar", "Eldric", "Ervyn", "Eryn", "Elthos",
"Eldros", "Erenlor", "Earyneth", "Estorin", "Elvoss", "Eldrosyn", "Erath", "Eryth", "Erenvaros", "Estorin",
"Eaelthor", "Earynlor", "Elmar", "Estyn", "Erenvoss", "Eldyn", "Erathor", "Erynth", "Elvyr", "Estros",
"Erenmar", "Eaelvyn", "Earyndar", "Elthosyn", "Estarin", "Erenvyr", "Eldran", "Ervoss", "Erynor", "Elvarin",
"Estyros", "Erenlorin", "Eaelvar", "Earynoss", "Elthorin", "Estyrion", "Erenvath", "Eldrynn", "Erathos", "Eryndar",
"Elvath", "Estorinyn", "Erenvarin", "Eaelthos", "Earyndor", "Elmaros", "Estyrionis",

# F (57)
"Faelor", "Faedros", "Faryn", "Falthor", "Fastor", "Frenvar", "Faldric", "Farvyn", "Feryn", "Falthos",
"Feldros", "Frenlor", "Faryneth", "Fastorin", "Felvoss", "Faldros", "Faranth", "Feryth", "Frenvaros", "Fastorin",
"Faelthor", "Farynlor", "Felmar", "Fastyn", "Frenvoss", "Faldyn", "Farathor", "Ferynth", "Felvyr", "Fastros",
"Frenmar", "Faelvyn", "Faryndar", "Felthos", "Fastarin", "Frenvyr", "Faldrosyn", "Farvoss", "Ferynor", "Felvarin",
"Fastyros", "Frenlorin", "Faelvar", "Farynoss", "Felthorin", "Fastyrion", "Frenvath", "Faldrynn", "Faranthos", "Feryndar",
"Felvath", "Fastorinyn", "Frenvarin", "Faelthos", "Faryndor", "Felmaros", "Fastyrionis",

# G (57)
"Gaelor", "Gaedran", "Garyn", "Galthor", "Gastor", "Grenvar", "Galdric", "Garvyn", "Geryn", "Galthos",
"Geldros", "Grenlor", "Garyneth", "Gastorin", "Gelvoss", "Galdros", "Garanth", "Geryth", "Grenvaros", "Gastorin",
"Gaelthor", "Garynlor", "Gelmar", "Gastyn", "Grenvoss", "Galdyn", "Garathor", "Gerynth", "Gelvyr", "Gastros",
"Grenmar", "Gaelvyn", "Garyndar", "Gelthos", "Gastarin", "Grenvyr", "Galdrosyn", "Garvoss", "Gerynor", "Gelvarin",
"Gastyros", "Grenlorin", "Gaelvar", "Garynoss", "Gelthorin", "Gastyrion", "Grenvath", "Galdrynn", "Garanthos", "Geryndar",
"Gelvath", "Gastorinyn", "Grenvarin", "Gaelthos", "Garyndor", "Gelmaros", "Gastyrionis",

# H (57)
"Haelor", "Haedros", "Haryn", "Halthor", "Hastor", "Hrenvar", "Haldric", "Harvyn", "Heryn", "Halthos",
"Heldros", "Hrenlor", "Haryneth", "Hastorin", "Helvoss", "Haldros", "Haranth", "Heryth", "Hrenvaros", "Hastorin",
"Haelthor", "Harynlor", "Helmar", "Hastyn", "Hrenvoss", "Haldyn", "Harathor", "Herynth", "Helvyr", "Hastros",
"Hrenmar", "Haelvyn", "Haryndar", "Helthos", "Hastarin", "Hrenvyr", "Haldrosyn", "Harvoss", "Herynor", "Helvarin",
"Hastyros", "Hrenlorin", "Haelvar", "Harynoss", "Helthorin", "Hastyrion", "Hrenvath", "Haldrynn", "Haranthos", "Heryndar",
"Helvath", "Hastorinyn", "Hrenvarin", "Haelthos", "Haryndor", "Helmaros", "Hastyrionis",

# I (57)
"Iaelor", "Iaedros", "Iaryn", "Ialthor", "Iastor", "Irenvar", "Ialdric", "Iarvyn", "Ieryn", "Ialthos",
"Ieldros", "Irenlor", "Iaryneth", "Iastorin", "Ielvoss", "Ialdros", "Iaranth", "Ieryth", "Irenvaros", "Iastorin",
"Iaelthor", "Iarynlor", "Ielmar", "Iastyn", "Irenvoss", "Ialdyn", "Iarathor", "Ierynth", "Ielvyr", "Iastros",
"Irenmar", "Iaelvyn", "Iaryndar", "Ielthos", "Iastarin", "Irenvyr", "Ialdrosyn", "Iarvoss", "Ierynor", "Ielvarin",
"Iastyros", "Irenlorin", "Iaelvar", "Iarynoss", "Ielthorin", "Iastyrion", "Irenvath", "Ialdrynn", "Iaranthos", "Ieryndar",
"Ielvath", "Iastorinyn", "Irenvarin", "Iaelthos", "Iaryndor", "Ielmaros", "Iastyrionis",

# J (57)
"Jaelor", "Jaedros", "Jaryn", "Jalthor", "Jastor", "Jrenvar", "Jaldric", "Jarvyn", "Jeryn", "Jalthos",
"Jeldros", "Jrenlor", "Jaryneth", "Jastorin", "Jelvoss", "Jaldros", "Jaranth", "Jeryth", "Jrenvaros", "Jastorin",
"Jaelthor", "Jarynlor", "Jelmar", "Jastyn", "Jrenvoss", "Jaldyn", "Jarathor", "Jerynth", "Jelvyr", "Jastros",
"Jrenmar", "Jaelvyn", "Jaryndar", "Jelthos", "Jastarin", "Jrenvyr", "Jaldrosyn", "Jarvoss", "Jerynor", "Jelvarin",
"Jastyros", "Jrenlorin", "Jaelvar", "Jarynoss", "Jelthorin", "Jastyrion", "Jrenvath", "Jaldrynn", "Jaranthos", "Jeryndar",
"Jelvath", "Jastorinyn", "Jrenvarin", "Jaelthos", "Jaryndor", "Jelmaros", "Jastyrionis",

# K (57)
"Kaelor", "Kaedros", "Karyn", "Kalthor", "Kastor", "Krenvar", "Kaldric", "Karvyn", "Keryn", "Kalthos",
"Keldros", "Krenlor", "Karyneth", "Kastorin", "Kelvoss", "Kaldros", "Karanth", "Keryth", "Krenvaros", "Kastorin",
"Kaelthor", "Karynlor", "Kelmar", "Kastyn", "Krenvoss", "Kaldyn", "Karathor", "Kerynth", "Kelvyr", "Kastros",
"Krenmar", "Kaelvyn", "Karyndar", "Kelthos", "Kastarin", "Krenvyr", "Kaldrosyn", "Karvoss", "Kerynor", "Kelvarin",
"Kastyros", "Krenlorin", "Kaelvar", "Karynoss", "Kelthorin", "Kastyrion", "Krenvath", "Kaldrynn", "Karanthos", "Keryndar",
"Kelvath", "Kastorinyn", "Krenvarin", "Kaelthos", "Karyndor", "Kelmaros", "Kastyrionis",

# L (57)
"Laelor", "Laedros", "Laryn", "Lalthor", "Lastor", "Lrenvar", "Laldric", "Larvyn", "Leryn", "Lalthos",
"Leldros", "Lrenlor", "Laryneth", "Lastorin", "Lelvoss", "Laldros", "Laranth", "Leryth", "Lrenvaros", "Lastorin",
"Laelthor", "Larynlor", "Lelmar", "Lastyn", "Lrenvoss", "Laldyn", "Larathor", "Lerynth", "Lelvyr", "Lastros",
"Lrenmar", "Laelvyn", "Laryndar", "Lelthos", "Lastarin", "Lrenvyr", "Laldrosyn", "Larvoss", "Lerynor", "Lelvarin",
"Lastyros", "Lrenlorin", "Laelvar", "Larynoss", "Lelthorin", "Lastyrion", "Lrenvath", "Laldrynn", "Laranthos", "Leryndar",
"Lelvath", "Lastorinyn", "Lrenvarin", "Laelthos", "Laryndor", "Lelmaros", "Lastyrionis",

# M (57)
"Maelor", "Maedros", "Maryn", "Malthor", "Mastor", "Mrenvar", "Maldric", "Marvyn", "Meryn", "Malthos",
"Meldros", "Mrenlor", "Maryneth", "Mastorin", "Melvoss", "Maldros", "Maranth", "Meryth", "Mrenvaros", "Mastorin",
"Maelthor", "Marynlor", "Melmar", "Mastyn", "Mrenvoss", "Maldyn", "Marathor", "Merynth", "Melvyr", "Mastros",
"Mrenmar", "Maelvyn", "Maryndar", "Melthos", "Mastarin", "Mrenvyr", "Maldrosyn", "Marvoss", "Merynor", "Melvarin",
"Mastyros", "Mrenlorin", "Maelvar", "Marynoss", "Melthorin", "Mastyrion", "Mrenvath", "Maldrynn", "Maranthos", "Meryndar",
"Melvath", "Mastorinyn", "Mrenvarin", "Maelthos", "Maryndor", "Melmaros", "Mastyrionis",

# N (57)
"Naelor", "Naedros", "Naryn", "Nalthor", "Nastor", "Nrenvar", "Naldric", "Narvyn", "Neryn", "Nalthos",
"Neldros", "Nrenlor", "Naryneth", "Nastorin", "Nelvoss", "Naldros", "Naranth", "Neryth", "Nrenvaros", "Nastorin",
"Naelthor", "Narynlor", "Nelmar", "Nastyn", "Nrenvoss", "Naldyn", "Narathor", "Nerynth", "Nelvyr", "Nastros",
"Nrenmar", "Naelvyn", "Naryndar", "Nelthos", "Nastarin", "Nrenvyr", "Naldrosyn", "Narvoss", "Nerynor", "Nelvarin",
"Nastyros", "Nrenlorin", "Naelvar", "Narynoss", "Nelthorin", "Nastyrion", "Nrenvath", "Naldrynn", "Naranthos", "Neryndar",
"Nelvath", "Nastorinyn", "Nrenvarin", "Naelthos", "Naryndor", "Nelmaros", "Nastyrionis",

# O (57)
"Oaelor", "Oaedros", "Oaryn", "Oalthor", "Oastor", "Orenvar", "Oaldric", "Oarvyn", "Oeryn", "Oalthos",
"Oeldros", "Orenlor", "Oaryneth", "Oastorin", "Oelvoss", "Oaldros", "Oaranth", "Oeryth", "Orenvaros", "Oastorin",
"Oaelthor", "Oarynlor", "Oelmar", "Oastyn", "Orenvoss", "Oaldyn", "Oarathor", "Oerynth", "Oelvyr", "Oastros",
"Orenmar", "Oaelvyn", "Oaryndar", "Oelthos", "Oastarin", "Orenvyr", "Oaldrosyn", "Oarvoss", "Oerynor", "Oelvarin",
"Oastyros", "Orenlorin", "Oaelvar", "Oarynoss", "Oelthorin", "Oastyrion", "Orenvath", "Oaldrynn", "Oaranthos", "Oeryndar",
"Oelvath", "Oastorinyn", "Orenvarin", "Oaelthos", "Oaryndor", "Oelmaros", "Oastyrionis",

# P (57)
"Paelor", "Paedros", "Paryn", "Palthor", "Pastor", "Prenvar", "Paldric", "Parvyn", "Peryn", "Palthos",
"Peldros", "Prenlor", "Paryneth", "Pastorin", "Pelvoss", "Paldros", "Paranth", "Peryth", "Prenvaros", "Pastorin",
"Paelthor", "Parynlor", "Pelmar", "Qaelor","Qaedros","Qaryn","Qalthor","Qastor","Qrenvar","Qaldric","Qarvyn","Qeryn","Qalthos",
    "Qeldros","Qrenlor","Qaryneth","Qastorin","Qelvoss","Qaldros","Qaranth","Qeryth","Qrenvaros","Qastorin",
    "Qaelthor","Qarynlor","Qelmar","Qastyn","Qrenvoss","Qaldyn","Qarathor","Qerynth","Qelvyr","Qastros",
    "Qrenmar","Qaelvyn","Qaryndar","Qelthos","Qastarin","Qrenvyr","Qaldrosyn","Qarvoss","Qerynor","Qelvarin",
    "Qastyros","Qrenlorin","Qaelvar","Qarynoss","Qelthorin","Qastyrion","Qrenvath","Qaldrynn","Qaranthos","Qeryndar",
    "Qelvath","Qastorinyn","Qrenvarin","Qaelthos","Qaryndor","Qelmaros","Qastyrionis",

    # R (57)
    "Raelor","Raedros","Raryn","Ralthor","Rastor","Rrenvar","Raldric","Rarvyn","Reryn","Ralthos",
    "Reldros","Rrenlor","Raryneth","Rastorin","Relvoss","Raldros","Raranth","Reryth","Rrenvaros","Rastorin",
    "Raelthor","Rarynlor","Relmar","Rastyn","Rrenvoss","Raldyn","Rarathor","Rerynth","Relvyr","Rastros",
    "Rrenmar","Raelvyn","Raryndar","Relthos","Rastarin","Rrenvyr","Raldrosyn","Rarvoss","Rerynor","Relvarin",
    "Rastyros","Rrenlorin","Raelvar","Rarynoss","Relthorin","Rastyrion","Rrenvath","Raldrynn","Raranthos","Reryndar",
    "Relvath","Rastorinyn","Rrenvarin","Raelthos","Raryndor","Relmaros","Rastyrionis",

    # S (57)
    "Saelor","Saedros","Saryn","Salthor","Sastor","Srenvar","Saldric","Sarvyn","Seryn","Salthos",
    "Seldros","Srenlor","Saryneth","Sastorin","Selvoss","Saldros","Saranth","Seryth","Srenvaros","Sastorin",
    "Saelthor","Sarynlor","Selmar","Sastyn","Srenvoss","Saldyn","Sarathor","Serynth","Selvyr","Sastros",
    "Srenmar","Saelvyn","Saryndar","Selthos","Sastarin","Srenvyr","Saldrosyn","Sarvoss","Serynor","Selvarin",
    "Sastyros","Srenlorin","Saelvar","Sarynoss","Selthorin","Sastyrion","Srenvath","Saldrynn","Saranthos","Seryndar",
    "Selvath","Sastorinyn","Srenvarin","Saelthos","Saryndor","Selmaros","Sastyrionis",

    # T (57)
    "Taelor","Taedros","Taryn","Talthor","Tastor","Trenvar","Taldric","Tarvyn","Teryn","Talthos",
    "Teldros","Trenlor","Taryneth","Tastorin","Telvoss","Taldros","Taranth","Teryth","Trenvaros","Tastorin",
    "Taelthor","Tarynlor","Telmar","Tastyn","Trenvoss","Taldyn","Tarathor","Terynth","Telvyr","Tastros",
    "Trenmar","Taelvyn","Taryndar","Telthos","Tastarin","Trenvyr","Taldrosyn","Tarvoss","Terynor","Telvarin",
    "Tastyros","Trenlorin","Taelvar","Tarynoss","Telthorin","Tastyrion","Trenvath","Taldrynn","Taranthos","Teryndar",
    "Telvath","Tastorinyn","Trenvarin","Taelthos","Taryndor","Telmaros","Tastyrionis",

    # U (57)
    "Uaelor","Uaedros","Uaryn","Ualthor","Uastor","Urenvar","Ualdric","Uarvyn","Ueryn","Ualthos",
    "Ueldros","Urenlor","Uaryneth","Uastorin","Uelvoss","Ualdros","Uaranth","Ueryth","Urenvaros","Uastorin",
    "Uaelthor","Uarynlor","Uelmar","Uastyn","Urenvoss","Ualdyn","Uarathor","Uerynth","Uelvyr","Uastros",
    "Urenmar","Uaelvyn","Uaryndar","Uelthos","Uastarin","Urenvyr","Ualdrosyn","Uarvoss","Uerynor","Uelvarin",
    "Uastyros","Urenlorin","Uaelvar","Uarynoss","Uelthorin","Uastyrion","Urenvath","Ualdrynn","Uaranthos","Ueryndar",
    "Uelvath","Uastorinyn","Urenvarin","Uaelthos","Uaryndor","Uelmaros","Uastyrionis",

    # V (57)
    "Vaelor","Vaedros","Varyn","Valthor","Vastor","Vrenvar","Valdric","Varvyn","Veryn","Valthos",
    "Veldros","Vrenlor","Varyneth","Vastorin","Velvoss","Valdros","Varanth","Veryth","Vrenvaros","Vastorin",
    "Vaelthor","Varynlor","Velmar","Vastyn","Vrenvoss","Valdyn","Varathor","Verynth","Velvyr","Vastros",
    "Vrenmar","Vaelvyn","Varyndar","Velthos","Vastarin","Vrenvyr","Valdrosyn","Varvoss","Verynor","Velvarin",
    "Vastyros","Vrenlorin","Vaelvar","Varynoss","Velthorin","Vastyrion","Vrenvath","Valdrynn","Varanthos","Veryndar",
    "Velvath","Vastorinyn","Vrenvarin","Vaelthos","Varyndor","Velmaros","Vastyrionis",

    # W (57)
    "Waelor","Waedros","Waryn","Walthor","Wastor","Wrenvar","Waldric","Warvyn","Weryn","Walthos",
    "Weldros","Wrenlor","Waryneth","Wastorin","Welvoss","Waldros","Waranth","Weryth","Wrenvaros","Wastorin",
    "Waelthor","Warynlor","Welmar","Wastyn","Wrenvoss","Waldyn","Warathor","Werynth","Welvyr","Wastros",
    "Wrenmar","Waelvyn","Waryndar","Welthos","Wastarin","Wrenvyr","Waldrosyn","Warvoss","Werynor","Welvarin",
    "Wastyros","Wrenlorin","Waelvar","Warynoss","Welthorin","Wastyrion","Wrenvath","Waldrynn","Waranthos","Weryndar",
    "Welvath","Wastorinyn","Wrenvarin","Waelthos","Waryndor","Welmaros","Wastyrionis",

    # X (57)
    "Xaelor","Xaedros","Xaryn","Xalthor","Xastor","Xrenvar","Xaldric","Xarvyn","Xeryn","Xalthos",
    "Xeldros","Xrenlor","Xaryneth","Xastorin","Xelvoss","Xaldros","Xaranth","Xeryth","Xrenvaros","Xastorin",
    "Xaelthor","Xarynlor","Xelmar","Xastyn","Xrenvoss","Xaldyn","Xarathor","Xerynth","Xelvyr","Xastros",
    "Xrenmar","Xaelvyn","Xaryndar","Xelthos","Xastarin","Xrenvyr","Xaldrosyn","Xarvoss","Xerynor","Xelvarin",
    "Xastyros","Xrenlorin","Xaelvar","Xarynoss","Xelthorin","Xastyrion","Xrenvath","Xaldrynn","Xaranthos","Xeryndar",
    "Xelvath","Xastorinyn","Xrenvarin","Xaelthos","Xaryndor","Xelmaros","Xastyrionis",

    # Y (57)
    "Yaelor","Yaedros","Yaryn","Yalthor","Yastor","Yrenvar","Yaldric","Yarvyn","Yeryn","Yalthos",
    "Yeldros","Yrenlor","Yaryneth","Yastorin","Yelvoss","Yaldros","Yaranth","Yeryth","Yrenvaros","Yastorin",
    "Yaelthor","Yarynlor","Yelmar","Yastyn","Yrenvoss","Yaldyn","Yarathor","Yerynth","Yelvyr","Yastros",
    "Yrenmar","Yaelvyn","Yaryndar","Yelthos","Yastarin","Yrenvyr","Yaldrosyn","Yarvoss","Yerynor","Yelvarin",
    "Yastyros","Yrenlorin","Yaelvar","Yarynoss","Yelthorin","Yastyrion","Yrenvath","Yaldrynn","Yaranthos","Yeryndar",
    "Yelvath","Yastorinyn","Yrenvarin","Yaelthos","Yaryndor","Yelmaros","Yastyrionis",

    # Z (57)
    "Zaelor","Zaedros","Zaryn","Zalthor","Zastor","Zrenvar","Zaldric","Zarvyn","Zeryn","Zalthos",
    "Zeldros","Zrenlor","Zaryneth","Zastorin","Zelvoss","Zaldros","Zaranth","Zeryth","Zrenvaros","Zastorin",
    "Zaelthor","Zarynlor","Zelmar","Zastyn","Zrenvoss","Zaldyn","Zarathor","Zerynth","Zelvyr","Zastros",
    "Zrenmar","Zaelvyn","Zaryndar","Zelthos","Zastarin","Zrenvyr","Zaldrosyn","Zarvoss","Zerynor","Zelvarin",
    "Zastyros","Zrenlorin","Zaelvar","Zarynoss","Zelthorin","Zastyrion","Zrenvath","Zaldrynn","Zaranthos","Zeryndar",
    "Zelvath","Zastorinyn","Zrenvarin","Zaelthos","Zaryndor","Zelmaros","Zastyrionis"]
tsallis_madhi_names1 = ["Aeron", "Aelric", "Aethor", "Avaron", "Aldric", "Arvyn", "Arenlor", "Astarin", "Atheron", "Alyndar",
"Arenith", "Arkos", "Azeron", "Aldros", "Aethyn", "Arvoss", "Alyrion", "Avaric", "Arenvar", "Ashron",
"Aelthor", "Arenos", "Arthyn", "Avarn", "Alythos", "Azerith", "Aldran", "Aethros", "Arvandar", "Alyrith",
"Astaros", "Arenmar", "Aldyn", "Avaros", "Aethorin", "Arvyr", "Alyndaros", "Azeronyn", "Aldevor", "Arenlorin",
"Aethorin", "Arkosyn", "Avarith", "Alyrath", "Aldevyn", "Arenvoss", "Aetharion", "Arveth", "Astarion", "Alyrionis",
"Azerath", "Aldrynn", "Arenvaros", "Aethyros", "Arvandaros", "Alythorin", "Avarion",

# B (57)
"Baelor", "Baedran", "Baryn", "Belthor", "Bastor", "Brenvar", "Baldric", "Barvyn", "Beryn", "Bastyr",
"Beldros", "Brenlor", "Baryneth", "Bastorin", "Belvoss", "Baldros", "Baranth", "Beryth", "Brenvaros", "Bastorin",
"Baelthor", "Barynlor", "Belmar", "Bastyn", "Brenvoss", "Baldyn", "Barathor", "Berynth", "Belvyr", "Bastros",
"Brenmar", "Baelvyn", "Baryndar", "Belthos", "Bastarin", "Brenvyr", "Baldrosyn", "Barvoss", "Berynor", "Belvarin",
"Bastyrin", "Brenlorin", "Baelvar", "Barynoss", "Belthorin", "Bastyrion", "Brenvath", "Baldrynn", "Baranthos", "Beryndar",
"Belvath", "Bastorinyn", "Brenvarin", "Baelthos", "Baryndor", "Belmaros", "Bastyrionis",

# C (57)
"Caelor", "Caedros", "Caryn", "Calthor", "Castor", "Crenvar", "Caldric", "Carvyn", "Ceryn", "Calthos",
"Celdros", "Crenlor", "Caryneth", "Castorin", "Celvoss", "Caldros", "Caranth", "Ceryth", "Crenvaros", "Castorin",
"Caelthor", "Carynlor", "Celmar", "Castyn", "Crenvoss", "Caldyn", "Carathor", "Cerynth", "Celvyr", "Castros",
"Crenmar", "Caelvyn", "Caryndar", "Celthos", "Castarin", "Crenvyr", "Caldrosyn", "Carvoss", "Cerynor", "Celvarin",
"Castyros", "Crenlorin", "Caelvar", "Carynoss", "Celthorin", "Castyrion", "Crenvath", "Caldrynn", "Caranthos", "Ceryndar",
"Celvath", "Castorinyn", "Crenvarin", "Caelthos", "Caryndor", "Celmaros", "Castyrionis", "Cerberus"

# D (57)
"Daelor", "Daedran", "Daryn", "Dalthor", "Dastor", "Drenvar", "Daldric", "Darvyn", "Deryn", "Dalthos",
"Deldros", "Drenlor", "Daryneth", "Dastorin", "Delvoss", "Daldros", "Daranth", "Deryth", "Drenvaros", "Dastorin",
"Daelthor", "Darynlor", "Delmar", "Dastyn", "Drenvoss", "Daldyn", "Darathor", "Derynth", "Delvyr", "Dastros",
"Drenmar", "Daelvyn", "Daryndar", "Delthos", "Dastarin", "Drenvyr", "Daldrosyn", "Darvoss", "Derynor", "Delvarin",
"Dastyros", "Drenlorin", "Daelvar", "Darynoss", "Delthorin", "Dastyrion", "Drenvath", "Daldrynn", "Daranthos", "Deryndar",
"Delvath", "Dastorinyn", "Drenvarin", "Daelthos", "Daryndor", "Delmaros", "Dastyrionis",

# E (57)
"Eaelor", "Eaethor", "Earyn", "Elthor", "Estor", "Erenvar", "Eldric", "Ervyn", "Eryn", "Elthos",
"Eldros", "Erenlor", "Earyneth", "Estorin", "Elvoss", "Eldrosyn", "Erath", "Eryth", "Erenvaros", "Estorin",
"Eaelthor", "Earynlor", "Elmar", "Estyn", "Erenvoss", "Eldyn", "Erathor", "Erynth", "Elvyr", "Estros",
"Erenmar", "Eaelvyn", "Earyndar", "Elthosyn", "Estarin", "Erenvyr", "Eldran", "Ervoss", "Erynor", "Elvarin",
"Estyros", "Erenlorin", "Eaelvar", "Earynoss", "Elthorin", "Estyrion", "Erenvath", "Eldrynn", "Erathos", "Eryndar",
"Elvath", "Estorinyn", "Erenvarin", "Eaelthos", "Earyndor", "Elmaros", "Estyrionis",

# F (57)
"Faelor", "Faedros", "Faryn", "Falthor", "Fastor", "Frenvar", "Faldric", "Farvyn", "Feryn", "Falthos",
"Feldros", "Frenlor", "Faryneth", "Fastorin", "Felvoss", "Faldros", "Faranth", "Feryth", "Frenvaros", "Fastorin",
"Faelthor", "Farynlor", "Felmar", "Fastyn", "Frenvoss", "Faldyn", "Farathor", "Ferynth", "Felvyr", "Fastros",
"Frenmar", "Faelvyn", "Faryndar", "Felthos", "Fastarin", "Frenvyr", "Faldrosyn", "Farvoss", "Ferynor", "Felvarin",
"Fastyros", "Frenlorin", "Faelvar", "Farynoss", "Felthorin", "Fastyrion", "Frenvath", "Faldrynn", "Faranthos", "Feryndar",
"Felvath", "Fastorinyn", "Frenvarin", "Faelthos", "Faryndor", "Felmaros", "Fastyrionis",

# G (57)
"Gaelor", "Gaedran", "Garyn", "Galthor", "Gastor", "Grenvar", "Galdric", "Garvyn", "Geryn", "Galthos",
"Geldros", "Grenlor", "Garyneth", "Gastorin", "Gelvoss", "Galdros", "Garanth", "Geryth", "Grenvaros", "Gastorin",
"Gaelthor", "Garynlor", "Gelmar", "Gastyn", "Grenvoss", "Galdyn", "Garathor", "Gerynth", "Gelvyr", "Gastros",
"Grenmar", "Gaelvyn", "Garyndar", "Gelthos", "Gastarin", "Grenvyr", "Galdrosyn", "Garvoss", "Gerynor", "Gelvarin",
"Gastyros", "Grenlorin", "Gaelvar", "Garynoss", "Gelthorin", "Gastyrion", "Grenvath", "Galdrynn", "Garanthos", "Geryndar",
"Gelvath", "Gastorinyn", "Grenvarin", "Gaelthos", "Garyndor", "Gelmaros", "Gastyrionis",

# H (57)
"Haelor", "Haedros", "Haryn", "Halthor", "Hastor", "Hrenvar", "Haldric", "Harvyn", "Heryn", "Halthos",
"Heldros", "Hrenlor", "Haryneth", "Hastorin", "Helvoss", "Haldros", "Haranth", "Heryth", "Hrenvaros", "Hastorin",
"Haelthor", "Harynlor", "Helmar", "Hastyn", "Hrenvoss", "Haldyn", "Harathor", "Herynth", "Helvyr", "Hastros",
"Hrenmar", "Haelvyn", "Haryndar", "Helthos", "Hastarin", "Hrenvyr", "Haldrosyn", "Harvoss", "Herynor", "Helvarin",
"Hastyros", "Hrenlorin", "Haelvar", "Harynoss", "Helthorin", "Hastyrion", "Hrenvath", "Haldrynn", "Haranthos", "Heryndar",
"Helvath", "Hastorinyn", "Hrenvarin", "Haelthos", "Haryndor", "Helmaros", "Hastyrionis",

# I (57)
"Iaelor", "Iaedros", "Iaryn", "Ialthor", "Iastor", "Irenvar", "Ialdric", "Iarvyn", "Ieryn", "Ialthos",
"Ieldros", "Irenlor", "Iaryneth", "Iastorin", "Ielvoss", "Ialdros", "Iaranth", "Ieryth", "Irenvaros", "Iastorin",
"Iaelthor", "Iarynlor", "Ielmar", "Iastyn", "Irenvoss", "Ialdyn", "Iarathor", "Ierynth", "Ielvyr", "Iastros",
"Irenmar", "Iaelvyn", "Iaryndar", "Ielthos", "Iastarin", "Irenvyr", "Ialdrosyn", "Iarvoss", "Ierynor", "Ielvarin",
"Iastyros", "Irenlorin", "Iaelvar", "Iarynoss", "Ielthorin", "Iastyrion", "Irenvath", "Ialdrynn", "Iaranthos", "Ieryndar",
"Ielvath", "Iastorinyn", "Irenvarin", "Iaelthos", "Iaryndor", "Ielmaros", "Iastyrionis",

# J (57)
"Jaelor", "Jaedros", "Jaryn", "Jalthor", "Jastor", "Jrenvar", "Jaldric", "Jarvyn", "Jeryn", "Jalthos",
"Jeldros", "Jrenlor", "Jaryneth", "Jastorin", "Jelvoss", "Jaldros", "Jaranth", "Jeryth", "Jrenvaros", "Jastorin",
"Jaelthor", "Jarynlor", "Jelmar", "Jastyn", "Jrenvoss", "Jaldyn", "Jarathor", "Jerynth", "Jelvyr", "Jastros",
"Jrenmar", "Jaelvyn", "Jaryndar", "Jelthos", "Jastarin", "Jrenvyr", "Jaldrosyn", "Jarvoss", "Jerynor", "Jelvarin",
"Jastyros", "Jrenlorin", "Jaelvar", "Jarynoss", "Jelthorin", "Jastyrion", "Jrenvath", "Jaldrynn", "Jaranthos", "Jeryndar",
"Jelvath", "Jastorinyn", "Jrenvarin", "Jaelthos", "Jaryndor", "Jelmaros", "Jastyrionis",

# K (57)
"Kaelor", "Kaedros", "Karyn", "Kalthor", "Kastor", "Krenvar", "Kaldric", "Karvyn", "Keryn", "Kalthos",
"Keldros", "Krenlor", "Karyneth", "Kastorin", "Kelvoss", "Kaldros", "Karanth", "Keryth", "Krenvaros", "Kastorin",
"Kaelthor", "Karynlor", "Kelmar", "Kastyn", "Krenvoss", "Kaldyn", "Karathor", "Kerynth", "Kelvyr", "Kastros",
"Krenmar", "Kaelvyn", "Karyndar", "Kelthos", "Kastarin", "Krenvyr", "Kaldrosyn", "Karvoss", "Kerynor", "Kelvarin",
"Kastyros", "Krenlorin", "Kaelvar", "Karynoss", "Kelthorin", "Kastyrion", "Krenvath", "Kaldrynn", "Karanthos", "Keryndar",
"Kelvath", "Kastorinyn", "Krenvarin", "Kaelthos", "Karyndor", "Kelmaros", "Kastyrionis",

# L (57)
"Laelor", "Laedros", "Laryn", "Lalthor", "Lastor", "Lrenvar", "Laldric", "Larvyn", "Leryn", "Lalthos",
"Leldros", "Lrenlor", "Laryneth", "Lastorin", "Lelvoss", "Laldros", "Laranth", "Leryth", "Lrenvaros", "Lastorin",
"Laelthor", "Larynlor", "Lelmar", "Lastyn", "Lrenvoss", "Laldyn", "Larathor", "Lerynth", "Lelvyr", "Lastros",
"Lrenmar", "Laelvyn", "Laryndar", "Lelthos", "Lastarin", "Lrenvyr", "Laldrosyn", "Larvoss", "Lerynor", "Lelvarin",
"Lastyros", "Lrenlorin", "Laelvar", "Larynoss", "Lelthorin", "Lastyrion", "Lrenvath", "Laldrynn", "Laranthos", "Leryndar",
"Lelvath", "Lastorinyn", "Lrenvarin", "Laelthos", "Laryndor", "Lelmaros", "Lastyrionis",

# M (57)
"Maelor", "Maedros", "Maryn", "Malthor", "Mastor", "Mrenvar", "Maldric", "Marvyn", "Meryn", "Malthos",
"Meldros", "Mrenlor", "Maryneth", "Mastorin", "Melvoss", "Maldros", "Maranth", "Meryth", "Mrenvaros", "Mastorin",
"Maelthor", "Marynlor", "Melmar", "Mastyn", "Mrenvoss", "Maldyn", "Marathor", "Merynth", "Melvyr", "Mastros",
"Mrenmar", "Maelvyn", "Maryndar", "Melthos", "Mastarin", "Mrenvyr", "Maldrosyn", "Marvoss", "Merynor", "Melvarin",
"Mastyros", "Mrenlorin", "Maelvar", "Marynoss", "Melthorin", "Mastyrion", "Mrenvath", "Maldrynn", "Maranthos", "Meryndar",
"Melvath", "Mastorinyn", "Mrenvarin", "Maelthos", "Maryndor", "Melmaros", "Mastyrionis",

# N (57)
"Naelor", "Naedros", "Naryn", "Nalthor", "Nastor", "Nrenvar", "Naldric", "Narvyn", "Neryn", "Nalthos",
"Neldros", "Nrenlor", "Naryneth", "Nastorin", "Nelvoss", "Naldros", "Naranth", "Neryth", "Nrenvaros", "Nastorin",
"Naelthor", "Narynlor", "Nelmar", "Nastyn", "Nrenvoss", "Naldyn", "Narathor", "Nerynth", "Nelvyr", "Nastros",
"Nrenmar", "Naelvyn", "Naryndar", "Nelthos", "Nastarin", "Nrenvyr", "Naldrosyn", "Narvoss", "Nerynor", "Nelvarin",
"Nastyros", "Nrenlorin", "Naelvar", "Narynoss", "Nelthorin", "Nastyrion", "Nrenvath", "Naldrynn", "Naranthos", "Neryndar",
"Nelvath", "Nastorinyn", "Nrenvarin", "Naelthos", "Naryndor", "Nelmaros", "Nastyrionis",

# O (57)
"Oaelor", "Oaedros", "Oaryn", "Oalthor", "Oastor", "Orenvar", "Oaldric", "Oarvyn", "Oeryn", "Oalthos",
"Oeldros", "Orenlor", "Oaryneth", "Oastorin", "Oelvoss", "Oaldros", "Oaranth", "Oeryth", "Orenvaros", "Oastorin",
"Oaelthor", "Oarynlor", "Oelmar", "Oastyn", "Orenvoss", "Oaldyn", "Oarathor", "Oerynth", "Oelvyr", "Oastros",
"Orenmar", "Oaelvyn", "Oaryndar", "Oelthos", "Oastarin", "Orenvyr", "Oaldrosyn", "Oarvoss", "Oerynor", "Oelvarin",
"Oastyros", "Orenlorin", "Oaelvar", "Oarynoss", "Oelthorin", "Oastyrion", "Orenvath", "Oaldrynn", "Oaranthos", "Oeryndar",
"Oelvath", "Oastorinyn", "Orenvarin", "Oaelthos", "Oaryndor", "Oelmaros", "Oastyrionis",

# P (57)
"Paelor", "Paedros", "Paryn", "Palthor", "Pastor", "Prenvar", "Paldric", "Parvyn", "Peryn", "Palthos",
"Peldros", "Prenlor", "Paryneth", "Pastorin", "Pelvoss", "Paldros", "Paranth", "Peryth", "Prenvaros", "Pastorin",
"Paelthor", "Parynlor", "Pelmar", "Qaelor","Qaedros","Qaryn","Qalthor","Qastor","Qrenvar","Qaldric","Qarvyn","Qeryn","Qalthos",
    "Qeldros","Qrenlor","Qaryneth","Qastorin","Qelvoss","Qaldros","Qaranth","Qeryth","Qrenvaros","Qastorin",
    "Qaelthor","Qarynlor","Qelmar","Qastyn","Qrenvoss","Qaldyn","Qarathor","Qerynth","Qelvyr","Qastros",
    "Qrenmar","Qaelvyn","Qaryndar","Qelthos","Qastarin","Qrenvyr","Qaldrosyn","Qarvoss","Qerynor","Qelvarin",
    "Qastyros","Qrenlorin","Qaelvar","Qarynoss","Qelthorin","Qastyrion","Qrenvath","Qaldrynn","Qaranthos","Qeryndar",
    "Qelvath","Qastorinyn","Qrenvarin","Qaelthos","Qaryndor","Qelmaros","Qastyrionis",

    # R (57)
    "Raelor","Raedros","Raryn","Ralthor","Rastor","Rrenvar","Raldric","Rarvyn","Reryn","Ralthos",
    "Reldros","Rrenlor","Raryneth","Rastorin","Relvoss","Raldros","Raranth","Reryth","Rrenvaros","Rastorin",
    "Raelthor","Rarynlor","Relmar","Rastyn","Rrenvoss","Raldyn","Rarathor","Rerynth","Relvyr","Rastros",
    "Rrenmar","Raelvyn","Raryndar","Relthos","Rastarin","Rrenvyr","Raldrosyn","Rarvoss","Rerynor","Relvarin",
    "Rastyros","Rrenlorin","Raelvar","Rarynoss","Relthorin","Rastyrion","Rrenvath","Raldrynn","Raranthos","Reryndar",
    "Relvath","Rastorinyn","Rrenvarin","Raelthos","Raryndor","Relmaros","Rastyrionis",

    # S (57)
    "Saelor","Saedros","Saryn","Salthor","Sastor","Srenvar","Saldric","Sarvyn","Seryn","Salthos",
    "Seldros","Srenlor","Saryneth","Sastorin","Selvoss","Saldros","Saranth","Seryth","Srenvaros","Sastorin",
    "Saelthor","Sarynlor","Selmar","Sastyn","Srenvoss","Saldyn","Sarathor","Serynth","Selvyr","Sastros",
    "Srenmar","Saelvyn","Saryndar","Selthos","Sastarin","Srenvyr","Saldrosyn","Sarvoss","Serynor","Selvarin",
    "Sastyros","Srenlorin","Saelvar","Sarynoss","Selthorin","Sastyrion","Srenvath","Saldrynn","Saranthos","Seryndar",
    "Selvath","Sastorinyn","Srenvarin","Saelthos","Saryndor","Selmaros","Sastyrionis",

    # T (57)
    "Taelor","Taedros","Taryn","Talthor","Tastor","Trenvar","Taldric","Tarvyn","Teryn","Talthos",
    "Teldros","Trenlor","Taryneth","Tastorin","Telvoss","Taldros","Taranth","Teryth","Trenvaros","Tastorin",
    "Taelthor","Tarynlor","Telmar","Tastyn","Trenvoss","Taldyn","Tarathor","Terynth","Telvyr","Tastros",
    "Trenmar","Taelvyn","Taryndar","Telthos","Tastarin","Trenvyr","Taldrosyn","Tarvoss","Terynor","Telvarin",
    "Tastyros","Trenlorin","Taelvar","Tarynoss","Telthorin","Tastyrion","Trenvath","Taldrynn","Taranthos","Teryndar",
    "Telvath","Tastorinyn","Trenvarin","Taelthos","Taryndor","Telmaros","Tastyrionis",

    # U (57)
    "Uaelor","Uaedros","Uaryn","Ualthor","Uastor","Urenvar","Ualdric","Uarvyn","Ueryn","Ualthos",
    "Ueldros","Urenlor","Uaryneth","Uastorin","Uelvoss","Ualdros","Uaranth","Ueryth","Urenvaros","Uastorin",
    "Uaelthor","Uarynlor","Uelmar","Uastyn","Urenvoss","Ualdyn","Uarathor","Uerynth","Uelvyr","Uastros",
    "Urenmar","Uaelvyn","Uaryndar","Uelthos","Uastarin","Urenvyr","Ualdrosyn","Uarvoss","Uerynor","Uelvarin",
    "Uastyros","Urenlorin","Uaelvar","Uarynoss","Uelthorin","Uastyrion","Urenvath","Ualdrynn","Uaranthos","Ueryndar",
    "Uelvath","Uastorinyn","Urenvarin","Uaelthos","Uaryndor","Uelmaros","Uastyrionis",

    # V (57)
    "Vaelor","Vaedros","Varyn","Valthor","Vastor","Vrenvar","Valdric","Varvyn","Veryn","Valthos",
    "Veldros","Vrenlor","Varyneth","Vastorin","Velvoss","Valdros","Varanth","Veryth","Vrenvaros","Vastorin",
    "Vaelthor","Varynlor","Velmar","Vastyn","Vrenvoss","Valdyn","Varathor","Verynth","Velvyr","Vastros",
    "Vrenmar","Vaelvyn","Varyndar","Velthos","Vastarin","Vrenvyr","Valdrosyn","Varvoss","Verynor","Velvarin",
    "Vastyros","Vrenlorin","Vaelvar","Varynoss","Velthorin","Vastyrion","Vrenvath","Valdrynn","Varanthos","Veryndar",
    "Velvath","Vastorinyn","Vrenvarin","Vaelthos","Varyndor","Velmaros","Vastyrionis",

    # W (57)
    "Waelor","Waedros","Waryn","Walthor","Wastor","Wrenvar","Waldric","Warvyn","Weryn","Walthos",
    "Weldros","Wrenlor","Waryneth","Wastorin","Welvoss","Waldros","Waranth","Weryth","Wrenvaros","Wastorin",
    "Waelthor","Warynlor","Welmar","Wastyn","Wrenvoss","Waldyn","Warathor","Werynth","Welvyr","Wastros",
    "Wrenmar","Waelvyn","Waryndar","Welthos","Wastarin","Wrenvyr","Waldrosyn","Warvoss","Werynor","Welvarin",
    "Wastyros","Wrenlorin","Waelvar","Warynoss","Welthorin","Wastyrion","Wrenvath","Waldrynn","Waranthos","Weryndar",
    "Welvath","Wastorinyn","Wrenvarin","Waelthos","Waryndor","Welmaros","Wastyrionis",

    # X (57)
    "Xaelor","Xaedros","Xaryn","Xalthor","Xastor","Xrenvar","Xaldric","Xarvyn","Xeryn","Xalthos",
    "Xeldros","Xrenlor","Xaryneth","Xastorin","Xelvoss","Xaldros","Xaranth","Xeryth","Xrenvaros","Xastorin",
    "Xaelthor","Xarynlor","Xelmar","Xastyn","Xrenvoss","Xaldyn","Xarathor","Xerynth","Xelvyr","Xastros",
    "Xrenmar","Xaelvyn","Xaryndar","Xelthos","Xastarin","Xrenvyr","Xaldrosyn","Xarvoss","Xerynor","Xelvarin",
    "Xastyros","Xrenlorin","Xaelvar","Xarynoss","Xelthorin","Xastyrion","Xrenvath","Xaldrynn","Xaranthos","Xeryndar",
    "Xelvath","Xastorinyn","Xrenvarin","Xaelthos","Xaryndor","Xelmaros","Xastyrionis",

    # Y (57)
    "Yaelor","Yaedros","Yaryn","Yalthor","Yastor","Yrenvar","Yaldric","Yarvyn","Yeryn","Yalthos",
    "Yeldros","Yrenlor","Yaryneth","Yastorin","Yelvoss","Yaldros","Yaranth","Yeryth","Yrenvaros","Yastorin",
    "Yaelthor","Yarynlor","Yelmar","Yastyn","Yrenvoss","Yaldyn","Yarathor","Yerynth","Yelvyr","Yastros",
    "Yrenmar","Yaelvyn","Yaryndar","Yelthos","Yastarin","Yrenvyr","Yaldrosyn","Yarvoss","Yerynor","Yelvarin",
    "Yastyros","Yrenlorin","Yaelvar","Yarynoss","Yelthorin","Yastyrion","Yrenvath","Yaldrynn","Yaranthos","Yeryndar",
    "Yelvath","Yastorinyn","Yrenvarin","Yaelthos","Yaryndor","Yelmaros","Yastyrionis",

    # Z (57)
    "Zaelor","Zaedros","Zaryn","Zalthor","Zastor","Zrenvar","Zaldric","Zarvyn","Zeryn","Zalthos",
    "Zeldros","Zrenlor","Zaryneth","Zastorin","Zelvoss","Zaldros","Zaranth","Zeryth","Zrenvaros","Zastorin",
    "Zaelthor","Zarynlor","Zelmar","Zastyn","Zrenvoss","Zaldyn","Zarathor","Zerynth","Zelvyr","Zastros",
    "Zrenmar","Zaelvyn","Zaryndar","Zelthos","Zastarin","Zrenvyr","Zaldrosyn","Zarvoss","Zerynor","Zelvarin",
    "Zastyros","Zrenlorin","Zaelvar","Zarynoss","Zelthorin","Zastyrion","Zrenvath","Zaldrynn","Zaranthos","Zeryndar",
    "Zelvath","Zastorinyn","Zrenvarin","Zaelthos","Zaryndor","Zelmaros","Zastyrionis"]
massieu_names = [
    # A (57)
    "Aurelienn","Avariste","Aldémar","Arsavoix","Aubrennel","Amandric","Avermont","Alaireau","Ardévant","Aubryel",
    "Aurelvois","Amandrel","Arclavien","Aubrenoir","Aldévoix","Arsélian","Avarmont","Aubrelien","Ardennaux","Alaivert",
    "Aurelmarc","Amandier","Arsavoine","Aubrenard","Aldémont","Arclavier","Avariel","Aubryvant","Ardémar","Alaivaux",
    "Aurelvoine","Amandricel","Arsélavoix","Aubrenval","Aldérian","Arclavert","Avarnois","Aubrelmont","Ardévain","Alaivern",
    "Aurelvoin","Amandrelle","Arsélienn","Aubrenoiré","Aldévant","Arclavaux","Avarniel","Aubryvantel","Ardévaux","Alaivertin",
    "Aurelmont","Amandrois","Arsélavoine","Aubrenvalle","Aldévoine","Arclavienn","Avarmontel",

    # B (57)
    "Bastienn","Beauremont","Bravien","Bellerand","Bastavoix","Brennoir","Baldéric","Briavoine","Beaureval","Brandelin",
    "Bastelmarc","Brenvalois","Belleric","Bravern","Beaurevant","Bastelvoix","Brennois","Baldérand","Briavert","Brandelmont",
    "Bastelvain","Brenvalier","Bellerandé","Bravernois","Beaurevoix","Bastelvainel","Brennoire","Baldéricel","Briavoix","Brandelvois",
    "Bastelrois","Brenvalmont","Bellerain","Bravernaux","Beaurevaux","Bastelroin","Brennoiré","Baldérien","Briavaux","Brandelvain",
    "Bastelmont","Brenvalin","Bellerainel","Bravernoix","Beaurevoine","Bastelvaux","Brennoiraux","Baldérin","Briavern","Brandelrois",
    "Bastelvoine","Brenvalierin","Bellerandaux","Braverniel","Beauremontel","Bastelvainnoir","Brenvalvois",

    # C (57)
    "Célavert","Clérian","Corvaux","Cendrémon","Cavernois","Clévoine","Corlavier","Cendréval","Caverniel","Clérianne",
    "Corvoix","Cendrévain","Cavermont","Clérianaux","Corlavoix","Cendrérois","Cavernaux","Clérianvois","Corlavierin","Cendrévaux",
    "Cavernier","Clérianval","Corvoine","Cendrélin","Cavernauxel","Clérianvert","Corlavoine","Cendréroin","Cavernval","Clérianmont",
    "Corvauxel","Cendrévainel","Cavernvois","Clérianrois","Corlavieraux","Cendrévauxel","Cavernierin","Clérianvertin","Corvoin","Cendrélinel",
    "Cavernmont","Clérianvaux","Corlavoixel","Cendréroisel","Cavernrois","Clérianvoine","Corlaviernoir","Cendrévauxin","Cavernvalin","Clérianmontel",
    "Corvoisel","Cendrévainnoir","Cavernvoine","Clérianroisel","Corlaviermont","Cendrévauxnoir","Caverniernois",

    # D (57)
    "Damiervain","Delaurent","Drevaux","Dorianne","Delairemont","Drevainel","Damiervaux","Delauric","Drevainnoir","Dorianvois",
    "Delauriel","Drevauxin","Damiervant","Delaurmont","Drevainaux","Dorianvert","Delaurvois","Drevainrois","Damiervauxel","Delaurain",
    "Drevainvert","Dorianval","Delaurainel","Drevainmont","Damiervainel","Delaurvoine","Drevainvaux","Dorianrois","Delaurainnoir","Drevainvertin",
    "Damiervauxnoir","Delaurmontel","Drevainroisel","Dorianvaux","Delaurvoisel","Drevainmontel","Damiervainnoir","Delaurainaux","Drevainvauxel","Dorianvoine",
    "Delaurmontaux","Drevainroisnoir","Damiervauxin","Delaurvoisaux","Drevainmontaux","Dorianroisel","Delaurainvert","Drevainvauxnoir","Damiervainaux","Delaurmontnoir",
    "Drevainroisvert","Dorianvauxel","Delaurvoin","Drevainmontnoir","Damiervauxvert","Delaurainvois","Drevainvauxin",

    # E (57)
    "Évarmont","Éloyric","Édravoix","Émervain","Élancourt","Édravaux","Évarnois","Éloyrand","Édravert","Émervaux",
    "Élancrois","Édravoine","Évarmontel","Éloyrin","Édravauxel","Émervainel","Élancroisel","Édravertin","Évarnoisel","Éloyrandaux",
    "Édravauxnoir","Émervauxin","Élancourtin","Édravertaux","Évarmontaux","Éloyrandel","Édravoisin","Émervainnoir","Élancroisvert","Édravauxin",
    "Évarnoisvert","Éloyrandnoir","Édravertnoir","Émervauxnoir","Élancourtaux","Édravoisvert","Évarmontnoir","Éloyrandin","Édravauxvert","Émervainaux",
    "Élancroisnoir","Édravertinnoir","Évarnoisaux","Éloyrandvert","Édravoisnoir","Émervauxvert","Élancourtnoir","Édravauxmont","Évarmontvert","Éloyrandmont",
    "Édravertmont","Émervainvert","Élancroismont","Édravoismont","Évarnoismont","Éloyrandvois","Édravauxmontel",

    # F (57)
    "Félorien","Fauvermont","Fravain","Fendrel","Fauveraux","Fravert","Félorienn","Fauvernois","Fravaux","Fendrois",
    "Fauverain","Fravainel","Félorvois","Fauvermontel","Fravauxin","Fendrelaux","Fauverainel","Fravertin","Félorain","Fauvernoisel",
    "Fravauxnoir","Fendroisel","Fauverainnoir","Fravertaux","Félorvoine","Fauvermontaux","Fravauxvert","Fendrelnoir","Fauvernoisvert","Fravertnoir",
    "Félorainel","Fauvermontnoir","Fravauxmont","Fendroisvert","Fauverainaux","Fravertmont","Félorvoisel","Fauvernoisaux","Fravauxmontel","Fendrelmont",
    "Fauvermontvert","Fravertinnoir","Félorainnoir","Fauverainvert","Fravauxnoisel","Fendroismont","Fauvernoismont","Fravertmontel","Félorvoismont","Fauvermontin",
    "Fravauxinnoir","Fendrelvois","Fauverainmont","Fravertvois","Félorainvert","Fauvernoisnoir","Fravauxvois",

    # G (57)
    "Gérauvois","Gavernin","Gréval","Gendrois","Gavermont","Grévoix","Gérauvain","Gavernaux","Grévalin","Gendrel",
    "Gavernoisel","Grévoine","Gérauvoine","Gavermontel","Grévalnoir","Gendroisel","Gavernauxel","Grévoixnoir","Gérauvaux","Gaverninnoir",
    "Grévalvert","Gendrelaux","Gavermontaux","Grévoixvert","Gérauvainel","Gavernoismont","Grévalmont","Gendroisvert","Gavernauxnoir","Grévoinmont",
    "Gérauvauxel","Gaverninaux","Grévalmontel","Gendrelnoir","Gavermontnoir","Grévoixmont","Gérauvainnoir","Gavernoismontel","Grévalinnoir","Gendroismont",
    "Gavernauxvert","Grévoinnoir","Gérauvauxnoir","Gaverninmont","Grévalvois","Gendrelmont","Gavermontvert","Grévoixin","Gérauvainmont","Gavernoismontaux",
    "Grévalmontnoir","Gendroisnoir","Gavernauxmont","Grévoixvois","Gérauvauxmont","Gaverninvois","Grévalvoisel",

    # H (57)
    "Hervaint","Havernois","Hélavoix","Hendrel","Havermont","Hélavert","Hervainel","Havernaux","Hélavoine","Hendrois",
    "Havernoisel","Hélavaux","Hervaintin","Havermontel","Hélavoisel","Hendrelaux","Havernauxel","Hélavertin","Hervainnoir","Havernin",
    "Hélavauxnoir","Hendroisel","Havermontaux","Hélavoixnoir","Hervainvert","Haverninnoir","Hélavertaux","Hendrelnoir","Havernoismont","Hélavoinevert",
    "Hervainmont","Havernauxnoir","Hélavauxvert","Hendroisvert","Havermontnoir","Hélavoixmont","Hervainvois","Haverninaux","Hélavertnoir","Hendrelmont",
    "Havernoismontel","Hélavoinein","Hervainaux","Havernauxvert","Hélavauxin","Hendroismont","Havermontvert","Hélavoixin","Hervainmontel","Haverninmont",
    "Hélavertmont","Hendrelvois","Havernoismontaux","Hélavoinevois","Hervainvoisel","Havernauxmont","Hélavauxmont",

    # I (57)
    "Isambrois","Ivainel","Irévoix","Indrel","Ivairmont","Irévaux","Isambroin","Ivainaux","Irévoine","Indrois",
    "Ivairnoisel","Irévauxel","Isambroisnoir","Ivainnoir","Irévoixnoir","Indrelaux","Ivairmontel","Irévauxnoir","Isambroinnoir","Ivainvert",
    "Irévoin","Indroisel","Ivairnoisvert","Irévauxvert","Isambroisvert","Ivainmont","Irévoixvert","Indrelnoir","Ivairmontaux","Irévoinnoir",
    "Isambroinaux","Ivainvaux","Irévauxmont","Indroisvert","Ivairnoisaux","Irévoixmont","Isambroisaux","Ivainmontel","Irévauxin","Indrelmont",
    "Ivairmontnoir","Irévoinmont","Isambroinmont","Ivainvois","Irévauxmontel","Indroismont","Ivairnoismont","Irévoixin","Isambroisvois","Ivainvauxel",
    "Irévauxvois","Indrelvois","Ivairmontvert","Irévoinvois","Isambroisvertin","Ivainmontaux","Irévauxmontnoir",

    # J (57)
    "Javernois","Jéravain","Jolvoix","Jendrel","Javermont","Jolvert","Javernaux","Jéravaux","Jolvoine","Jendrois",
    "Javernoisel","Jolvoisel","Jéravainel","Javermontel","Jolvaux","Jendrelaux","Javernauxel","Jolvertin","Jéravainnoir","Javernin",
    "Jolvauxnoir","Jendroisel","Javermontaux","Jolvoixnoir","Jéravainvert","Javerninnoir","Jolvertaux","Jendrelnoir","Javernoismont","Jolvoinevert",
    "Jéravainmont","Javernauxnoir","Jolvauxvert","Jendroisvert","Javermontnoir","Jolvoixmont","Jéravainvois","Javerninaux","Jolvertnoir","Jendrelmont",
    "Javernoismontel","Jolvoinein","Jéravainaux","Javernauxvert","Jolvauxin","Jendroismont","Javermontvert","Jolvoixin","Jéravainmontel","Javerninmont",
    "Jolvertmont","Jendrelvois","Javernoismontaux","Jolvoinevois","Jéravainvoisel","Javernauxmont","Jolvauxmont",

    # K (57)
    "Kervaint","Kavernois","Kélavoix","Kendrel","Kavermont","Kélavert","Kervainel","Kavernaux","Kélavoine","Kendrois",
    "Kavernoisel","Kélavaux","Kervaintin","Kavermontel","Kélavoisel","Kendrelaux","Kavernauxel","Kélavertin","Kervainnoir","Kavernin",
    "Kélavauxnoir","Kendroisel","Kavermontaux","Kélavoixnoir","Kervainvert","Kaverninnoir","Kélavertaux","Kendrelnoir","Kavernoismont","Kélavoinevert",
    "Kervainmont","Kavernauxnoir","Kélavauxvert","Kendroisvert","Kavermontnoir","Kélavoixmont","Kervainvois","Kaverninaux","Kélavertnoir","Kendrelmont",
    "Kavernoismontel","Kélavoinein","Kervainaux","Kavernauxvert","Kélavauxin","Kendroismont","Kavermontvert","Kélavoixin","Kervainmontel","Kaverninmont",
    "Kélavertmont","Kendrelvois","Kavernoismontaux","Kélavoinevois","Kervainvoisel","Kavernauxmont","Kélavauxmont",

    # L (57)
    "Lévairmont","Lavernoix","Lorianne","Lendrois","Lavermont","Loravert","Lévainel","Lavernaux","Lorianvois","Lendrel",
    "Lavernoisel","Loravaux","Lévainnoir","Lavermontel","Lorianvert","Lendroisel","Lavernauxel","Loravertin","Lévainmont","Lavernin",
    "Lorianvaux","Lendrelaux","Lavermontaux","Loravoix","Lévainvert","Laverninnoir","Lorianmont","Lendroisvert","Lavernoismont","Loravoine",
    "Lévainvois","Lavernauxnoir","Loriannoir","Lendrelnoir","Lavermontnoir","Loravoixnoir","Lévainmontel","Laverninaux","Lorianvauxel","Lendroismont",
    "Lavernoismontel","Loravoinevert","Lévainaux","Lavernauxvert","Lorianin","Lendrelmont", "Quendrel","Quervaux","Quillavois","Quendrois","Quervain","Quillavert","Quendrelaux","Quervauxel","Quillavoine","Quendroisel",
    "Quervainel","Quillavaux","Quendrelnoir","Quervainnoir","Quillavoisel","Quendroisvert","Quervauxnoir","Quillavertin","Quendrelmont","Quervainmont",
    "Quillavoix","Quendroismont","Quervauxvert","Quillavauxnoir","Quendrelvois","Quervainaux","Quillavoinevert","Quendroisnoir","Quervauxmont","Quillavertnoir",
    "Quendrelvert","Quervainvois","Quillavoixin","Quendroismontel","Quervauxin","Quillavauxvert","Quendrelauxin","Quervainmontel","Quillavoinein","Quendroisaux",
    "Quervauxmontel","Quillavertmont","Quendrelmontel","Quervainvert","Quillavoisnoir","Quendroisvertin","Quervauxvois","Quillavauxmont","Quendrelvoisel","Quervainnoisel",
    "Quillavoinevois","Quendroisvois","Quervauxmontnoir","Quillavertaux","Quendrelmontnoir","Quervainvaux","Quillavoismont",

    # R (57)
    "Ravernois","Rélavoix","Rendrel","Ravermont","Rélavert","Ravernaux","Rélavoine","Rendrois","Ravernin","Rélavaux",
    "Ravermontel","Rélavoisel","Rendrelaux","Ravernauxel","Rélavertin","Rendroisel","Raverninnoir","Rélavauxnoir","Rendrelnoir","Ravernoismont",
    "Rélavoinevert","Rendroisvert","Ravermontnoir","Rélavoixnoir","Rendrelmont","Ravernauxnoir","Rélavauxvert","Rendroismont","Ravernoismontel","Rélavoinein",
    "Rendrelvois","Ravernauxvert","Rélavauxin","Rendroisnoir","Ravermontvert","Rélavoixin","Rendrelmontel","Raverninaux","Rélavertnoir","Rendroismontel",
    "Ravernoismontaux","Rélavoinevois","Rendrelauxin","Ravernauxmont","Rélavauxmont","Rendroisvertin","Ravermontin","Rélavoismont","Rendrelvaux","Raverninmont",
    "Rélavertmont","Rendroisvois","Ravernoismontnoir","Rélavoixvert","Rendrelvauxel","Ravernauxvois","Rélavauxvois",

    # S (57)
    "Savernois","Sélavoix","Sendrel","Savermont","Sélavert","Savernaux","Sélavoine","Sendrois","Savernin","Sélavaux",
    "Savermontel","Sélavoisel","Sendrelaux","Savernauxel","Sélavertin","Sendroisel","Saverninnoir","Sélavauxnoir","Sendrelnoir","Savernoismont",
    "Sélavoinevert","Sendroisvert","Savermontnoir","Sélavoixnoir","Sendrelmont","Savernauxnoir","Sélavauxvert","Sendroismont","Savernoismontel","Sélavoinein",
    "Sendrelvois","Savernauxvert","Sélavauxin","Sendroisnoir","Savermontvert","Sélavoixin","Sendrelmontel","Saverninaux","Sélavertnoir","Sendroismontel",
    "Savernoismontaux","Sélavoinevois","Sendrelauxin","Savernauxmont","Sélavauxmont","Sendroisvertin","Savermontin","Sélavoismont","Sendrelvaux","Saverninmont",
    "Sélavertmont","Sendroisvois","Savernoismontnoir","Sélavoixvert","Sendrelvauxel","Savernauxvois","Sélavauxvois",

    # T (57)
    "Tavernois","Télavoix","Tendrel","Tavermont","Télavert","Tavernaux","Télavoine","Tendrois","Tavernin","Télavaux",
    "Tavermontel","Télavoisel","Tendrelaux","Tavernauxel","Télavertin","Tendroisel","Taverninnoir","Télavauxnoir","Tendrelnoir","Tavernoismont",
    "Télavoinevert","Tendroisvert","Tavermontnoir","Télavoixnoir","Tendrelmont","Tavernauxnoir","Télavauxvert","Tendroismont","Tavernoismontel","Télavoinein",
    "Tendrelvois","Tavernauxvert","Télavauxin","Tendroisnoir","Tavermontvert","Télavoixin","Tendrelmontel","Taverninaux","Télavertnoir","Tendroismontel",
    "Tavernoismontaux","Télavoinevois","Tendrelauxin","Tavernauxmont","Télavauxmont","Tendroisvertin","Tavermontin","Télavoismont","Tendrelvaux","Taverninmont",
    "Télavertmont","Tendroisvois","Tavernoismontnoir","Télavoixvert","Tendrelvauxel","Tavernauxvois","Télavauxvois",

    # U (57)
    "Uvermont","Ulavoix","Undrel","Uvernais","Ulavert","Uverneaux","Ulavoine","Undrois","Uvernin","Ulavaux",
    "Uvermontel","Ulavoisel","Undrelaux","Uverneauxel","Ulavertin","Undroisel","Uverninnoir","Ulavauxnoir","Undrelnoir","Uvernoismont",
    "Ulavoinevert","Undroisvert","Uvermontnoir","Ulavoixnoir","Undrelmont","Uverneauxnoir","Ulavauxvert","Undroismont","Uvernoismontel","Ulavoinein",
    "Undrelvois","Uverneauxvert","Ulavauxin","Undroisnoir","Uvermontvert","Ulavoixin","Undrelmontel","Uverninaux","Ulavertnoir","Undroismontel",
    "Uvernoismontaux","Ulavoinevois","Undrelauxin","Uverneauxmont","Ulavauxmont","Undroisvertin","Uvermontin","Ulavoismont","Undrelvaux","Uverninmont",
    "Ulavertmont","Undroisvois","Uvernoismontnoir","Ulavoixvert","Undrelvauxel","Uverneauxvois","Ulavauxvois",

    # V (57)
    "Vavernois","Vélavoix","Vendrel","Vavermont","Vélavert","Vavernaux","Vélavoine","Vandrois","Vavernin","Vélavaux",
    "Vavermontel","Vélavoisel","Vendrelaux","Vavernauxel","Vélavertin","Vandroisel","Vaverninnoir","Vélavauxnoir","Vendrelnoir","Vavernoismont",
    "Vélavoinevert","Vandroisvert","Vavermontnoir","Vélavoixnoir","Vendrelmont","Vavernauxnoir","Vélavauxvert","Vandroismont","Vavernoismontel","Vélavoinein",
    "Vendrelvois","Vavernauxvert","Vélavauxin","Vandroisnoir","Vavermontvert","Vélavoixin","Vendrelmontel","Vaverninaux","Vélavertnoir","Vandroismontel",
    "Vavernoismontaux","Vélavoinevois","Vendrelauxin","Vavernauxmont","Vélavauxmont","Vandroisvertin","Vavermontin","Vélavoismont","Vendrelvaux","Vaverninmont",
    "Vélavertmont","Vandroisvois","Vavernoismontnoir","Vélavoixvert","Vendrelvauxel","Vavernauxvois","Vélavauxvois",

    # W (57)
    "Wavernois","Wélavoix","Wendrel","Wavermont","Wélavert","Wavernaux","Wélavoine","Wendrois","Wavernin","Wélavaux",
    "Wavermontel","Wélavoisel","Wendrelaux","Wavernauxel","Wélavertin","Wendroisel","Waverninnoir","Wélavauxnoir","Wendrelnoir","Wavernoismont",
    "Wélavoinevert","Wendroisvert","Wavermontnoir","Wélavoixnoir","Wendrelmont","Wavernauxnoir","Wélavauxvert","Wendroismont","Wavernoismontel","Wélavoinein",
    "Wendrelvois","Wavernauxvert","Wélavauxin","Wendroisnoir","Wavermontvert","Wélavoixin","Wendrelmontel","Waverninaux","Wélavertnoir","Wendroismontel",
    "Wavernoismontaux","Wélavoinevois","Wendrelauxin","Wavernauxmont","Wélavauxmont","Wendroisvertin","Wavermontin","Wélavoismont","Wendrelvaux","Waverninmont",
    "Wélavertmont","Wendroisvois","Wavernoismontnoir","Wélavoixvert","Wendrelvauxel","Wavernauxvois","Wélavauxvois",

    # X (57)
    "Xavernois","Xélavoix","Xendrel","Xavermont","Xélavert","Xavernaux","Xélavoine","Xendrois","Xavernin","Xélavaux",
    "Xavermontel","Xélavoisel","Xendrelaux","Xavernauxel","Xélavertin","Xendroisel","Xaverninnoir","Xélavauxnoir","Xendrelnoir","Xavernoismont",
    "Xélavoinevert","Xendroisvert","Xavermontnoir","Xélavoixnoir","Xendrelmont","Xavernauxnoir","Xélavauxvert","Xendroismont","Xavernoismontel","Xélavoinein",
    "Xendrelvois","Xavernauxvert","Xélavauxin","Xendroisnoir","Xavermontvert","Xélavoixin","Xendrelmontel","Xaverninaux","Xélavertnoir","Xendroismontel",
    "Xavernoismontaux","Xélavoinevois","Xendrelauxin","Xavernauxmont","Xélavauxmont","Xendroisvertin","Xavermontin","Xélavoismont","Xendrelvaux","Xaverninmont",
    "Xélavertmont","Xendroisvois","Xavernoismontnoir","Xélavoixvert","Xendrelvauxel","Xavernauxvois","Xélavauxvois",

    # Y (57)
    "Yavernois","Yélavoix","Yendrel","Yavermont","Yélavert","Yavernaux","Yélavoine","Yendrois","Yavernin","Yélavaux",
    "Yavermontel","Yélavoisel","Yendrelaux","Yavernauxel","Yélavertin","Yendroisel","Yaverninnoir","Yélavauxnoir","Yendrelnoir","Yavernoismont",
    "Yélavoinevert","Yendroisvert","Yavermontnoir","Yélavoixnoir","Yendrelmont","Yavernauxnoir","Yélavauxvert","Yendroismont","Yavernoismontel","Yélavoinein",
    "Yendrelvois","Yavernauxvert","Yélavauxin","Yendroisnoir","Yavermontvert","Yélavoixin","Yendrelmontel","Yaverninaux","Yélavertnoir","Yendroismontel",
    "Yavernoismontaux","Yélavoinevois","Yendrelauxin","Yavernauxmont","Yélavauxmont","Yendroisvertin","Yavermontin","Yélavoismont","Yendrelvaux","Yaverninmont",
    "Yélavertmont","Yendroisvois","Yavernoismontnoir","Yélavoixvert","Yendrelvauxel","Yavernauxvois","Yélavauxvois",

    # Z (57)
    "Zavernois","Zélavoix","Zendrel","Zavermont","Zélavert","Zavernaux","Zélavoine","Zendrois","Zavernin","Zélavaux",
    "Zavermontel","Zélavoisel","Zendrelaux","Zavernauxel","Zélavertin","Zendroisel","Zaverninnoir","Zélavauxnoir","Zendrelnoir","Zavernoismont",
    "Zélavoinevert","Zendroisvert","Zavermontnoir","Zélavoixnoir","Zendrelmont","Zavernauxnoir","Zélavauxvert","Zendroismont","Zavernoismontel","Zélavoinein",
    "Zendrelvois","Zavernauxvert","Zélavauxin","Zendroisnoir","Zavermontvert","Zélavoixin","Zendrelmontel","Zaverninaux","Zélavertnoir","Zendroismontel",
    "Zavernoismontaux","Zélavoinevois","Zendrelauxin","Zavernauxmont","Zélavauxmont","Zendroisvertin","Zavermontin","Zélavoismont","Zendrelvaux","Zaverninmont",
    "Zélavertmont","Zendroisvois","Zavernoismontnoir","Zélavoixvert","Zendrelvauxel","Zavernauxvois","Zélavauxvois"]
massieu_names1 = [
    # A (57)
    "Aurelienn","Avariste","Aldémar","Arsavoix","Aubrennel","Amandric","Avermont","Alaireau","Ardévant","Aubryel",
    "Aurelvois","Amandrel","Arclavien","Aubrenoir","Aldévoix","Arsélian","Avarmont","Aubrelien","Ardennaux","Alaivert",
    "Aurelmarc","Amandier","Arsavoine","Aubrenard","Aldémont","Arclavier","Avariel","Aubryvant","Ardémar","Alaivaux",
    "Aurelvoine","Amandricel","Arsélavoix","Aubrenval","Aldérian","Arclavert","Avarnois","Aubrelmont","Ardévain","Alaivern",
    "Aurelvoin","Amandrelle","Arsélienn","Aubrenoiré","Aldévant","Arclavaux","Avarniel","Aubryvantel","Ardévaux","Alaivertin",
    "Aurelmont","Amandrois","Arsélavoine","Aubrenvalle","Aldévoine","Arclavienn","Avarmontel",

    # B (57)
    "Bastienn","Beauremont","Bravien","Bellerand","Bastavoix","Brennoir","Baldéric","Briavoine","Beaureval","Brandelin",
    "Bastelmarc","Brenvalois","Belleric","Bravern","Beaurevant","Bastelvoix","Brennois","Baldérand","Briavert","Brandelmont",
    "Bastelvain","Brenvalier","Bellerandé","Bravernois","Beaurevoix","Bastelvainel","Brennoire","Baldéricel","Briavoix","Brandelvois",
    "Bastelrois","Brenvalmont","Bellerain","Bravernaux","Beaurevaux","Bastelroin","Brennoiré","Baldérien","Briavaux","Brandelvain",
    "Bastelmont","Brenvalin","Bellerainel","Bravernoix","Beaurevoine","Bastelvaux","Brennoiraux","Baldérin","Briavern","Brandelrois",
    "Bastelvoine","Brenvalierin","Bellerandaux","Braverniel","Beauremontel","Bastelvainnoir","Brenvalvois",

    # C (57)
    "Célavert","Clérian","Corvaux","Cendrémon","Cavernois","Clévoine","Corlavier","Cendréval","Caverniel","Clérianne",
    "Corvoix","Cendrévain","Cavermont","Clérianaux","Corlavoix","Cendrérois","Cavernaux","Clérianvois","Corlavierin","Cendrévaux",
    "Cavernier","Clérianval","Corvoine","Cendrélin","Cavernauxel","Clérianvert","Corlavoine","Cendréroin","Cavernval","Clérianmont",
    "Corvauxel","Cendrévainel","Cavernvois","Clérianrois","Corlavieraux","Cendrévauxel","Cavernierin","Clérianvertin","Corvoin","Cendrélinel",
    "Cavernmont","Clérianvaux","Corlavoixel","Cendréroisel","Cavernrois","Clérianvoine","Corlaviernoir","Cendrévauxin","Cavernvalin","Clérianmontel",
    "Corvoisel","Cendrévainnoir","Cavernvoine","Clérianroisel","Corlaviermont","Cendrévauxnoir","Caverniernois",

    # D (57)
    "Damiervain","Delaurent","Drevaux","Dorianne","Delairemont","Drevainel","Damiervaux","Delauric","Drevainnoir","Dorianvois",
    "Delauriel","Drevauxin","Damiervant","Delaurmont","Drevainaux","Dorianvert","Delaurvois","Drevainrois","Damiervauxel","Delaurain",
    "Drevainvert","Dorianval","Delaurainel","Drevainmont","Damiervainel","Delaurvoine","Drevainvaux","Dorianrois","Delaurainnoir","Drevainvertin",
    "Damiervauxnoir","Delaurmontel","Drevainroisel","Dorianvaux","Delaurvoisel","Drevainmontel","Damiervainnoir","Delaurainaux","Drevainvauxel","Dorianvoine",
    "Delaurmontaux","Drevainroisnoir","Damiervauxin","Delaurvoisaux","Drevainmontaux","Dorianroisel","Delaurainvert","Drevainvauxnoir","Damiervainaux","Delaurmontnoir",
    "Drevainroisvert","Dorianvauxel","Delaurvoin","Drevainmontnoir","Damiervauxvert","Delaurainvois","Drevainvauxin",

    # E (57)
    "Évarmont","Éloyric","Édravoix","Émervain","Élancourt","Édravaux","Évarnois","Éloyrand","Édravert","Émervaux",
    "Élancrois","Édravoine","Évarmontel","Éloyrin","Édravauxel","Émervainel","Élancroisel","Édravertin","Évarnoisel","Éloyrandaux",
    "Édravauxnoir","Émervauxin","Élancourtin","Édravertaux","Évarmontaux","Éloyrandel","Édravoisin","Émervainnoir","Élancroisvert","Édravauxin",
    "Évarnoisvert","Éloyrandnoir","Édravertnoir","Émervauxnoir","Élancourtaux","Édravoisvert","Évarmontnoir","Éloyrandin","Édravauxvert","Émervainaux",
    "Élancroisnoir","Édravertinnoir","Évarnoisaux","Éloyrandvert","Édravoisnoir","Émervauxvert","Élancourtnoir","Édravauxmont","Évarmontvert","Éloyrandmont",
    "Édravertmont","Émervainvert","Élancroismont","Édravoismont","Évarnoismont","Éloyrandvois","Édravauxmontel",

    # F (57)
    "Félorien","Fauvermont","Fravain","Fendrel","Fauveraux","Fravert","Félorienn","Fauvernois","Fravaux","Fendrois",
    "Fauverain","Fravainel","Félorvois","Fauvermontel","Fravauxin","Fendrelaux","Fauverainel","Fravertin","Félorain","Fauvernoisel",
    "Fravauxnoir","Fendroisel","Fauverainnoir","Fravertaux","Félorvoine","Fauvermontaux","Fravauxvert","Fendrelnoir","Fauvernoisvert","Fravertnoir",
    "Félorainel","Fauvermontnoir","Fravauxmont","Fendroisvert","Fauverainaux","Fravertmont","Félorvoisel","Fauvernoisaux","Fravauxmontel","Fendrelmont",
    "Fauvermontvert","Fravertinnoir","Félorainnoir","Fauverainvert","Fravauxnoisel","Fendroismont","Fauvernoismont","Fravertmontel","Félorvoismont","Fauvermontin",
    "Fravauxinnoir","Fendrelvois","Fauverainmont","Fravertvois","Félorainvert","Fauvernoisnoir","Fravauxvois",

    # G (57)
    "Gérauvois","Gavernin","Gréval","Gendrois","Gavermont","Grévoix","Gérauvain","Gavernaux","Grévalin","Gendrel",
    "Gavernoisel","Grévoine","Gérauvoine","Gavermontel","Grévalnoir","Gendroisel","Gavernauxel","Grévoixnoir","Gérauvaux","Gaverninnoir",
    "Grévalvert","Gendrelaux","Gavermontaux","Grévoixvert","Gérauvainel","Gavernoismont","Grévalmont","Gendroisvert","Gavernauxnoir","Grévoinmont",
    "Gérauvauxel","Gaverninaux","Grévalmontel","Gendrelnoir","Gavermontnoir","Grévoixmont","Gérauvainnoir","Gavernoismontel","Grévalinnoir","Gendroismont",
    "Gavernauxvert","Grévoinnoir","Gérauvauxnoir","Gaverninmont","Grévalvois","Gendrelmont","Gavermontvert","Grévoixin","Gérauvainmont","Gavernoismontaux",
    "Grévalmontnoir","Gendroisnoir","Gavernauxmont","Grévoixvois","Gérauvauxmont","Gaverninvois","Grévalvoisel",

    # H (57)
    "Hervaint","Havernois","Hélavoix","Hendrel","Havermont","Hélavert","Hervainel","Havernaux","Hélavoine","Hendrois",
    "Havernoisel","Hélavaux","Hervaintin","Havermontel","Hélavoisel","Hendrelaux","Havernauxel","Hélavertin","Hervainnoir","Havernin",
    "Hélavauxnoir","Hendroisel","Havermontaux","Hélavoixnoir","Hervainvert","Haverninnoir","Hélavertaux","Hendrelnoir","Havernoismont","Hélavoinevert",
    "Hervainmont","Havernauxnoir","Hélavauxvert","Hendroisvert","Havermontnoir","Hélavoixmont","Hervainvois","Haverninaux","Hélavertnoir","Hendrelmont",
    "Havernoismontel","Hélavoinein","Hervainaux","Havernauxvert","Hélavauxin","Hendroismont","Havermontvert","Hélavoixin","Hervainmontel","Haverninmont",
    "Hélavertmont","Hendrelvois","Havernoismontaux","Hélavoinevois","Hervainvoisel","Havernauxmont","Hélavauxmont",

    # I (57)
    "Isambrois","Ivainel","Irévoix","Indrel","Ivairmont","Irévaux","Isambroin","Ivainaux","Irévoine","Indrois",
    "Ivairnoisel","Irévauxel","Isambroisnoir","Ivainnoir","Irévoixnoir","Indrelaux","Ivairmontel","Irévauxnoir","Isambroinnoir","Ivainvert",
    "Irévoin","Indroisel","Ivairnoisvert","Irévauxvert","Isambroisvert","Ivainmont","Irévoixvert","Indrelnoir","Ivairmontaux","Irévoinnoir",
    "Isambroinaux","Ivainvaux","Irévauxmont","Indroisvert","Ivairnoisaux","Irévoixmont","Isambroisaux","Ivainmontel","Irévauxin","Indrelmont",
    "Ivairmontnoir","Irévoinmont","Isambroinmont","Ivainvois","Irévauxmontel","Indroismont","Ivairnoismont","Irévoixin","Isambroisvois","Ivainvauxel",
    "Irévauxvois","Indrelvois","Ivairmontvert","Irévoinvois","Isambroisvertin","Ivainmontaux","Irévauxmontnoir",

    # J (57)
    "Javernois","Jéravain","Jolvoix","Jendrel","Javermont","Jolvert","Javernaux","Jéravaux","Jolvoine","Jendrois",
    "Javernoisel","Jolvoisel","Jéravainel","Javermontel","Jolvaux","Jendrelaux","Javernauxel","Jolvertin","Jéravainnoir","Javernin",
    "Jolvauxnoir","Jendroisel","Javermontaux","Jolvoixnoir","Jéravainvert","Javerninnoir","Jolvertaux","Jendrelnoir","Javernoismont","Jolvoinevert",
    "Jéravainmont","Javernauxnoir","Jolvauxvert","Jendroisvert","Javermontnoir","Jolvoixmont","Jéravainvois","Javerninaux","Jolvertnoir","Jendrelmont",
    "Javernoismontel","Jolvoinein","Jéravainaux","Javernauxvert","Jolvauxin","Jendroismont","Javermontvert","Jolvoixin","Jéravainmontel","Javerninmont",
    "Jolvertmont","Jendrelvois","Javernoismontaux","Jolvoinevois","Jéravainvoisel","Javernauxmont","Jolvauxmont",

    # K (57)
    "Kervaint","Kavernois","Kélavoix","Kendrel","Kavermont","Kélavert","Kervainel","Kavernaux","Kélavoine","Kendrois",
    "Kavernoisel","Kélavaux","Kervaintin","Kavermontel","Kélavoisel","Kendrelaux","Kavernauxel","Kélavertin","Kervainnoir","Kavernin",
    "Kélavauxnoir","Kendroisel","Kavermontaux","Kélavoixnoir","Kervainvert","Kaverninnoir","Kélavertaux","Kendrelnoir","Kavernoismont","Kélavoinevert",
    "Kervainmont","Kavernauxnoir","Kélavauxvert","Kendroisvert","Kavermontnoir","Kélavoixmont","Kervainvois","Kaverninaux","Kélavertnoir","Kendrelmont",
    "Kavernoismontel","Kélavoinein","Kervainaux","Kavernauxvert","Kélavauxin","Kendroismont","Kavermontvert","Kélavoixin","Kervainmontel","Kaverninmont",
    "Kélavertmont","Kendrelvois","Kavernoismontaux","Kélavoinevois","Kervainvoisel","Kavernauxmont","Kélavauxmont",

    # L (57)
    "Lévairmont","Lavernoix","Lorianne","Lendrois","Lavermont","Loravert","Lévainel","Lavernaux","Lorianvois","Lendrel",
    "Lavernoisel","Loravaux","Lévainnoir","Lavermontel","Lorianvert","Lendroisel","Lavernauxel","Loravertin","Lévainmont","Lavernin",
    "Lorianvaux","Lendrelaux","Lavermontaux","Loravoix","Lévainvert","Laverninnoir","Lorianmont","Lendroisvert","Lavernoismont","Loravoine",
    "Lévainvois","Lavernauxnoir","Loriannoir","Lendrelnoir","Lavermontnoir","Loravoixnoir","Lévainmontel","Laverninaux","Lorianvauxel","Lendroismont",
    "Lavernoismontel","Loravoinevert","Lévainaux","Lavernauxvert","Lorianin","Lendrelmont", "Quendrel","Quervaux","Quillavois","Quendrois","Quervain","Quillavert","Quendrelaux","Quervauxel","Quillavoine","Quendroisel",
    "Quervainel","Quillavaux","Quendrelnoir","Quervainnoir","Quillavoisel","Quendroisvert","Quervauxnoir","Quillavertin","Quendrelmont","Quervainmont",
    "Quillavoix","Quendroismont","Quervauxvert","Quillavauxnoir","Quendrelvois","Quervainaux","Quillavoinevert","Quendroisnoir","Quervauxmont","Quillavertnoir",
    "Quendrelvert","Quervainvois","Quillavoixin","Quendroismontel","Quervauxin","Quillavauxvert","Quendrelauxin","Quervainmontel","Quillavoinein","Quendroisaux",
    "Quervauxmontel","Quillavertmont","Quendrelmontel","Quervainvert","Quillavoisnoir","Quendroisvertin","Quervauxvois","Quillavauxmont","Quendrelvoisel","Quervainnoisel",
    "Quillavoinevois","Quendroisvois","Quervauxmontnoir","Quillavertaux","Quendrelmontnoir","Quervainvaux","Quillavoismont",

    # R (57)
    "Ravernois","Rélavoix","Rendrel","Ravermont","Rélavert","Ravernaux","Rélavoine","Rendrois","Ravernin","Rélavaux",
    "Ravermontel","Rélavoisel","Rendrelaux","Ravernauxel","Rélavertin","Rendroisel","Raverninnoir","Rélavauxnoir","Rendrelnoir","Ravernoismont",
    "Rélavoinevert","Rendroisvert","Ravermontnoir","Rélavoixnoir","Rendrelmont","Ravernauxnoir","Rélavauxvert","Rendroismont","Ravernoismontel","Rélavoinein",
    "Rendrelvois","Ravernauxvert","Rélavauxin","Rendroisnoir","Ravermontvert","Rélavoixin","Rendrelmontel","Raverninaux","Rélavertnoir","Rendroismontel",
    "Ravernoismontaux","Rélavoinevois","Rendrelauxin","Ravernauxmont","Rélavauxmont","Rendroisvertin","Ravermontin","Rélavoismont","Rendrelvaux","Raverninmont",
    "Rélavertmont","Rendroisvois","Ravernoismontnoir","Rélavoixvert","Rendrelvauxel","Ravernauxvois","Rélavauxvois",

    # S (57)
    "Savernois","Sélavoix","Sendrel","Savermont","Sélavert","Savernaux","Sélavoine","Sendrois","Savernin","Sélavaux",
    "Savermontel","Sélavoisel","Sendrelaux","Savernauxel","Sélavertin","Sendroisel","Saverninnoir","Sélavauxnoir","Sendrelnoir","Savernoismont",
    "Sélavoinevert","Sendroisvert","Savermontnoir","Sélavoixnoir","Sendrelmont","Savernauxnoir","Sélavauxvert","Sendroismont","Savernoismontel","Sélavoinein",
    "Sendrelvois","Savernauxvert","Sélavauxin","Sendroisnoir","Savermontvert","Sélavoixin","Sendrelmontel","Saverninaux","Sélavertnoir","Sendroismontel",
    "Savernoismontaux","Sélavoinevois","Sendrelauxin","Savernauxmont","Sélavauxmont","Sendroisvertin","Savermontin","Sélavoismont","Sendrelvaux","Saverninmont",
    "Sélavertmont","Sendroisvois","Savernoismontnoir","Sélavoixvert","Sendrelvauxel","Savernauxvois","Sélavauxvois",

    # T (57)
    "Tavernois","Télavoix","Tendrel","Tavermont","Télavert","Tavernaux","Télavoine","Tendrois","Tavernin","Télavaux",
    "Tavermontel","Télavoisel","Tendrelaux","Tavernauxel","Télavertin","Tendroisel","Taverninnoir","Télavauxnoir","Tendrelnoir","Tavernoismont",
    "Télavoinevert","Tendroisvert","Tavermontnoir","Télavoixnoir","Tendrelmont","Tavernauxnoir","Télavauxvert","Tendroismont","Tavernoismontel","Télavoinein",
    "Tendrelvois","Tavernauxvert","Télavauxin","Tendroisnoir","Tavermontvert","Télavoixin","Tendrelmontel","Taverninaux","Télavertnoir","Tendroismontel",
    "Tavernoismontaux","Télavoinevois","Tendrelauxin","Tavernauxmont","Télavauxmont","Tendroisvertin","Tavermontin","Télavoismont","Tendrelvaux","Taverninmont",
    "Télavertmont","Tendroisvois","Tavernoismontnoir","Télavoixvert","Tendrelvauxel","Tavernauxvois","Télavauxvois",

    # U (57)
    "Uvermont","Ulavoix","Undrel","Uvernais","Ulavert","Uverneaux","Ulavoine","Undrois","Uvernin","Ulavaux",
    "Uvermontel","Ulavoisel","Undrelaux","Uverneauxel","Ulavertin","Undroisel","Uverninnoir","Ulavauxnoir","Undrelnoir","Uvernoismont",
    "Ulavoinevert","Undroisvert","Uvermontnoir","Ulavoixnoir","Undrelmont","Uverneauxnoir","Ulavauxvert","Undroismont","Uvernoismontel","Ulavoinein",
    "Undrelvois","Uverneauxvert","Ulavauxin","Undroisnoir","Uvermontvert","Ulavoixin","Undrelmontel","Uverninaux","Ulavertnoir","Undroismontel",
    "Uvernoismontaux","Ulavoinevois","Undrelauxin","Uverneauxmont","Ulavauxmont","Undroisvertin","Uvermontin","Ulavoismont","Undrelvaux","Uverninmont",
    "Ulavertmont","Undroisvois","Uvernoismontnoir","Ulavoixvert","Undrelvauxel","Uverneauxvois","Ulavauxvois",

    # V (57)
    "Vavernois","Vélavoix","Vendrel","Vavermont","Vélavert","Vavernaux","Vélavoine","Vandrois","Vavernin","Vélavaux",
    "Vavermontel","Vélavoisel","Vendrelaux","Vavernauxel","Vélavertin","Vandroisel","Vaverninnoir","Vélavauxnoir","Vendrelnoir","Vavernoismont",
    "Vélavoinevert","Vandroisvert","Vavermontnoir","Vélavoixnoir","Vendrelmont","Vavernauxnoir","Vélavauxvert","Vandroismont","Vavernoismontel","Vélavoinein",
    "Vendrelvois","Vavernauxvert","Vélavauxin","Vandroisnoir","Vavermontvert","Vélavoixin","Vendrelmontel","Vaverninaux","Vélavertnoir","Vandroismontel",
    "Vavernoismontaux","Vélavoinevois","Vendrelauxin","Vavernauxmont","Vélavauxmont","Vandroisvertin","Vavermontin","Vélavoismont","Vendrelvaux","Vaverninmont",
    "Vélavertmont","Vandroisvois","Vavernoismontnoir","Vélavoixvert","Vendrelvauxel","Vavernauxvois","Vélavauxvois",

    # W (57)
    "Wavernois","Wélavoix","Wendrel","Wavermont","Wélavert","Wavernaux","Wélavoine","Wendrois","Wavernin","Wélavaux",
    "Wavermontel","Wélavoisel","Wendrelaux","Wavernauxel","Wélavertin","Wendroisel","Waverninnoir","Wélavauxnoir","Wendrelnoir","Wavernoismont",
    "Wélavoinevert","Wendroisvert","Wavermontnoir","Wélavoixnoir","Wendrelmont","Wavernauxnoir","Wélavauxvert","Wendroismont","Wavernoismontel","Wélavoinein",
    "Wendrelvois","Wavernauxvert","Wélavauxin","Wendroisnoir","Wavermontvert","Wélavoixin","Wendrelmontel","Waverninaux","Wélavertnoir","Wendroismontel",
    "Wavernoismontaux","Wélavoinevois","Wendrelauxin","Wavernauxmont","Wélavauxmont","Wendroisvertin","Wavermontin","Wélavoismont","Wendrelvaux","Waverninmont",
    "Wélavertmont","Wendroisvois","Wavernoismontnoir","Wélavoixvert","Wendrelvauxel","Wavernauxvois","Wélavauxvois",

    # X (57)
    "Xavernois","Xélavoix","Xendrel","Xavermont","Xélavert","Xavernaux","Xélavoine","Xendrois","Xavernin","Xélavaux",
    "Xavermontel","Xélavoisel","Xendrelaux","Xavernauxel","Xélavertin","Xendroisel","Xaverninnoir","Xélavauxnoir","Xendrelnoir","Xavernoismont",
    "Xélavoinevert","Xendroisvert","Xavermontnoir","Xélavoixnoir","Xendrelmont","Xavernauxnoir","Xélavauxvert","Xendroismont","Xavernoismontel","Xélavoinein",
    "Xendrelvois","Xavernauxvert","Xélavauxin","Xendroisnoir","Xavermontvert","Xélavoixin","Xendrelmontel","Xaverninaux","Xélavertnoir","Xendroismontel",
    "Xavernoismontaux","Xélavoinevois","Xendrelauxin","Xavernauxmont","Xélavauxmont","Xendroisvertin","Xavermontin","Xélavoismont","Xendrelvaux","Xaverninmont",
    "Xélavertmont","Xendroisvois","Xavernoismontnoir","Xélavoixvert","Xendrelvauxel","Xavernauxvois","Xélavauxvois",

    # Y (57)
    "Yavernois","Yélavoix","Yendrel","Yavermont","Yélavert","Yavernaux","Yélavoine","Yendrois","Yavernin","Yélavaux",
    "Yavermontel","Yélavoisel","Yendrelaux","Yavernauxel","Yélavertin","Yendroisel","Yaverninnoir","Yélavauxnoir","Yendrelnoir","Yavernoismont",
    "Yélavoinevert","Yendroisvert","Yavermontnoir","Yélavoixnoir","Yendrelmont","Yavernauxnoir","Yélavauxvert","Yendroismont","Yavernoismontel","Yélavoinein",
    "Yendrelvois","Yavernauxvert","Yélavauxin","Yendroisnoir","Yavermontvert","Yélavoixin","Yendrelmontel","Yaverninaux","Yélavertnoir","Yendroismontel",
    "Yavernoismontaux","Yélavoinevois","Yendrelauxin","Yavernauxmont","Yélavauxmont","Yendroisvertin","Yavermontin","Yélavoismont","Yendrelvaux","Yaverninmont",
    "Yélavertmont","Yendroisvois","Yavernoismontnoir","Yélavoixvert","Yendrelvauxel","Yavernauxvois","Yélavauxvois",

    # Z (57)
    "Zavernois","Zélavoix","Zendrel","Zavermont","Zélavert","Zavernaux","Zélavoine","Zendrois","Zavernin","Zélavaux",
    "Zavermontel","Zélavoisel","Zendrelaux","Zavernauxel","Zélavertin","Zendroisel","Zaverninnoir","Zélavauxnoir","Zendrelnoir","Zavernoismont",
    "Zélavoinevert","Zendroisvert","Zavermontnoir","Zélavoixnoir","Zendrelmont","Zavernauxnoir","Zélavauxvert","Zendroismont","Zavernoismontel","Zélavoinein",
    "Zendrelvois","Zavernauxvert","Zélavauxin","Zendroisnoir","Zavermontvert","Zélavoixin","Zendrelmontel","Zaverninaux","Zélavertnoir","Zendroismontel",
    "Zavernoismontaux","Zélavoinevois","Zendrelauxin","Zavernauxmont","Zélavauxmont","Zendroisvertin","Zavermontin","Zélavoismont","Zendrelvaux","Zaverninmont",
    "Zélavertmont","Zendroisvois","Zavernoismontnoir","Zélavoixvert","Zendrelvauxel","Zavernauxvois","Zélavauxvois"]
massieu_names2 = [
    # A (57)
    "Aurelienn","Avariste","Aldémar","Arsavoix","Aubrennel","Amandric","Avermont","Alaireau","Ardévant","Aubryel",
    "Aurelvois","Amandrel","Arclavien","Aubrenoir","Aldévoix","Arsélian","Avarmont","Aubrelien","Ardennaux","Alaivert",
    "Aurelmarc","Amandier","Arsavoine","Aubrenard","Aldémont","Arclavier","Avariel","Aubryvant","Ardémar","Alaivaux",
    "Aurelvoine","Amandricel","Arsélavoix","Aubrenval","Aldérian","Arclavert","Avarnois","Aubrelmont","Ardévain","Alaivern",
    "Aurelvoin","Amandrelle","Arsélienn","Aubrenoiré","Aldévant","Arclavaux","Avarniel","Aubryvantel","Ardévaux","Alaivertin",
    "Aurelmont","Amandrois","Arsélavoine","Aubrenvalle","Aldévoine","Arclavienn","Avarmontel",

    # B (57)
    "Bastienn","Beauremont","Bravien","Bellerand","Bastavoix","Brennoir","Baldéric","Briavoine","Beaureval","Brandelin",
    "Bastelmarc","Brenvalois","Belleric","Bravern","Beaurevant","Bastelvoix","Brennois","Baldérand","Briavert","Brandelmont",
    "Bastelvain","Brenvalier","Bellerandé","Bravernois","Beaurevoix","Bastelvainel","Brennoire","Baldéricel","Briavoix","Brandelvois",
    "Bastelrois","Brenvalmont","Bellerain","Bravernaux","Beaurevaux","Bastelroin","Brennoiré","Baldérien","Briavaux","Brandelvain",
    "Bastelmont","Brenvalin","Bellerainel","Bravernoix","Beaurevoine","Bastelvaux","Brennoiraux","Baldérin","Briavern","Brandelrois",
    "Bastelvoine","Brenvalierin","Bellerandaux","Braverniel","Beauremontel","Bastelvainnoir","Brenvalvois",

    # C (57)
    "Célavert","Clérian","Corvaux","Cendrémon","Cavernois","Clévoine","Corlavier","Cendréval","Caverniel","Clérianne",
    "Corvoix","Cendrévain","Cavermont","Clérianaux","Corlavoix","Cendrérois","Cavernaux","Clérianvois","Corlavierin","Cendrévaux",
    "Cavernier","Clérianval","Corvoine","Cendrélin","Cavernauxel","Clérianvert","Corlavoine","Cendréroin","Cavernval","Clérianmont",
    "Corvauxel","Cendrévainel","Cavernvois","Clérianrois","Corlavieraux","Cendrévauxel","Cavernierin","Clérianvertin","Corvoin","Cendrélinel",
    "Cavernmont","Clérianvaux","Corlavoixel","Cendréroisel","Cavernrois","Clérianvoine","Corlaviernoir","Cendrévauxin","Cavernvalin","Clérianmontel",
    "Corvoisel","Cendrévainnoir","Cavernvoine","Clérianroisel","Corlaviermont","Cendrévauxnoir","Caverniernois",

    # D (57)
    "Damiervain","Delaurent","Drevaux","Dorianne","Delairemont","Drevainel","Damiervaux","Delauric","Drevainnoir","Dorianvois",
    "Delauriel","Drevauxin","Damiervant","Delaurmont","Drevainaux","Dorianvert","Delaurvois","Drevainrois","Damiervauxel","Delaurain",
    "Drevainvert","Dorianval","Delaurainel","Drevainmont","Damiervainel","Delaurvoine","Drevainvaux","Dorianrois","Delaurainnoir","Drevainvertin",
    "Damiervauxnoir","Delaurmontel","Drevainroisel","Dorianvaux","Delaurvoisel","Drevainmontel","Damiervainnoir","Delaurainaux","Drevainvauxel","Dorianvoine",
    "Delaurmontaux","Drevainroisnoir","Damiervauxin","Delaurvoisaux","Drevainmontaux","Dorianroisel","Delaurainvert","Drevainvauxnoir","Damiervainaux","Delaurmontnoir",
    "Drevainroisvert","Dorianvauxel","Delaurvoin","Drevainmontnoir","Damiervauxvert","Delaurainvois","Drevainvauxin",

    # E (57)
    "Évarmont","Éloyric","Édravoix","Émervain","Élancourt","Édravaux","Évarnois","Éloyrand","Édravert","Émervaux",
    "Élancrois","Édravoine","Évarmontel","Éloyrin","Édravauxel","Émervainel","Élancroisel","Édravertin","Évarnoisel","Éloyrandaux",
    "Édravauxnoir","Émervauxin","Élancourtin","Édravertaux","Évarmontaux","Éloyrandel","Édravoisin","Émervainnoir","Élancroisvert","Édravauxin",
    "Évarnoisvert","Éloyrandnoir","Édravertnoir","Émervauxnoir","Élancourtaux","Édravoisvert","Évarmontnoir","Éloyrandin","Édravauxvert","Émervainaux",
    "Élancroisnoir","Édravertinnoir","Évarnoisaux","Éloyrandvert","Édravoisnoir","Émervauxvert","Élancourtnoir","Édravauxmont","Évarmontvert","Éloyrandmont",
    "Édravertmont","Émervainvert","Élancroismont","Édravoismont","Évarnoismont","Éloyrandvois","Édravauxmontel",

    # F (57)
    "Félorien","Fauvermont","Fravain","Fendrel","Fauveraux","Fravert","Félorienn","Fauvernois","Fravaux","Fendrois",
    "Fauverain","Fravainel","Félorvois","Fauvermontel","Fravauxin","Fendrelaux","Fauverainel","Fravertin","Félorain","Fauvernoisel",
    "Fravauxnoir","Fendroisel","Fauverainnoir","Fravertaux","Félorvoine","Fauvermontaux","Fravauxvert","Fendrelnoir","Fauvernoisvert","Fravertnoir",
    "Félorainel","Fauvermontnoir","Fravauxmont","Fendroisvert","Fauverainaux","Fravertmont","Félorvoisel","Fauvernoisaux","Fravauxmontel","Fendrelmont",
    "Fauvermontvert","Fravertinnoir","Félorainnoir","Fauverainvert","Fravauxnoisel","Fendroismont","Fauvernoismont","Fravertmontel","Félorvoismont","Fauvermontin",
    "Fravauxinnoir","Fendrelvois","Fauverainmont","Fravertvois","Félorainvert","Fauvernoisnoir","Fravauxvois",

    # G (57)
    "Gérauvois","Gavernin","Gréval","Gendrois","Gavermont","Grévoix","Gérauvain","Gavernaux","Grévalin","Gendrel",
    "Gavernoisel","Grévoine","Gérauvoine","Gavermontel","Grévalnoir","Gendroisel","Gavernauxel","Grévoixnoir","Gérauvaux","Gaverninnoir",
    "Grévalvert","Gendrelaux","Gavermontaux","Grévoixvert","Gérauvainel","Gavernoismont","Grévalmont","Gendroisvert","Gavernauxnoir","Grévoinmont",
    "Gérauvauxel","Gaverninaux","Grévalmontel","Gendrelnoir","Gavermontnoir","Grévoixmont","Gérauvainnoir","Gavernoismontel","Grévalinnoir","Gendroismont",
    "Gavernauxvert","Grévoinnoir","Gérauvauxnoir","Gaverninmont","Grévalvois","Gendrelmont","Gavermontvert","Grévoixin","Gérauvainmont","Gavernoismontaux",
    "Grévalmontnoir","Gendroisnoir","Gavernauxmont","Grévoixvois","Gérauvauxmont","Gaverninvois","Grévalvoisel",

    # H (57)
    "Hervaint","Havernois","Hélavoix","Hendrel","Havermont","Hélavert","Hervainel","Havernaux","Hélavoine","Hendrois",
    "Havernoisel","Hélavaux","Hervaintin","Havermontel","Hélavoisel","Hendrelaux","Havernauxel","Hélavertin","Hervainnoir","Havernin",
    "Hélavauxnoir","Hendroisel","Havermontaux","Hélavoixnoir","Hervainvert","Haverninnoir","Hélavertaux","Hendrelnoir","Havernoismont","Hélavoinevert",
    "Hervainmont","Havernauxnoir","Hélavauxvert","Hendroisvert","Havermontnoir","Hélavoixmont","Hervainvois","Haverninaux","Hélavertnoir","Hendrelmont",
    "Havernoismontel","Hélavoinein","Hervainaux","Havernauxvert","Hélavauxin","Hendroismont","Havermontvert","Hélavoixin","Hervainmontel","Haverninmont",
    "Hélavertmont","Hendrelvois","Havernoismontaux","Hélavoinevois","Hervainvoisel","Havernauxmont","Hélavauxmont",

    # I (57)
    "Isambrois","Ivainel","Irévoix","Indrel","Ivairmont","Irévaux","Isambroin","Ivainaux","Irévoine","Indrois",
    "Ivairnoisel","Irévauxel","Isambroisnoir","Ivainnoir","Irévoixnoir","Indrelaux","Ivairmontel","Irévauxnoir","Isambroinnoir","Ivainvert",
    "Irévoin","Indroisel","Ivairnoisvert","Irévauxvert","Isambroisvert","Ivainmont","Irévoixvert","Indrelnoir","Ivairmontaux","Irévoinnoir",
    "Isambroinaux","Ivainvaux","Irévauxmont","Indroisvert","Ivairnoisaux","Irévoixmont","Isambroisaux","Ivainmontel","Irévauxin","Indrelmont",
    "Ivairmontnoir","Irévoinmont","Isambroinmont","Ivainvois","Irévauxmontel","Indroismont","Ivairnoismont","Irévoixin","Isambroisvois","Ivainvauxel",
    "Irévauxvois","Indrelvois","Ivairmontvert","Irévoinvois","Isambroisvertin","Ivainmontaux","Irévauxmontnoir",

    # J (57)
    "Javernois","Jéravain","Jolvoix","Jendrel","Javermont","Jolvert","Javernaux","Jéravaux","Jolvoine","Jendrois",
    "Javernoisel","Jolvoisel","Jéravainel","Javermontel","Jolvaux","Jendrelaux","Javernauxel","Jolvertin","Jéravainnoir","Javernin",
    "Jolvauxnoir","Jendroisel","Javermontaux","Jolvoixnoir","Jéravainvert","Javerninnoir","Jolvertaux","Jendrelnoir","Javernoismont","Jolvoinevert",
    "Jéravainmont","Javernauxnoir","Jolvauxvert","Jendroisvert","Javermontnoir","Jolvoixmont","Jéravainvois","Javerninaux","Jolvertnoir","Jendrelmont",
    "Javernoismontel","Jolvoinein","Jéravainaux","Javernauxvert","Jolvauxin","Jendroismont","Javermontvert","Jolvoixin","Jéravainmontel","Javerninmont",
    "Jolvertmont","Jendrelvois","Javernoismontaux","Jolvoinevois","Jéravainvoisel","Javernauxmont","Jolvauxmont",

    # K (57)
    "Kervaint","Kavernois","Kélavoix","Kendrel","Kavermont","Kélavert","Kervainel","Kavernaux","Kélavoine","Kendrois",
    "Kavernoisel","Kélavaux","Kervaintin","Kavermontel","Kélavoisel","Kendrelaux","Kavernauxel","Kélavertin","Kervainnoir","Kavernin",
    "Kélavauxnoir","Kendroisel","Kavermontaux","Kélavoixnoir","Kervainvert","Kaverninnoir","Kélavertaux","Kendrelnoir","Kavernoismont","Kélavoinevert",
    "Kervainmont","Kavernauxnoir","Kélavauxvert","Kendroisvert","Kavermontnoir","Kélavoixmont","Kervainvois","Kaverninaux","Kélavertnoir","Kendrelmont",
    "Kavernoismontel","Kélavoinein","Kervainaux","Kavernauxvert","Kélavauxin","Kendroismont","Kavermontvert","Kélavoixin","Kervainmontel","Kaverninmont",
    "Kélavertmont","Kendrelvois","Kavernoismontaux","Kélavoinevois","Kervainvoisel","Kavernauxmont","Kélavauxmont",

    # L (57)
    "Lévairmont","Lavernoix","Lorianne","Lendrois","Lavermont","Loravert","Lévainel","Lavernaux","Lorianvois","Lendrel",
    "Lavernoisel","Loravaux","Lévainnoir","Lavermontel","Lorianvert","Lendroisel","Lavernauxel","Loravertin","Lévainmont","Lavernin",
    "Lorianvaux","Lendrelaux","Lavermontaux","Loravoix","Lévainvert","Laverninnoir","Lorianmont","Lendroisvert","Lavernoismont","Loravoine",
    "Lévainvois","Lavernauxnoir","Loriannoir","Lendrelnoir","Lavermontnoir","Loravoixnoir","Lévainmontel","Laverninaux","Lorianvauxel","Lendroismont",
    "Lavernoismontel","Loravoinevert","Lévainaux","Lavernauxvert","Lorianin","Lendrelmont", "Quendrel","Quervaux","Quillavois","Quendrois","Quervain","Quillavert","Quendrelaux","Quervauxel","Quillavoine","Quendroisel",
    "Quervainel","Quillavaux","Quendrelnoir","Quervainnoir","Quillavoisel","Quendroisvert","Quervauxnoir","Quillavertin","Quendrelmont","Quervainmont",
    "Quillavoix","Quendroismont","Quervauxvert","Quillavauxnoir","Quendrelvois","Quervainaux","Quillavoinevert","Quendroisnoir","Quervauxmont","Quillavertnoir",
    "Quendrelvert","Quervainvois","Quillavoixin","Quendroismontel","Quervauxin","Quillavauxvert","Quendrelauxin","Quervainmontel","Quillavoinein","Quendroisaux",
    "Quervauxmontel","Quillavertmont","Quendrelmontel","Quervainvert","Quillavoisnoir","Quendroisvertin","Quervauxvois","Quillavauxmont","Quendrelvoisel","Quervainnoisel",
    "Quillavoinevois","Quendroisvois","Quervauxmontnoir","Quillavertaux","Quendrelmontnoir","Quervainvaux","Quillavoismont",

    # R (57)
    "Ravernois","Rélavoix","Rendrel","Ravermont","Rélavert","Ravernaux","Rélavoine","Rendrois","Ravernin","Rélavaux",
    "Ravermontel","Rélavoisel","Rendrelaux","Ravernauxel","Rélavertin","Rendroisel","Raverninnoir","Rélavauxnoir","Rendrelnoir","Ravernoismont",
    "Rélavoinevert","Rendroisvert","Ravermontnoir","Rélavoixnoir","Rendrelmont","Ravernauxnoir","Rélavauxvert","Rendroismont","Ravernoismontel","Rélavoinein",
    "Rendrelvois","Ravernauxvert","Rélavauxin","Rendroisnoir","Ravermontvert","Rélavoixin","Rendrelmontel","Raverninaux","Rélavertnoir","Rendroismontel",
    "Ravernoismontaux","Rélavoinevois","Rendrelauxin","Ravernauxmont","Rélavauxmont","Rendroisvertin","Ravermontin","Rélavoismont","Rendrelvaux","Raverninmont",
    "Rélavertmont","Rendroisvois","Ravernoismontnoir","Rélavoixvert","Rendrelvauxel","Ravernauxvois","Rélavauxvois",

    # S (57)
    "Savernois","Sélavoix","Sendrel","Savermont","Sélavert","Savernaux","Sélavoine","Sendrois","Savernin","Sélavaux",
    "Savermontel","Sélavoisel","Sendrelaux","Savernauxel","Sélavertin","Sendroisel","Saverninnoir","Sélavauxnoir","Sendrelnoir","Savernoismont",
    "Sélavoinevert","Sendroisvert","Savermontnoir","Sélavoixnoir","Sendrelmont","Savernauxnoir","Sélavauxvert","Sendroismont","Savernoismontel","Sélavoinein",
    "Sendrelvois","Savernauxvert","Sélavauxin","Sendroisnoir","Savermontvert","Sélavoixin","Sendrelmontel","Saverninaux","Sélavertnoir","Sendroismontel",
    "Savernoismontaux","Sélavoinevois","Sendrelauxin","Savernauxmont","Sélavauxmont","Sendroisvertin","Savermontin","Sélavoismont","Sendrelvaux","Saverninmont",
    "Sélavertmont","Sendroisvois","Savernoismontnoir","Sélavoixvert","Sendrelvauxel","Savernauxvois","Sélavauxvois",

    # T (57)
    "Tavernois","Télavoix","Tendrel","Tavermont","Télavert","Tavernaux","Télavoine","Tendrois","Tavernin","Télavaux",
    "Tavermontel","Télavoisel","Tendrelaux","Tavernauxel","Télavertin","Tendroisel","Taverninnoir","Télavauxnoir","Tendrelnoir","Tavernoismont",
    "Télavoinevert","Tendroisvert","Tavermontnoir","Télavoixnoir","Tendrelmont","Tavernauxnoir","Télavauxvert","Tendroismont","Tavernoismontel","Télavoinein",
    "Tendrelvois","Tavernauxvert","Télavauxin","Tendroisnoir","Tavermontvert","Télavoixin","Tendrelmontel","Taverninaux","Télavertnoir","Tendroismontel",
    "Tavernoismontaux","Télavoinevois","Tendrelauxin","Tavernauxmont","Télavauxmont","Tendroisvertin","Tavermontin","Télavoismont","Tendrelvaux","Taverninmont",
    "Télavertmont","Tendroisvois","Tavernoismontnoir","Télavoixvert","Tendrelvauxel","Tavernauxvois","Télavauxvois",

    # U (57)
    "Uvermont","Ulavoix","Undrel","Uvernais","Ulavert","Uverneaux","Ulavoine","Undrois","Uvernin","Ulavaux",
    "Uvermontel","Ulavoisel","Undrelaux","Uverneauxel","Ulavertin","Undroisel","Uverninnoir","Ulavauxnoir","Undrelnoir","Uvernoismont",
    "Ulavoinevert","Undroisvert","Uvermontnoir","Ulavoixnoir","Undrelmont","Uverneauxnoir","Ulavauxvert","Undroismont","Uvernoismontel","Ulavoinein",
    "Undrelvois","Uverneauxvert","Ulavauxin","Undroisnoir","Uvermontvert","Ulavoixin","Undrelmontel","Uverninaux","Ulavertnoir","Undroismontel",
    "Uvernoismontaux","Ulavoinevois","Undrelauxin","Uverneauxmont","Ulavauxmont","Undroisvertin","Uvermontin","Ulavoismont","Undrelvaux","Uverninmont",
    "Ulavertmont","Undroisvois","Uvernoismontnoir","Ulavoixvert","Undrelvauxel","Uverneauxvois","Ulavauxvois",

    # V (57)
    "Vavernois","Vélavoix","Vendrel","Vavermont","Vélavert","Vavernaux","Vélavoine","Vandrois","Vavernin","Vélavaux",
    "Vavermontel","Vélavoisel","Vendrelaux","Vavernauxel","Vélavertin","Vandroisel","Vaverninnoir","Vélavauxnoir","Vendrelnoir","Vavernoismont",
    "Vélavoinevert","Vandroisvert","Vavermontnoir","Vélavoixnoir","Vendrelmont","Vavernauxnoir","Vélavauxvert","Vandroismont","Vavernoismontel","Vélavoinein",
    "Vendrelvois","Vavernauxvert","Vélavauxin","Vandroisnoir","Vavermontvert","Vélavoixin","Vendrelmontel","Vaverninaux","Vélavertnoir","Vandroismontel",
    "Vavernoismontaux","Vélavoinevois","Vendrelauxin","Vavernauxmont","Vélavauxmont","Vandroisvertin","Vavermontin","Vélavoismont","Vendrelvaux","Vaverninmont",
    "Vélavertmont","Vandroisvois","Vavernoismontnoir","Vélavoixvert","Vendrelvauxel","Vavernauxvois","Vélavauxvois",

    # W (57)
    "Wavernois","Wélavoix","Wendrel","Wavermont","Wélavert","Wavernaux","Wélavoine","Wendrois","Wavernin","Wélavaux",
    "Wavermontel","Wélavoisel","Wendrelaux","Wavernauxel","Wélavertin","Wendroisel","Waverninnoir","Wélavauxnoir","Wendrelnoir","Wavernoismont",
    "Wélavoinevert","Wendroisvert","Wavermontnoir","Wélavoixnoir","Wendrelmont","Wavernauxnoir","Wélavauxvert","Wendroismont","Wavernoismontel","Wélavoinein",
    "Wendrelvois","Wavernauxvert","Wélavauxin","Wendroisnoir","Wavermontvert","Wélavoixin","Wendrelmontel","Waverninaux","Wélavertnoir","Wendroismontel",
    "Wavernoismontaux","Wélavoinevois","Wendrelauxin","Wavernauxmont","Wélavauxmont","Wendroisvertin","Wavermontin","Wélavoismont","Wendrelvaux","Waverninmont",
    "Wélavertmont","Wendroisvois","Wavernoismontnoir","Wélavoixvert","Wendrelvauxel","Wavernauxvois","Wélavauxvois",

    # X (57)
    "Xavernois","Xélavoix","Xendrel","Xavermont","Xélavert","Xavernaux","Xélavoine","Xendrois","Xavernin","Xélavaux",
    "Xavermontel","Xélavoisel","Xendrelaux","Xavernauxel","Xélavertin","Xendroisel","Xaverninnoir","Xélavauxnoir","Xendrelnoir","Xavernoismont",
    "Xélavoinevert","Xendroisvert","Xavermontnoir","Xélavoixnoir","Xendrelmont","Xavernauxnoir","Xélavauxvert","Xendroismont","Xavernoismontel","Xélavoinein",
    "Xendrelvois","Xavernauxvert","Xélavauxin","Xendroisnoir","Xavermontvert","Xélavoixin","Xendrelmontel","Xaverninaux","Xélavertnoir","Xendroismontel",
    "Xavernoismontaux","Xélavoinevois","Xendrelauxin","Xavernauxmont","Xélavauxmont","Xendroisvertin","Xavermontin","Xélavoismont","Xendrelvaux","Xaverninmont",
    "Xélavertmont","Xendroisvois","Xavernoismontnoir","Xélavoixvert","Xendrelvauxel","Xavernauxvois","Xélavauxvois",

    # Y (57)
    "Yavernois","Yélavoix","Yendrel","Yavermont","Yélavert","Yavernaux","Yélavoine","Yendrois","Yavernin","Yélavaux",
    "Yavermontel","Yélavoisel","Yendrelaux","Yavernauxel","Yélavertin","Yendroisel","Yaverninnoir","Yélavauxnoir","Yendrelnoir","Yavernoismont",
    "Yélavoinevert","Yendroisvert","Yavermontnoir","Yélavoixnoir","Yendrelmont","Yavernauxnoir","Yélavauxvert","Yendroismont","Yavernoismontel","Yélavoinein",
    "Yendrelvois","Yavernauxvert","Yélavauxin","Yendroisnoir","Yavermontvert","Yélavoixin","Yendrelmontel","Yaverninaux","Yélavertnoir","Yendroismontel",
    "Yavernoismontaux","Yélavoinevois","Yendrelauxin","Yavernauxmont","Yélavauxmont","Yendroisvertin","Yavermontin","Yélavoismont","Yendrelvaux","Yaverninmont",
    "Yélavertmont","Yendroisvois","Yavernoismontnoir","Yélavoixvert","Yendrelvauxel","Yavernauxvois","Yélavauxvois",

    # Z (57)
    "Zavernois","Zélavoix","Zendrel","Zavermont","Zélavert","Zavernaux","Zélavoine","Zendrois","Zavernin","Zélavaux",
    "Zavermontel","Zélavoisel","Zendrelaux","Zavernauxel","Zélavertin","Zendroisel","Zaverninnoir","Zélavauxnoir","Zendrelnoir","Zavernoismont",
    "Zélavoinevert","Zendroisvert","Zavermontnoir","Zélavoixnoir","Zendrelmont","Zavernauxnoir","Zélavauxvert","Zendroismont","Zavernoismontel","Zélavoinein",
    "Zendrelvois","Zavernauxvert","Zélavauxin","Zendroisnoir","Zavermontvert","Zélavoixin","Zendrelmontel","Zaverninaux","Zélavertnoir","Zendroismontel",
    "Zavernoismontaux","Zélavoinevois","Zendrelauxin","Zavernauxmont","Zélavauxmont","Zendroisvertin","Zavermontin","Zélavoismont","Zendrelvaux","Zaverninmont",
    "Zélavertmont","Zendroisvois","Zavernoismontnoir","Zélavoixvert","Zendrelvauxel","Zavernauxvois","Zélavauxvois"]

clausius = random.choice(clausius_names)
clausius1 = random.choice(clausius_names1)
clausius2 = random.choice(clausius_names2)
tsallis_madhi = random.choice(tsallis_madhi_names)
tsallis_madhi1 = random.choice(tsallis_madhi_names)
massieu = random.choice(massieu_names)
massieu1 = random.choice(massieu_names1)
massieu2 = random.choice(massieu_names2)

madhi1_or2 = random.randint(1, 7)
if madhi1_or2 == 1:
    madhi_name = tsallis_madhi + ' "' + r.word(include_parts_of_speech=['noun']) + '" ' + tsallis_madhi1
elif madhi1_or2 == 2:
    madhi_name = tsallis_madhi + ' "' + r.word(include_parts_of_speech=['noun']) + '" ' + tsallis_madhi1
elif madhi1_or2 == 3:
    madhi_name = tsallis_madhi + ' "The ' + r.word(include_parts_of_speech=['noun']) + '" ' + tsallis_madhi1
elif madhi1_or2 == 4:
    madhi_name = tsallis_madhi + ' ' + tsallis_madhi1
elif madhi1_or2 == 5:
    madhi_name = tsallis_madhi + ', ' + r.word(include_parts_of_speech=['adjective']) + ' ' + r.word(include_parts_of_speech=['noun'])
elif madhi1_or2 == 6:
    madhi_name = tsallis_madhi + ', ' + r.word(include_parts_of_speech=['adjective']) + ' ' + r.word(include_parts_of_speech=['noun'])
elif madhi1_or2 == 7:
    madhi_name = tsallis_madhi + ' ' + tsallis_madhi1 + ' the ' + r.word(include_parts_of_speech=['adjective']) + ' ' + r.word(include_parts_of_speech=['noun'])

clausius1_or2 = random.randint(1, 6)
if clausius1_or2 == 1:
    clausius_name = clausius + ' the ' + r.word(include_parts_of_speech=['adjective']) + ' ' + r.word(include_parts_of_speech=['noun'])
elif clausius1_or2 == 2:
    clausius_name = clausius + ' ' + clausius1 + ', ' + r.word(include_parts_of_speech=['adjective']) + ' ' + r.word(include_parts_of_speech=['noun'])
elif clausius1_or2 == 3:
    clausius_name = clausius + ', ' + r.word(include_parts_of_speech=['adjective']) + ' ' + r.word(include_parts_of_speech=['noun'])
elif clausius1_or2 == 4:
    clausius_name = clausius + ' ' + clausius1 + ' ' + clausius2
elif clausius1_or2 == 5:
    clausius_name = clausius + ' ' + clausius1 +' the ' + r.word(include_parts_of_speech=['adjective'])
elif clausius1_or2 == 6:
    clausius_name = clausius + ' the ' + r.word(include_parts_of_speech=['adjective'])

massieu1_or2 = random.randint(1, 9)
if massieu1_or2 == 1:
    massieu_name = massieu + ' the ' + r.word(include_parts_of_speech=['noun'])
elif massieu1_or2 == 2:
    massieu_name = massieu + ' ' + massieu1 + ' the ' + r.word(include_parts_of_speech=['adjective']) + ' ' + r.word(include_parts_of_speech=['adjective']) + ' ' + r.word(include_parts_of_speech=['noun'])
elif massieu1_or2 == 3:
    massieu_name = massieu + ' the ' + r.word(include_parts_of_speech=['noun'])
elif massieu1_or2 == 4:
    massieu_name = massieu + ' "' + massieu1 + '" ' + massieu2
elif massieu1_or2 == 5:
    massieu_name = 'The ' + r.word(include_parts_of_speech=['adjective']) + ' ' + r.word(include_parts_of_speech=['noun']) + ' ' + r.word(include_parts_of_speech=['verb']) + 'er'
elif massieu1_or2 == 5:
    massieu_name = 'The ' + r.word(include_parts_of_speech=['noun']) + ' ' + r.word(include_parts_of_speech=['verb']) + 'er'
elif massieu1_or2 == 6:
    massieu_name = massieu + ' the ' + r.word(include_parts_of_speech=['adjective']) + ' ' + r.word(include_parts_of_speech=['adjective']) + ' ' +r.word(include_parts_of_speech=['noun'])
elif massieu1_or2 == 7:
    massieu_name = massieu + ' the ' + massieu1
elif massieu1_or2 == 8:
    massieu_name = massieu + ', ' + r.word(include_parts_of_speech=['adjective']) + ' ' + r.word(include_parts_of_speech=['adjective']) + ' ' +r.word(include_parts_of_speech=['noun'])
elif massieu1_or2 == 9:
    massieu_name = massieu + ', ' + r.word(include_parts_of_speech=['adjective']) + ' ' +r.word(include_parts_of_speech=['noun'])

tsallis1_or2 = random.randint(1, 9)
if tsallis1_or2 == 1:
    tsallis_name = tsallis_madhi + ' the ' + r.word(include_parts_of_speech=['adjective']) + ' ' + r.word(include_parts_of_speech=['adjective']) + ' ' + r.word(include_parts_of_speech=['noun'])
elif tsallis1_or2 == 2:
    tsallis_name = 'The ' + r.word(include_parts_of_speech=['adjective']) + ' ' + r.word(include_parts_of_speech=['adjective']) + ' ' + r.word(include_parts_of_speech=['adjective']) + ' ' + r.word(include_parts_of_speech=['noun'])
elif tsallis1_or2 == 3:
    tsallis_name = tsallis_madhi + ', ' + r.word(include_parts_of_speech=['adjective']) + ' ' + r.word(include_parts_of_speech=['noun'])
elif tsallis1_or2 == 4:
    tsallis_name = r.word(include_parts_of_speech=['verb']) + 'er ' + tsallis_madhi
elif tsallis1_or2 == 5:
    tsallis_name = 'The ' + r.word(include_parts_of_speech=['verb']) + 'ing ' + r.word(include_parts_of_speech=['noun'])
elif tsallis1_or2 == 6:
    tsallis_name = tsallis_madhi + ', ' + r.word(include_parts_of_speech=['noun']) + ' of the ' + r.word(include_parts_of_speech=['noun'])
elif tsallis1_or2 == 7:
    tsallis_name = 'The ' + r.word(include_parts_of_speech=['verb']) + 'ing ' + r.word(include_parts_of_speech=['noun']) + ' of ' + r.word(include_parts_of_speech=['noun'])
elif tsallis1_or2 == 8:
    tsallis_name = 'The ' + r.word(include_parts_of_speech=['verb']) + 'less ' + r.word(include_parts_of_speech=['noun']) + ' of ' + r.word(include_parts_of_speech=['noun'])
elif tsallis1_or2 == 9:
    tsallis_name = 'The ' + r.word(include_parts_of_speech=['adjective']) + 'ly ' + r.word(include_parts_of_speech=['adjective']) + ' ' + r.word(include_parts_of_speech=['noun'])

st.write("Madhi Name: ", madhi_name)
st.write("Clausius Name: ", clausius_name)
st.write("Massieu Name: ", massieu_name)
st.write("Tsallis Name: ", tsallis_name)
button = st.button("Get Names")
if button:
    st.toast('Success!')