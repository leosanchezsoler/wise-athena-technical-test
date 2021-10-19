# Imports
import seaborn as sns
import matplotlib.pyplot as plt 
from matplotlib import RcParams, rcParams
import plotly_express as px
import squarify
import plotly

#Config data viz params 
sns.set_style("white")
sns.set_context('notebook')
sns.set_style("ticks")
sns.set(rc={"figure.dpi":300, "savefig.dpi": 300})


class Viz:
    
    """
    This class is used to build all kinds of charts
    """
    @staticmethod
    def draw_treemap(df, path, color, values, title, filename, html_path, save=False):
        '''
        This function draws a colormap based on numeric data.
        It is used to represent to see the data hierarchy
        Parameters: 
            - df: a pandas Dataframe.
            - path: a list with the hierarchy that will be represented.
            - color: the value that will assign the color
            - values: the values that will be structured
            - title: plot title
            - filename: the filename to save it
            - html_path: the directory in which the plot will be saved in html
            - save: a bool. If true, it will save the plot in both html and .png DEFAULT(False)
        ''' 
        doc_name = html_path + filename + '.html'
        fig = px.treemap(
        df,
        path= path,
        color=color,
        values=values,
        title=title,
        color_continuous_scale=["#F1EAD8", "#7393A8", "#2F374F"]
    )

        fig.update_layout(
                        title_font_size=36,
                        title_font_family='Helvetica',
        )

        if save:
            plotly.offline.plot(fig, filename=doc_name)
            
        fig.show()

    @staticmethod
    def draw_sunburst(df, path, color, values, title, html_path, save=False, filename=None):
        '''
        This function draws a colormap based on numeric data.
        It is used to represent to see the data hierarchy
        Parameters: 
            - df: a pandas Dataframe.
            - path: a list with the hierarchy that will be represented.
            - color: the value that will assign the color
            - values: the values that will be structured
            - title: plot title
            - filename: the filename to save it
            - html_path: the directory in which the plot will be saved in html
            - save: a bool. If true, it will save the plot in both html and .png DEFAULT(False)
        ''' 
        doc_name = html_path + filename + '.html'
        fig = px.sunburst(
        df,
        path= path,
        color=color,
        values=values,
        title=title,
        color_continuous_scale=["#F1EAD8", "#7393A8", "#2F374F"]
    )

        fig.update_layout(
                        title_font_size=36,
                        title_font_family='Helvetica',
        )

        if save:
            plotly.offline.plot(fig, filename=doc_name)
            
        fig.show()

    @staticmethod
    def draw_heatmap(df_corr, title, path, filename=None, save=False, ):
        '''
        This function draws a seaborn heatmap
        Parameters:
            - df: a pandas DataFrame with corr() method
            - title: the plot title
            - path
            - save: if True, will save the plot
        ''' 
        plt.figure(figsize=(15, 15))
        fig = sns.heatmap(df_corr,
        center=0,
        square= True,
        linewidths = .3,
        robust=True,
        cmap=sns.cm.mako_r
        )

        
        fig.set_title(title, fontdict= {'fontsize': 24, 'fontweight': 'bold'}, y=1.1);

        if save:
            doc_name = path + filename + '.png'
            plt.savefig(doc_name)

    @staticmethod
    def draw_barplot(df, x, y, title, path, filename=None, save=False):
        '''
        this function draws a barplot
        Parameters:
            - df: a pandas DataFrame
            - x: x axis
            - y: y axis
            - title: chart title
            - path
            - filename: name of the file. DEFAULT()
            - save: if True, saves the plot
        '''

        fig = px.bar(
            df,
            x=x, 
            y=y, 
            title=title
        )

        fig.update_layout(
                        title_font_size=36,
                        title_font_family='<b>Helvetica</b>',
                        font=dict(
                            family='Helvetica',
                            size=12
                        )

        )
        
        fig.update_traces(
        marker_color= '#2F374F'
        )

        if save:
            doc_name = path + filename + '.html'

            plotly.offline.plot(fig, filename=doc_name)

        fig.show()

    @staticmethod
    def draw_histogram(df, x, y, title, filename=None, path=None, save=False):
        '''
        This function draws a histogram
        Parameters:
            - df: a pandas Dataframe
            - x: x axis
            - y: y axis
            - title: the plot title.
            - filename: the name of the file
            - path: the path where it will be saved
            - save: if true, will save the plot 
        '''
        fig = px.histogram(
            df, 
            x=x, 
            y=y,
            title=title
        )

        fig.update_layout(
            title_font_size=36,
            title_font_family='<b>Helvetica</b>',
            font=dict(
                family='Helvetica',
                size=12
            )
        )

        fig.update_traces(
            marker_color= '#ABD0C9'
            )

        if save:
            doc_name = path + filename + '.html'

            plotly.offline.plot(fig, filename=doc_name)

        fig.show()

    @staticmethod
    def draw_violinplot(df, col, title, path=None, filename=None, save=False):
        '''
        This function draws a violinplot
        Parameters:
            - df: a pandas Dataframe
            - col: the column of the dataframe
            - title: the plot title
            - path
            - filename: the name of the file
            - save: if True, will save the file. DEFAULT False
        '''
        plt.figure(figsize=(10, 5))
        fig = sns.violinplot(df[col],
        linewidths = .3,
        robust=True,
        cmap=sns.cm.mako_r
        )
        fig.set_title(title, fontdict= {'fontsize': 24, 'fontweight': 'bold'}, y=1);


        if save:
            doc_name = path + filename + '.png'
            plt.savefig(doc_name)
