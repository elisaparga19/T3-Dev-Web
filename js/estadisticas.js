function generateChart(data, ticks, title, xlabel, ylabel) {
    let dataset = [{label: `${title}`, data: data, color: "#5482FF"}]
    let options = {
        series: {
            bars: {
                show: true
            }
        },
        bars: {
            align: "center",
            barWidth: 0.5,
        },
        xaxis: {
            axisLabel: `${xlabel}`,
            axisLabelUseCanvas: true,
            axisLabelFontSizePixels: 12,
            axisLabelFontFamily: 'Verdana, Arial',
            axisLabelPadding: 10,
            autoscaleMargin: 0.1,
            ticks: ticks
        },
        yaxis: {
            axisLabel: `${ylabel}`,
            axisLabelUseCanvas: true,
            axisLabelFontSizePixels: 12,
            axisLabelFontFamily: 'Verdana, Arial',
            autoscaleMargin: 0.1,
            axisLabelPadding: 3
        },
        grid: {
            hoverable: true,
            borderWidth: 2,
            borderColor: "#633200",
            backgroundColor: { colors: ["#ffffff", "#EDF5FF"] }
        },
        colors: ["#FF0000", "#0022FF"]
    }
    return {"dataset": dataset, "options": options}
}

function getKilos() {
    return $.get('https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3/cgi-bin/estadisticas.py?info=kilos')
}

function getEspacio() {
    return $.get('https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3/cgi-bin/estadisticas.py?info=espacio')
}

function generateDict(array) {
    let dict = {}
    let counter = 1
    for (element in array){
        dict[counter] = 0
        counter += 1
    }
    return dict
}

getKilos().done(function(response){
    let ticks_kilos = response
    let viajes_kilos = generateDict(ticks_kilos)
    
    getEspacio().done(function(response){
        let ticks_espacio = response
        let viajes_espacio = generateDict(ticks_espacio)
        $.get('https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3/cgi-bin/estadisticas.py?info=viaje').done(function(response){
            $.each(response, function(key, val){
                viajes_espacio[val[6]] += 1
                viajes_kilos[val[5]] += 1
            })

            let data_espacio = Object.entries(viajes_espacio)
            let data_kilos = Object.entries(viajes_kilos)

            let dataset_espacio = generateChart(data_espacio, ticks_espacio, "Viajes por Espacio", "Espacio", "Viajes")["dataset"]
            let options_espacio = generateChart(data_espacio, ticks_espacio, "Viajes por Espacio", "Espacio", "Viajes")["options"]
            
            let dataset_kilos = generateChart(data_kilos, ticks_kilos, "Viajes por Kilos", "Kilos", "Viajes")["dataset"]
            let options_kilos = generateChart(data_kilos, ticks_kilos, "Viajes por Kilos", "Kilos", "Viajes")["options"]

            $(document).ready(function () {
                $.plot($("#viaje-espacio"), dataset_espacio, options_espacio);
            });
            $(document).ready(function () {
                $.plot($("#viaje-kilos"), dataset_kilos, options_kilos);
            });
        })
    })
})

getKilos().done(function(response){
    let ticks_kilos = response
    let encargo_kilos = generateDict(ticks_kilos)
    
    getEspacio().done(function(response){
        let ticks_espacio = response
        let encargo_espacio = generateDict(ticks_espacio)
        $.get('https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3/cgi-bin/estadisticas.py?info=encargo').done(function(response){
            $.each(response, function(key, val){
                encargo_espacio[val[2]] += 1
                encargo_kilos[val[3]] += 1
            })
        
            let data_espacio = Object.entries(encargo_espacio)
            let data_kilos = Object.entries(encargo_kilos)
        
            let dataset_espacio = generateChart(data_espacio, ticks_espacio, "Encargos por Espacio", "Espacio", "Encargos")["dataset"]
            let options_espacio = generateChart(data_espacio, ticks_espacio, "Encargos por Espacio", "Espacio", "Encargos")["options"]
            
            let dataset_kilos = generateChart(data_kilos, ticks_kilos, "Encargos por Espacio", "Kilos", "Encargos")["dataset"]
            let options_kilos = generateChart(data_kilos, ticks_kilos, "Encargos por Espacio", "Kilos", "Encargos")["options"]
        
            $(document).ready(function () {
                $.plot($("#encargo-espacio"), dataset_espacio, options_espacio);
            });
            $(document).ready(function () {
                $.plot($("#encargo-kilos"), dataset_kilos, options_kilos);
            });
        })

    })
})
