import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from PIL import Image
import os, sys
import requests

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

class StreamlitFunctions:
    """
    This class contains all the necessary functions to run streamlit in app.py
    """
    def __init__(self, maestro_clientes, maestro_productos, sellin_total, sellout_prov1, sellout_prov2,
                sellin_final, sellout_final):
        self.maestro_clientes = maestro_clientes
        self.maestr_productos = maestro_productos
        self.sellin_total = sellin_total
        self.sellout_prov1 = sellout_prov1
        self.sellout_prov2 = sellout_prov2
        self.sellin_final = sellin_final
        self.sellout_final = sellout_final

    def welcome(self):
        '''
        This method returns a streamlit welcome page
        '''
        st.title('Wise Athena Technical Test')
        st.subheader('Exploratory Data Analysis by: Leonardo Sánchez')
        st.write("![wise-athena-logo](https://www.wiseathena.com/wp-content/uploads/2020/10/Wise-Athena-Logo-with-Text.png)")
        st.write('The following is a research on various datasets coming from a Wise Athena CPG (Consumer Packaged Goods) client.')
        st.write('This test consists on analyzing the data and extracting valuable insights from it.')
        st.write("The goal is to apply some data cleaning techniques in order to create a data structure accessible for the Data Science team, so they can apply their models to it.")
        st.write("To achieve it, data needs to be not only clean, but tidy and coherent.")
        st.write("The deadline date is *October 20th*")

        st.subheader("If you need to contact me, don't be afraid: \
        * Email: **leonardo.sanchezsoler@gmail.com** \
        * Linkedin: **https://www.linkedin.com/in/leonardosanchezsoler/**")
        st.subheader("Check my repo in Github: **https://github.com/leosanchezsoler/wise-athena-technical-test/**")

    
    def prompt(self):
        '''
        This function has the prompt
        '''
        st.write("# Prompt")
        st.write("## Here is what the project was all about")
        st.write("El  objetivo  es  realizar  una  limpieza  y  ajuste  de  estos  datos,  y  generar  una estructura de datos que sea fácilmente consultable por el equipo de data scientists  para  generar  sus  modelos.")
        st.write("Esto  requiere  que  los  datos  no  sólo estén  limpios,  sino  que  sean  coherentes  entre  si  y  estén  perfectamente ordenados.")
        st.write("Un  ejemplo  de  consulta  que  el  equipo  de  datascientists puede requerir es:")
        st.write("##  Necesito todos los registros de sellout y sellin entre las fechas X e Y para los productos A,B,C y D en esta lista concreta de tiendas: T1,  T2,  T3,  T4,  T5  y  T6") 
        st.write("## siendo  X,Y,  A,  B,  C,  D,  T1,  T2,  T3,  T4,  T5,  y  T6 variables.")

    def data_page(self):
        '''
        This template returns a page with info about the data
        '''
        st.title('Input Data')
        st.write("Here's a sample of the data our client sent to us:")
        droplist = st.sidebar.selectbox("Select the dataset",
                    options=['Maestro Clientes', 'Maestro Productos',
                    'Sellin Total', 'Sellout prov1', 'Sellout prov2'])

        if droplist == 'Maestro Clientes':
            st.dataframe(self.maestro_clientes)
        
        if droplist == 'Maestro Productos':
            st.dataframe(self.maestro_productos)
        if droplist == 'Sellin Total':
            st.dataframe(self.sellin_total)
        if droplist == 'Sellout prov1':
            st.dataframe(self.sellout_prov1)
        if droplist == 'Sellout prov2':
            st.dataframe(self.sellout_prov2)
        if droplist == 'maestro_clientes':
            st.dataframe(self.maestro_clientes)


    def analysis(self):
        '''
        This method returns a page with information about the data analysis process.
        '''
        st.write("# Exploratory Data Analysis (EDA)")
        st.subheader("Overview")
        st.write("""
        Our data consists on:
 * A master or product catalogue (`maestro_productos.csv`)
    - Contains all available info about the products sold by the client and its competitors.
    
* A master or clients catalogue (`maestro_clientes.xlsx`)
    - Contains all available info about stores and distributors that sell their products.

* Sellout files for 2 different suppliers (`sellout-proveedor1.csv` & `sellout-proveedor2.csv`)
    - Contains sales and sellout price for each product and store

* Sellin file (`sellin.csv`)
    - Contains sales and sellin price (from fabricant to retailer) for each product and store.
        """)

        st.write("## Data Cleaning")
        st.write("""
        Before extracting insights from the data, it is mandatory to take a look at it's structure and check if there are some rare values, as well as missing values or wrong data types assigned to a specific column.

In this stage, every single dataset will be analyzed in order to fix them. The process will be very similar for each of them.
        """)

        st.write("```maestro_clientes, maestro_productos, sellin_total, sellout_prov1, sellout_prov2```")

        st.write("#### Data Merging")
        st.write("""

#### After cleaning the data, we now have an overview of what it looks like and have a glimpse of the relations that can be established between the datasets.

* Some columns seem to be suitable for merging and joining our data:
    * `Dates`
    * `skus`
    * `proveedores`

* It is also interesting to create new columns based on numeric data:
    * `prices` 
    * `pieces`


####  Let's find a way in which data can be combined. By doing this, we would be able to have a wider scope when looking for worthy insights

_PS: Before merging data, our data analyst spent some hours trying to get valuable info from each dataset separately. It was after realising that the conclusions were not satisfactory enough, that he changed his mind._
        """)

    st.write("**Sellout Data**")
    st.write("""
        It is surprising that all the data related to the stores that sell our products is divided in only 2 suppliers(`cadena` column):
    * `proveedor_1`
    * `proveedor_2`

    So it is appropiate to merge it with our sellout data, which is also divided in 2 suppliers:
    * `sellout_prov1`
    * `sellout_prov2`

    This will link the historic sales registry with further description of our clients. By doing these, we will be able to see which stores ordered more units in the last few years.

    #### To achieve this, we will take the following steps:
    - divide `maestro_client` in two datasets filtered by each supplier
    - rename the necessary columns to merge datasets
    - merge each resulting dataset with their sellout dataset
        - we could merge them by store_id
    - subtract each dataset length to know how many observations didn't match properly
    - check for duplicates or strange values (mispelling, wrong registries...)
    - report any relevant issue in order to ask the client for more information
        """)

    st.write("""
    Now our historic sellout data is combined with information about our clients.
    As we mentioned above, it is also possible to combine this data with `maestro_products` due to the fact that they both have a sku column
    """)
    st.write("""
    Merge it with `maestro_productos`
    """)

    st.write("**Sellin Data**")
    st.write("""
        #### Now it's time to apply the same methodology to the Sellin Data. 

    At this point, we are getting a huge grasp of our data and begin to understand interrelations between datasets

    Once again, `sku` and `store_id` columns are suitable for merging.

    We've dealt with `maestro_clientes` & `maestro_productos` idiosincrasy before, so we can merge it without inspecting it again.
        """)

    st.write("""
        #### Very interesting insight and another issue to report to our client.
    - Supplier 1 only has registries in 2017
    - Supplier 2 only has registries in 2016


    - Sellin total info has registries since 2015

    #### With this data, we cannot compare how both suppliers performed during the same year, but we can track each supplier separately and compare them with sellin_total

    #### We will remove data from 2015 because it does not provide info about our suppliers

    #### Now we realised that the missing data from merging comes from this lack of years information
        """)
    
    st.write("### TIME TO MERGE IT")

    st.write("## Data Analysis")
    st.write("""
    
    After having our data merged, we need to find insights from our resulting data.

    On the previous stage, we noticed some issues that should be reported to our client:
    - after merging, very little observations did not merge successfully
    - very few values were below or equal to zero

    Now is when we are going to see why these things are happening.

    First things first:
    - We are going to tidy our dataset by:
        - changing column's names 
        - changing column's order


    - Later on:
        - Check our historic of sales to determine our date ranges
        - Check values' distribution to see if there are some outliers that could unbalance our data


    - Finally:
        - Add some columns based on numeric data
        """)

    st.write("## Data Visualization")
    st.write("""
        ### Once our data is structured, it's time to make some data viz to get a consistent sense of it.

    #### Although some columns may seem obvious, here are some definitions of the ones that can be misleading:
    - `grade`: Is related with the Areas in which AC Nielsen divides the country of Mexico.
        - These areas are divided based on economic criteria.
        - For further detail: check this [url](https://docplayer.es/18341200-Consumo-del-nivel-socioeconomico-bajo-nielsen-homescan.html)
        - The `documentation` directory has 2 maps of the area distribution.
        """)

    st.write("#### Sellin Visualizations")
    st.write("""
        #### Time to analyse sellin data. In this stage, we will do some visualizations:
    - Heatmap to see correlations between variables.
    - Treemaps:
        - A treemap to see the total amount of sellin units per category.
        - A treemap to see the total units sold to each supplier.
    - A sunburst to see the total amount of units sold per Nielsen Area.
    - Bar plots
        - A Bar plot to see the states that sell the most.
        - Total Sell-in unit Margin per Nielsen Area
    - A histogram to see the total sellin margin revenue per Nielsen Area.
    - Violin plot o see how unit prices are distributed
        """)

    st.write("#### Sellout Visualizations")
    st.write("""
        #### For the sellout data, we will make very similar visualizations.
    - Heatmap to see correlations between variables.
    - Treemaps:
        - A treemap to see the total amount of sellin units per category.
        - A treemap to see the total units sold to each supplier.
    - A sunburst to see the total amount of units sold per Nielsen Area.
    - Bar plots
        - A Bar plot to see the states that sell the most.
        - Total Sell-in unit Margin per Nielsen Area
    - A histogram to see the total sellin margin revenue per Nielsen Area.
    - Violin plot o see how unit prices are distributed
        """)

    def data_viz(self):
        '''
        This method returns a page with all data visualizations
        '''
        droplist = st.sidebar.selectbox('Choose Dataset',
                        options=['Sell-in Data', 'Sell-out Data'])
        
        if droplist == 'Sell-in Data':
            st.title('SELL-IN DATA')
            st.write("### HTML charts")
            sellin_tot_margin_revenue_per_NA = open(os.path.dirname(path) + os.sep + 'reports' + os.sep + 'html' + os.sep + 'sellin_tot_margin_revenue_per_NA.html', 'r', encoding='utf-8')
            source_code = sellin_tot_margin_revenue_per_NA.read() 
            components.html(source_code, height=500, width=1500)

            tot_sellin_units_per_cat = open(os.path.dirname(path) + os.sep + 'reports' + os.sep + 'html' + os.sep + 'tot_sellin_units_per_cat.html', 'r', encoding='utf-8')
            source_code1 = tot_sellin_units_per_cat.read() 
            components.html(source_code1, height=500, width=1500)

            tot_sellin_units_per_nielsen_area = open(os.path.dirname(path) + os.sep + 'reports' + os.sep + 'html' + os.sep + 'tot_sellin_units_per_nielsen_area.html', 'r', encoding='utf-8')
            source_code2 = tot_sellin_units_per_nielsen_area.read() 
            components.html(source_code2, height=500, width=1500)
            
            tot_sellin_margin_per_NA = open(os.path.dirname(path) + os.sep + 'reports' + os.sep + 'html' + os.sep + 'tot_sellin_units_sold_to_suppliers.html', 'r', encoding='utf-8')
            source_code3 = tot_sellin_margin_per_NA.read() 
            components.html(source_code3, height=500, width=1500)

            total_sellin_revenue_per_state = open(os.path.dirname(path) + os.sep + 'reports' + os.sep + 'html' + os.sep + 'total_sellin_revenue_per_state.html', 'r', encoding='utf-8')
            source_code4 = total_sellin_revenue_per_state.read() 
            components.html(source_code4, height=500, width=1500)
            st.write("### Static charts")
            sellin_heatmap = Image.open(os.path.dirname(path) + os.sep + 'reports' + os.sep + 'static' + os.sep + 'sellin_heatmap.png')
            sellin_price_distribution = Image.open(os.path.dirname(path) + os.sep + 'reports' + os.sep + 'static' + os.sep + 'sellin_price_distribution.png')

            st.image(sellin_heatmap, use_column_width='auto')
            st.image(sellin_price_distribution, use_column_width='auto')
        
        if droplist == 'Sell-out Data':

            st.title("SELL-OUT DATA")
            st.write("### HTML charts")
            tot_sellout_units_per_cat = open(os.path.dirname(path) + os.sep + 'reports' + os.sep + 'html' + os.sep + 'tot_sellout_units_per_cat.html', 'r', encoding='utf-8')
            source_code5 = tot_sellout_units_per_cat.read() 
            components.html(source_code5, height=500, width=1500)
            tot_sellout_units_per_nielsen_area = open(os.path.dirname(path) + os.sep + 'reports' + os.sep + 'html' + os.sep + 'tot_sellout_units_per_nielsen_area.html', 'r', encoding='utf-8')
            source_code6 = tot_sellout_units_per_nielsen_area.read() 
            components.html(source_code6, height=500, width=1500)
            tot_sellout_units_sold_to_suppliers = open(os.path.dirname(path) + os.sep + 'reports' + os.sep + 'html' + os.sep + 'tot_sellout_units_sold_to_suppliers.html', 'r', encoding='utf-8')
            source_code7 = tot_sellout_units_per_nielsen_area.read() 
            components.html(source_code7, height=500, width=1500)            
            total_sellout_revenue_per_state = open(os.path.dirname(path) + os.sep + 'reports' + os.sep + 'html' + os.sep + 'total_sellout_revenue_per_state.html', 'r', encoding='utf-8')
            source_code8 = total_sellout_revenue_per_state.read() 
            components.html(source_code8, height=500, width=1500)  
            st.write("### Static charts")

            sellout_heatmap = Image.open(os.path.dirname(path) + os.sep + 'reports' + os.sep + 'static' + os.sep + 'sellout_heatmap.png')
            sellout_price_distribution = Image.open(os.path.dirname(path) + os.sep + 'reports' + os.sep + 'static' + os.sep +'sellout_price_distribution.png')

            st.image(sellout_heatmap, use_column_width='auto')
            st.image(sellout_price_distribution, use_column_width='auto')


    def final_output(self):
        '''
        This method returns a template with the final output data
        '''
        st.title('Output Data')
        st.write("Here's a sample of the data we finally created")
        droplist = st.sidebar.selectbox("Select the dataset",
                    options=['Sellin Final', 'Sellout Final'])

        if droplist == 'Sellin Final':
            st.dataframe(self.sellin_final)
        if droplist == 'Sellout Final':
            st.dataframe(self.sellout_final)

    def conclusion(self):
        st.write("# Conclusion")
        st.write("## About the Data:")
        st.write('To sum up, there are some issues concerning the data that should be highlighted.')
        st.write("### **On the first place, the datatypes weren't, in most cases, the desired ones.**")
        st.write("  - From the Data Analysis team, we should suggest other data collection tool or structure in order to avoid some incompatibilities and time consumption doing repetitive tasks.")

        st.write("### **We should also ask our client about registries that belong to 2015.**")
        st.write("    - We found some issues merging our sellin data with `maestro productos` and `maestro clientes`.")
        st.write("    - In particular, the sellin dataset does not have extra information about suppliers that bought their products")
        
        st.write(" ### **Consistent amount of outliers in both final datasets**")
        st.write("    - There are not a small degree of observations that were classified as outliers due to the fact they exceeded the 'normal' distribution.")
        st.write("    - We should have an appointment with our client to gather more information about this data and see if we can do something with it.")

        st.write("### **Some observations with 0 or less units/prices**")
        st.write("- There were some sales with 0 or negative units/prices assigned to them. This may seem irrelevant at first sight, but in the long term could result in serious trouble for our client. We should ask about what happened in that particular cases")


        st.write("## Further Steps")
        st.write("### **After dealing with this sales data, we suggest our team to store it in a relational database that can be acessed easier by some SaaS or SQL queries.**")
        st.write("### **The pipeline for this particular task can be optimised. By doing this, the time spent dealing with incompatibilities would have been significantly shorter.**")
        st.write("### **Once the analysis and data preparation is done for our client, from the Data Analysis team we suggest Data Science Department the following:**")
        st.write("- Drop id related columns.")
        st.write("- Apply units, price and margin tresholds to get a better performance of our model.")
        st.write("- Try vectorization in columns like division, state or other categorical columns.")

        
    def about_the_company(self):
        '''
        This method returns a template about the company
        '''
        st.title('About Wise Athena')
        st.subheader("Wise Athena are on a mission to help CPG companies to optimize their pricing and promotion strategies through A.I., thereby achieving the increase in sales and margin")
        st.video("https://www.youtube.com/watch?v=z-4jYNXwWs0&t=4s")
        st.subheader("Mission")
        st.write('Our mission is to use AI to help CPG companies make faster and more precise decisions.')
        st.subheader('Vision')
        st.write("Our vision for enterprises is to create an easier and more accessible way to navigate difficult business strategies.")
        st.subheader("Shaking up the CPG industry.")
        st.write("Wise Athena is an Artificial Intelligence pricing and trade prediction agent. We let CPG companies of any size securely access and optimize margin and volume.")
        st.write("Freeing millions of workers from ceaselessly repetitive tasks in a job that has not changed in decades, seven years ago we built WA’s artificial technology from scratch to shake up the industry.")
        st.write("Our unique algorithm analyzes thousands of sales data and immediately predicts the best pricing strategies starting with fast, accurate access, that automatically retains your latest data. From this, you can share scenarios with your team while you work from any place in the world.")
        st.subheader("Values")
        st.write("- Open\
        - Bold\
        - Love")
        url = "https://www.wiseathena.com/"
        st.write("Check out our website [link](%s)" % url)

   
    def github_repo(self):
        '''
        This function provides a link to the github repository
        '''
        st.write("# Github repository")
        st.write("## Check out the full project in my github Repo")
        url = "https://github.com/leosanchezsoler/wise_athena_tech_test"
        st.write("Check out this [link](%s)" % url)

    def end(self):
        '''
        This function shows the end of the streamlit page
        '''
        st.title("That's all, folks!")
        st.video("https://www.youtube.com/watch?v=b9434BoGkNQ")