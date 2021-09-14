library(leaflet)
library(here)
library(shiny)


mapa <- read.csv("huertos.csv")
options("scipen"=100, "digits"=15)

popup = paste0( paste("<b>", mapa$nombre, "</b><hr>", sep = "")
                , "<br><b>Tipo de Huerto:</b> "
                , mapa$tipo
                , "<br><br><b>Descripción:</b> "
                , mapa$descripcion
                , paste('<br><br><b><a href="', mapa$redes_sociales, '" target=“_blank”>Redes Sociales</a>', sep = "")
)

icono_semilla <- makeIcon(
  iconUrl = "plant.png",
  iconWidth = 40, iconHeight = 50,
  iconAnchorX = 0, iconAnchorY = 0
)


leaflet() %>% 
  setView( lat=20, lng=-100, zoom=5) %>%
  addProviderTiles("Stamen.Watercolor") %>%
  addProviderTiles("Stamen.TonerLabels") %>%
  addMarkers(data = mapa, ~longitud, ~latitud, icon = icono_semilla,
             popup =  popup)

