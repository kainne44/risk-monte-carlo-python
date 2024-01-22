# Intent is to create a monte carlo sim of risks based on their assessed
# likelihood and consequence

"""
IMPORTS
"""
import yaml
import xlrd
import pandas as pd
import random

"""
FUNCTIONS
"""
# Random event generator
# generates a random number
# Compares to probability parameter passed from risk
# If the rng is less than or equal to the probability, the event occurs


def eventGen(probability, consequence):
    rng = int(random.Random())
    if rng <= probability:
        return consequence
    else:
        return 0


"""
INPUTS
"""
# Get excel file and sheet name from YAML
with open(r'config.yaml') as file:
    configDict = yaml.load(file, Loader=yaml.FullLoader)

# Read in Excel sheet of risks
fileName = configDict['inputFileName']
sheetName = configDict['inputSheetName']
rawRiskDF = pd.read_excel(fileName, sheet_name=sheetName)

riskDict = rawRiskDF.to_dict('records')

# convert likelihoods to range between 0 and 1
for risk in riskDict:
    if risk['Likelihood'] == 1:
        risk['Likelihood'] = configDict['likelihoodConfig'][1]
    elif risk['Likelihood'] == 2:
        risk['Likelihood'] = configDict['likelihoodConfig'][2]
    elif risk['Likelihood'] == 3:
        risk['Likelihood'] = configDict['likelihoodConfig'][3]
    elif risk['Likelihood'] == 4:
        risk['Likelihood'] = configDict['likelihoodConfig'][4]
    elif risk['Likelihood'] == 5:
        risk['Likelihood'] = configDict['likelihoodConfig'][5]
    else:
        print('There was an input problem -- check input file')

# generate a set of random risk events
runResults = []
for risk in riskDict:
    runResults.append(eventGen(risk['Likelihood'], risk['Consequence']))
