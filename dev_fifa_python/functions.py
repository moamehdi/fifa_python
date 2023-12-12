import os

def line_count_in_file(file):
    file1 = open(file, "r")
    lenght = 0
    for line in file1:
        lenght += 1
    return lenght

def supprimer_colonne(nom_fichier, numero_colonne,fichier_sortie):
    lignes = []

    with open(nom_fichier, 'r') as fichier:
        for ligne in fichier:
            colonnes = ligne.split(',')

            nouvelle_ligne = ''
            indice_colonne = 1
            for colonne in colonnes:
                if indice_colonne != numero_colonne:
                    nouvelle_ligne += colonne + ','

                indice_colonne += 1

            nouvelle_ligne = nouvelle_ligne.rstrip(',')

            lignes.append(nouvelle_ligne)
    with open(fichier_sortie, 'w') as fichier_sortie:
        fichier_sortie.write(''.join(lignes))

def column_count_in_file(fileName):
    column = 1
    fileData = open(fileName, "r")
    line=fileData.readline()    
    for letter in line:
        if letter == ',':
            column +=1
    return column                
            
            

def copy_file_content_without_entete(fileData,fileResult):

    file1 = open(fileData, "r")
    file2 = open(fileResult, "w")

    i=0
    for line in file1 :
        if i==0:
            i+=1
            continue
        else:        
            file2.write(line)
    file1.close()
    file2.close()


def trois_lettre_for_all_team(fileData, numero_colonne):
    with open(fileData, 'r') as fichier:
        for ligne in fichier:
            colonnes = ligne.split(',')
            if colonnes[numero_colonne] is not None:
                trois_lettre(colonnes[numero_colonne])
                
def trois_lettre(string):
    string_maj=string.upper()
    print(string_maj[0:3])

def calculer_difference_buts(fileData):
    i = 0
    with open(fileData, 'r') as fichier:
        test = fichier.readline()
        test2 = test.split(',')
        goals_for = None
        goals_against = None

        for test3 in test2:

            if test3 == 'Goals For':
                goals_for = i
            elif test3 == 'Goals Against':
                goals_against = i
            elif test3 == 'Team':
                teams = i
            i += 1

        if goals_for is None or goals_against is None:
            print("Les colonnes 'Goals For' et 'Goals Against' sont introuvables dans le fichier.")
            return

        for ligne in fichier:
            colonnes = ligne.split(',')
            goal_for_value = colonnes[goals_for]
            goal_against_value = colonnes[goals_against]   
            team = colonnes[teams]       
            difference = int(goal_for_value) - int(goal_against_value)
            print("pour l'équipe :" , team)
            print("Difference:", difference)
            print('--------------------')


def calculer_points(fileData):
    i = 0
    with open(fileData, 'r') as fichier:
        test = fichier.readline()
        test2 = test.split(',')
        win = None
        draw = None

        for test3 in test2:

            if test3 == 'Win':
                win = i
            elif test3 == 'Draw':
                draw = i
            elif test3 == 'Team':
                teams = i
            i += 1

        if win is None or draw is None:
            print("Les colonnes 'Goals For' et 'Goals Against' sont introuvables dans le fichier.")
            return

        for ligne in fichier:
            colonnes = ligne.split(',')
            win_value = colonnes[win]
            draw_value = colonnes[draw]   
            team = colonnes[teams]       
            points = int(win_value ) * 3 + int(draw_value)
            print("pour l'équipe :" , team)
            print("Points:", points)
            print('--------------------')