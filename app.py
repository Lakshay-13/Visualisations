import streamlit as st
from visualizations import *

st.set_option('deprecation.showPyplotGlobalUse', False)

# Paths to your JSON files
path_with_santiago = r'Results/results_with_santiago_january_2024.json'
path_without_santiago = r'Results/results_without_santiago_january_2024.json'

# Load JSON data
data_with_santiago = load_json_data(path_with_santiago)
data_without_santiago = load_json_data(path_without_santiago)

# Define the Streamlit UI components
st.title('Crop Elements Analysis')

available_metrics = ['R2 Score', 'MAE', 'MAPE']

c1, c2, c3, c4 = st.columns(4)

with c1:
    # Selection for Santiago
    with_santiago = st.radio('Select Data Type', ('With Santiago', 'Without Santiago'))

with c2:
    # Nutrient type selection
    nutrient_type = st.radio("Select Nutrient Type", ['All', 'Macro Nutrients', 'Micro Nutrients'])

with c3:
    # Selecting between base model and crop model
    model_type = st.radio('Model Type', ('Base Model', 'Crop Model'))

with c4:
    selected_metric = st.radio('Select Metric', available_metrics)

# Assuming you have a function to get a list of available crops and elements from your dataset
available_crops = ["Limón", "Café", "Maiz", "Naranja", "Uva", "Nogal"]  # This should be dynamically generated from your data
selected_crop = get_crop_id(st.selectbox('Select Crops', available_crops))

metric_index =available_metrics.index(selected_metric)

# Placeholder for your plotting function, adjust as necessary
if st.button('Plot Data'):
    st.pyplot(plot_data(data_with_santiago, data_without_santiago, selected_crop, nutrient_type, metric_index,
                            True if model_type=='Base Model' else False, with_santiago))