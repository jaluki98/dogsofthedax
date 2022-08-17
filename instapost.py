from instabot import Bot
from PIL import Image
import time as tmes
import shutil

image = Image.open('bg.jpg')
chart = Image.open('dogs_of_the_dax_charttwitterupdate.jpg')
image_copy = image.copy()
position = (0,325)
image_copy.paste(chart, position)
image_copy.save('pasted_image.jpg')

image2 = Image.open('bg.jpg')
chart2 = Image.open('Barchart_Einzelaktien_Dogs.jpg')
image_copy2 = image2.copy()
position2 = (0,325)
image_copy2.paste(chart2, position2)
image_copy2.save('pasted_image2.jpg')

dir_path = 'config'

try:
    shutil.rmtree(dir_path)
except OSError as e:
    print("Error: %s : %s" % (dir_path, e.strerror))

tmes.sleep(15)

bot = Bot()
bot.login(username="dogsofthedax", password="SCi100%h!!")
bot.upload_photo("pasted_image.jpg", caption="Dogs of the DAX Performance Update 📈☝️ Weitere Informationen unter: dogsofthedax.com #aktien #finanzen #geld #finanziellefreiheit #unternehmer #dogsofthedax #trading #unternehmertum #investieren #dividende #passiveseinkommen #ziele #aktie #stocks #aktienmitkopf #DJIA #investment #wirtschaft #dax #depot #kapital #dividenden #erfolg #sparplan #investition #motivation #corona #dogsofthedax #dax #dow Alle Texte sowie die Hinweise und Informationen auf den Social-Media Kanälen, sowie auf der Webseite dogsofthedax.com stellen keine Anlageberatung oder Empfehlung zum Kauf oder Verkauf von Wertpapieren dar (§ 85 WpHG). Sie dienen lediglich der persönlichen Information und geben ausschließlich die Meinung des Autors wieder. Es wird keine Empfehlung für eine bestimmte Anlagestrategie abgegeben. Die Inhalte von dogsofthedax.com richten sich ausschließlich an natürliche Personen mit Wohnsitz in der Bundesrepublik Deutschland. Die veröffentlichten Artikel, Analysen, Daten, Tools und Prognosen sind mit größter Sorgfalt und nach bestem Wissen und Gewissen recherchiert und erstellt. Die Quellen wurden als vertrauenswürdig erachtet. Eine Garantie, Gewährleistung oder Haftung für die Richtigkeit, Vollständigkeit und Aktualität der zur Verfügung gestellten Inhalte und Informationen kann nicht übernommen werden. Sollten Sie sich die auf dieser Seite angebotenen Inhalte zu eigen machen oder etwaigen Ratschlägen folgen, so handeln Sie eigenverantwortlich auf eigenes Risiko. Bitte beachten Sie, dass Wertpapiere grundsätzlich mit Risiko verbunden sind und im Wert schwanken können. Auch ein Totalverlust des eingesetzten Kapitals kann nicht ausgeschlossen werden. Die Dividende eines Unternehmens ist nicht garantiert, kann gekürzt oder ganz gestrichen werden. Eine Haftung, gleich aus welchem Rechtsgrund, wird nicht übernommen. Soweit es rechtlich möglich ist, sind Schadensersatzansprüche ausgeschlossen.")
bot.upload_photo("pasted_image2.jpg", caption="Dogs of the DAX Daily-Change der Einzelpositionen als Bar-Chart 📈☝️ Weitere Informationen unter: dogsofthedax.com #aktien #finanzen #geld #finanziellefreiheit #unternehmer #dogsofthedax #trading #unternehmertum #investieren #dividende #passiveseinkommen #ziele #aktie #stocks #aktienmitkopf #DJIA #investment #wirtschaft #dax #depot #kapital #dividenden #erfolg #sparplan #investition #motivation #corona #dogsofthedax #dax #dow Alle Texte sowie die Hinweise und Informationen auf den Social-Media Kanälen, sowie auf der Webseite dogsofthedax.com stellen keine Anlageberatung oder Empfehlung zum Kauf oder Verkauf von Wertpapieren dar (§ 85 WpHG). Sie dienen lediglich der persönlichen Information und geben ausschließlich die Meinung des Autors wieder. Es wird keine Empfehlung für eine bestimmte Anlagestrategie abgegeben. Die Inhalte von dogsofthedax.com richten sich ausschließlich an natürliche Personen mit Wohnsitz in der Bundesrepublik Deutschland. Die veröffentlichten Artikel, Analysen, Daten, Tools und Prognosen sind mit größter Sorgfalt und nach bestem Wissen und Gewissen recherchiert und erstellt. Die Quellen wurden als vertrauenswürdig erachtet. Eine Garantie, Gewährleistung oder Haftung für die Richtigkeit, Vollständigkeit und Aktualität der zur Verfügung gestellten Inhalte und Informationen kann nicht übernommen werden. Sollten Sie sich die auf dieser Seite angebotenen Inhalte zu eigen machen oder etwaigen Ratschlägen folgen, so handeln Sie eigenverantwortlich auf eigenes Risiko. Bitte beachten Sie, dass Wertpapiere grundsätzlich mit Risiko verbunden sind und im Wert schwanken können. Auch ein Totalverlust des eingesetzten Kapitals kann nicht ausgeschlossen werden. Die Dividende eines Unternehmens ist nicht garantiert, kann gekürzt oder ganz gestrichen werden. Eine Haftung, gleich aus welchem Rechtsgrund, wird nicht übernommen. Soweit es rechtlich möglich ist, sind Schadensersatzansprüche ausgeschlossen.")