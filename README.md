# CO2 Sammlerdruck Bestimmung

[**Zur Live-Anwendung**](https://co2sammler.streamlit.app/)

Dieses Projekt stellt ein webbasiertes Tool zur Verfügung, mit dem der **maximale absolute Sammlerstillstandsdruck** für **CO2** aus Sammlervolumen, Kältemittelfüllmenge und maximaler Umgebungstemperatur bestimmt wird. Die Berechnung basiert auf der in der hochgeladenen Python-Datei enthaltenen Logik mit **CoolProp** und der Zustandsbestimmung über Dichte und Temperatur.

## Funktionen

- Eingabe von **Gesamtem Sammlervolumen [l]**, **Kältemittelfüllmenge [kg]** und **maximaler Umgebungstemperatur [°C]**
- Berechnung der **Dichte** aus Füllmenge und Sammlervolumen
- Berechnung des **maximalen absoluten Sammlerstillstandsdrucks** für **CO2** mit **CoolProp**
- Ergebnisdarstellung in einer übersichtlichen Tabelle
- CSV-Export der Ergebnisdaten
- Zusätzliche Anleitung direkt in der Anwendung

## Berechnungslogik

Die Ausgangsdatei berechnet zuerst das Sammlervolumen in Kubikmetern und die Temperatur in Kelvin, danach die Dichte aus Masse und Volumen, und verwendet anschließend `CoolProp.PropsSI('P', 'D', d_ambient, 'T', T_amb_K, "CO2")` zur Druckbestimmung. Der ausgegebene Wert wird von Pascal in bar umgerechnet und in der Oberfläche als maximaler Sammlerstillstandsdruck angezeigt.

## Technologie

Das Projekt basiert auf:

- **Python**
- **Streamlit** für die Weboberfläche
- **CoolProp** zur Stoffwert- und Druckberechnung
- **Pandas** für die tabellarische Ergebnisdarstellung
