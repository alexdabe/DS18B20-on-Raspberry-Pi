# mesure de temperatures avec raspberrypi
# sondes ds18b20
import time
import datetime
import csv


def lire_fichier (emplacement) :
    fichier = open(emplacement)
    contenu = fichier.read()
    fichier.close()
    return contenu
    
    
def extraire_temperature (contenu) :
    seconde_ligne = contenu.split("\n")[1]
    donnees_temperature = seconde_ligne.split(" ")[9]
    return float(donnees_temperature[2:]) / 1000


def sauvegarde(temperature_ext, temperature_int, date, emplacement):
    with open(emplacement, 'a') as file:
        writer = csv.writer(file,delimiter=',',lineterminator='\n')
        #  headerList = ['t', 'te', 'ti']
        t = date
        te = temperature_ext
        ti = temperature_int
        data = [t,te, ti]
        print(data)
        writer.writerow(data)
    file.close()
        
        
while True:
    date = datetime.datetime.now()
    contenu_fichier1 = lire_fichier("/sys/bus/w1/devices/28-0114531c89aa/w1_slave")  # Lecture de la sonde exterieure
    contenu_fichier2 = lire_fichier("/sys/bus/w1/devices/28-0300a279c595/w1_slave")  # Lecture de la sonde interieure
    temperature_ext = extraire_temperature(contenu_fichier1)
    temperature_int = extraire_temperature(contenu_fichier2)   
    sauvegarde(temperature_ext, temperature_int, date, "Temp.csv")  # Appel de la fonction sauvegarde avec 4 variables
    time.sleep(120)
