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
  # Markers
  addMarkers(m, lat=19.435011442107704, lng=-99.13265026035839, popup="<b>Parque República de Guatemala</b>", icon=icon_park) %>%
  addMarkers(m, lat=19.42982058040328, lng=-99.13279050032122, popup="<b>Parque Francisco Primo De Verdad Y Ramos</b>", icon=icon) %>%
  addMarkers(m, lat=19.43640005202161, lng=-99.14397464702137, popup="<b>Alameda Central</b>", icon=icon) %>%
  addMarkers(m, lat=19.433655882695284, lng=-99.14372922687433, popup="<b>Parque Santos Degollado</b>", icon=icon) %>%
  addMarkers(m, lat=19.426977108120735, lng=-99.14572764812497, popup="<b>Parque Pujibet</b>", icon=icon)
m


  
