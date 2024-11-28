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
    "channel_configuration"
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
    "hydrophone",
    "recorder"
]

const EMPTY_VALUE = "-"

/**
 * Populate table cell
 */
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
*closePanel of bottom panel
*/
function closePanel(table_length) {
    document.getElementById("title_panel").innerText = ""
    document.getElementById("mysidepanel").style.transition = "none";
    document.getElementById("mysidepanel").style.width = "0";
    document.getElementById("mysidepanel").style.transition = "0.5s";
    closeMetadataPanel(length-1);
}
/**
*closeMetadataPanel of channel configuration panel and go back to deployment panel
*/
function closeMetadataPanel(length) {
    document.getElementById('deployment').style.display = '';
    if (length>1)  {
      document.getElementById("bottom_right_arrow").innerText = ">";
    }
    document.getElementById("bottom_left_arrow").innerText = "";
    document.getElementById("bottom_pagination").innerText = "";
    document.getElementById("bottom_right_arrow").onclick = function() { showAndHideElement(CHANNEL_KEYS,  0, length-1) };
    for (var l = 0 ; l< length-1; l++) {
           document.getElementById("channel_configuration"+l).style.display = 'none';
    }
}
/**
*showAndHideElement of bottom panel
*/
function showAndHideElement (array, index, length) {
    document.getElementById('deployment').style.display = 'none';
   for (var c = 0 ; c< length; c++) {
        if (index == c) {
           document.getElementById("channel_configuration"+c).style.display = '';
            document.getElementById("bottom_pagination").innerText = index+1+" / "+length
            document.getElementById("bottom_right_arrow").onclick = function() {
             document.getElementById("bottom_pagination").innerText = index+" / "+length;
           showAndHideElement (array, index+1, length)};
            document.getElementById("bottom_left_arrow").onclick = function() {
                       document.getElementById("bottom_pagination").innerText = index+" / "+length;
                        showAndHideElement (array, index-1, length)};
        }
        else {
            document.getElementById("channel_configuration"+c).style.display = 'none';
        }
    }
     showArrow(index, 0 ,"bottom_left_arrow", "<" )
     showArrow(index,  length-1 ,"bottom_right_arrow", ">" )
}
/**
* Show  bottom panel with navigation
*/
function showArrow(index,value, id , text) {
    if (index == value) {
       document.getElementById(id).onclick = function() {};
       document.getElementById(id).innerText = ""
    }
    else {
      document.getElementById(id).innerText = text
      }
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
        closePanel(table.tBodies.length);
        return;
    }
    const deployment = e.sourceTarget.feature.properties.deployment;
    document.getElementById("title_panel").innerText = `Project: ${deployment.project.name}`;
    document.getElementById("bottom_panel").innerText = ` ${deployment.channel.length} Channel configuration`;
    if (`${deployment.channel.length}` !=0) {
        document.getElementById("bottom_right_arrow").innerText = ">";
        document.getElementById("bottom_right_arrow").onclick = function() { showAndHideElement(CHANNEL_KEYS,  0, deployment.channel.length) };
    }
    else {
            document.getElementById("bottom_right_arrow").innerText = "";
    }
    tbody= table.appendChild(document.createElement('tbody'))
    tbody.id="deployment"
    displayElement(DEPLOYMENT_KEYS, deployment, "deployment")
    const panel = document.getElementById("mysidepanel");
    panel.scrollTop = 0;
    panel.style.width = "500px";

/**
 * Hide element
 */
function hide(element, type) {
    for (const e of element) {
       document.getElementById(type+e).style.display="none";
    }
}
/**
 * Show or hide element
 */
function showOrHideElement(element, type){
    for (const e of element) {
        document.getElementById(type+e).style.display= (document.getElementById(type+e)?.style?.display == "none")  ? "": "none";
    }
}

/**
 * Create and populate table
 */
function displayElement(element, attribute, type) {
    for (const key of element) {
        if (key == "hydrophone") {
                labelCell = populateTable(table, type, key )
               generateCollapse(attribute.hydrophone, HYDROPHONE_KEYS,HYDROPHONE_MODEL_KEYS,type+key, labelCell);
        }
        else if (key == "recorder") {
                labelCell = populateTable(table, type, key )
                generateCollapse(attribute.recorder, RECORDER_KEYS,RECORDER_MODEL_KEYS,type+key, labelCell);
        }
        else if (key == "channel_configuration") {
          for (const c in deployment.channel) {
            tbody= table.appendChild(document.createElement('tbody'))
            tbody.id=key+c
            labelCell = populateTable(tbody, c, key)
            displayElement(CHANNEL_KEYS,deployment.channel[c], tbody.id)
            document.getElementById(tbody.id).style.display = 'none';
           }
        }
        else if (key == "model") {
            labelCell = populateTable(table, type, key)
            index = type.split("channel_configuration")[1].substring(0,1)
            if ( attribute[key].directivity != undefined ) {
               generateCollapse( deployment.channel[index].hydrophone[key], HYDROPHONE_MODEL_KEYS, [], type+key, labelCell);
            }
            else {
                generateCollapse( deployment.channel[index].recorder[key], RECORDER_MODEL_KEYS, [], type+key, labelCell);
           }
        }
        else {
            const row = table.insertRow();
            row.setAttribute("id", type+key);
            const labelCell = row.insertCell();
            labelCell.innerText = key.replaceAll('_', ' ');
            labelCell.className = "label"
            const valueCell = row.insertCell();
             valueCell.innerText = getCellInnerText(attribute, key);
        }
    }
}
/**
 * Collapse optionnal element
 */
function generateCollapse(attribute, array,sub_array,  id, labelCell) {
                labelCell.onclick = function() {
                                showOrHideElement(array,  id);
                                if (sub_array) {  hide(sub_array,  id+"model"); }
                                };
                displayElement(array,attribute, id)
                hide(array, id)
}
/**
 * populate row element of table, return new labelCell
 */
function populateTable(table, type, key) {
                const row = table.insertRow();
                row.setAttribute("id", type+key);
                const labelCell = row.insertCell();
                labelCell.innerText = key.replaceAll('_', ' ');
                labelCell.className = "popuptitle"
                labelCell.colSpan = 2
                return labelCell
    }
}


const getRandomColor = () => "#" + ((1 << 24) * Math.random() | 0).toString(16).padStart(6, "0");
const ProjectColor = new Map();

let map;

window.onload = function () {
    for (const deployment of DATA) {
        if (ProjectColor.has(deployment.project.id)) continue;
        ProjectColor.set(deployment.project.id, getRandomColor())
    }

  const bounds= [[-200, -200], [200, 200]]
    map = L.map('map', {
        minZoom: 2, zoom: 3,
        zoomControl: true,
        preferCanvas: true,
    }).setView([48.400002, -4.48333], 4.5).setMaxBounds(bounds);

    var url ='https://wms.gebco.net/mapserv?'
    var request;
    if(window.XMLHttpRequest)
       request = new XMLHttpRequest();
    else
       request = new ActiveXObject("Microsoft.XMLHTTP");
    request.open('GET', url, false);
    try {
        request.send();
         if (request.status !== 200) {
            url =' https://tile.openstreetmap.org/{z}/{x}/{y}.png'
        }
    }
    catch (error) {
      url =' https://tile.openstreetmap.org/{z}/{x}/{y}.png'
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

    const geojsonValue = DATA.map(deployment => ({
        type: "Feature",
        properties: {
            deployment,
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
                       <b>Project:</b> ${feature.properties.deployment.project.name}<br>
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
    L.control.scale().addTo(map);
}

