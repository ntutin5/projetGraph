import networkx as nx
import matplotlib.pyplot as plt

# 1. Création du graphe
G = nx.Graph()

# Ajout des nœuds (PC, routeurs, serveurs)
G.add_node("PC1", type="ordinateur", localisation="Salle 1")
G.add_node("PC2", type="ordinateur", localisation="Salle 2")
G.add_node("PC3", type="ordinateur", localisation="Salle 3")
G.add_node("PC4", type="ordinateur", localisation="Salle 4")
G.add_node("R1", type="routeur", localisation="Etage 1")
G.add_node("R2", type="routeur", localisation="Etage 2")
G.add_node("R3", type="routeur", localisation="Etage 3")
G.add_node("R4", type="routeur", localisation="Etage 4")
G.add_node("Serveur1", type="serveur", localisation="Datacenter A")
G.add_node("Serveur2", type="serveur", localisation="Datacenter B")

# Ajout des arêtes avec une latence en ms
G.add_edge("PC1", "R1", latence=2)
G.add_edge("PC2", "R1", latence=3)
G.add_edge("PC3", "R2", latence=4)
G.add_edge("PC4", "R3", latence=5)
G.add_edge("R1", "R2", latence=10)
G.add_edge("R2", "R3", latence=8)
G.add_edge("R3", "R4", latence=12)
G.add_edge("R1", "Serveur1", latence=15)
G.add_edge("R2", "Serveur1", latence=7)
G.add_edge("R3", "Serveur2", latence=9)
G.add_edge("R4", "Serveur2", latence=6)
G.add_edge("Serveur1", "Serveur2", latence=20)


# 3. Fonction pour trouver le chemin le plus rapide depuis un PC vers tous les autres nœuds
def chemin_plus_rapide_depuis(source):
    print(f"\n--- Chemins les plus rapides depuis {source} ---")
    for target in G.nodes():
        if source != target:
            try:
                chemin = nx.shortest_path(G, source=source, target=target, weight='latence')
                latence_totale = nx.shortest_path_length(G, source=source, target=target, weight='latence')
                print(f"De {source} à {target} : {chemin} | Latence : {latence_totale} ms")
            except nx.NetworkXNoPath:
                print(f"Aucun chemin trouvé de {source} à {target}")


# 4. Exemples d'utilisation
chemin_plus_rapide_depuis("PC1")
chemin_plus_rapide_depuis("PC3")
chemin_plus_rapide_depuis("PC4")

# 2. Visualisation du réseau
def visualiser_reseau():
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G, seed=42)  # Positionnement des nœuds
    nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold', node_size=800)

    # Affichage des latences sur les arêtes
    edge_labels = nx.get_edge_attributes(G, 'latence')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Réseau informatique avec latences (ms)")
    plt.show()

visualiser_reseau()
