# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
import numpy as np
import streamlit as st
from streamlit_echarts import st_echarts
import json
from streamlit_folium import folium_static

import folium as fl
import pickle
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.preprocessing import RobustScaler
import warnings

# a method to load data
@st.cache(persist= True)



##########the method below is used to draw a guage to show crime rate.
#It is called later in the program#####

def draw_guage():
    option = {
    "tooltip": {
        "formatter": '{a} <br/>{b} : {c}%'
    },
    "series": [{
        "name": 'SF',
        "type": 'gauge',
        "startAngle": 180,
        "endAngle": 0,
        "progress": {
            "show": "true"
        },
        "radius": '100%',

        "itemStyle": {
            "color": '#58D9F9',
            "shadowColor": 'rgba(0,138,255,0.45)',
            "shadowBlur": 10,
            "shadowOffsetX": 2,
            "shadowOffsetY": 2,
            "radius": '55%',
        },
        "progress": {
            "show": "true",
            "roundCap": "true",
            "width": 15
        },
        "pointer": {
            "length": '60%',
            "width": 8,
            "offsetCenter": [0, '5%']
        },
        "detail": {
            "valueAnimation": "true",
            "formatter": '{value}%',
            "backgroundColor": '#58D9F9',
            "borderColor": '#999',
            "borderWidth": 4,
            "width": '60%',
            "lineHeight": 20,
            "height": 20,
            "borderRadius": 188,
            "offsetCenter": [0, '40%'],
            "valueAnimation": "true",
        },
        "data": [{
            "value": 70.34,
            "name": "RATE OF CRIME IN SF"
        }]
    }]
};

    st_echarts(options=option, key="1")
@st.cache(suppress_st_warning=True)
def get_coordinates(selectedRegion):
        df = pd.read_csv("df45.csv", low_memory = False)
        df["Month"] = pd.DatetimeIndex(df["Dates"]).month
        df["Year"] = pd.DatetimeIndex(df["Dates"]).year
        df["Day"] = pd.DatetimeIndex(df["Dates"]).day
        df["Hour"] = pd.DatetimeIndex(df["Dates"]).hour
        df= df.query("Year>= 2012")

        if regions== "BAYVIEW":
            dQueries = df.query("PdDistrict=='BAYVIEW'")
            f = dQueries.X.max()
            t = dQueries.X.min()
            b = dQueries.Y.max()
            c = dQueries.Y.min()
            xt = np.random.uniform(t, f)
            yt = np.random.uniform(c, b)
            return xt, yt
        elif regions== "CENTRAL":
            dQueries = df.query("PdDistrict=='CENTRAL'")
            f = dQueries.X.max()
            t = dQueries.X.min()
            b = dQueries.Y.max()
            c = dQueries.Y.min()
            xt = np.random.uniform(t, f)
            yt = np.random.uniform(c, b)
            return xt, yt

        elif regions== "INGLESIDE":
            dQueries = df.query("PdDistrict=='INGLESIDE'")
            f = dQueries.X.max()
            t = dQueries.X.min()
            b = dQueries.Y.max()
            c = dQueries.Y.min()
            xt = np.random.uniform(t, f)
            yt = np.random.uniform(c, b)
            return xt, yt

        elif regions == "MISSION":
            dQueries = df.query("PdDistrict=='MISSION'")
            f = dQueries.X.max()
            t = dQueries.X.min()
            b = dQueries.Y.max()
            c = dQueries.Y.min()
            xt = np.random.uniform(t, f)
            yt = np.random.uniform(c, b)
            return xt, yt
        elif regions == "NORTHERN":
            dQueries = df.query("PdDistrict=='NORTHERN'")
            f = dQueries.X.max()
            t = dQueries.X.min()
            b = dQueries.Y.max()
            c = dQueries.Y.min()
            xt = np.random.uniform(t, f)
            yt = np.random.uniform(c, b)
            return xt, yt
        elif regions == "PARK":
            dQueries = df.query("PdDistrict=='PARK'")
            f = dQueries.X.max()
            t = dQueries.X.min()
            b = dQueries.Y.max()
            c = dQueries.Y.min()
            xt = np.random.uniform(t, f)
            yt = np.random.uniform(c, b)
            return xt, yt
        elif regions == "RICHMOND":
            dQueries = df.query("PdDistrict=='RICHMOND'")
            f = dQueries.X.max()
            t = dQueries.X.min()
            b = dQueries.Y.max()
            c = dQueries.Y.min()
            xt = np.random.uniform(t, f)
            yt = np.random.uniform(c, b)
            return xt, yt
        elif regions== "SOUTHERN":
            dQueries = df.query("PdDistrict=='SOUTHERN'")
            f = dQueries.X.max()
            t = dQueries.X.min()
            b = dQueries.Y.max()
            c = dQueries.Y.min()
            xt = np.random.uniform(t, f)
            yt = np.random.uniform(c, b)
            return xt, yt
        elif regions == "TARAVAL":
            dQueries = df.query("PdDistrict=='TARAVAL'")
            f = dQueries.X.max()
            t = dQueries.X.min()
            b = dQueries.Y.max()
            c = dQueries.Y.min()
            xt = np.random.uniform(t, f)
            yt = np.random.uniform(c, b)
            return xt, yt
        else:
            dQueries = df.query("PdDistrict=='TENDERLOIN'")
            f = dQueries.X.max()
            t = dQueries.X.min()
            b = dQueries.Y.max()
            c = dQueries.Y.min()
            xt = np.random.uniform(t, f)
            yt = np.random.uniform(c, b)
            return xt, yt

