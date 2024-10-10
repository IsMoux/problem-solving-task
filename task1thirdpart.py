import json

def parse_categories():
    # Charger les données JSON des catégories
    with open('categories.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    categories = []

    def get_categories_recursive(block_id, path=[]):
        if block_id not in data:
            return
        node = data[block_id]

        # Ajouter le texte de la catégorie actuelle au chemin
        text = node.get('props', {}).get('label') or node.get('props', {}).get('text', 'Unknown')
        if text != "Ver todo":  # Éviter les répétitions inutiles
            new_path = path + [text]
        else:
            new_path = path

        # Vérifier si le nœud a des blocs enfants
        if 'blocks' in node and node['blocks']:
            for block in node['blocks']:
                get_categories_recursive(block['blockId'], new_path)
        else:
            if new_path:  # Ajouter uniquement les chemins non vides
                categories.append(new_path)

    # Identifier la clé racine et démarrer la récursion à partir de là
    root_keys = list(data.keys())
    for root_key in root_keys:
        get_categories_recursive(root_key)

    # Éliminer les chemins dupliqués
    unique_categories = []
    for category in categories:
        if category not in unique_categories:
            unique_categories.append(category)

    return unique_categories

categories = [
  ["Súper"],
  ["Vinos y Licores"],
  ["Bebés"],
  ["Farmacia"],
  ["Frutas y Verduras"],
  ["Carnes, pescados y mariscos"],
  ["Pescados y Mariscos"],
  ["Salchichonería"],
  ["Lácteos y Huevos"],
  ["Quesos"],
  ["Despensa"],
  ["Refrigerado y Congelado"],
  ["Panadería y Tortillería"],
  ["Limpieza del hogar"],
  ["Bebidas"],
  ["Cuidado personal"],
  ["Fuente de sodas"],
  ["Productos a granel"],
  ["Desechables"],
  ["Vinos"],
  ["Licores y destilados"],
  ["Cervezas"],
  ["Complementos"],
  ["Alimentación"],
  ["Higiene de bebé"],
  ["Ropa"],
  ["Accesorios"],
  ["Juguetes"],
  ["Ropa de cama"],
  ["Equipo y botiquín"],
  ["Incontinencia"],
  ["Medicamentos"],
  ["Salud sexual"],
  ["Vitaminas y suplementos"]
]

# Initialiser un dictionnaire vide pour les catégories
categories_dict = {}

# Parcourir les listes et remplir le dictionnaire  avec les sous catégories
for i in range(0, len(categories), 2):
    category = categories[i][0]
    if i + 1 < len(categories) and "Ver todo" not in categories[i + 1]:
        subcategory = categories[i + 1][0]
        if category in categories_dict:
            categories_dict[category].append(subcategory)
        else:
            categories_dict[category] = [subcategory]
    else:
        categories_dict[category] = []

print(categories_dict)
