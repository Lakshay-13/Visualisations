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
          'figure.figsize': (8, 8),
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

def filter_data(data_with_santiago, data_without_santiago, crop, elements, metrics,base_model, with_santiago):
    if with_santiago:
        data = data_with_santiago
    else:
        data = data_without_santiago
    if base_model:
        model = "Base Model"
    else:
        model = "Crop Model"
    # cro = {}
    crop_data = {}
    for element in elements:
        ele = []
        for metric in metrics:
            ele.append(data[crop][model][element][metric])
        crop_data[element] = ele
    # cro[crop] = crop_data
    
    return crop, crop_data

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

def plot_data(crop,crop_data, xlabels):
    
    crop_name, elements_data = crop, crop_data
    for i, metric in enumerate(xlabels):
        values = [float(elements_data[element_name][i].split(' ± ')[0]) for element_name in elements_data]
        stds = [float(elements_data[element_name][i].split(' ± ')[1]) for element_name in elements_data]
        plt.errorbar(elements_data.keys(), values, yerr=stds, fmt='o', label=metric)
    plt.xticks(rotation=45)
    plt.title(f'Elements Analysis for {get_crop_name(crop_name)}')
    plt.xlabel('Element(s)')
    plt.ylabel('Values')

    plt.grid(alpha=0.6)
    plt.legend(loc='upper center', bbox_to_anchor=(1.2, 0.5), ncol=1)
    plt.show()
