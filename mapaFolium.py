# import sys
# print(sys.executable)
# /usr/bin/python3 -m pip install folium

import folium
from folium.features import CustomIcon

m = folium.Map(location=[19.43274052957381, -99.133221555212], zoom_start=12, tiles="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png", attr= '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>')

url = "http://leafletjs.com/examples/custom-icons/{}".format
icon_image = url("leaf-red.png")
shadow_image = url("leaf-shadow.png")

icon = CustomIcon(
    icon_image,
    icon_size=(38, 95),
    icon_anchor=(22, 94),
    shadow_image=shadow_image,
    shadow_size=(50, 64),
    shadow_anchor=(4, 62),
    popup_anchor=(-3, -76)
    )


tooltip = "Click me!"

folium.Marker([19.435814905084374, -99.13233435292825], popup="<i>Librería Nely</i>", tooltip=tooltip).add_to(m)
folium.Marker([19.4358958446759, -99.13158333443202], popup="<b>Librería Porrúa</b>", tooltip=tooltip).add_to(m)
m.save("output/index.html")
