import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st


def _read_hudl_export(path: str) -> pd.DataFrame:
    return pd.read_excel(path)

def display_sidebar(games: dict) -> str:
    with st.sidebar:
        selection = st.selectbox(label="Games", options=games.keys())

        if st.button("Load Dataset"):
            return _read_hudl_export(games.get(selection))


def display_momentum(games:dict) -> str:
    sorted_data = games
    def wtd_to_value(entry):
        if isinstance(entry, str):
            if entry.startswith('Y'):
                return 1
            elif entry.startswith('N'):
                return -1
        return 0

    wtd_data = sorted_data["WTD"].apply(wtd_to_value).cumsum()

    # Farben basierend auf der "ODK"-Serie
    colors = np.where(sorted_data["ODK"] == 'O', 'yellow', 'navy')

    # Balkendiagramm für "O" und "D" separat erstellen
    fig, ax = plt.subplots(figsize=(8, 4))  # Hier wird die Größe des Diagramms auf 10x8 Zoll festgelegt
    ax.bar(np.arange(len(wtd_data))[sorted_data["ODK"] == 'O'], 
        wtd_data[sorted_data["ODK"] == 'O'], 
        color='yellow', label='O')

    ax.bar(np.arange(len(wtd_data))[sorted_data["ODK"] == 'D'], 
        wtd_data[sorted_data["ODK"] == 'D'], 
        color='navy', label='D')



    # Titel und Achsenbeschriftungen hinzufügen
    ax.set_title('Momentum Progression')
    ax.set_xlabel('Plays')
    ax.set_ylabel('Momentum')

    # Benutzerdefinierte Legende hinzufügen
    ax.legend(title='ODK')
    # Horizontale Linien zeichnen
    quarter = 2
    for i, value in enumerate(sorted_data["QTR"].diff()):
        if value == 1:
            ax.axvline(i, color='white', linestyle='dashdot', linewidth=0.5, label=f"{i+1}. Quarter")
            ax.text(i, ax.get_ylim()[1]-2, f"Q{quarter}", color='white', ha='left', va='bottom')
            quarter += 1
    ax.set_facecolor('lightsteelblue')
    # Diagramm anzeigen
    # plt.show()
    st.pyplot(fig)
    return