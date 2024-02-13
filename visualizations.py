import json
import numpy as np

# Helper code to make graphs look better
import seaborn as sns
from cycler import cycler
import matplotlib.pyplot as plt

large = 24; medium = 20; small = 18
colors = ['#66bb6a', '#558ed5', '#dd6a63', '#dcd0ff', '#ffa726', '#8c5eff', '#f44336', '#00bcd4', '#ffc107', '#9c27b0']
text_color = "#404040"

# Update here with the color #6b6b6b for the desired elements
params = {'axes.titlesize': medium,
          'legend.fontsize': small,
          'figure.figsize': (4, 4),
          'axes.labelsize': small,
          'axes.linewidth': 2,
          'xtick.labelsize': small,
          'xtick.color': text_color,  
          'ytick.color': text_color,  
          'ytick.labelsize': small,
          'axes.edgecolor': text_color,  
          'figure.titlesize': medium,
          'axes.prop_cycle': cycler(color=colors),
          'axes.titlecolor': text_color,  
          'axes.labelcolor': text_color,  
         }

plt.rcParams.update(params)

def load_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def filter_data(data_with_santiago, data_without_santiago, crop, elements, metric_index, base_model, with_santiago):
    
    data = data_with_santiago if with_santiago == "With Santiago" else data_without_santiago
    model = "Base Model" if base_model else "Crop Model"

    crop_data = {}
    for element in elements:
        ele = []
        for run in data.keys():
            ele.append(data[run][crop][model][element][metric_index])
        crop_data[element] = ele

    return list(crop_data.values())

def get_crop_name(x):
    ['pi', 'lim', 'caf', 'ma', 'naranja', 'uva', 'nogal']
    ["Piña", "Limón", "Café", "Maiz", "Naranja", "Uva", "Nogal"]
    if x == "pi":
        return "Piña"
    elif x == "lim":
        return "Limón"
    elif x == "caf":
        return "Café"
    elif x == "ma":
        return "Maiz"
    elif x == "naranja":
        return "Naranja"
    elif x == "uva":
        return "Uva"
    elif x == "nogal":
        return "Nogal"

def get_crop_id(x):
    if x == "Piña":
        return "pi"
    elif x == "Limón":
        return "lim"
    elif x == "Café":
        return "caf"
    elif x == "Maiz":
        return "ma"
    elif x == "Naranja":
        return "naranja"
    elif x == "Uva":
        return "uva"
    elif x == "Nogal":
        return "nogal"

def get_color(element):
    elements = ['N [%]', 'P [%]', 'K [%]', 'Ca [%]', 'Mg [%]', 'Fe [mg/kg]', 'Cu [mg/kg]', 'Zn [mg/kg]', 'Mn [mg/kg]', 'B [mg/kg]']
    return colors[elements.index(element)]

def get_element_name(elements):
    return [element.split()[0] for element in elements]


def plot_data(data_with_santiago, data_without_santiago, selected_crop, nutrient_type, metric_index,
              base_model, with_santiago):  
    
    # Define macro and micro elements
    macro_elements = ['N [%]', 'P [%]', 'K [%]', 'Ca [%]', 'Mg [%]']
    macro_elements_ = ['N', 'P', 'K', 'Ca', 'Mg']
    micro_elements = ['Fe [mg/kg]', 'Cu [mg/kg]', 'Zn [mg/kg]', 'Mn [mg/kg]', 'B [mg/kg]']
    micro_elements_ = ['Fe', 'Cu', 'Zn', 'Mn', 'B']
    available_metrics = ['R2 Score', 'MAE', 'MAPE']

    font_props = {'fontsize': small, 'color': text_color}

    if nutrient_type=="All":

        # 2 subplots side-by-side
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8)) 

        # Macro Nutrients Plotting Logic
        data = filter_data(data_with_santiago, data_without_santiago, selected_crop, macro_elements, metric_index, base_model, with_santiago)
        ax1.boxplot(data, labels=macro_elements_)
        ax1.set_title(f'Macronutrients')
        ax1.set_ylabel(available_metrics[metric_index])
        ax1.grid(alpha=0.6)
        ax1.annotate('Unit: %', xy=(0.5, -0.12), xycoords='axes fraction', ha='center', va='top', **font_props)

        # Micro Nutrients Plotting Logic
        data = filter_data(data_with_santiago, data_without_santiago, selected_crop, micro_elements, metric_index, base_model, with_santiago)
        ax2.boxplot(data, labels=micro_elements_)
        ax2.set_title(f'Micronutrients')
        ax2.grid(alpha=0.6)
        ax2.annotate('Unit: mg/kg', xy=(0.5, -0.12), xycoords='axes fraction', ha='center', va='top', **font_props)

        fig.suptitle(f'All Nutrients Analysis for {get_crop_name(selected_crop)}', fontsize=large, color=text_color)
        plt.tight_layout()
        plt.show()
    
    elif nutrient_type=='Macro Nutrients':
        data = filter_data(data_with_santiago, data_without_santiago, selected_crop, macro_elements, metric_index, base_model, with_santiago)
        plt.boxplot(data, labels=macro_elements_)
        plt.ylabel(available_metrics[metric_index])
        plt.grid(alpha=0.6)
        plt.annotate('Unit: %', xy=(0.5, -0.12), xycoords='axes fraction', ha='center', va='top', **font_props)
        plt.title(f'Macro Nutrients Analysis for {get_crop_name(selected_crop)}')
        plt.tight_layout()
        plt.show()
    
    else:
        data = filter_data(data_with_santiago, data_without_santiago, selected_crop, micro_elements, metric_index, base_model, with_santiago)
        plt.boxplot(data, labels=micro_elements_)
        plt.ylabel(available_metrics[metric_index])
        plt.grid(alpha=0.6)
        plt.annotate('Unit: mg/kg', xy=(0.5, -0.12), xycoords='axes fraction', ha='center', va='top', **font_props)
        plt.title(f'Micro Nutrients Analysis for {get_crop_name(selected_crop)}')
        plt.tight_layout()
        plt.show()
