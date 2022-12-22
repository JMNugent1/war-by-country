// Store our API endpoint as queryUrl.
var queryUrl = "/api/v1.0/geojson";

// Perform a GET request to the query URL/
d3.json(queryUrl).then(function (data) {
  console.log(data.features)
  // Once we get a response, send the data.features object to the createFeatures function.
  createFeatures(data);
});

function createFeatures(baseballData) {

  // Define a function that we want to run once for each feature in the features array.
  // Give each feature a popup that describes the player and war of the baseball player.
  function onEachFeature(feature, layer) {
    layer.bindPopup(`<h3>${feature.properties.player_name}</h3><hr><p>${feature.properties.war}</p>`);
  }

  // Create a GeoJSON layer that contains the features array on the earthquakeData object.
  // Run the onEachFeature function once for each piece of data in the array.
  var birthplace = L.geoJSON(baseballData, {
    onEachFeature: onEachFeature
  });

  // Send our earthquakes layer to the createMap function/
  createMap(birthplace);
}

function createMap(birthplace) {

  // Create the base layers.
  var street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  })


  // Create a baseMaps object.
  var baseMaps = {
    "Street Map": street
  };

  // Create an overlay object to hold our overlay.
  var overlayMaps = {
    Birthplace: birthplace,
    Heatmap: birthplace
  };


  // Create our map, giving it the streetmap layers to display on load.
  var myMap = L.map("map", {
    center: [
      37.09, -95.71
    ],
    zoom: 5,
    layers: [street, birthplace]
  });

  // Create a layer control.
  // Pass it our baseMaps and overlayMaps.
  // Add the layer control to the map.
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);

}

function getColor(d) {
    return d > 90 ? '#bd0026' :
           d > 70  ? '#f03b20' :
           d > 50  ? '#fd8d3c' :
           d > 30  ? '#feb24c' :
           d > 10   ? '#fed976' :
                      '#ffffb2';
}

function getColor(d) {
    return d === '90+' ? '#bd0026' :
           d === '70-90'  ? '#f03b20' :
           d === '50-70'  ? '#fd8d3c' :
           d === '30-50'  ? '#feb24c' :
           d === '10-30'   ? '#fed976' :
                    '#ffffb2';
}
