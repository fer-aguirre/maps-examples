from prettymaps import *
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt

# SQUARE PLOT WITH ROUNDED EDGES
# Style parameters
palette = ['#001c5a', '#ffab15']
background_c = '#e5c6f5'
dilate = 100

# Setup figure
fig, ax = plt.subplots(figsize = (10, 10), constrained_layout = True)

# Plot
layers = plot(
    (19.449885835076476, -99.15688024541792), radius = 500,
    ax = ax,
    layers = {
        'perimeter': {'circle': False, 'dilate': dilate},
        'streets': {
            'width': {
                'primary': 5,
                'secondary': 4,
                'tertiary': 3,
                'residential': 2,
                'footway': 1,
            },
            'circle': False,
            'dilate': dilate
        },
        'building': {
            'tags': {'building': True},
            'union': False,
            'circle': False,
            'dilate': dilate
        },
        'green': {
            'tags': {
                'landuse': ['grass', 'village_green'],
                'leisure': 'park'
            },
            'circle': False,
            'dilate': dilate
        },
    },
    drawing_kwargs = {
        'background': {'fc': '#fdf9a0', 'ec': '#ffedac', 'hatch': 'ooo...', 'zorder': -1},
        'perimeter': {'fill': False, 'lw': 0, 'zorder': 0},
        'green': {'fc': '#8BB174', 'ec': '#2F3737', 'hatch_c': '#A7C497', 'hatch': 'ooo...', 'lw': 1, 'zorder': 1},
        'water': {'fc': '#a8e1e6', 'ec': '#2F3737', 'hatch_c': '#9bc3d4', 'hatch': 'ooo...', 'lw': 1, 'zorder': 3},
        'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 4},
        'building': {'palette': palette, 'ec': '#005858', 'lw': .5, 'zorder': 5},
    },
    osm_credit = {'x': .02, 'y': .01, 'color': '#2F3737'}
)

# Set bounds
xmin, ymin, xmax, ymax = layers['perimeter'].bounds
dx, dy = xmax-xmin, ymax-ymin
ax.set_xlim(xmin-.06*dx, xmax+.06*dx)
ax.set_ylim(ymin-.06*dy, ymax+.06*dy)

# Draw right text
ax.text(
    #xmin-.05*dx, ymin-.06*dy,
    xmin+1.02*dx, ymin+.26*dy,
    'Kiosco Morisco, CDMX, México',
    color = '#2F3737',
    rotation = 270,
    fontproperties = fm.FontProperties(fname = 'assets/fonts/HashedBrowns-WyJgn.ttf', size = 40)
)

plt.savefig('ejemplos/kiosco-morisco.png')


###############################################################################

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


plt.savefig('ejemplos/zocalo.png')

###############################################################################

# BOUNDARY DEFINED BY GEOGRAPHY
def postprocessing(layers):
    layers['perimeter'] = layers['perimeter'].buffer(10)
    return layers

fig, ax = plt.subplots(figsize = (15, 12), constrained_layout = True)

layers = plot(
    'Bosque de Chapultepec, Miguel Hidalgo, Ciudad de México',

    ax = ax,

    postprocessing = postprocessing,

    layers = {
            'perimeter': {},
            'streets': {
                'width': {
                    #'motorway': 8,
                    'trunk': 6,
                    'primary': 6,
                    'secondary': 5,
                    'tertiary': 4,
                    'residential': 3,
                    #'living_street': 3,
                    'pedestrian': 1.5,
                    'footway': 1.5,
                    #'track': 1,
                    #'bridleway': 1
                }
            },
            'building': {'tags': {'building': True}, 'union': False},
            'water': {'tags': {'natural': ['water', 'bay']}},
            'green': {'tags': {'landuse': 'grass', 'natural': ['island', 'wood'], 'leisure': 'park'}},
        },
        drawing_kwargs = {
            'background': {'fc': '#F9BACA', 'ec': '#F4A5B9', 'hatch': 'ooo...', 'zorder': -1},
            'perimeter': {'fc': '#F7F3F5', 'ec': '#2F3737', 'lw': 3, 'hatch': 'ooo...', 'hatch_c': '#EFE7EB',  'zorder': 0},
            'green': {'fc': '#AABD8C', 'ec': '#2F3737', 'hatch_c': '#b3cfa5', 'hatch': 'ooo...', 'lw': 0, 'zorder': 1},
            'water': {'fc': '#a1e3ff', 'hatch': 'ooo...', 'hatch_c': '#80bed9', 'lw': 0, 'zorder': 2},
            'streets': {'fc': '#3b4545', 'lw': 0, 'zorder': 3},
            'building': {'palette': ['#433633', '#FF5E5B'], 'ec': '#2F3737', 'hatch': 'ooo...', 'hatch_c': '#b3504f', 'lw': 0, 'zorder': 4},
        },

        osm_credit = {'color': '#3b4545'}
)

# Set bounds
xmin, ymin, xmax, ymax = layers['perimeter'].bounds
dx, dy = xmax-xmin, ymax-ymin
ax.set_xlim(xmin-.06*dx, xmax+.06*dx)
ax.set_ylim(ymin-.06*dy, ymax+.06*dy)


# Draw left text
ax.text(
    xmin-.06*dx, ymin+.5*dy,
    'Bosque de Chapultepec,\nCDMX, México',
    color = '#2F3737',
    rotation = 90,
    fontproperties = fm.FontProperties(fname = 'assets/fonts/HashedBrowns-WyJgn.ttf', size = 40)
)

plt.savefig('ejemplos/bosque-chapultepec.png')

###############################################################################
