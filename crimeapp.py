



import pandas as pd
import numpy as np
import streamlit as st
from streamlit_echarts import st_echarts
#import plotly.graph_objects as go
#from PIL import Image
import streamlit.components.v1 as components
#import plotly.express as px
import json
from streamlit_folium import folium_static
import folium as fl
import pickle
#import matplotlib.pyplot as plt
from sklearn.preprocessing import RobustScaler
import warnings

@st.cache(persist= True)
def load_data():
    df = pd.read_csv("df45.csv", low_memory=False)
    return df
# the method below is used to draw a guage to show crime rate.
#It is called later in the program

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

warnings.filterwarnings("ignore")
st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_title="CRIME ANALYSIS")



with st.container():
    st.title("Crime Analysis and Prediction App")
    st.subheader('"Crime  be tamed if anticipitated"~ (Derrick et al., 2022)')
    st.write("A San-Francisco Case")
    data = pd.read_csv("df4.csv")
    #st.checkbox("Show dataFrame")
    with st.container():
        if st.checkbox("Show a compressed dataFrame"):

            data = pd.read_csv("df4.csv")
            data
        else:
            st.empty()
    #general map
with st.container():
    with open("model1_pickle", "rb") as file:
        groups = pickle.load(file)

    #with open("rs_pickle", "rb") as file:
        #rs = pickle.load(file)
    #rs= RobustScaler()

    #df = pd.read_csv("df45.csv")
    #df["Month"] = pd.DatetimeIndex(df["Dates"]).month
    #df["Year"] = pd.DatetimeIndex(df["Dates"]).year
    #df["Day"] = pd.DatetimeIndex(df["Dates"]).day
    #df["Hour"] = pd.DatetimeIndex(df["Dates"]).hour


    #df
dt= st.sidebar.write("WELCOME!!!!!Choose an action from below")

menu= ["Analysis", "Predict"]
selection= st.sidebar.selectbox("Select Action--(Analysis or Prediction)", menu)

select= st.sidebar.file_uploader("Upload New File", type=["csv", "xlsx"])

if selection== "Analysis":
    st.title("Scroll Down to View Analysis")
    container1= st.container()

    data= pd.read_csv("df4.csv")

    with container1:

        st.markdown("**A choropleth Map for Crime Distribution in SF**")
        geo_file = open("Districts.geojson")
        open_geoFile = json.load(geo_file)

        sf_map = fl.Map(location=[37.7749, -122.4194],
                    zoom_start=12.3,
                    )
    # bins = [8699, 12648, 16597, 20546, 24495, 28445]

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
                html=f"""<div style="font-family: Fantasy; font-weight:20px;font-size: 20px;color: green">{data.iloc[i]['Number'], data.iloc[i]["PdDistrict"]}</div>""")
                    ).add_to(sf_map)

        folium_static(sf_map)
    with st.container():
        draw_guage()

    container2= st.container()
    col1, col2 = st.columns(2)

    with container2:
        #load_data()
        df = pd.read_csv("df45.csv", low_memory=False)

        #fig, ax= plt.subplots(1, squeeze= True, sharey = "row", sharex= "col")

        dist = df["PdDistrict"].value_counts()
        with col1:
            st.write("A pie chart for crime distribution by Districts")
            explode =[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
            ax.pie(dist, labels = dist.index, explode= explode)
            years = df["Year"].value_counts()
            #ax[0][1].plot(years.index,years)
            #plt.show()
            st.pyplot(fig)
            #st.plotly_chart(fig, sharing="streamlit", use_container_width=True)



            #plt.pie(dist, labels = dist.index, explode= explode)

        with col2:
            st.write("Crime Distribution by Years")
            st.line_chart(years)

    with st.container():
        left_side, right_side = st.columns(2)


        with left_side:
            st.write("Crime Distribution by Months")
            months = df["Month"].value_counts()
            st.bar_chart(months)

        with right_side:
            st.write("Crime Distribution by DayofWeek")

            st.bar_chart(df["DayOfWeek"].value_counts())

elif selection=="Predict":

    st.markdown("**Make Predictions on the Rate of crime**")
    with st.container():

        left_col, right_col= st.columns(2)
        right_col.title("Results:")
        #month= left_col.selectbox(range(1,12))
        #left_col.button("Press")

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


#@st.cache(persist=True)
@st.cache(suppress_st_warning=True)
def get_coordinates(ss):
        df = pd.read_csv("train.csv", low_memory = False)
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


d=get_coordinates(regions)
st.write(d)
with st.container():
    draw_guage()
c1=d[0]
c2=d[1]


categories= [[c1, c2,months, Year, Day, hours]]


scaling= rs.transform(categories)
pred= groups.predict(scaling)
st.write(pred.item())
if pred.item()==2:
      right_col.title("VERY HIGH rate of Crime expected")
elif pred.item()==1:
    right_col.title("MODERATE rate of Crime expected")
else:
    right_col.title("LOW rate of Crime expected")


