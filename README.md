# mapas
Ejemplos de mapas con distintas librerías y lenguajes de programación

## Mapas en Python

  * ### Ejemplo de [prettymaps](https://github.com/marceloprates/prettymaps) (Aquí más [ejemplos](https://github.com/fer-aguirre/mapas/blob/master/notebooks/ejemplosPrettymaps.ipynb))
 
  ```python
 from prettymaps import *
 import matplotlib.font_manager as fm
 from matplotlib import pyplot as plt

 # CIRCLE PLOT
 # Setup figure
 fig, ax = plt.subplots(figsize = (12, 12), constrained_layout = True)

 layers = plot(
     'CDMX, México', radius = 1100,

     ax = ax,

     layers = {
             'perimeter': {},
             'streets': {
                 'custom_filter': '["highway"~"motorway|trunk|primary|secondary|tertiary|residential|service|unclassified|pedestrian|footway"]',
                 'width': {
                     'motorway': 5,
                     'trunk': 5,
                     'primary': 4.5,
                     'secondary': 4,
                     'tertiary': 3.5,
                     'residential': 3,
                     'service': 2,
                     'unclassified': 2,
                     'pedestrian': 2,
                     'footway': 1,
                 }
             },
             'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': False},
             'water': {'tags': {'natural': ['water', 'bay']}},
             'green': {'tags': {'landuse': 'grass', 'natural': ['island', 'wood'], 'leisure': 'park'}},
             'forest': {'tags': {'landuse': 'forest'}},
             'parking': {'tags': {'amenity': 'parking', 'highway': 'pedestrian', 'man_made': 'pier'}}
         },
         drawing_kwargs = {
             'background': {'fc': '#CCD8F6', 'ec': '#dadbc1', 'hatch': 'ooo...', 'zorder': -1},
             'perimeter': {'fc': '#CCD8F6', 'ec': '#dadbc1', 'lw': 0, 'hatch': 'ooo...',  'zorder': 0},
             'green': {'fc': '#D0F1BF', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
             'forest': {'fc': '#64B96A', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
             'water': {'fc': '#a1e3ff', 'ec': '#2F3737', 'hatch': 'ooo...', 'hatch_c': '#85c9e6', 'lw': 1, 'zorder': 2},
             'parking': {'fc': '#F1E4FF', 'ec': '#003939', 'lw': 1, 'zorder': 3},
             'streets': {'fc': '#570257', 'ec': '#0F6166', 'alpha': 1, 'lw': 0, 'zorder': 3},
             'building': {'palette': ['#460379', '#FF5E5B', '#FFE290'], 'ec': '#050030', 'lw': .5, 'zorder': 4},
         },

         osm_credit = {'color': '#2F3737'}
 )

 # Set bounds
 xmin, ymin, xmax, ymax = layers['perimeter'].bounds
 dx, dy = xmax-xmin, ymax-ymin
 ax.set_xlim(xmin-.06*dx, xmax+.06*dx)
 ax.set_ylim(ymin-.06*dy, ymax+.06*dy)


 # Draw top text
 ax.text(
     xmax-.25*dx, ymax-.05*dy,
     'Zócalo,\nCDMX, México',
     color = '#2F3737',
     fontproperties = fm.FontProperties(fname = 'assets/fonts/HashedBrowns-WyJgn.ttf', size = 40)
 )
```
 
  ![Zocalo](https://github.com/fer-aguirre/mapas/blob/master/prints/zocalo.png)
  
  ### Galería:
  
  ![Bosque de Chapultepec](https://github.com/fer-aguirre/mapas/blob/master/prints/bosque-chapultepec.png)
  ![Kiosco Morisco](https://github.com/fer-aguirre/mapas/blob/master/prints/kiosco-morisco.png)


 * ### Ejemplo de [folium](https://github.com/python-visualization/folium) (Aquí más [ejemplos](https://github.com/fer-aguirre/mapas/blob/master/mapaFolium.py))

```python
import folium
from folium.features import CustomIcon

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
folium.Marker([19.42982058040328, -99.13279050032122], icon=icon, popup="<b>Parque Francisco Primo De Verdad Y Ramos</b>", tooltip=tooltip).add_to(m)
folium.Marker([19.43640005202161, -99.14397464702137], icon=icon, popup="<b>Alameda Central</b>", tooltip=tooltip).add_to(m)
folium.Marker([19.433655882695284, -99.14372922687433], icon=icon, popup="<b>Parque Santos Degollado</b>", tooltip=tooltip).add_to(m)
folium.Marker([19.426977108120735, -99.14572764812497], icon=icon, popup="<b>Parque Pujibet</b>", tooltip=tooltip).add_to(m)
```

  ![Floium](https://github.com/fer-aguirre/mapas/blob/master/prints/folium-python.png)


## Mapas en R

 * ### Ejemplo de [leaflet](https://github.com/rstudio/leaflet) (Aquí más [ejemplos](https://github.com/fer-aguirre/mapas/blob/master/mapaLeaflet.R))

```R
library(leaflet)
library(here)

# Custom icon
icon_park <- makeIcon(
  iconUrl = "assets/icons/park.png",
  iconWidth = 30, iconHeight = 40,
  iconAnchorX = 0, iconAnchorY = 0
)

m <- leaflet() %>% 
  setView( lat=19.432750647216512, lng=-99.13317863986936, zoom=14) %>%
  # Add layers
  addProviderTiles("Stamen.Toner") %>%
  # Add markers
  addMarkers(m, lat=19.435011442107704, lng=-99.13265026035839, popup="<b>Parque República de Guatemala</b>", icon=icon_park) %>%
  addMarkers(m, lat=19.42982058040328, lng=-99.13279050032122, popup="<b>Parque Francisco Primo De Verdad Y Ramos</b>", icon=icon_park) %>%
  addMarkers(m, lat=19.43640005202161, lng=-99.14397464702137, popup="<b>Alameda Central</b>", icon=icon_park) %>%
  addMarkers(m, lat=19.433655882695284, lng=-99.14372922687433, popup="<b>Parque Santos Degollado</b>", icon=icon_park) %>%
  addMarkers(m, lat=19.426977108120735, lng=-99.14572764812497, popup="<b>Parque Pujibet</b>", icon=icon_park)
```

![Leaflet-R](https://github.com/fer-aguirre/mapas/blob/master/prints/leaflet-r.png)

## Mapas en Javascript

  * ### [leaflet](https://github.com/Leaflet/Leaflet)

## Mapas en React

  * ### [leaflet](https://github.com/PaulLeCam/react-leaflet)

