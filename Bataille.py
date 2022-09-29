from sys import *
import random

################### Fonctions utilitaires ####################

def aff(var_str):
	print(var_str)

def affnn(var_str):
	print(var_str, end = '')

def rand_int(a, b):
	res = random.randint(a, b)
	if (res>b): res = b
	if (res<a): res = a

	return res	

def aff_tab (tab, nom_tab="tab"):
	print(nom_tab+" : \n")
	for i in tab:
		print(i)
	print()

'''
	Affiche un dictionnaire
'''
def aff_dict(dict):
	if (dict):
		for i in dict:
			aff("\n"+i+" : "+str(dict[i]))
def is_number(a):
	chiffres = [".", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	nombre_de_points = 0
	a_tmp = (str)(a)

	if (a==""):
		return False
	j = 0
	for i in a_tmp:
		if (i=="-" and j>0):
			return False
		if (i=="."):
			nombre_de_points+=1
		if (nombre_de_points>1):
			return False
		if i not in chiffres:
			return False
		j+=1
	return True

def is_integer(a):
	if (is_number(a)):
		return ("." not in str(a))
	else:
		return False

def entre_entier(phrase):
	cmp = 0
	res = ""
	while (not is_integer(res)):
		if (cmp>0):
			print("\nVeuiller entrer un entier")
		res = input(phrase)
		cmp+=1
	return int(res)

def lecture_fichier (nom_fichier):
	fichier_oo = open(nom_fichier, 'r')
	oo = fichier_oo.read()
	fichier_oo.close()
	return oo

def ecriture_fichier (nom_du_fichier, res_final):
	fic_w = open(nom_du_fichier, 'w')
	fic_w.write(res_final)
	fic_w.close()

############# Fonctions utilitiares importantes ################

dictionnaire_famille = {
10:"Valet",
11:"Dame",
12:"Roi",
13:"AS",
}

dictionnaire_couleur = {
1:"trèfles",
2:"coeur",
3:"pique",
4:"carré"
}

def affiche_jeu(jeu):
	for carte in jeu:
		aff(str(carte[2])+" "+str(carte[3]))

def donne_dictionnaire_couleur(couleur):
	return dictionnaire_couleur[couleur]

def donne_dictionnaire_famille(chiffre):
	if (chiffre<11):
		return str(chiffre)
	return dictionnaire_famille[chiffre]

def jeu_de_carte():
	jeu = []
	for chiffre in range(1, 13+1):
		for couleur in range(1, 4+1):
			jeu.append([chiffre, couleur, donne_dictionnaire_famille(chiffre), donne_dictionnaire_couleur(couleur)])

	return jeu

def affiche_un_tour(jeu_1, jeu_2, titre):
	aff("\n"+titre+" :\n")
	affiche_jeu(jeu_1)
	affnn("\n")
	affiche_jeu(jeu_2)

def affiche_tab(titre_tab, tab):
	if (len(titre_tab)>0):
		aff(titre_tab+" : ")
	for i in tab:
		aff(i)
	aff("\n")
	

#################### Fonctions principales #####################

def melange_jeu(jeu_1):
	jeu_melange = []
	for i in range(0, len(jeu_1)):
		rand_int_1 = rand_int(0, len(jeu_1)-1)
		jeu_melange.append(jeu_1[rand_int_1])

	return jeu_melange

def distribue (paquet):
	jeu_distribué_1 = []
	jeu_distribué_2 = []

	while (len(paquet)-1>0):
		jeu_distribué_1.append(paquet.pop())
		jeu_distribué_2.append(paquet.pop())

	return (jeu_distribué_1, jeu_distribué_2)

def jeu():
	paquet = jeu_de_carte()

	#aff("\nDébut du jeu :\n"); affiche_jeu(paquet)

	paquet = melange_jeu(paquet)

	#aff("\nPaquet mélangé :\n"); affiche_jeu(paquet)

	(jeu_1, jeu_2)  = distribue (paquet)

	#affiche_un_tour(jeu_1, jeu_2, "Jeux distribués")

	coups = []

	nombre_de_tours = 0
	while (not verifie_fin_jeu(jeu_1, jeu_2)):
		coups.append("Nombre de cartes dans le jeu 1 = "+str(len(jeu_1)))
		coups.append("Nombre de cartes dans le jeu 2 = "+str(len(jeu_2)))
		(jeu_1, jeu_2, cartes_en_jeu_1) = tour_de_jeu(jeu_1, jeu_2)
		#affiche_un_tour(jeu_1, jeu_2, "\nTour de jeu n°"+str(nombre_de_tours)+"\n")
		coups.append("Tour "+str(cartes_en_jeu_1))
		coups.append("Tour de jeu n°"+str(nombre_de_tours)+"\n")
		nombre_de_tours+=1

	#affiche_un_tour(jeu_1, jeu_2, "Fin du jeu")
	#affiche_tab("", coups)

	nombre_de_secondes_par_tour = 3
	secondes = nombre_de_tours*nombre_de_secondes_par_tour
	minutes = secondes//60

	aff("\nLe nombre de tour(s) est de "+str(nombre_de_tours)+".")
	aff("A compter de "+str(nombre_de_secondes_par_tour)+" tour(s) par seconde, on a un total supposé de "+str(secondes)+" seconde(s).")
	if (secondes>=60):
		aff("C'est à dire "+str(minutes)+" minute(s).")

def verifie_fin_jeu(jeu_1, jeu_2):
	gagnant = 0
	if (len(jeu_1)==0):
		gagnant = 1
	if (len(jeu_2)==0):
		gagnant = 2

	if (gagnant==0):
		return False

	aff("\nLe joueur "+str(gagnant)+" a gagné !\n")

	return True		

def tour_de_jeu (jeu_1, jeu_2):
	cartes_en_jeu_1 = []

	if (len(jeu_1)<1 or len(jeu_2)<1):
		return (jeu_1, jeu_2, cartes_en_jeu_1)

	cartes_en_jeu_1.append(jeu_1.pop())
	cartes_en_jeu_1.append(jeu_2.pop())

	res_tmp = compare_deux_cartes(cartes_en_jeu_1[0], cartes_en_jeu_1[1])
	if (res_tmp==0):
		(res_tmp, cartes_en_jeu_1) = bataille_de_cartes(jeu_1, jeu_2, cartes_en_jeu_1)
	if (res_tmp==1):
		for carte in cartes_en_jeu_1:
			jeu_1.append(carte)
	if (res_tmp==2):
		for carte in cartes_en_jeu_1:
			jeu_2.append(carte)

	return (jeu_1, jeu_2, cartes_en_jeu_1)

def bataille_de_cartes(jeu_1, jeu_2, cartes_en_jeu_1):
	if (len(jeu_1)<1 or len(jeu_2)<1):
		return (-1, cartes_en_jeu_1)

	# cartes retournées

	cartes_en_jeu_1.append(jeu_1.pop())
	cartes_en_jeu_1.append(jeu_2.pop())

	if (len(jeu_1)<1 or len(jeu_2)<1):
		return (-1, cartes_en_jeu_1)

	cartes_en_jeu_1.append(jeu_1.pop())
	cartes_en_jeu_1.append(jeu_2.pop())

	res_tmp = compare_deux_cartes(cartes_en_jeu_1[len(cartes_en_jeu_1)-2], cartes_en_jeu_1[len(cartes_en_jeu_1)-1])
	if (res_tmp==0):
		(res_tmp, cartes_en_jeu_1) = bataille_de_cartes(jeu_1, jeu_2, cartes_en_jeu_1)

	return (res_tmp, cartes_en_jeu_1)

def compare_deux_cartes(carte_1, carte_2):
	if (carte_1[0] > carte_2[0]):
		return 1
	if (carte_1[0] < carte_2[0]):
		return 2
	if (carte_1[0] == carte_2[0]):
		return 0

############################ Main ##############################

def tests():
	test1()

def test1():
	pass

def main():
	jeu()

#tests()
main()