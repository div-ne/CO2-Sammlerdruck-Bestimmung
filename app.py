import pandas as pd
import streamlit as st
import CoolProp.CoolProp as cp

APP_TITLE = "CO2-Sammlerdruck-Bestimmung"
APP_VERSION = "0.1.0V"
STREAMLIT_URL = "https://co2sammler.streamlit.app/"
GITHUB_URL = "https://github.com/div-ne/CO2-Sammlerdruck-Bestimmung"

st.set_page_config(page_title=APP_TITLE, layout="wide")


def calculate_pressure(volume_l, mass_kg, ambient_temp_c):
    volume_m3 = volume_l / 1e3
    ambient_temp_k = ambient_temp_c + 273.15
    density = mass_kg / volume_m3
    pressure_pa = cp.PropsSI("P", "D", density, "T", ambient_temp_k, "CO2")
    pressure_bar = pressure_pa / 1e5
    result_text = (
        f"Der maximale absolute Druck bei gegebenem Sammlervolumen von V = {volume_l:.2f} l "
        f"und gegebener Kältemittelfüllmenge m = {mass_kg:.2f} kg beträgt {pressure_bar:.2f} bar "
        f"bei T = {ambient_temp_c:.2f} °C."
    )
    result_table = pd.DataFrame(
        [
            ("Sammlervolumen [l]", round(volume_l, 2)),
            ("Kältemittelfüllmenge [kg]", round(mass_kg, 2)),
            ("Umgebungstemperatur [°C]", round(ambient_temp_c, 2)),
            ("Dichte [kg/m³]", round(density, 2)),
            ("Maximaler Sammlerstillstandsdruck [bar(abs)]", round(pressure_bar, 2)),
        ],
        columns=["Parameter", "Wert"],
    )
    return result_table, result_text


st.markdown(
    f"""
    <div style='display:flex; align-items:baseline; gap:14px; flex-wrap:wrap; margin-bottom:0.2rem;'>
        <div style='font-size:3rem; font-weight:700; line-height:1.1;'>{APP_TITLE}</div>
        <div style='color:#9ca3af; font-size:1rem; line-height:1.1;'>{APP_VERSION}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("Bestimmung des maximalen absoluten Sammlerstillstandsdrucks für CO2 aus Volumen, Füllmenge und maximaler Umgebungstemperatur.")

left, right = st.columns([1, 1.2])

with left:
    volume_l = st.number_input("Gesamtes Sammlervolumen [l]", min_value=0.01, value=10.0, step=0.1)
    mass_kg = st.number_input("Kältemittelfüllmenge [kg]", min_value=0.01, value=5.0, step=0.1)
    ambient_temp_c = st.number_input("Maximale Umgebungstemperatur [°C]", value=40.0, step=0.1)
    run = st.button("Berechnen", use_container_width=True)

with right:
    st.subheader("Ergebnis")
    if run:
        try:
            result_df, result_text = calculate_pressure(float(volume_l), float(mass_kg), float(ambient_temp_c))
            st.dataframe(result_df, use_container_width=True, hide_index=True)
            st.download_button(
                label="CSV herunterladen",
                data=result_df.to_csv(index=False, sep=";").encode("utf-8"),
                file_name="co2-sammlerdruck-ergebnis.csv",
                mime="text/csv",
                use_container_width=True,
            )
            with st.expander("Textausgabe"):
                st.write(result_text)
        except Exception as e:
            st.error(f"Fehler bei der Berechnung: {e}")
    else:
        st.info("Eingaben setzen und auf Berechnen klicken.")

st.markdown("---")
with st.expander("Anleitung"):
    st.markdown(
        f"""
Mit diesem Tool wird der **maximale absolute Sammlerstillstandsdruck** für **CO2** berechnet.

Dafür gibst du ein:
- **Gesamtes Sammlervolumen [l]**,
- **Kältemittelfüllmenge [kg]**,
- **maximale Umgebungstemperatur [°C]**.

Aus diesen Eingaben wird zunächst die **Dichte** des Kältemittels im Sammler bestimmt. Anschließend wird mit **CoolProp** der zugehörige absolute Druck für CO2 berechnet.

Die Ergebnisanzeige enthält die wichtigsten Eingangs- und Ergebnisgrößen in Tabellenform. Zusätzlich kann die Ausgabe als **CSV-Datei** heruntergeladen werden.

Live-App:
[{STREAMLIT_URL}]({STREAMLIT_URL})

Repository:
[{GITHUB_URL}]({GITHUB_URL})
"""
    )
