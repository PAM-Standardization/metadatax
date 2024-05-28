/**
 * Create Cluster for close up deployments.
 * Clustering depends on distance between points and zoom level.
 */
const markers = L.markerClusterGroup({
    maxClusterRadius: (maxZoom) => 5 ? 5 : 40,
});


/**
 * Labels for the popup content lines
 * @type {Array<string>}
 */
const KEYS = [
    "name",
    "provider",
    "campaign",
    "site",
    "deployment_date",
    "deployment_vessel",
    "recovery_date",
    "recovery_vessel",
    "description",
    "coordinates",
    "bathymetric_depth",
    "platform",
]

const EMPTY_VALUE = "-"

function getCellInnerText(deployment, key) {
    switch (key) {
        case "campaign":
        case "site":
        case "provider":
        case "platform":
            return deployment[key]?.name ?? EMPTY_VALUE;
        case "deployment_date":
        case "recovery_date":
            return deployment[key] ? (new Date(deployment[key])).toISOString() : EMPTY_VALUE;
        case "coordinates":
            return `${deployment.latitude}, ${deployment.longitude}`;
        default:
            return deployment[key] ?? EMPTY_VALUE;
    }
}

function closePanel() {
    document.getElementById("title_panel").innerText = ""
    document.getElementById("mysidepanel").style.transition = "none";
    document.getElementById("mysidepanel").style.width = "0";
    document.getElementById("mysidepanel").style.transition = "0.5s";
}


/**
 * Create popup content
 * @param e {any}
 * @returns {any|*}
 */
function showContent(e) {
    // Empty table
    const table = document.getElementById('table');
    table.innerHTML = "";

    if (!e?.sourceTarget?.feature?.properties?.deployment) {
        closePanel();
        return;
    }

    const deployment = e.sourceTarget.feature.properties.deployment;

    document.getElementById("title_panel").innerText = `Project: ${deployment.project.name}`;
    for (const key of KEYS) {
        const row = table.insertRow();
        row.setAttribute("id", key);
        const labelCell = row.insertCell();
        labelCell.className = "label"
        labelCell.innerText = key.replaceAll('_', ' ');
        const valueCell = row.insertCell();
        valueCell.innerText = getCellInnerText(deployment, key)
    }
    const panel = document.getElementById("mysidepanel");
    panel.scrollTop = 0;
    panel.style.width = "500px";
}

const getRandomColor = () => "#" + ((1 << 24) * Math.random() | 0).toString(16).padStart(6, "0");
const ProjectColor = new Map();

let map;

window.onload = function () {
    for (const deployment of DATA) {
        if (ProjectColor.has(deployment.project.id)) continue;
        ProjectColor.set(deployment.project.id, getRandomColor())
    }

    map = L.map('map', {
        minZoom: 2, zoom: 3,
        zoomControl: true,
        preferCanvas: true,
    }).setView([48.400002, -4.48333], 4.5);
    L.tileLayer.wms("https://www.gebco.net/data_and_products/gebco_web_services/web_map_service/mapserv?",
        {
            "attribution": "",
            "format": "image/png",
            "layers": "GEBCO_latest",
            "styles": "",
            "transparent": true,
            "version": "1.3.0",
            "noWrap": true,
            "bounds": [[-90, -180], [90, 180]]
        }
    ).addTo(map);


    const geojsonValue = DATA.map(deployment => ({
        type: "Feature",
        properties: {
            deployment,
            // "tooltipContent": getTooltipContent(deployment),
            // "popupContent": showContent()
        },
        geometry: {
            "type": "Point",
            "coordinates": [deployment.longitude, deployment.latitude]
        }
    }))


    const geoJsonPoint = L.geoJSON(geojsonValue, {
        pointToLayer: (feature, coordinates) => {
            return L.circleMarker(coordinates, {
                color: 'black',
                fillColor: ProjectColor.get(feature.properties.deployment.project.id),
                fillOpacity: 1,
                radius: 10,
            })
        },
        onEachFeature: (feature, layer) => {
            layer.bindTooltip(`
                    <div>
                       <b>Deployment:</b> ${feature.properties.deployment.name}<br>
                       <b>Responsible parties:</b> ${feature.properties.deployment.project.responsible_parties.map(i => i.name).join(', ')}<br>
                       <b>Period:</b> ${new Date(feature.properties.deployment.deployment_date).toDateString()} to ${new Date(feature.properties.deployment.recovery_date).toDateString()}<br>
                    </div>
                    <br>
                    <b> Click on the circle to see the associated metadata</div>
          `)
            layer.on({click: showContent,});
        },
    })
    markers.on('clusterclick', showContent);
    markers.addLayer(geoJsonPoint);
    map.addLayer(markers);
}

function getTooltipContent(deployment) {
    return `
            <div>
               <b>Deployment:</b> ${deployment.name}<br>
               <b>Responsible parties:</b> ${deployment.project.responsible_parties.map(i => i.name).join(', ')}<br>
               <b>Period:</b> ${new Date(deployment.deployment_date).toDateString()} to ${new Date(deployment.recovery_date).toDateString()}<br>
            </div>
            <br>
            <b> Click on the circle to see the associated metadata</div>
          `;
}
