import streamlit as st
import pandas as pd
import os, sys
import webbrowser

# TESTING: python -m streamlit run C:\Users\leona\Documents\programming\data-science\work\technical_tests\wise_athena_tech_test\src\dashboard\app.py
path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from utils.dashboarding import StreamlitFunctions
from utils.folders import Folders

#Input data
maestro_clientes = pd.read_excel(os.path.dirname(path) + os.sep + 'data' + os.sep + 'maestro_clientes.xlsx', engine='openpyxl')
maestro_productos = pd.read_csv(os.path.dirname(path) + os.sep + 'data' + os.sep + 'maestro_productos.csv')
sellin_total = pd.read_csv(os.path.dirname(path) + os.sep + 'data' + os.sep + 'sellin-total.csv')
sellout_proveedor1 = pd.read_csv(os.path.dirname(path) + os.sep + 'data' + os.sep + 'sellout-proveedor1.csv')
sellout_proveedor2 = pd.read_csv(os.path.dirname(path) + os.sep + 'data' + os.sep + 'sellout-proveedor2.csv')

#Output Data
sellin_final = pd.read_csv(os.path.dirname(path) + os.sep + 'data' + os.sep + 'output' + os.sep + 'sellin_final.csv')
sellout_final = pd.read_csv(os.path.dirname(path) + os.sep + 'data' + os.sep + 'output' + os.sep + 'sellout_final.csv')

#StreamlitFunctions input
stream = StreamlitFunctions(maestro_clientes=maestro_clientes.sample(), maestro_productos=maestro_productos.sample(), sellin_total=sellin_total.sample(), sellout_prov1=sellout_proveedor1.sample(), sellout_prov2=sellout_proveedor2.sample(),
                            sellin_final=sellin_final.sample(), sellout_final=sellout_final.sample())

menu = st.sidebar.selectbox('Menu:',
                options=['Welcome', 'Prompt', 'Input Data', 'Data Analysis', 'Final Output',
                'Conclusion', 'About the company', 'Github Repository'])

if menu == 'Welcome':
    stream.welcome()

if menu == 'Prompt':
    stream.prompt()

if menu == 'Input Data':
    stream.data_page()

if menu == 'Data Analysis':
    stream.analysis()

if menu == 'Final Output':
    stream.final_output()

if menu == 'Conclusion':
    stream.conclusion()

if menu == 'About the company':
    stream.about_the_company()

if menu == 'Github Repository':
    stream.github_repo()
