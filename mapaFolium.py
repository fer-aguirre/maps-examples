# import sys
# print(sys.executable)
# /usr/bin/python3 -m pip install folium
import folium
from folium.features import CustomIcon
import io
from PIL import Image

m = folium.Map(location=[19.43274052957381, -99.133221555212], zoom_start=16, tiles="Stamen Watercolor", attr= '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>')
# Add another layer
folium.TileLayer(tiles='Stamen Toner Labels').add_to(m)
# Custom icon image
icon_image = "assets/icons/tree.png"
icon = CustomIcon(
    icon_image,
    icon_size=(50, 50),
    icon_anchor=(20, 10),
    popup_anchor=(-3, -76),
)
# Custom tooltip message
tooltip = "¡Haz click!"
# Add markers
folium.Marker([19.435011442107704, -99.13265026035839], icon=icon, popup="<b>Parque República de Guatemala</b>", tooltip=tooltip).add_to(m)
folium.Marker([19.42982058040328, -99.13279050032122], icon=icon, popup="<b>Parque Francisco Primo De Verdad Y Ramos</b>",          tooltip=tooltip).add_to(m)
folium.Marker([19.43640005202161, -99.14397464702137], icon=icon, popup="<b>Alameda Central</b>", tooltip=tooltip).add_to(m)
folium.Marker([19.433655882695284, -99.14372922687433], icon=icon, popup="<b>Parque Santos Degollado</b>", tooltip=tooltip).add_to(m)
folium.Marker([19.426977108120735, -99.14572764812497], icon=icon, popup="<b>Parque Pujibet</b>", tooltip=tooltip).add_to(m)

# Save as 'html'
m.save("ejemplos/folium-python.html")
# Save as 'png'
img_data = m._to_png(5)
img = Image.open(io.BytesIO(img_data))
img.save('ejemplos/folium-python.png')
