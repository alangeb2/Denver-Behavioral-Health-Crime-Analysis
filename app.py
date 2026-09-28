import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Denver Neighborhood Analysis", layout="wide")

# 2. Load the Labeled Data
@st.cache_data
def load_data():
    df = pd.read_csv('clean_persona.csv')
    return df

df_personas = load_data()
df_personas = df_personas.reset_index(drop=True)

if 'zip_code' in df_personas.columns:
    df_personas['zip_code'] = df_personas['zip_code'].astype(str)

for col in df_personas.select_dtypes(include=['object']).columns:
    df_personas[col] = df_personas[col].astype(str)

# 3. Sidebar Filters
st.sidebar.header("Dashboard Controls")
st.sidebar.write("Filter the map by neighborhood persona:")

# Create a multiselect tool so users can toggle specific personas on and off
selected_personas = st.sidebar.multiselect(
    "Select Personas:",
    options=df_personas['persona'].unique(),
    default=df_personas['persona'].unique() # Select all by default
)

# Apply the filter to the dataframe
filtered_df = df_personas[df_personas['persona'].isin(selected_personas)]

# 4. Main Dashboard UI
st.title("Denver Behavioral Health & Crime Analysis")
st.markdown("This dashboard clusters Denver zip codes into distinct personas based on crime rates and available health infrastructure.")

# 5. Build the Interactive Map
if 'latitude' in filtered_df.columns and 'longitude' in filtered_df.columns:
    
    fig = px.scatter_mapbox(
        filtered_df, 
        lat="latitude",
        lon="longitude", 
        color="persona", 
        size='total_health_centers', 
        hover_name="zip_code",
        hover_data={"total_health_centers": True, "mental_health_centers": True, "latitude": False, "longitude": False},
        color_discrete_map={
            "Intervention Priority": "red",
            "Baseline": "gray",
            "Resource Hubs": "blue"
        },
        zoom=10, 
        height=600,
        mapbox_style="open-street-map" 
    )
    
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    st.plotly_chart(fig, use_container_width=True)
    
else:
    st.warning("Latitude and Longitude columns are missing. Please add 'lat' and 'lon' coordinates for each zip code to render the map.")

# 6. Display the Raw Data Table
st.subheader("Filtered Zip Code Data")
st.dataframe(filtered_df, use_container_width=True)