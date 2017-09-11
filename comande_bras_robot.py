import Adafruit_PCA9685
from sense_hat import SenseHat
import time
from sense_hat import *

print ('veuiller patienter 4 secondes')

  # x = 01234567
  #     --------
  
  # y = 0|
  #     1|
  #     2|
  #     3|
  #     4|
  #     5|
  #     6|
  #     7|

vitesse = 10

x = 2

V = [255, 0, 255]#rose
r = [255, 0, 0]#rouge
B = [255, 255, 255]# blanc
b = [0, 0, 255]#bleu
n = [0, 0, 0]#noir
v = [0, 255, 0]#vert
j = [255, 255, 0]#jaune

rouge_menu = [
        n, r, r, r, V, r, r, r,
        n, r, r, V, V, V, r, r,
        n, r, r, r, V, r, v, r,
        n, r, r, r, r, r, v, v,
        n, r, r, r, r, r, v, r,
        n, r, r, r, r, r, r, r,
        n, r, r, V, V, V, r, r,
        n, r, r, r, r, r, r, r
        ]

vert_menu = [
        n,v ,v ,v ,V ,v ,v ,v ,
        n,v ,v ,V ,V ,V ,v ,v ,
        n,v ,r ,v ,V ,v ,B ,v ,
        n,r ,r ,v ,v ,v ,B ,B ,
        n,v ,r ,v ,v ,v ,B ,v ,
        n,v ,v ,v ,v ,v ,v ,v ,
        n,v ,v ,V ,V ,V ,v ,v ,
        n,v ,v ,v ,v ,v ,v ,v ,
        ]

blanc_menu = [
        n, B, B, B, V, B, B, B,
        n, B, B, V, V, V, B, B,
        n, B, v, B, V, B, b, B,
        n, v, v, B, B, B, b, b,
        n, B, v, B, B, B, b, B,
        n, B, B, B, B, B, B, B,
        n, B, B, V, V, V, B, B,
        n, B, B, B, B, B, B, B,
        ]

bleu_menu = [
        n, b, b, b, V, b, b, b,
        n, b, b, V, V, V, b, b,
        n, b, B, b, V, b, j, b,
        n, B, B, b, b, b, j, j,
        n, b, B, b, b, b, j, b,
        n, b, b, b, b, b, b, b,
        n, b, b, V, V, V, b, b,
        n, b, b, b, b, b, b, b,
        ]

jaune_menu = [
        n, j, j, j, V, j, j, j,
        n, j, j, V, V, V, j, j,
        n, j, b, j, V, j, j, j,
        n, b, b, j, j, j, j, j,
        n, j, b, j, j, j, j, j,
        n, j, j, j, j, j, j, j,
        n, j, j, V, V, V, j, j,
        n, j, j, j, j, j, j, j,
        ]



def limites(value, min_value=0, max_value=4):
        return min(max_value, max(min_value, value))

def deplacer_menu(event):
    global x
    if event.action in ('pressed', 'held'):
            x = limites(x + {
                'left': -1,
                'right': 1,
                }.get(event.direction, 0))
            menu()
            


def menu():
        global x
        if x == 0 :
                hat.set_pixels(rouge_menu)
        elif x == 1:
                hat.set_pixels(vert_menu)
        elif x == 2:
                hat.set_pixels(blanc_menu)
        elif x == 3:
                hat.set_pixels(bleu_menu)
        elif x == 4:
                hat.set_pixels(jaune_menu)



base = 375



def base_plus(event):
   global base
   if event.action in ('pressed','held'):
        base = base + vitesse
        if base>600:
                base=base-vitesse
                hat.show_message("MAX", 0.08, r)
                menu()
                #print("la base est au maximum")
                
   servo.set_pwm(0,0,base)

def base_moin(event):
   global base
   if event.action in ('pressed','held'):
        base = base - vitesse
        if base<150:
                base=base + vitesse
                hat.show_message("MIN", 0.08, r)
                menu()
                #print("la base est au minimum")
                
   servo.set_pwm(0,0,base)





epaule = 375
epaule1 = 375

def epaule_plus(event):
   global epaule, epaule1
   if event.action in ('pressed','held'):
        epaule = epaule + vitesse
        epaule1 = epaule1 - vitesse
        if epaule>600:
                epaule=epaule-vitesse
                epaule1=epaule1+vitesse
                hat.show_message("MAX", 0.08, v)
                menu()
                #print("l'epaule est au maximum")
                
   servo.set_pwm(1,0,epaule)
   servo.set_pwm(2,0,epaule1)

def epaule_moin(event):
   global epaule,epaule1
   if event.action in ('pressed','held'):
        epaule = epaule - vitesse
        epaule1 = epaule1 + vitesse
        if epaule<150:
                epaule=epaule + vitesse
                epaule1=epaule1 - vitesse
                hat.show_message("MIN", 0.08, v)
                menu()
                #print("l'epaule est au minimum")
                
   servo.set_pwm(1,0,epaule)
   servo.set_pwm(2,0,epaule1)

