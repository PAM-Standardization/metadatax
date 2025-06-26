/**
 * Create Cluster for close up deployments.
 * Clustering depends on distance between points and zoom level.
 */
const markers = L.markerClusterGroup({
    maxClusterRadius: (maxZoom) => 5 ? 5 : 40,
});

function componentToHex(c) {
  let hex = c.toString(16);
  return hex.length === 1 ? "0" + hex : hex;
}
function intToRGB(value) {
    value *= 319
  //credit to https://stackoverflow.com/a/2262117/2737978 for the idea of how to implement
  let blue = 128 + Math.floor(value % 128);
  let green = 128 + Math.floor(value / 128 % 128);
  let red = 128 + Math.floor(value / 128 / 128 % 128);
  return '#' + componentToHex(red) + componentToHex(green) + componentToHex(blue)
}

const ProjectColor = new Map();

let map;

window.onload = function () {
    for (const deployment of DEPLOYMENTS) {
        if (ProjectColor.has(deployment.project)) continue;
        ProjectColor.set(deployment.project, intToRGB(deployment.project))
    }
    const bounds = [[-200, -200], [200, 200]]
    map = L.map('map', {
        minZoom: 2, zoom: 3,
        zoomControl: true,
        preferCanvas: true,
    }).setView([48.400002, -4.48333], 4.5).setMaxBounds(bounds);

    var url = 'https://wms.gebco.net/mapserv?'
    var request;
    if (window.XMLHttpRequest)
        request = new XMLHttpRequest();
    else
        request = new ActiveXObject("Microsoft.XMLHTTP");
    request.open('GET', url, false);
    try {
        request.send();
        if (request.status !== 200) {
            url = ' https://tile.openstreetmap.org/{z}/{x}/{y}.png'
        }
    } catch (error) {
        url = ' https://tile.openstreetmap.org/{z}/{x}/{y}.png'
    }
    L.tileLayer.wms(url,
        {
            "attribution": "",
            "format": "image/png",
            "layers": "GEBCO_latest",
            "styles": "",
            "transparent": true,
            "version": "1.3.0",
            "noWrap": true,
            "bounds": [[-90, -180], [90, 180]],
        }
    ).addTo(map);

    const geojsonValue = DEPLOYMENTS.map(deployment => ({
        type: "Feature",
        properties: {
            deployment,
        },
        geometry: {
            "type": deployment.mobile_positions.length === 0 ? "Point" : "LineString",
            "coordinates": deployment.mobile_positions.length === 0 ? [deployment.longitude, deployment.latitude] :
                deployment.mobile_positions.map((element) => Array.of(element.longitude, element.latitude))
        }
    }))
    console.log(geojsonValue)
    const geoJsonPoint = L.geoJSON(geojsonValue, {
        pointToLayer: (feature, coordinates) => {
            if (feature.properties.deployment.mobile_positions.length === 0) {
                return L.circleMarker(coordinates, {
                    color: 'black',
                    fillColor: ProjectColor.get(feature.properties.deployment.project),
                    fillOpacity: 1,
                    radius: 10,
                })
            }
        },
        style: function (feature) {
            switch (feature.geometry.type) {
                case 'LineString':
                    return {
                        color: ProjectColor.get(feature.properties.deployment.project),
                        weight: 5,
                        opacity: 1
                    }
            }
        },
        onEachFeature: (feature, layer) => {
            const deployment = feature.properties?.deployment;
            const project = PROJECTS.find(p => p.id === deployment?.project);
            layer.bindTooltip(`
                    <div>
                       <b>Project:</b> ${project.name}<br>
                       <b>Deployment:</b> ${feature.properties.deployment.name}<br>
                       <b>Responsible parties:</b> ${feature.properties.deployment.contacts.map(i => i.contact.name).join(', ')}<br>
                       <b>Period:</b> ${new Date(feature.properties.deployment.deployment_date).toDateString()} to ${new Date(feature.properties.deployment.recovery_date).toDateString()}<br>
                    </div>
                    <br>
                    <b> Click on the circle to see the associated metadata</div>
          `)
            layer.on({click: DeploymentPanel.open.bind(DeploymentPanel),});
        },
    })
    markers.on('clusterclick', DeploymentPanel.open.bind(DeploymentPanel));
    markers.addLayer(geoJsonPoint);
    map.addLayer(markers);
    L.control.scale().addTo(map);
}

