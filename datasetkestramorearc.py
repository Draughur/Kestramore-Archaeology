
import pandas as pd
print("Pandas is ready!")

#gather some simple data from kestramore
#focus on the elven ruins in morias and ruin roads

elven_ruins = ["Elven Gardens, Pyrgos, Propylon, Moon Ring, The Ampitheater"]
ages = ["~1500BW, ~200BW, ~5BW, ~1000-2000BW, ~1000-2000BW"] #age should be under the kestran calender in this case BW
materials = ["Clay/Stone, Mudbrick/Red-terracota, Mudbrick/Red-terracota/Stone, Stone, Stone"]
locations = ["Castle Mori, Ruined Roads, Ruined Roads, Island, Smoke Valley"]
types = ["Ylvari, Ylvari, Ylvari, Moon-Elf, Moon Elf"]

# Step 2: Create a dictionary for the dataframe
data = {
    "Elven Ruins": elven_ruins,
    "Age": ages,
    "Material": materials,
    "Location": locations,
    "Type": types
}

df = pd.DataFrame(data)
print(df)