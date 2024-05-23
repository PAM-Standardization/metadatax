var markers = L.markerClusterGroup({
maxClusterRadius: function (mapZoom) {
   if (mapZoom >5) {return 5;} else {return 40;}
}
});



function showContent(e) {



 if (!e.length) {

    var tbl= document.getElementById('table')
    for (var row =0; row <tbl.rows.length;){
     tbl.deleteRow(row);
    }
    for (var index =0 ; index < tooltip_obj.length; index++) {
        if (tooltip_obj[index].Latitude == e.latlng.lat && tooltip_obj[index].Longitude == e.latlng.lng) {
                document.getElementById("mysidepanel").style.width = "500px";
               for (var line =0; line<Object.keys(tooltip_obj[index]).length; line++) {
                    let tr = tbl.insertRow();
                    tr.setAttribute("id",Object.keys(tooltip_obj[index])[line]);
                     let th = tr.insertCell();
                     th.appendChild(document.createTextNode(Object.keys(tooltip_obj[index])[line]));
                     let td = tr.insertCell();
                     try {
                        td.appendChild(document.createTextNode(JSON.parse(view[index][Object.keys(tooltip_obj[index])[line]])));
                        console.log(tooltip_obj[index][Object.keys(tooltip_obj[index])[line]]);
                        }
                        catch(err) {
                        td.appendChild(document.createTextNode(tooltip_obj[index][Object.keys(tooltip_obj[index])[line]]));
                        }
                 }
          }
    }
  }
  else {
  return e;
  }
}
function onEachFeature(feature, layer) {
    if (feature.properties && feature.properties.popupContent) {
        layer.bindTooltip(feature.properties.tooltipContent);
    }
    layer.on({
        click: showContent
    });
}

function pointToLayer(geoJsonPoint, latlng) {
    return L.circleMarker(latlng, {
        color: 'black',
        fillColor: geoJsonPoint.properties.popupContent,
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
            "version": "1.3.0",
            "noWrap": true,
            "bounds": [   [-90, -180],   [90, 180] ]        }
).addTo(map);


    const geojsonValue = [];
    for (const k in tooltip_obj) {
        geojsonValue.push(
            {
                "type": "Feature",
                "properties": {
                    "tooltipContent": generateTooltip(Object.keys(tooltip_obj[k]),tooltip_obj[k]),
                    "popupContent":showContent(tooltip_obj[k]["Color"])//'<a href =/admin/metadatax/deployment/?q=' + obj[k].name + '> See deployment metadata </a>',
           //      "popupContent": generatePopupContent(obj[k])
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [tooltip_obj[k].Longitude, tooltip_obj[k].Latitude]
                }
            })
    }


   var geoJsonPoint = L.geoJSON(geojsonValue, {
        onEachFeature: onEachFeature,
        pointToLayer: pointToLayer
    })
markers.on('clusterclick', function(e) {showContent(e)});
markers.addLayer(geoJsonPoint);
map.addLayer(markers);
}

function generateTooltip(key, value) {
var text = '<div> ';
console.log(key)
    for (let index = 0; index <key.length-3; index ++ ) {
        text+=  '<b> '+key[index]+' : </b>' + value[key[index]]+ '<br>';
    }
return text+'<br><b> Click on the circle to see the associated metadata</div>'
}
//function generatePopupContent(k) {
// document.getElementById("mysidepanel").style.width = "250px";
//}
