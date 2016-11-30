import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import os
# New Antecedent/Consequent objects hold universe variables and membership
# functions
buildingType = ctrl.Antecedent(np.arange(15,400,5) , 'Typ budynku')

quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

"""

"""
buildingType['starebudownictwo'] = fuzz.trapmf(buildingType.universe,[ 300,350,400,400])
buildingType['70-85'] = fuzz.gaussmf(buildingType.universe, 260, 15)
buildingType['86-92'] = fuzz.gaussmf(buildingType.universe, 200, 15)
buildingType['93-97'] = fuzz.gaussmf(buildingType.universe,160,15 )
buildingType['98-07'] = fuzz.gaussmf(buildingType.universe, 120,15)
buildingType['energooszczedny'] = fuzz.gaussmf(buildingType.universe, 80,15)
buildingType['niskoenegetyczny'] =  fuzz.gaussmf(buildingType.universe, 45,15)
buildingType['pasywny'] =  fuzz.trapmf(buildingType.universe, [0,0,15,25])

buildingType['70-85'].view()


os.system("pause")