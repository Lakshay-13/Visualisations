import streamlit as st
from visualizations import *

st.set_option('deprecation.showPyplotGlobalUse', False)

# Paths to your JSON files
path_with_santiago = 'compiled_with_santiago_january_2024.json'
path_without_santiago = 'compiled_without_santiago_january_2024.json'

# Load JSON data
data_with_santiago = load_json_data(path_with_santiago)
data_without_santiago = load_json_data(path_without_santiago)

# Define the Streamlit UI components
st.title('Crop Elements Analysis')

# Selection for Santiago
with_santiago = st.radio('Select Data Type', ('With Santiago', 'Without Santiago'))

# Assuming you have a function to get a list of available crops and elements from your dataset
available_crops = ["Piña", "Limón", "Café", "Maiz", "Naranja", "Uva", "Nogal"]  # This should be dynamically generated from your data
selected_crops = st.multiselect('Select Crops', available_crops)
crops = [get_crop_id(i) for i in selected_crops]

available_elements = ['N [%]', 'P [%]', 'K [%]', 'Ca [%]', 'Mg [%]', 'Fe [mg/kg]', 'Cu [mg/kg]', 'Zn [mg/kg]', 'Mn [mg/kg]', 'B [mg/kg]']  # This should also be dynamic
elements = st.multiselect('Select Elements', available_elements)

available_metrics = ['$R^2 Score$', 'MAE', 'MAPE']
selected_metrics = st.multiselect('Select Elements', available_metrics)
metrics = [available_metrics.index(i) for i in selected_metrics]

# Selecting between base model and crop model
model_type = st.radio('Model Type', ('Base Model', 'Crop Model'))

# Assuming you have a separate function to filter data based on selected options
# This is a placeholder for whatever data filtering logic you need
filtered_data = filter_data(data_with_santiago, data_without_santiago, crops, elements, metrics,
                            True if model_type=='Base Model' else False, with_santiago)  # Filter your data based on selected options

# Placeholder for your plotting function, adjust as necessary
if st.button('Plot Data'):
    st.pyplot(plot_data(filtered_data, selected_metrics))