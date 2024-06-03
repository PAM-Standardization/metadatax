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
const DEPLOYMENT_KEYS = [
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
const HYDROPHONE_MODEL_KEYS = [
    "directivity",
    "max_bandwidth",
    "max_dynamic_range",
    "max_operating_depth",
    "min_bandwidth",
    "min_dynamic_range",
    "name",
    "noise_floor",
    "operating_max_temperature",
    "operating_min_temperature"
]
const RECORDER_MODEL_KEYS = [
    "name",
    "number_of_channels",
]

const HYDROPHONE_KEYS = [
    "serial_number",
    "sensitivity",
    "model",
]
const RECORDER_KEYS = [
    "serial_number",
    "model",
]
const MENU_KEYS = [
    "deployment",
    "channel",
    "hydrophone",
    "recorder",
]
const CHANNEL_KEYS = [
    "channel_name",
    "continuous",
    "duty_cycle_off",
    "duty_cycle_on",
    "gain (dB)",
    "hydrophone_depth (m)",
    "sample_depth",
    "sampling_frequency",
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

    if (!e?.sourceTarget?.feature?.properties?.channel) {
        closePanel();
        return;
    }

    const channel = e.sourceTarget.feature.properties.channel;
    document.getElementById("title_panel").innerText = `Project: ${channel.deployment.project.name}`;
    displayElement(MENU_KEYS, channel, "channel")
    const panel = document.getElementById("mysidepanel");
    panel.scrollTop = 0;
    panel.style.width = "500px";



function hide(element, type) {
  for (const e of element) {
       document.getElementById(type+e).style.display="none";
}
}
function showOrHideElement(element, type){
    for (const e of element) {
        document.getElementById(type+e).style.display= (document.getElementById(type+e)?.style?.display == "none")  ? "": "none";
    }

}
function displayElement(element, attribute, type) {
    for (const key of element) {
        const row = table.insertRow();
        row.setAttribute("id", type+key);
        const labelCell = row.insertCell();
        labelCell.className = "popuptitle"
        labelCell.innerText = key.replaceAll('_', ' ');
        if (key == "hydrophone") {
                   generateCollapse(key, HYDROPHONE_KEYS,channel[key], labelCell);
                  labelCell.onclick = function() { showOrHideElement(HYDROPHONE_KEYS,  key); hide(HYDROPHONE_MODEL_KEYS,  key); };
        }
        else if (key == "recorder") {
                    generateCollapse(key, RECORDER_KEYS,channel[key], labelCell);
                    labelCell.onclick = function() { showOrHideElement(RECORDER_KEYS,  key); hide(RECORDER_MODEL_KEYS,  key);  };
        }
        else if (key == "channel") {
             generateCollapse(key, CHANNEL_KEYS,channel, labelCell);
        }
        else if (key == "model") {
          if ( attribute[key].directivity != undefined ) {
              generateCollapse("hydrophone", HYDROPHONE_MODEL_KEYS,channel.hydrophone[key], labelCell);
              }
           else {
               generateCollapse( "recorder", RECORDER_MODEL_KEYS, channel.recorder[key], labelCell);
           }
        }
        else if (key == "deployment") {
             displayElement(DEPLOYMENT_KEYS, channel[key], key)
             labelCell.colSpan = 2
        }
        else {
           labelCell.className = "label"
           const valueCell = row.insertCell();
           valueCell.innerText = getCellInnerText(attribute, key);
        }
    }
}

function generateCollapse(key, array, attribute, labelCell) {
                  labelCell.onclick = function() { showOrHideElement(array,  key) };
                  displayElement(array,attribute, key)
                  hide(array, key)
                  labelCell.colSpan = 2
}
}
const getRandomColor = () => "#" + ((1 << 24) * Math.random() | 0).toString(16).padStart(6, "0");
const ProjectColor = new Map();

let map;

window.onload = function () {
    for (const channel of DATA) {
        if (ProjectColor.has(channel.deployment.project.id)) continue;
        ProjectColor.set(channel.deployment.project.id, getRandomColor())
    }

  const bounds= [[-200, -200], [200, 200]]
    map = L.map('map', {
        minZoom: 2, zoom: 3,
        zoomControl: true,
        preferCanvas: true,
    }).setView([48.400002, -4.48333], 4.5).setMaxBounds(bounds);
    L.tileLayer.wms("https://www.gebco.net/data_and_products/gebco_web_services/web_map_service/mapserv?",
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

    const geojsonValue = DATA.map(channel => ({
        type: "Feature",
        properties: {
            channel,
        },
        geometry: {
            "type": "Point",
            "coordinates": [channel.deployment.longitude, channel.deployment.latitude]
        }
    }))

    const geoJsonPoint = L.geoJSON(geojsonValue, {
        pointToLayer: (feature, coordinates) => {
            return L.circleMarker(coordinates, {
                color: 'black',
                fillColor: ProjectColor.get(feature.properties.channel.deployment.project.id),
                fillOpacity: 1,
                radius: 10,
            })
        },
        onEachFeature: (feature, layer) => {
            layer.bindTooltip(`
                    <div>
                       <b>Project:</b> ${feature.properties.channel.deployment.project.name}<br>
                       <b>Deployment:</b> ${feature.properties.channel.deployment.name}<br>
                       <b>Responsible parties:</b> ${feature.properties.channel.deployment.project.responsible_parties.map(i => i.name).join(', ')}<br>
                       <b>Period:</b> ${new Date(feature.properties.channel.deployment.deployment_date).toDateString()} to ${new Date(feature.properties.channel.deployment.recovery_date).toDateString()}<br>
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
    L.control.scale().addTo(map);
}

