import pandas as pd
import streamlit as st
import plotly.express as px

table = pd.read_csv("../private-data/data/processed/test_2.csv")

st.set_page_config(layout="wide")

players = table.player.unique()
features = table.feature.unique()

feature_labels = [i.replace("_", " ").title() for i in features]
feature_dict = dict(zip(feature_labels, features))

st.set_page_config(layout="wide")

st.title("Trackman what does good look like?")

feature_label = st.sidebar.selectbox("Select Feature: ", feature_labels)
feature = feature_dict[feature_label]

player_1 = st.sidebar.selectbox("Select Player: ", players)
st.write("Looking at {feat} for {player} ".format(feat=feature_label, player=player_1))

df_plot = table[(table["player"] == player_1) & (table["feature"] == feature)].copy()
df_plot = df_plot[["good", "bad"]].melt(value_name=feature)

fig = px.histogram(df_plot, x=feature, color="variable", barmode="overlay")

st.plotly_chart(fig, use_container_width=True)


# st.set_page_config(layout="wide")
# df = pd.DataFrame(px.data.gapminder())
# st.header("National Statistics")
# page = st.sidebar.selectbox("Select page", ["Country data", "Continent data"])
# if page == "Country data":
#     ## Countries
#     clist = df["country"].unique()
#     country = st.selectbox("Select a country:", clist)
#     col1, col2 = st.columns(2)
#     fig = px.line(
#         df[df["country"] == country], x="year", y="gdpPercap", title="GDP per Capita"
#     )

#     col1.plotly_chart(fig, use_container_width=True)
#     fig = px.line(
#         df[df["country"] == country], x="year", y="pop", title="Population Growth"
#     )

#     col2.plotly_chart(fig, use_container_width=True)
