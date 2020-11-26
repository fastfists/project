import pandas as pd

well_productions = pd.read_csv("well_productions/well productions.csv")

"""
Sets a proppant per stage as "ppf" defaults to the maximum weight
method can be ["min, "max", "avg"]
"""
def propant_per_stage(dataframe: pd.DataFrame, method="avg"):
    if method == "min":
        val = min(dataframe["proppant weight (lbs)"])
    elif method == "max":
        val = max(dataframe["proppant weight (lbs)"])
    elif method == "avg":
        val = dataframe["proppant weight (lbs)"].describe()["mean"]
    else:
        raise Exception(f"No method found for {method}")
    dataframe["ppf"] = val

"""
Calculates the original oil in place and places the data in
row "ooip"
"""
def original_oil_in_place(dataframe: pd.DataFrame):
    
    

"""
Sets a pump rate as "pr" defaults to the maximum weight
method can be ["min, "max", "avg"]
"""
def pump_rate(dataframe: pd.DataFrame, method="avg"):
    if method == "min":
        val = min(dataframe["pump rate (cubic feet/min)"])
    elif method == "max":
        val = max(dataframe["pump rate (cubic feet/min)"])
    elif method == "avg":
        val = dataframe["pump rate (cubic feet/min)"].describe()["mean"]
    else:
        raise Exception(f"No method found for {method}")
    dataframe["pr"] = val

def calc_production():
    print("hi")

def well_length(dataframe: pd.DataFrame):
    dataframe["well length"] = dataframe["easting"].iloc[-1] - dataframe["easting"][0]

def frac_stages(dataframe : pd.DataFrame):
    dataframe["frac stages"] = dataframe[dataframe["proppant weight (lbs)"].isna() == False].shape[0]
