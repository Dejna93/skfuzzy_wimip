import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import os

class CalcFuzzy:

    def __init__(self):
        #INPUTY
        self.buildingType= ctrl.Antecedent(np.arange(0,400,1), "Technologia budynku")
        self.wearWater = ctrl.Antecedent(np.arange(1,8,1), "Ilośc osób")
        self.sourceTermal = ctrl.Antecedent(np.arange(0,100,1),"Rodzaj źródła ciepła")
        self.zone = ctrl.Antecedent(np.arange(1,6,1), "Strefa klimatyczna")
        self.isolation = ctrl.Antecedent(np.arange(1,100,1), "Procentowa termoizolacja budynku")
        self.surface = ctrl.Antecedent(np.arange(20,300,1),"Powierzchnia grzewcza")
        #OUTPUTY
        self.typeFurnance = ctrl.Consequent(np.arange(1,50,1),"Rodzaj pieca")

        #MEMBERSHIPS FUN

        self.buildingType['starebudownictwo'] = fuzz.trapmf(self.buildingType.universe, [300, 350, 400, 400])
        self.buildingType['70-85'] = fuzz.gaussmf(self.buildingType.universe, 260, 25)
        self.buildingType['86-92'] = fuzz.gaussmf(self.buildingType.universe, 200, 20)
        self.buildingType['93-97'] = fuzz.gaussmf(self.buildingType.universe, 160, 15)
        self.buildingType['98-07'] = fuzz.gaussmf(self.buildingType.universe, 120, 15)
        self.buildingType['energooszczedny'] = fuzz.gaussmf(self.buildingType.universe, 80, 15)
        self.buildingType['niskoenegetyczny'] = fuzz.gaussmf(self.buildingType.universe, 45, 10)
        self.buildingType['pasywny'] = fuzz.trapmf(self.buildingType.universe, [0, 0, 15, 25])

        #----------------------

        self.wearWater['1 osoba'] = fuzz.gaussmf(self.wearWater.universe,50,20)
        self.wearWater['2 osoba'] = fuzz.gaussmf(self.wearWater.universe,100,30)
        self.wearWater['3 osoba'] = fuzz.gaussmf(self.wearWater.universe,150,30)
        self.wearWater['4 osoba'] = fuzz.gaussmf(self.wearWater.universe,200,40)
        self.wearWater['5 osoba'] = fuzz.gaussmf(self.wearWater.universe,250,50)
        self.wearWater['6 osoba'] = fuzz.gaussmf(self.wearWater.universe,300,60)
        self.wearWater['7 osoba'] = fuzz.gaussmf(self.wearWater.universe,350,60)
        self.wearWater['8 osoba'] = fuzz.sigmf(self.wearWater.universe,0.04 , 350)

        #----------------------

        self.zone['Strefa 1'] = fuzz.trimf(self.zone.universe, [0, 1, 1.5])
        self.zone['Strefa 2'] = fuzz.trimf(self.zone.universe, [1, 2, 2.5])
        self.zone['Strefa 3'] = fuzz.trimf(self.zone.universe, [2, 3, 3.5])
        self.zone['Strefa 4'] = fuzz.trimf(self.zone.universe, [3, 4, 4.5])
        self.zone['Strefa 5'] = fuzz.trimf(self.zone.universe, [4, 5, 5])

        #---------------------

        self.surface['kawalerka'] = fuzz.trapmf(self.surface.universe, [0, 0, 30 , 55])
        self.surface['mieszkanie'] = fuzz.trimf(self.surface.universe, [40 , 65 , 90])
        self.surface['apartament'] = fuzz.trimf(self.surface.universe, [75, 100, 130])
        self.surface['dom_jednorodzinny'] = fuzz.trimf(self.surface.universe, [100, 130,160])
        self.surface['willa'] = fuzz.trapmf(self.surface.universe, [140 , 170, 200, 200])

        #--------------------

        self.isolation['brak']  = fuzz.trapmf(self.isolation.universe, [0, 0, 5 , 10])
        self.isolation['słabo'] = fuzz.trimf(self.isolation.universe, [5, 20, 35])
        self.isolation['średnio'] = fuzz.trimf(self.isolation.universe, [25, 50, 60])
        self.isolation['dobrze'] = fuzz.trimf(self.isolation.universe, [55, 65, 80])
        self.isolation['doskonale'] = fuzz.trapmf(self.isolation.universe, [70, 90, 100, 100])







class Input:

    technologia = None
    zapotrzebowanie = None
    zrodlo = None
    strefa = None
    termoizolacja = None
    powgrzewcza = None




