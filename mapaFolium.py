# import sys
# print(sys.executable)
# /usr/bin/python3 -m pip install folium
import folium
from folium.features import CustomIcon
import io
from PIL import Image

m = folium.Map(location=[19.43274052957381, -99.133221555212], zoom_start=16, tiles="Stamen Watercolor", attr= '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>')
# Add new layer
folium.TileLayer(tiles='Stamen Toner Labels').add_to(m)
# Custom icon image
icon_image = "assets/icons/tree.png"
icon = folium.features.CustomIcon(
    icon_image,
    icon_size=(50, 50),
    icon_anchor=(20, 10),
    popup_anchor=(-3, -76),
)

tooltip = "¡Haz click!"

folium.Marker([19.435011442107704, -99.13265026035839], icon=icon, popup="<b>Parque República de Guatemala</b>", tooltip=tooltip).add_to(m)

folium.Marker([19.42982058040328, -99.13279050032122], icon=icon, popup="<b>Parque Francisco Primo De Verdad Y Ramos</b>", tooltip=tooltip).add_to(m)

folium.Marker([19.43640005202161, -99.14397464702137], icon=icon, popup="<b>Alameda Central</b>", tooltip=tooltip).add_to(m)

folium.Marker([19.433655882695284, -99.14372922687433], icon=icon, popup="<b>Parque Santos Degollado</b>", tooltip=tooltip).add_to(m)

folium.Marker([19.426977108120735, -99.14572764812497], icon=icon, popup="<b>Parque Pujibet</b>", tooltip=tooltip).add_to(m)

folium.Marker([19.42509245375351, -99.14246706617165], icon=icon, popup="<b>Parque Fray servando Teresa de Mier</b>", tooltip=tooltip).add_to(m)

folium.Marker([19.42429890853207, -99.14001286470138], icon=icon, popup="<b>Parque Gilberto Owen</b>", tooltip=tooltip).add_to(m)

folium.Marker([19.422711806416164, -99.12774185713113], icon=icon, popup="<b>Parque El Indio</b>", tooltip=tooltip).add_to(m)

folium.Marker([19.43504749580566, -99.11170875643528], icon=icon, popup="<b>Parque San Antonio Tomatlan</b>", tooltip=tooltip).add_to(m)

folium.Marker([19.436423469877685, -99.10921966656204], icon=icon, popup="<b>Parque Héroe de Nacozari</b>", tooltip=tooltip).add_to(m)


# Save as 'html'
m.save("ejemplos/leaflet-python.html")
# Save as 'png'
img_data = m._to_png(5)
img = Image.open(io.BytesIO(img_data))
img.save('ejemplos/cdmx-folium.png')
