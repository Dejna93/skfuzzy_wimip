import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import os


class CalcFuzzy:
    def __init__(self):
        # INPUTY
        self.buildingType = ctrl.Antecedent(np.arange(0, 400, 1), "Technologia budynku")
        self.wearWater = ctrl.Antecedent(np.arange(0, 500, 0.1), "Zuzycie wody na osobe")

        self.zone = ctrl.Antecedent(np.arange(15, 25, 0.01), "Strefa klimatyczna")
        self.isolation = ctrl.Antecedent(np.arange(1, 100, 1), "Procentowa termoizolacja budynku")
        self.surface = ctrl.Antecedent(np.arange(20, 150, 0.01), "Powierzchnia grzewcza")
        # OUTPUTY
        self.typeFurnance = ctrl.Consequent(np.arange(1, 100, 1), "Rodzaj pieca")

        # MEMBERSHIPS FUN

        self.buildingType['starebudownictwo'] = fuzz.trapmf(self.buildingType.universe, [170, 350, 400, 400])
        self.buildingType['70-85'] = fuzz.gaussmf(self.buildingType.universe, 260, 25)
        self.buildingType['86-92'] = fuzz.gaussmf(self.buildingType.universe, 200, 20)
        self.buildingType['93-97'] = fuzz.gaussmf(self.buildingType.universe, 160, 15)
        self.buildingType['98-07'] = fuzz.gaussmf(self.buildingType.universe, 120, 15)
        self.buildingType['energooszczedny'] = fuzz.gaussmf(self.buildingType.universe, 80, 15)
        self.buildingType['niskoenegetyczny'] = fuzz.gaussmf(self.buildingType.universe, 45, 10)
        self.buildingType['pasywny'] = fuzz.trapmf(self.buildingType.universe, [0, 0, 15, 100])

        # ----------------------

        self.wearWater['1 osoba'] = fuzz.zmf(self.wearWater.universe, 20, 80)
        self.wearWater['2 osoba'] = fuzz.gaussmf(self.wearWater.universe, 100, 30)
        self.wearWater['3 osoba'] = fuzz.gaussmf(self.wearWater.universe, 150, 30)
        self.wearWater['4 osoba'] = fuzz.gaussmf(self.wearWater.universe, 200, 40)
        self.wearWater['5 osoba'] = fuzz.gaussmf(self.wearWater.universe, 250, 50)
        self.wearWater['6 osoba'] = fuzz.gaussmf(self.wearWater.universe, 300, 60)
        self.wearWater['7 osoba'] = fuzz.gaussmf(self.wearWater.universe, 350, 60)
        self.wearWater['8 osoba'] = fuzz.smf(self.wearWater.universe, 310, 470)

        # ----------------------

        self.zone['Strefa 1'] = fuzz.gaussmf(self.zone.universe, 16, 0.5)
        self.zone['Strefa 2'] = fuzz.gaussmf(self.zone.universe, 18, 0.9)
        self.zone['Strefa 3'] = fuzz.gaussmf(self.zone.universe, 20, 1.5)
        self.zone['Strefa 4'] = fuzz.gaussmf(self.zone.universe, 22, 1.2)
        self.zone['Strefa 5'] = fuzz.gaussmf(self.zone.universe, 24, 0.45)

        # ---------------------

        self.surface['kawalerka'] = fuzz.zmf(self.surface.universe, 25, 65)
        self.surface['mieszkanie'] = fuzz.gaussmf(self.surface.universe, 75, 30)
        self.surface['apartament'] = fuzz.gaussmf(self.surface.universe, 111, 8)
        self.surface['dom_jednorodzinny'] = fuzz.gaussmf(self.surface.universe, 130, 3.5)
        self.surface['willa'] = fuzz.smf(self.surface.universe, 130, 150)

        # --------------------

        self.isolation['brak'] = fuzz.zmf(self.isolation.universe, 5, 15)
        self.isolation['slabo'] = fuzz.gaussmf(self.isolation.universe, 20, 7)
        self.isolation['srednio'] = fuzz.gaussmf(self.isolation.universe, 50, 20)
        self.isolation['dobrze'] = fuzz.gaussmf(self.isolation.universe, 70, 10)
        self.isolation['doskonale'] = fuzz.smf(self.isolation.universe, 75, 95)

        self.typeFurnance['weglowy'] = fuzz.zmf(self.typeFurnance.universe, 4, 40)
        self.typeFurnance['gazowy'] = fuzz.gbellmf(self.typeFurnance.universe, 23, 2.5, 50)
        self.typeFurnance['pompa ciepla'] = fuzz.smf(self.typeFurnance.universe, 70, 100)

        # -----------------------
        # RULES
        rules = [

            ctrl.Rule(self.buildingType['pasywny'] & self.wearWater['4 osoba'] & self.surface['dom_jednorodzinny'] &
                      self.isolation['doskonale'], self.typeFurnance['pompa ciepla']),
            ctrl.Rule(self.buildingType['starebudownictwo'] & self.wearWater['8 osoba'] & self.isolation['brak'] &
                      self.surface['dom_jednorodzinny'],
                      self.typeFurnance['weglowy']),
            ctrl.Rule(self.buildingType['starebudownictwo'] & self.wearWater['7 osoba'] & self.isolation['slabo'] &
                      self.surface['dom_jednorodzinny'],
                      self.typeFurnance['weglowy']),
            ctrl.Rule(self.buildingType['starebudownictwo'] & self.wearWater['6 osoba'] & self.isolation['slabo'] &
                      self.surface['dom_jednorodzinny'],
                      self.typeFurnance['weglowy']),

            ctrl.Rule(self.buildingType['70-85'] & self.wearWater['6 osoba'] & self.isolation['slabo'] & self.surface[
                'dom_jednorodzinny'],
                      self.typeFurnance['weglowy']),

            ctrl.Rule(self.buildingType['niskoenegetyczny'] & self.wearWater['5 osoba'] & self.isolation['dobrze'] &
                      self.surface['dom_jednorodzinny'] | self.surface['willa'], self.typeFurnance['pompa ciepla']),

            ctrl.Rule(self.buildingType['energooszczedny'] & self.wearWater['5 osoba'] & self.isolation['dobrze'] &
                      self.surface['dom_jednorodzinny'] | self.surface['willa'], self.typeFurnance['pompa ciepla']),

            ctrl.Rule(self.buildingType['energooszczedny'] & self.wearWater['4 osoba'] & self.isolation['dobrze'] &
                      self.surface['dom_jednorodzinny'] | self.surface['willa'], self.typeFurnance['pompa ciepla']),

            ctrl.Rule(self.buildingType['niskoenegetyczny'] & self.wearWater['5 osoba'] & self.isolation['dobrze'] &
                      self.surface['dom_jednorodzinny'] | self.surface['willa'], self.typeFurnance['pompa ciepla']),

            ctrl.Rule(self.buildingType['93-97'] & self.wearWater['2 osoba'] & self.isolation['srednio'] & self.surface[
                'kawalerka'], self.typeFurnance['gazowy']),

            ctrl.Rule(self.buildingType['93-97'] & self.wearWater['3 osoba'] & self.isolation['srednio'] & self.surface[
                'mieszkanie'], self.typeFurnance['gazowy']),

            ctrl.Rule(self.buildingType['93-97'] & self.wearWater['4 osoba'] & self.isolation['srednio'] & self.surface[
                'mieszkanie'], self.typeFurnance['gazowy']),

            ctrl.Rule(self.buildingType['98-07'] & self.wearWater['2 osoba'] & self.isolation['srednio'] & self.surface[
                'kawalerka'], self.typeFurnance['gazowy']),
            ctrl.Rule(self.buildingType['98-07'] & self.wearWater['3 osoba'] & self.isolation['srednio'] & self.surface[
                'mieszkanie'], self.typeFurnance['gazowy']),
            ctrl.Rule(self.buildingType['98-07'] & self.wearWater['4 osoba'] & self.isolation['srednio'] & self.surface[
                'mieszkanie'], self.typeFurnance['gazowy']),
            ctrl.Rule(self.buildingType['98-07'] & self.wearWater['5 osoba'] & self.isolation['srednio'] & self.surface[
                'apartament'], self.typeFurnance['gazowy']),
        ]

        # Controll System
        self.typeControl = ctrl.ControlSystem(rules)

        self.type = ctrl.ControlSystemSimulation(self.typeControl)

    def viewBuildingType(self):
        self.buildingType.view()

    def viewWearWater(self):
        self.wearWater.view()

    def viewZone(self):
        self.zone.view()

    def viewSurface(self):
        self.surface.view()

    def viewIsolation(self):
        self.isolation.view()

    def viewType(self):
        self.typeFurnance.view()

    def set_input(self, name, value):
        self.type.input[name] = value

    def set_inputs(self, building_type, wear_water, zone, surface, isolation):
        self.type.input['buildingType'] = int(building_type)

        self.type.input['wearWater'] = int(wear_water)

        self.type.input['zone'] = int(zone)

        self.type.input['surface'] = int(surface)

        self.type.input['isolation'] = int(isolation)

    def compute(self):
        self.type.compute()
        print(self.type.output['Rodzaj pieca'])
        self.typeFurnance.view(sim=self.type)

    def show_output(self):
        self.typeFurnance.view()