#side bar
warnings.filterwarnings("ignore")
st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_title="CRIME ANALYSIS")

dt= st.sidebar.write("WELCOME!!!!!Choose an action from below")

menu= ["Analysis", "Predict"]
selection= st.sidebar.selectbox("Select Action--(Analysis or Prediction)", menu)

select= st.sidebar.file_uploader("Upload New File", type=["csv", "xlsx"])


with st.container():
    st.title("Crime Analysis and Prediction App")
    #st.subheader('"Crime  be tamed if anticipitated"~ (Derrick et al., 2022)')
    st.write("A San-Francisco Case")
    data = pd.read_csv("df4.csv")
    #st.checkbox("Show dataFrame")


with st.container():
    with open("model1_pickle", "rb") as file:
        groups = pickle.load(file)

    with open("rs_pickle", "rb") as file:
        rs = pickle.load(file)

if selection == "Analysis":
    data = pd.read_csv("df4.csv")
    data1 = pd.read_csv("https://data.sfgov.org/resource/wg3w-h783.csv", low_memory= False)
    #df = pd.read_csv("train.csv", low_memory=False)

    with st.container():
        st.subheader("Choose analysis type below:")
        choice = st.radio("Make Visualizations on:",
                        ("Maps", "Data", "Districts","Time-based Visualizations", "Crime-Types"))


        if choice == "Maps":
            with st.container():
                st.title("Maps")

                geo_file = open("Districts.geojson")
                open_geoFile = json.load(geo_file)

                sf_map = fl.Map(location=[37.7749, -122.4194],
                                zoom_start=12.3,
                                )
                folium_static(sf_map)

                st.subheader("**A choropleth Map for Crime Distribution**")
                sf_map.choropleth(
                    geo_data=open_geoFile,
                    data=data,
                    columns=["PdDistrict", "Number"],
                    # threshold_scale = bins,
                    key_on='feature.properties.district',
                    fill_color='YlOrRd',
                    fill_opacity=0.7,
                    line_opacity=0.2,
                    legend_name='San Francisco Crime Incidents')

                folium_static(sf_map)

                for i in range(0, len(data)):
                    fl.Marker(
                        location=[data.iloc[i]['y'], data.iloc[i]['x']],
                        popup=data.iloc[i][["Number"]],
                        icon=fl.DivIcon(
                            html=f"""<div style="font-family: Fantasy; font-weight:20px;font-size: 20px;color: blue">{data.iloc[i]['Number'], data.iloc[i]["PdDistrict"]}</div>""")
                    ).add_to(sf_map)

                folium_static(sf_map)

        elif choice== "Data":
            with st.container():
                st.title("Data")
  
                datashow = pd.read_csv("https://data.sfgov.org/resource/wg3w-h783.csv", low_memory=False)
                datashow
                
        elif choice == "Districts":
            with st.container():
                # load_data()

                fig, ax = plt.subplots(1, squeeze=True, sharey="row", sharex="col")

                dist = data1["police_district"].value_counts()

                st.write("A pie chart for crime distribution by Districts")
                #explode = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
                ax.pie(dist, labels=dist.index)
                #years = df["Year"].value_counts()
                st.pyplot(fig)
        elif choice== "Crime-Types":
            data1= pd.read_csv("https://data.sfgov.org/resource/wg3w-h783.csv")
            st.title("Crime-Types")
            data2= pd.read_csv("https://data.sfgov.org/resource/tmnf-yvry.csv")
            #fig, ax = plt.subplots(1, squeeze=True, sharey="row", sharex="col")
            #plt.figure(figsize=(12, 10))

            st.write("Distribution of Crime-Types: Scroll down")

            #fig4= plt.bar(data=df, x=y4, y=x4)
            #x4= df["Category"].value_counts()
            #y4= df["Category"].value_counts().index
            x7= data1["incident_category"].value_counts()
            y7= data1["incident_category"].value_counts().index
            fig6= px.bar(df,x=x7, y=y7)
            fig6.update_layout(width = 900, height=600)
            fig6.update_layout(xaxis= dict(title= "Number of Occurrences"),
                               yaxis= dict(title= "Crime category"))
            fig6.update_layout(title= dict(text= "Crime Categories Distribution",
                                           font=dict(family="Gravity One", color="blue", size=26)))

            st.plotly_chart(fig6)

            #with st.container():

                #st.pyplot(fig)
        elif choice== "Time-based Visualizations":
            st.title("Time-based Visualizations")
            #data2= pd.read_csv("https://data.sfgov.org/resource/tmnf-yvry.csv")
            data1["Year"] = pd.DatetimeIndex(data1["incident_datetime"]).year
            data1 = data1.query("Year<= 2022")
            data1["Month"] = pd.DatetimeIndex(data1["incident_datetime"]).month
            #data1["Day"] = pd.DatetimeIndex(data1["Dates"]).day
            data1["Hour"] = pd.DatetimeIndex(data1["incident_datetime"]).hour

            with st.container():
                time_select_menu = ["Months", "DayofWeek", "Years"]
                time_selection = st.selectbox("Select period:", time_select_menu)

                if time_selection == "Months":
                    #data1 = data1.query("Year==2018")
                    data3= pd.read_csv("df45.csv")
                    #data3["Month"] = pd.DatetimeIndex(data3["Dates]).month
                    x2 = data3["Month"].value_counts().index
                    y2 = data3["Month"].value_counts()

                    fig1 = go.Figure()
                    fig1.add_trace(go.Bar(x=x2, y=y2, marker=dict(color="orange")))
                    # fig1.add_trace(go.Line(x=x2, y=y2)

                    fig1.update_layout(paper_bgcolor="black")
                    fig1.update_layout(plot_bgcolor="grey", width=800, height=500)
                    fig1.update_layout(title=dict(text="Crime Distribution By Months",
                                                  font=dict(family="Mono spaced", color="crimson", size=26)))
                    fig1.update_layout(xaxis=dict(title="Months", ticklen=5, color= "white",zeroline=False),
                                       yaxis=dict(title="Crimes", ticklen=5, color= "white"))
                    st.plotly_chart(fig1)

                elif time_selection == "Years":
                    x1 = data1["incident_year"].value_counts().index
                    y1 = data1["incident_year"].value_counts()
                    fig = go.Figure()
                    fig.add_trace(go.Bar(x=x1, y=y1, marker=dict(color="rgba(174,19,236,0.8)")))
                    fig.update_layout(paper_bgcolor="cyan")
                    fig.update_layout(plot_bgcolor="grey", width=800, height=500)
                    fig.update_layout(title=dict(text="Crime Distribution By Years",
                                                 font=dict(family="Gravity One", color="crimson", size=26)))
                    fig.update_layout(xaxis=dict(title="Years", ticklen=5, zeroline=False),
                                      yaxis=dict(title="Crimes", ticklen=5))
                    st.plotly_chart(fig)

                elif time_selection == "DayofWeek":

                    x5 = data1["incident_day_of_week"].value_counts().index
                    y5 = data1["incident_day_of_week"].value_counts()

                    fig4= go.Figure()
                    fig4.add_trace(go.Bar(x=x5, y=y5, marker=dict(color="rgba(200,19,236,0.8)")))
                    fig4.update_layout(paper_bgcolor="cyan")
                    fig4.update_layout(plot_bgcolor="grey", width=800, height=500)
                    fig4.update_layout(title=dict(text="Crime Distribution By Days of the Week",
                                                 font=dict(family="Gravity One", color="crimson", size=26)))
                    fig4.update_layout(xaxis=dict(title="Days", ticklen=5, zeroline=False),
                                      yaxis=dict(title="Crimes", ticklen=5))
                    st.plotly_chart(fig4)





            #st.line_chart(df["Year"].value_counts())

    #draw_guage()


