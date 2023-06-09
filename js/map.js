
var map = L.map('map').setView([-33.6167, -70.5667], 2).setView(new L.LatLng(20, 0));

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

const viajeIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
  });

const encargoIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
  });

$.get('https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3/cgi-bin/map.py?info=viaje').done(function(response){
    $.each(response, function(key, val){
        let id = val[0]
        let idOrigen = val[1]
        let idDestino = val[2]
        let fecha_ida = new Date(val[3]).toLocaleDateString('cl-ES')
        let fecha_regreso = new Date(val[4]).toLocaleDateString('cl-ES')
        let email = val[7]

        let info = {'id': id, 'fechaIda': fecha_ida, 'fechaRegreso': fecha_regreso, 'email': email}
        getCityName('origen', idOrigen).done(function(cityNameOrigen){
            getCountryCapital().done(function(countryCapitalJSON){
                $.each(countryCapitalJSON, function(key, val){
                    if (val['CapitalName'] == cityNameOrigen) {
                        let latOrigen = val['CapitalLatitude']
                        let longOrigen = val['CapitalLongitude']
                        getCityName('destino', idDestino).done(function(cityNameDestino){
                            getCountryCapital().done(function(countryCapitalJSON){
                                $.each(countryCapitalJSON, function(key, val){
                                    if (val['CapitalName'] == cityNameDestino) {
                                        let latDestino = val['CapitalLatitude']
                                        let longDestino = val['CapitalLongitude']
                                        insertInMap(latOrigen, longOrigen, latDestino, longDestino, info, cityNameOrigen, cityNameDestino, viajeIcon)
                                    }
                                })
                            })
                        })
                    }
                })
            })
        })
    })
})

$.get('https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3/cgi-bin/map.py?info=encargo').done(function(response){
    $.each(response, function(key, val){
        let id = val[0]
        let descripcion = val[1]
        let idOrigen = val[4]
        let idDestino = val[5]
        let email = val[6]

        let info = {'id': id, 'descripcion': descripcion, 'email': email}
        getCityName('origen', idOrigen).done(function(cityNameOrigen){
            getCountryCapital().done(function(countryCapitalJSON){
                $.each(countryCapitalJSON, function(key, val){
                    if (val['CapitalName'] == cityNameOrigen) {
                        let latOrigen = val['CapitalLatitude']
                        let longOrigen = val['CapitalLongitude']
                        getCityName('destino', idDestino).done(function(cityNameDestino){
                            getCountryCapital().done(function(countryCapitalJSON){
                                $.each(countryCapitalJSON, function(key, val){
                                    if (val['CapitalName'] == cityNameDestino) {
                                        let latDestino = val['CapitalLatitude']
                                        let longDestino = val['CapitalLongitude']
                                        insertInMap(latOrigen, longOrigen, latDestino, longDestino, info, cityNameOrigen, cityNameDestino, encargoIcon)
                                    }
                                })
                            })
                        })
                    }
                })
            })
        })
    })
})

var legend = L.control({position: 'bottomleft'});
    legend.onAdd = function () {
        var legendViajes = '<span style="color: green; font-size: large;">&bull;</span> Viajes <br>'
        var legendEncargos = '<span style="color: red; font-size: large;">&bull;</span> Encargos'
        var div = L.DomUtil.create('div', 'info legend');
        div.innerHTML = legendViajes + legendEncargos
    return div;
    };

legend.addTo(map);

function getCountryCapital(){
    return $.get('https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3/country-capitals.json')
}

function getCityName(origenDestino, id){
    return $.get(`https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3/cgi-bin/map.py?info=${origenDestino}&id=${id}`)
}

function insertInMap(latOrigen, longOrigen, latDestino, longDestino, infoViajeEncargo, cityNameOrigen, cityNameDestino, viajeEncargo) {
    var markerOrigen = L.marker([latOrigen, longOrigen], {icon: viajeEncargo}).addTo(map)
    var markerDestino = L.marker([latDestino, longDestino], {icon: viajeEncargo}).addTo(map)
    if (viajeEncargo == viajeIcon) {
        L.polyline([[latOrigen, longOrigen], [latDestino, longDestino]], {color: 'green'}).addTo(map)
        let popup = generatePopupViaje(infoViajeEncargo, cityNameOrigen, cityNameDestino)
        markerOrigen.bindPopup(popup)
        markerDestino.bindPopup(popup)
    } else {
        L.polyline([[latOrigen, longOrigen], [latDestino, longDestino]], {color: 'red'}).addTo(map)
        let popup = generatePopupEncargo(infoViajeEncargo, cityNameOrigen, cityNameDestino)
        markerOrigen.bindPopup(popup)
        markerDestino.bindPopup(popup)
    }
}

function generatePopupViaje(infoViaje, cityNameOrigen, cityNameDestino){
    let idLine = `<b>ID Viaje:</b> ${infoViaje['id']}<br>`
    let cities = `<b>Origen:</b> ${cityNameOrigen}&nbsp;&nbsp;&nbsp;&nbsp;<b>Destino:</b> ${cityNameDestino}<br>`
    let fechas = `<b>Fecha Ida:</b> ${infoViaje['fechaIda']}&nbsp;&nbsp;&nbsp;&nbsp;<b>Fecha Regreso:</b> ${infoViaje['fechaRegreso']}<br>`
    let emailLine = `<b>Email:</b> ${infoViaje['email']}<br>`
    return idLine + cities + fechas + emailLine
}

function generatePopupEncargo(infoEncargo, cityNameOrigen, cityNameDestino){
    let idLine = `<b>ID Viaje:</b> ${infoEncargo['id']}<br>`
    let cities = `<b>Origen:</b> ${cityNameOrigen}&nbsp;&nbsp;&nbsp;&nbsp;<b>Destino:</b> ${cityNameDestino}<br>`
    let descripcion = `<b>Descripción:</b> ${infoEncargo['descripcion']}<br>`
    let emailLine = `<b>Email:</b> ${infoEncargo['email']}<br>`
    return idLine + cities + descripcion + emailLine
}