# https://www.youtube.com/watch?v=Sb0A9i6d320&ab_channel=CodingIsFun

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="MDA Weekly Panel",
    page_icon = ":bar_chart:",
    layout = 'wide'
)
#---- MAIN PAGE----# 
st.title(":bar_chart: MDA Weekly Panel")
st.markdown("##")

url = (r"C:\Users\goncavic01\Electrolux\BI Brasil - Dados Internos - Documentos\General\00. TABLEAU\14. MDA - Painel Semanal\2022\week_33\bd_WeeklyPanel_MDA_W33_V06.xlsx")

df = pd.read_excel(
    url,
    engine = 'openpyxl',
    sheet_name='BDGERAL',
    #skiprows=,
    usecols= "A:Q",
    nrows= 100
)

# st.dataframe(df)

#---- SIDEBAR ----#
st.sidebar.header('FILTROS')
cliente = st.sidebar.multiselect(
    "Selecione o CLIENTE:",
    options= df["CLIENTE"].unique(),
    default= df["CLIENTE"].unique()
)

ref = st.sidebar.multiselect(
    "Selecione a REFERENCIA:",
    options= df["REFERENCIA"].unique(),
    default= df["REFERENCIA"].unique()
)

#---- Aplicando os filtros ----# 
df_selection = df.query(
    "CLIENTE == @cliente & REFERENCIA == @ref"
)
# st.dataframe(df_selection)

#---- KPIs ----# 
total_sellout = int(df_selection["SELLOUT"].sum())
total_estoque = int(df_selection["ESTOQUE"].sum())

left_col,mid_col,rig_col = st.columns(3)

with left_col:
    st.subheader("Total Sell Out")
    st.subheader(f"Sell Out : {total_sellout}")
with mid_col:
    st.subheader("Total Estoque")
    st.subheader(f"Estoque : {total_estoque}")

st.markdown("---")

st.dataframe(df_selection)



