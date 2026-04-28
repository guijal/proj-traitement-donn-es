import random


def afficher_echantillon_hasard(titre: str, dictionnaire: dict):
    """Affiche un échantillon aléatoire d'objets depuis un dictionnaire de la db."""
    items = list(dictionnaire.values())
    if not items:
        print(f"\nAucune donnée n'a été trouvée pour : {titre}.")
        return

    print(f"\n--- {titre} ---")
    print(f"Il y a un total de {len(items)} enregistrements.")
    choix = input("Combien voulez-vous en afficher au hasard ? (Entrez un nombre ou 'tout') : ").strip().lower()
    
    if choix == "tout":
        echantillon = items
    else:
        try:
            nb = int(choix)
            nb = max(1, min(nb, len(items))) # Sécurité : borne le nombre entre 1 et le max d'items
            echantillon = random.sample(items, nb)
        except ValueError:
            print("Entrée invalide. Affichage de 5 éléments au hasard par défaut.")
            echantillon = random.sample(items, min(5, len(items)))
            
    for item in echantillon:
        print(f"- {item}")