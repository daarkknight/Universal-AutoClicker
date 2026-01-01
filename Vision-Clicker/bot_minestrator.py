import pyautogui
import time
import winsound

# Configuration des temps (en secondes)
DEUX_HEURES = 2 * 60 * 60  # 7200 secondes
SCAN_INTERVAL = 60         # Vérifie le bouton toutes les minutes

print("--- BOT CLIQUEUR (Refresh toutes les 2h) ---")
print("Affiche la page MineStrator (Opera, Chrome, etc.) à l'écran.")
time.sleep(5)

# On initialise le compteur de temps pour le refresh
dernier_refresh = time.time()

while True:
    try:
        maintenant = time.time()

        # 1. Vérifier si ça fait 2 heures qu'on n'a pas actualisé
        if maintenant - dernier_refresh >= DEUX_HEURES:
            print(f"[{time.strftime('%H:%M:%S')}] Cela fait 2h. Actualisation de la page (F5)...")
            pyautogui.press('f5')
            dernier_refresh = maintenant
            time.sleep(10) # Laisse 10 sec à la page pour recharger

        # 2. Chercher le bouton "Démarrer" sur l'écran
        # Note : Assure-toi d'avoir ton fichier 'bouton.png' dans le dossier
        button_pos = pyautogui.locateCenterOnScreen('bouton.png', confidence=0.8)
        
        if button_pos:
            print(f"[{time.strftime('%H:%M:%S')}] Bouton détecté ! Clic en cours...")
            winsound.Beep(1500, 500)
            pyautogui.click(button_pos)
            
            # Après avoir cliqué, on attend un peu pour laisser le serveur démarrer
            time.sleep(20)
        else:
            # On ne fait rien, on attend juste le prochain scan
            pass

    except Exception as e:
        print(f"Erreur : {e}")
        print("Vérifie que 'bouton.png' existe et que la fenêtre est visible.")

    # Pause avant le prochain scan du bouton
    time.sleep(SCAN_INTERVAL)