pince = 325

def pince_plus(event):
   global pince
   if event.action in ('pressed','held'):
        pince = pince + vitesse
        if pince>400:
                pince=pince-vitesse
                hat.show_message("MAX", 0.08, B)
                menu()
                #print('les pinces sont au maximum')
                
   servo.set_pwm(5,0,pince)

def pince_moin(event):
   global pince
   if event.action in ('pressed','held'):
        pince = pince - vitesse
        if pince<325:
                pince=pince + vitesse
                hat.show_message("MIN", 0.08, B)
                
                menu()
                
                #print('les pinces sont au minimum')
                
   servo.set_pwm(5,0,pince)

coude = 375

def coude_plus(event):
   global coude
   if event.action in ('pressed','held'):
        coude = coude + vitesse
        if coude>600:
                coude=coude-vitesse
                hat.show_message("MAX", 0.08, b)
                
                menu()
                
                #print('le coude est au maximum')
                
   servo.set_pwm(4,0,coude)

def coude_moin(event):
   global coude
   if event.action in ('pressed','held'):
        coude = coude - vitesse
        if coude<150:
                coude=coude + vitesse
                hat.show_message("MIN", 0.08, b)
                menu()
                #print('le coude est au minimum')
                
   servo.set_pwm(4,0,coude)

poignet = 375

def poignet_plus(event):
   global poignet
   if event.action in ('pressed','held'):
        poignet = poignet + vitesse
        if poignet>600:
                poignet=poignet-vitesse
                hat.show_message("MAX", 0.08, j)
                menu()
                #print('le poignet est au maximum')
                
   servo.set_pwm(3,0,poignet)

def poignet_moin(event):
   global poignet
   if event.action in ('pressed','held'):
        poignet = poignet - vitesse
        if poignet<150:
                poignet=poignet + vitesse
                hat.show_message("MIN", 0.08, j)
                menu()
                #print('le poignet est au minimum')
                
   servo.set_pwm(3,0,poignet)

def deplacer_plus(event):
        global x
        if x == 0:
                base_plus(event)
        elif x == 1:
                epaule_plus(event)
        elif x == 2:
                pince_plus(event)
        elif x == 3:
                coude_plus(event)
        elif x == 4:
                poignet_plus(event)

def deplacer_moin(event):
        global x
        if x == 0:
                base_moin(event)
        elif x == 1:
                epaule_moin(event)
        elif x == 2:
                pince_moin(event)
        elif x == 3:
                coude_moin(event)
        elif x == 4:
                poignet_moin(event)

def ytr():
        hat.stick.direction_left = deplacer_menu
        hat.stick.direction_right = deplacer_menu
        hat.stick.direction_up = deplacer_plus
        hat.stick.direction_down = deplacer_moin
            
hat = SenseHat()
servo = Adafruit_PCA9685.PCA9685()
servo.set_pwm_freq(60)

servo.set_pwm(0,0,375)
time.sleep(1)
print ('veuiller patienter 3 secondes')
servo.set_pwm(1,0,375)
servo.set_pwm(2,0,375)
time.sleep(1)
print ('veuiller patienter 2 secondes')
servo.set_pwm(3,0,375)
time.sleep(1)
print ('veuiller patienter 1 secondes')
servo.set_pwm(4,0,375)
time.sleep(1)
print ('veuiller patienter 0 secondes')
servo.set_pwm(5,0,325)
        
hat.clear()                        
hat.set_pixels(blanc_menu)


print("entrer le nom du ficher a crée pour enregistrer")
nom_du_fichier = input()
nom_du_fichier_py = (nom_du_fichier + ".py")
print("nom du fichier:")
print(nom_du_fichier_py)
fichier = open(nom_du_fichier_py , "w")
fichier.write("import Adafruit_PCA9685")
fichier.write("\nimport time")
fichier.write("\n")
fichier.write("\nservo = Adafruit_PCA9685.PCA9685()")
fichier.write("\nservo.set_pwm_freq(60)")
fichier.write("\n")
fichier.close()
print("fichier créé")

print('')
print('comandes:')
print('r pour riset')
print('n pour crée un nouveau fichier')
print('e pour enregistrer toutes les position dans le fichier')
print('base pour bouger la base')
print("epaule pour bouger l'epaule")
print('coude pour bouger le coude')
print('poignet pour bouger le poignet')
print('pince pour bouger les pince')
print('vous pouvez egalement controler le bras avec le joy stick')
print('les code couleur son sur le bras mais si non les voici:')
print('rouge pour la base')
print("vert pour l'epaule")
print('jaune pour le coude')
print('bleu pour le poignet')
print('blanc pour les pinces')
print('')
print('/!\ veuiller pousez le joy stick par à-coups')
print('')
                    
