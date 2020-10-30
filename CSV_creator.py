from main import *

def create_csv():
    with open('projet2.csv', 'w') as P2_test:
        csv_writer = csv.Dictwriter(P2_test, delimiter='')
        csv_writer.writerow(get_all_product_infos())


#récupérer le dictionnaire ici qui permet de créer le create_csv
#utiliser dictwriter
#vérifier si on appelle 2 fois que ça crée 2 lignes