elif selection == "Predict":

        st.markdown("**Make Predictions on the Rate of crime--> "
                    "(click on PREDICT button)**")
        with st.container():
            left_col, right_col = st.columns(2)
            right_col.title("Results:")
            # month= left_col.selectbox(range(1,12))
            # left_col.button("Press")
        n = range(1, 13)
        months = left_col.selectbox("Select month",n )

        Year_menu= [2023, 2024, 2025, 2026, 2027]
        Year= left_col.selectbox("Select year", Year_menu)

        hour_range= range(0,25)
        hours= left_col.selectbox("Select Hour", hour_range)

        days_range= range(1,31)
        Day= left_col.selectbox("Select Day of Month", days_range)

        regions_data= data.PdDistrict
        regions = left_col.selectbox("Select District", regions_data)
        
        d=get_coordinates(regions)
        st.write(d)
#with st.container():

        c1=d[0]
        c2=d[1]


        categories= [[c1, c2,months, Year, Day, hours]]


        scaling= rs.transform(categories)
        pred= groups.predict(scaling)
#st.write(pred.item())
        def predictions():
            if pred.item() == 2:
            
                right_col.title("VERY HIGH rate of Crime expected")
            elif pred.item() == 1:
                right_col.title("MODERATE rate of Crime expected")
            else:
                right_col.title("LOW rate of Crime expected")
    #break
        if st.button("PREDICT"):
            predictions()
        else:
            right_col.title("Select Inputs")


        draw_guage()
        


#@st.cache(persist=True)




#regions= data.PdDistrict


