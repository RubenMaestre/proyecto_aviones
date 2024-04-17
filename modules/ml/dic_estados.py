import pandas as pd
import streamlit as st

def estados_en_espanol():
    estados = {
        'TX': 'Texas', 'OH': 'Ohio', 'GA': 'Georgia', 'MS': 'Misisipi',
        'FL': 'Florida', 'NC': 'Carolina del Norte', 'ND': 'Dakota del Norte',
        'PA': 'Pensilvania', 'MO': 'Misuri', 'AK': 'Alaska', 'HI': 'Hawái',
        'MI': 'Míchigan', 'MT': 'Montana', 'NE': 'Nebraska', 'NJ': 'Nueva Jersey',
        'TN': 'Tennessee', 'WI': 'Wisconsin', 'LA': 'Luisiana', 'WY': 'Wyoming',
        'NV': 'Nevada', 'OK': 'Oklahoma', 'WV': 'Virginia Occidental',
        'ID': 'Idaho', 'KY': 'Kentucky', 'KS': 'Kansas', 'AR': 'Arkansas',
        'CA': 'California', 'CO': 'Colorado', 'NH': 'Nuevo Hampshire',
        'IA': 'Iowa', 'OR': 'Oregón', 'MN': 'Minnesota', 'UT': 'Utah',
        'AL': 'Alabama', 'IL': 'Illinois', 'SC': 'Carolina del Sur',
        'NY': 'Nueva York', 'VA': 'Virginia', 'MD': 'Maryland', 'TT': 'Territorios No Incorporados a USA',
        'WA': 'Washington', 'AZ': 'Arizona', 'SD': 'Dakota del Sur',
        'PR': 'Puerto Rico', 'ME': 'Maine', 'RI': 'Rhode Island', 'NM': 'Nuevo México',
        'IN': 'Indiana', 'DC': 'Distrito de Columbia', 'DE': 'Delaware',
        'MA': 'Massachusetts', 'VT': 'Vermont', 'VI': 'Islas Vírgenes', 'CT': 'Connecticut'
    }
    return estados
