# Maps examples 🌎

Maps examples using folium and prettymaps modules in Python.

## Contents

- [folium](#folium)
- [prettymaps](#prettymaps)

---

## [folium](https://github.com/python-visualization/folium)

```python3
# Folium
import folium
import pandas as pd
from folium import plugins
from folium.features import CustomIcon, FeatureGroup

# Load data
wifi_pilares = pd.read_csv('../data/wifi_gratuito_en_pilares.csv', encoding = 'latin-1')
wifi_sitiospublicos = pd.read_csv('../data/wifi_gratuito_en_sitios_publicos.csv', encoding = 'latin-1')

m = folium.Map(location=[19.43274052957381, -99.133221555212], zoom_start=10, tiles=None)

# Add layer 
folium.TileLayer(tiles="CartoDB Positron", name="Free Wi-Fi Hotspots in Mexico City", attr= '''
            &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> 
            contributors &copy; <a href="https://carto.com/attributions">CARTO</a>''').add_to(m)

# Add a group
pilares = FeatureGroup(name="Pilares")
pilares.add_to(m)
sitiospublicos = FeatureGroup(name="Sitios Públicos")
sitiospublicos.add_to(m)

# Add the option to switch layers
folium.LayerControl('topright', collapsed= False).add_to(m)

# Add fullscreen option
plugins.Fullscreen(
    position="topright",
    title="Fullscreen",
    title_cancel="Exit fullscreen",
    force_separate_button=True,
).add_to(m)

# Iter a dataframe rows
for i, r in wifi_pilares.iterrows():
    # Custom icon image
    icon = CustomIcon('../assets/icons/wifi-pilares.png', 
    icon_size=(50, 50),
    icon_anchor=(20, 10),
    popup_anchor=(-2, -15))
    # Add markers
    folium.Marker([r['Latitud'], r['Longitud']],
    popup = folium.Popup('''
                        <div class="container">
                            Puntos de acceso: {}
                        </div>
                        
                        <style type='text/css'>
                        .container {{
                            width: 150px;
                            font-family: Verdana, sans-serif;
                            text-align:justify;
                            font-size:12px;
                            font-weight: 600; 
                            border-radius: 5px;
                            padding: 10px;
                        }}
                        '''.format(r["Puntos_de_acceso"])),
    tooltip = r['Colonia'],
    icon = icon
    ).add_to(pilares)

# Iter a dataframe rows
for i, r in wifi_sitiospublicos.iterrows():
    # Custom icon image
    icon = CustomIcon('../assets/icons/wifi-sitiospublicos.png', 
    icon_size=(50, 50),
    icon_anchor=(20, 10),
    popup_anchor=(-2, -15))
    # Add markers
    folium.Marker([r['Latitud'], r['Longitud']],
    popup = folium.Popup('''
                        <div class="container">
                            Puntos de acceso: {}
                        </div>
                        
                        <style type='text/css'>
                        .container {{
                            width: 150px;
                            font-family: Verdana, sans-serif;
                            text-align:justify;
                            font-size:12px;
                            font-weight: 600; 
                            border-radius: 5px;
                            padding: 10px;
                        }}
                        '''.format(r["Puntos_de_acceso"])),
    tooltip = r['Colonia'],
    icon = icon
    ).add_to(sitiospublicos)

# Show map
m
```

![Folium](https://github.com/fer-aguirre/maps-examples/blob/main/prints/python-folium.png)

The data were download from [here](https://datos.cdmx.gob.mx/group/conectividad)


## [prettymaps](https://github.com/marceloprates/prettymaps)
 
  ```python3
from prettymaps import *
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

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
    fontproperties = fm.FontProperties(fname = '../assets/fonts/HashedBrowns-WyJgn.ttf', size = 40)
)
```
 
![Zocalo](https://github.com/fer-aguirre/maps-examples/blob/main/prints/zocalo.png)
  
### Gallery:
  
![Bosque de Chapultepec](https://github.com/fer-aguirre/maps-examples/blob/main/prints/bosque-chapultepec.png)
![Kiosco Morisco](https://github.com/fer-aguirre/maps-examples/blob/main/prints/kiosco-morisco.png)

