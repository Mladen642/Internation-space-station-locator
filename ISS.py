import pandas as pd
import plotly.express as px

# Info about ISS location
url = "http://api.open-notify.org/iss-now.json"

# creating dataframe
df = pd.read_json(url)

# creating new columns
df["latitude"] = df.loc["latitude", "iss_position"]
df["longitude"] = df.loc["longitude", "iss_position"]
df.reset_index(inplace=True)

# formating dataframe
df = df.drop(["index", "message"], axis=1)

# plot
fig = px.scatter_geo(df, lat="latitude", lon="longitude")
fig.show()

print(df)
