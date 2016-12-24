(function () {
    'use strict';

    // Your additional js should go there

}());

function insertMap(geojson_url) {
  var map = new mapboxgl.Map({
      container: 'map', // container id
      style: 'mapbox://styles/mapbox/light-v9', //'mapbox://styles/rickymoorhouse/cih6ouins00f3bnm500a1d3dl',
      center: [-53, 20], // starting position
      zoom: 1.5 // starting zoom
  });
  map.on('load', function() {
    map.addSource("visited", {
      type: 'geojson',
      data: geojson_url
    });
    map.addLayer({
       "id": "points",
       "type": "symbol",
       "source": "visited",
       "layout": {
           "icon-image": "star-11",
           //"text-field": "{name}",
           "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
           "text-offset": [0, 0.6],
           "text-anchor": "top"
       }
     });
  });
}
