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


/**
 * Create popup content
 * @param e {any}
 * @returns {any|*}
 */
function showContent(e) {
    console.debug(e)
    if (!e) return;
    if (!e.length) {
        let table = document.getElementById('table')
        for (let row = 0; row < table.rows.length;) {
            table.deleteRow(row);
        }

        const deployment = DATA.find(d => d.latitude === e.latlng.lat && d.longitude === e.latlng.lng);
        if (!deployment) return;

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
        document.getElementById("mysidepanel").scrollTop = 0;
        document.getElementById("mysidepanel").style.width = "500px";

        if (table.rows.length === 0) {
            document.getElementById("mysidepanel").style.width = "0px";
        }
    } else {
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
    const deployment = DATA.find(d => d.latitude === latlng.lat && d.longitude === latlng.lng);
    return L.circleMarker(latlng, {
        color: 'black',
        fillColor: ProjectColor.get(deployment?.project.id),
        fillOpacity: 1,
        radius: 10
    });
}

const getRandomColor = () => "#" + ((1 << 24) * Math.random() | 0).toString(16).padStart(6, "0");
const ProjectColor = new Map();

window.onload = function () {
    for (const deployment of DATA) {
        if (ProjectColor.has(deployment.project.id)) continue;
        ProjectColor.set(deployment.project.id, getRandomColor())
    }

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
            "bounds": [[-90, -180], [90, 180]]
        }
    ).addTo(map);


    const geojsonValue = DATA.map(deployment => ({
        "type": "Feature",
        "properties": {
            "tooltipContent": getTooltipContent(deployment),
            "popupContent": showContent()
        },
        "geometry": {
            "type": "Point",
            "coordinates": [deployment.longitude, deployment.latitude]
        }
    }))


    const geoJsonPoint = L.geoJSON(geojsonValue, {onEachFeature, pointToLayer})
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
