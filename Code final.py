import requests #importation du module requetes qui a pour but de demander un fichiers
from lxml import etree #importation du module lxml qui permet de rechercher d'un fichier xml une valeur ou un texte 
import datetime #Importation du module datetime pour obtenir la date actuelle 
from time import sleep #Importation de la fonction sleep du module time dans le but d'arreter le code pendant un certain temps


for h in range(20): 
    #creation d'une boucle qui va nous permettre de faire 20 requettes 
    l=requests.get(f"https://data.montpellier3m.fr/sites/default/files/ressources/FR_MTP_OCCI.xml") 
    # l= permet de faire la demande de recuperation du fichier FR_MTP_OCCI.xml
    fname=open('FR_MTP_OCCI.txt' , "w" , encoding='utf8')
    # fname = ouvre un fichier nommé FR_MTP_OCCI qui contient le xlm a jours
    fname.write(f"{l.text}\n")
    #permet de recopier le texte de la variable l dans fname 
    fname.close()
    #ferme le fichier fname
    f2=open("FR_MTP_OCCI-result.txt","a",encoding='utf8')
    # f2 = ouvre un fichier txt nommée FR_MTP-OCCI-result.txt qui ajoute les données que nous voulons dedans et ne l'ecrase pas 
    tree = etree.parse("FR_MTP_OCCI.txt")
    # tree = parse les informations du fichiers xml en txt
    '''
    # f2.write("VOITURE\n")
    # date =str(datetime.datetime.now())
    # f2.write('Heure de la demande :')
    # f2.write(date)
    # f2.write('\n') '''
    #le programme au dessus permet d'inscrire la partie voiture , puis affiche ensuite la date de la demande et fait un retour a la ligne
    for user in tree.xpath("DateTime"):
        time=user.text
# time = correspond au temps contenu dans les balises datetime
        # f2.write('Date : ')
        f2.write(time)
        f2.write('\n')
        #Le programme au dessus permet d'inscrire dans la partie voiture la date actualiser a chaque nouveau passage dans le parking
    for user in tree.xpath("Total"):
        '''f2.write('Nombre total de place :')
        # f2.write(user.text)
        # f2.write('\n')'''
        total=int(user.text) 
# total = correspond au nombre total de place de parking 
        #ce programme permet de recuperer la partie 'total' d'un fichiers xml et de l'afficher 
    for user in tree.xpath("Free"):
        ''' f2.write('Nombre de place de libre : ')
        # f2.write(f"{user.text}\n")'''
        free=int(user.text)
# free = correspond au nombre de place libre
        #ce programme permet de recuperer la partie 'free' d'un fichiers xml et de l'afficher 
        '''pourcentfree=round((free*100)/total,2)'''
# pourcentage = correspond au place libre en pourcentage
        '''f2.write(str(pourcentfree))
        f2.write(" % de place libre \n")'''
        busy=total-free
# busy = definit les places occupées 
        busya=str(busy)
        # busya = definit les places occupées a affiché 
        '''f2.write('Nombre de place occupé : ')
        f2.write(busya)
        f2.write('\n')
        pourcentbusy=round((busy*100)/total,2)'''
# pourcentbusy = definit les places occupées a affiché en pourcentage 
        f2.write(str(pourcentbusy))
        # f2.write(" % de place occupé \n")
        f2.write('\n')
        #ce programme permet d'afficher les places occupées et le pourcentage de place occupé
    m=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml")
    # m= permet de faire la demande de recuperation du fichier TAM_MMM_VELOMAG.xml
    f3=open("FR_MTP_OCCI_VELO.txt", "w", encoding="utf8")
    # f3 = ouvre un fichier nommé FR_MTP_OCCI_VELO.txt qui contient le xlm a jours
    f3.write(f"{m.text}\n")
    #permet de recopier le texte de la variable m dans f3 
    f3.close()
    #ferme le fichier f3
    tree = etree.parse("FR_MTP_OCCI_VELO.txt")
    for si in tree.xpath("/vcs/sl/si"):
        id=si.get("id") #id correspond a la valeur id qui se trouve dans une balise si
        nam=si.get("na") #nam correspond a la valeur na qui se trouve dans une balise si
        fre=si.get("fr")#fre correspond a la valeur fr qui se trouve dans une balise si
        tot=si.get("to")#tot correspond a la valeur to qui se trouve dans une balise si
        total=int(tot) #total correspond a la valeur numerique de tot
        free=int(fre) #free correspond a la valeur numerique de fre
        date =str(datetime.datetime.now()) #date correspond a la valeur du module date time en chaine de caracteres
        if id=="036":
            '''# f2.write("VÉLO\n")
            # f2.write("l'heure :")'''
            f2.write(date)
            f2.write('\n')
            #Affiche la date du parking a vélo a chaque actualisation
            '''f2.write('le nom :')
            # f2.write(nam)
            # f2.write('\n')
            # # f2.write('le nombre de place libre :')
            # f2.write(fre)
            # f2.write('\n')
            # f2.write('le nombre de place total :')
            # f2.write(tot)
            # f2.write('\n')
            # f2.write('\n')'''
            busy1=total-free
            busy2=str(busy1)
            '''f2.write('Nombre de place occupé : ')'''
            f2.write(busy2)
            f2.write('\n')
            pourcentbusy=round((busy1*100)/total,2)
            f2.write(str(pourcentbusy))
            '''f2.write(" % de place occupé \n")'''
            f2.write('\n')
        #ce programme permet d'afficher les places occupées et le pourcentage de place occupé
            print(h)
            #ce programme permet d'afficher ou en et le programme dans les lignes de commandes
    sleep(180) #attente de  3 min entre chaque requetes
    f2.close() #ferme le fichier f2 