while True :

        hat.stick.direction_any = ytr
        print("comande:")
        act = input()
        if act == "n":
                print("entrer le nom du ficher a crée")
                nom_du_fichier = input()
                nom_du_fichier_py = (nom_du_fichier + ".py")
                print("nom du fichier:")
                print(nom_du_fichier_py)
                fichier = open(nom_du_fichier_py , "w")
                fichier.write("import Adafruit_PCA9685")
                fichier.write("\nimport time")
                fichier.write("\n")
                fichier.write("\nservo = Adafruit_PCA9685.PCA9685()")
                fichier.write("\nservo.set_pwm_freq(60)")
                fichier.write("\n")
                fichier.close()
                print("fichier créé")
        elif act == "e":
                baseA = str(base)
                epauleA = str(epaule)
                epaule1A = str(epaule1)
                poignetA = str(poignet)
                coudeA = str(coude)
                pinceA = str(pince)
                fichier = open(nom_du_fichier_py , "a")
                fichier.write("\ntime.sleep(1)")
                fichier.write("\nservo.set_pwm(0,0," + baseA + ")")
                print("servo.set_pwm(0,0," + baseA + ")")
                fichier.write("\ntime.sleep(0.1)")
                fichier.write("\nservo.set_pwm(1,0," + epauleA + ")")
                fichier.write("\nservo.set_pwm(2,0," + epaule1A + ")")
                print("servo.set_pwm(1,0," + epauleA + ")")
                print("servo.set_pwm(2,0," + epaule1A + ")")
                fichier.write("\ntime.sleep(0.1)")
                fichier.write("\nservo.set_pwm(3,0," + poignetA + ")")
                print("servo.set_pwm(3,0," + poignetA + ")")
                fichier.write("\ntime.sleep(0.1)")
                fichier.write("\nservo.set_pwm(4,0," + coudeA + ")")
                print("servo.set_pwm(4,0," + coudeA + ")")
                fichier.write("\ntime.sleep(0.1)")
                fichier.write("\nservo.set_pwm(5,0," + pinceA + ")")
                print("servo.set_pwm(5,0," + pinceA + ")")
                fichier.close()
                print("enregistée")
        elif act == "r":
                print ('riset en cour')
                print ('veuiller patienter 4 secondes')
                servo.set_pwm(0,0,375)
                time.sleep(1)
                print ('veuiller patienter 3 secondes')
                servo.set_pwm(1,0,375)
                servo.set_pwm(2,0,375)
                time.sleep(1)
                print ('veuiller patienter 2 secondes')
                servo.set_pwm(3,0,375)
                time.sleep(1)
                print ('veuiller patienter 1 secondes')
                servo.set_pwm(4,0,375)
                time.sleep(1)
                print ('veuiller patienter 0 secondes')
                servo.set_pwm(5,0,325)
                base = 375
                epaule = 375
                epaule1 = 375
                poignet = 375
                coude = 375
                pince = 325
                print("riset terminé")
        elif act == "base":
                print("base:")
                baseZ = input()
                baseX = int(baseZ)
                if baseX > 600:
                        print("chiffre trop grand: entre 150 et 600")
                elif baseX < 150:
                        print("chiffre trop petit: entre 150 et 600")
                else:
                        print(baseX)
                        base = baseX
                        servo.set_pwm(0,0,base)
        elif act == "coude":
                print("coude:")
                coudeZ = input()
                coudeX = int(coudeZ)
                if coudeX > 600:
                        print("chiffre trop grand: entre 150 et 600")
                elif coudeX < 150:
                        print("chiffre trop petit: entre 150 et 600")
                else:
                        print(coudeX)
                        coude = coudeX
                        servo.set_pwm(3,0,coude)
        elif act == "poignet":
                print("poignet:")
                poignetZ = input()
                poignetX = int(poignetZ)
                if poignetX > 600:
                        print("chiffre trop grand: entre 150 et 600")
                elif poignetX < 150:
                        print("chiffre trop petit: entre 150 et 600")
                else:
                        print(poignetX)
                        poignet = poignetX
                        servo.set_pwm(4,0,poignet)
        elif act == "pince":
                print("pince:")
                pinceZ = input()
                pinceX = int(pinceZ)
                if pinceX > 400:
                        print("chiffre trop grand: entre 325 et 400")
                elif pinceX < 325:
                        print("chiffre trop petit: entre 325 et 400")
                else:
                        print(pinceX)
                        pince = pinceX
                        servo.set_pwm(5,0,pince)
        elif act == "epaule":
                print("epaule:")
                epauleZ = input()
                epauleX = int(epauleZ)
                if epauleX > 600:
                        print("chiffre trop grand: entre 150 et 600")
                elif epauleX < 150:
                        print("chiffre trop petit: entre 150 et 600")
                else:
                        print(epauleX)
                        epaule = epauleX
                        epaule1W = epauleX - 375
                        epaule1 = 375 - epaule1W
                        servo.set_pwm(1,0,epaule)
                        servo.set_pwm(2,0,epaule1)
        else:
                print("la comande n'existe pas")


      