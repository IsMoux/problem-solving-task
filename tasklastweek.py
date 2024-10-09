import datetime
from datetime import date
from calendar import monthrange


# definiton de décorateur de formater la date
def date_decorator(func):
    def format():
        result = func()      
        return  result.strftime('%Y-%m/%d')
    
    return format





#fonction pour définire le denier jour du mois actuel
def dernier_jour_mois(dateactuel :date ):

    #nomobre de jour pour le mois actuel 
    dernier_jour_du_moi = monthrange(dateactuel.year, dateactuel.month)[1]
    
    #la date du fin du mois
    date_de_dernier_jour = datetime.date(dateactuel.year, dateactuel.month, dernier_jour_du_moi)
    return date_de_dernier_jour


#appelle de décorateur 
@date_decorator
def first_day_of_last_week():

    #la date du jour actuel
    aujourdui = datetime.date.today()
    #calculer la date de fin  de mois avec la fonction dernier jour de mois
    date_de_dernier_jour=dernier_jour_mois(aujourdui)

    #calcul de premier jour de la derniére semaine
    premier_jour_dela_dernier_semaine = date_de_dernier_jour - datetime.timedelta(days=date_de_dernier_jour.weekday())
    return premier_jour_dela_dernier_semaine

#appelle de la fonction
date1 = first_day_of_last_week()
print(date1)
