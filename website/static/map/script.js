function onEachFeature(feature, layer) {
    if (feature.properties && feature.properties.popupContent) {
        console.log(feature.properties)
        layer.bindPopup(feature.properties.popupContent);
        layer.bindTooltip(feature.properties.tooltipContent);
    }
}

function pointToLayer(geoJsonPoint, latlng) {
    return L.circleMarker(latlng, {
        color: 'black',
        fillColor: '#f03',
        fillOpacity: 1,
        radius: 10
    });
}


window.onload = function () {
    const map = L.map('map', {
        minZoom: 2, zoom: 3,
        zoomControl: true,
        preferCanvas: true,
    }).setView([48.400002, -4.48333], 4.5);
    map.setMaxBounds([[-230, -230], [230, 230]]);
    L.tileLayer.wms("https://www.gebco.net/data_and_products/gebco_web_services/web_map_service/mapserv?",
        {
            "attribution": "",
            "format": "image/png",
            "layers": "GEBCO_latest",
            "styles": "",
            "transparent": true,
            "version": "1.3.0"
        }).addTo(map);


    const geojsonValue = [];
    for (const k in obj) {
        geojsonValue.push(
            {
                "type": "Feature",
                "properties": {
                    "tooltipContent": '<div><b> Name: </b>' + obj[k].campaign + ' <br><b> Institution: </b>' + obj[k].provider + '<br><b> Period of deployment: </b>' + obj[k].period + '<br><br><b> Click on the circle to get a link to the associated metadata</div>',
                    "popupContent": '<a href =/admin/metadatax/deployment/?q=' + obj[k].name + '> See deployment metadata </a>'
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [obj[k].longitude, obj[k].latitude]
                }
            })
    }


    L.geoJSON(geojsonValue, {
        onEachFeature: onEachFeature,
        pointToLayer: pointToLayer
    }).addTo(map);

}