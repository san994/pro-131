import pandas as pd

columns = ["row_num","star_name","distance","mass","radius","gravity"]
df = pd.read_csv("final.csv",names=columns)
del df["row_num"]

temp_mass = df["mass"].tolist()
temp_mass.pop(0)
for data in temp_mass:
    mass = float(data)*1.989e+30
    df["mass"] = mass

temp_radius = df["radius"].tolist()
temp_radius.pop(0)
for data in temp_radius:
    radius = float(data)* 6.957e+8
    df["radius"] = radius

def calculate_gravity(mass,radius):
    #g = mg/r^2
    gravity = (float(mass)*5.972e+24) / (float(radius)*float(radius)*6371000*6371000) * 6.674e-11 
    return gravity

for mass in temp_mass:
    for radius in temp_radius:
        gravity = calculate_gravity(mass,radius)
        df["gravity"] = gravity


df.to_csv("final1.csv")