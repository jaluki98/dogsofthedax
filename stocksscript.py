# import stock_info module from yahoo_fin
from yahoo_fin import stock_info as si
import datetime

today_date = datetime.date.today()
now = today_date.strftime("%d/%m/%Y")

#Bayer
bayerp = si.get_live_price("BAYN.DE")
bayerpreis = "%.2f" % bayerp
#Start in den Handelstag
def bayerstart():
    return f'Beim Start in den heutigen Handelstag ({now}) steht der Aktienkurs von #BAYER bei {bayerpreis}€. #DogsOfTheDax'
#Börsenschluss
def bayerschluss():
    return f'Nach Börsenschluss des heutigen Handelstags ({now}) steht der Aktienkurs von #BAYER bei {bayerpreis}€. #DogsOfTheDax'

#---------------------------------------
#BASF
basfp = si.get_live_price("BAS.DE")
basfpreis = "%.2f" % basfp
#Start in den Handelstag
def basfstart():
    return f'Beim Start in den heutigen Handelstag ({now}) steht der Aktienkurs von #BASF bei {basfpreis}€. #DogsOfTheDax'
#Börsenschluss
def basfschluss():
    return f'Nach Börsenschluss des heutigen Handelstags ({now}) steht der Aktienkurs von #BASF bei {basfpreis}€. #DogsOfTheDax'

#---------------------------------------
#EON
eoanp = si.get_live_price("EOAN.DE")
eoanpreis = "%.2f" % eoanp
#Start in den Handelstag
def eoanstart():
    return f'Beim Start in den heutigen Handelstag ({now}) steht der Aktienkurs von #EON bei {eoanpreis}€. #DogsOfTheDax'
#Börsenschluss
def eoanschluss():
    return f'Nach Börsenschluss des heutigen Handelstags ({now}) steht der Aktienkurs von #EON bei {eoanpreis}€. #DogsOfTheDax'

#---------------------------------------
#allianz
allianzp = si.get_live_price("ALV.DE")
allianzpreis = "%.2f" % allianzp
#Start in den Handelstag
def allianzstart():
    return f'Beim Start in den heutigen Handelstag ({now}) steht der Aktienkurs von #ALLIANZ bei {allianzpreis}€. #DogsOfTheDax'
#Börsenschluss
def allianzschluss():
    return f'Nach Börsenschluss des heutigen Handelstags ({now}) steht der Aktienkurs von #ALLIANZ bei {allianzpreis}€. #DogsOfTheDax'

#---------------------------------------
#Münchener Rück. Vers.
muvrp = si.get_live_price("MUV2.DE")
muvrpreis = "%.2f" % muvrp
#Start in den Handelstag
def muvrstart():
    return f'Beim Start in den heutigen Handelstag ({now}) steht der Aktienkurs von #MunichReGroup bei {muvrpreis}€. #DogsOfTheDax'
#Börsenschluss
def muvrschluss():
    return f'Nach Börsenschluss des heutigen Handelstags ({now}) steht der Aktienkurs von #MunichReGroup bei {muvrpreis}€. #DogsOfTheDax'

#---------------------------------------
#Deutsche Telekom
telekomp = si.get_live_price("DTE.DE")
telekompreis = "%.2f" % telekomp
#Start in den Handelstag
def telekomstart():
    return f'Beim Start in den heutigen Handelstag ({now}) steht der Aktienkurs der Deutschen #Telekom AG bei {telekompreis}€. #DogsOfTheDax'
#Börsenschluss
def telekomschluss():
    return f'Nach Börsenschluss des heutigen Handelstags ({now}) steht der Aktienkurs der Deutschen #Telekom AG bei {telekompreis}€. #DogsOfTheDax'

#---------------------------------------
#BMW
bmwp = si.get_live_price("BMW.DE")
bmwpreis = "%.2f" % bmwp
#Start in den Handelstag
def bmwstart():
    return f'Beim Start in den heutigen Handelstag ({now}) steht der Aktienkurs von #BMW bei {bmwpreis}€. #DogsOfTheDax'
#Börsenschluss
def bmwschluss():
    return f'Nach Börsenschluss des heutigen Handelstags ({now}) steht der Aktienkurs von #BMW bei {bmwpreis}€. #DogsOfTheDax'

#---------------------------------------
#Siemens
siemensp = si.get_live_price("SIE.DE")
siemenspreis = "%.2f" % siemensp
#Start in den Handelstag
def siemensstart():
    return f'Beim Start in den heutigen Handelstag ({now}) steht der Aktienkurs von #Siemens bei {siemenspreis}€. #DogsOfTheDax'
#Börsenschluss
def siemensschluss():
    return f'Nach Börsenschluss des heutigen Handelstags ({now}) steht der Aktienkurs von #Siemens bei {siemenspreis}€. #DogsOfTheDax'

#---------------------------------------
#Volkswagen
volkswagenp = si.get_live_price("VOW3.DE")
volkswagenpreis = "%.2f" % volkswagenp
#Start in den Handelstag
def volkswagenstart():
    return f'Beim Start in den heutigen Handelstag ({now}) steht der Aktienkurs von #Volkswagen bei {volkswagenpreis}€. #DogsOfTheDax'
#Börsenschluss
def volkswagenschluss():
    return f'Nach Börsenschluss des heutigen Handelstags ({now}) steht der Aktienkurs von #Volkswagen bei {volkswagenpreis}€. #DogsOfTheDax'

#---------------------------------------
#DeutschePost
deutschepostp = si.get_live_price("DPW.DE")
deutschepostpreis = "%.2f" % deutschepostp
#Start in den Handelstag
def deutschepoststart():
    return f'Beim Start in den heutigen Handelstag ({now}) steht der Aktienkurs der #DeutschePost AG bei {deutschepostpreis}€. #DogsOfTheDax'
#Börsenschluss
def deutschepostschluss():
    return f'Nach Börsenschluss des heutigen Handelstags ({now}) steht der Aktienkurs der #DeutschePost AG bei {deutschepostpreis}€. #DogsOfTheDax'

#---------------------------------------
#Wochenende
def wochenende():
    return f'Die Handelswoche ist vorbei. Samstags, und Sonntags findet kein Handel an der Börse statt. Weitere Informationen zur Anlagestrategie finden Sie hier: http://dogsofthedax.com #DogsOfTheDax'

#---------------------------------------