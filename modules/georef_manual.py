import numpy as np
import pandas as pd

data_file = "Yonekura_1966//Fig4-2//georef.dat"
df = pd.read_csv(data_file)

target0 = df.loc[df["id"] == 0, ["lon", "lat"]].iloc[0].to_numpy()
target1 = df.loc[df["id"] == 1, ["lon", "lat"]].iloc[0].to_numpy()
origin0 = df.loc[df["id"] == 0, ["x", "y"]].iloc[0].to_numpy()
origin1 = df.loc[df["id"] == 1, ["x", "y"]].iloc[0].to_numpy()

scale = (target1-target0)/(origin1-origin0)
shift = target0 - origin0*scale

print(f"scale = {scale}")
print(f"shift = {shift}")
