import networkx as nx
import matplotlib.pyplot as plt

# Création du graphe
G = nx.Graph()

# Ajout des nœuds (PC, routeurs, serveurs)
nodes = [
    ("PC1", {"type": "ordinateur", "localisation": "Salle 1"}),
    ("PC2", {"type": "ordinateur", "localisation": "Salle 2"}),
    ("PC3", {"type": "ordinateur", "localisation": "Salle 3"}),
    ("PC4", {"type": "ordinateur", "localisation": "Salle 4"}),
    ("PC5", {"type": "ordinateur", "localisation": "Salle 5"}),
    ("PC6", {"type": "ordinateur", "localisation": "Salle 6"}),
    ("PC7", {"type": "ordinateur", "localisation": "Salle 7"}),
    ("PC8", {"type": "ordinateur", "localisation": "Salle 8"}),
    ("R1", {"type": "routeur", "localisation": "Etage 1"}),
    ("R2", {"type": "routeur", "localisation": "Etage 2"}),
    ("R3", {"type": "routeur", "localisation": "Etage 3"}),
    ("R4", {"type": "routeur", "localisation": "Etage 4"}),
    ("R5", {"type": "routeur", "localisation": "Etage 5"}),
    ("R6", {"type": "routeur", "localisation": "Etage 6"}),
    ("Serveur1", {"type": "serveur", "localisation": "Datacenter A"}),
    ("Serveur2", {"type": "serveur", "localisation": "Datacenter B"}),
    ("Serveur3", {"type": "serveur", "localisation": "Datacenter C"}),
    ("Serveur4", {"type": "serveur", "localisation": "Datacenter D"}),
]

G.add_nodes_from(nodes)

# Ajout des arêtes avec une latence en ms
edges = [
    ("PC1", "R1", {"latence": 2}),
    ("PC2", "R1", {"latence": 3}),
    ("PC3", "R2", {"latence": 4}),
    ("PC4", "R3", {"latence": 5}),
    ("PC5", "R4", {"latence": 6}),
    ("PC6", "R5", {"latence": 7}),
    ("PC7", "R6", {"latence": 8}),
    ("PC8", "R6", {"latence": 9}),
    ("R1", "R2", {"latence": 10}),
    ("R2", "R3", {"latence": 8}),
    ("R3", "R4", {"latence": 12}),
    ("R4", "R5", {"latence": 11}),
    ("R5", "R6", {"latence": 13}),
    ("R1", "Serveur1", {"latence": 15}),
    ("R2", "Serveur1", {"latence": 7}),
    ("R3", "Serveur2", {"latence": 9}),
    ("R4", "Serveur2", {"latence": 6}),
    ("R5", "Serveur3", {"latence": 13}),
    ("R6", "Serveur4", {"latence": 14}),
    ("Serveur1", "Serveur2", {"latence": 20}),
    ("Serveur2", "Serveur3", {"latence": 18}),
    ("Serveur3", "Serveur4", {"latence": 16}),
]

G.add_edges_from(edges)

# Fonction pour trouver le chemin le plus rapide depuis un PC vers tous les autres nœuds
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

# Exemples d'utilisation
chemin_plus_rapide_depuis("PC1")
chemin_plus_rapide_depuis("PC3")
chemin_plus_rapide_depuis("PC6")

# Visualisation du réseau
def visualiser_reseau():
    plt.figure(figsize=(14, 9))
    pos = nx.spring_layout(G, seed=42)  # Positionnement des nœuds

    # Dessiner les nœuds sans couleur spécifique
    nx.draw(G, pos, with_labels=True, node_color='skyblue', font_weight='bold', node_size=1000, font_size=8)

    # Affichage des latences sur les arêtes
    edge_labels = nx.get_edge_attributes(G, 'latence')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

    plt.title("Réseau informatique avec latences (ms)")
    plt.show()

visualiser_reseau()
