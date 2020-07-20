function unpack(rows, index) {
    return rows.map(function(row) {
        return row[index]
    });
};

getData();

var sampleId = d3.select("#selDataset").node().value;

function getData(sampleId) {
    d3.json("./samples.json").then(function(sampleData) {
        var name = sampleData.names;
        //Creating drop-down:
        var dropDown = d3.select("#selDataset")
        name.forEach(element => {
            //append dropown with options
            dropDown.append('option').text(element).property("value", element)
        });
    });
}

function getMetaData(sampleId) {
    d3.json("./samples.json").then(function(sampleData) {
        var metaData = sampleData.metadata.filter(x => x.id == sampleId)[0];
        console.log(metaData)

        d3.select('#sample-metadata').html("")

        Object.entries(metaData).forEach(function([key, value]) {
            //let info = `<p><b>${key}</b> : ${value} </p>`;
            //d3.select('#sample-metadata').append(info);
            d3.select('#sample-metadata').append("p").text(`${key}:${value}`);
        });
    });
}

function plotBar(sampleId) {
    d3.json("./samples.json").then(function(sampleData) {
        let dataSamples = sampleData.samples[0];
        let plotData = dataSamples["otu_ids"].map(function(e, i) {
            return [e, dataSamples["sample_values"][i]];
        });
        let plotDataSorted = plotData.sort((a, b) => b[1] - a[1]);
        x = plotDataSorted.map(x => x[1]).slice(0, 10).reverse()
        y = plotDataSorted.map(x => "OTU " + x[0]).slice(0, 10).reverse()

        var traceBar = [{
            type: 'bar',
            x: x,
            y: y,
            orientation: 'h'
        }];

        var layoutBar = {
            title: 'OTU Ids to Values'
        };

        Plotly.newPlot('bar', traceBar, layoutBar)

    })
}

function plotBubble(sampleId) {
    d3.json("./samples.json").then(function(sampleData) {
        var bubbleData = sampleData.samples.filter(x => x.id === sampleId)[0];

        var traceBubble = [{
            mode: 'markers',
            x: bubbleData.otu_ids,
            y: bubbleData.sample_values,
            marker: {
                size: bubbleData.sample_values
            }
        }];

        var data = [traceBubble]

        var layoutBubble = {
            title: 'OTU Ids to Values',
            showlegend: false,
        };

        Plotly.newPlot('bubble', data, layoutBubble)

    })
}

function plotGuage(sampleId) {
    d3.json("./samples.json").then(function(sampleData) {
        let guageData = sampleData.metadata.filter(x => x.id == sampleId)[0];
        let allWashFreq = sampleData.metadata.map(x => x.wfreq);
        let washFreq = guageData.wfreq;
        console.log(allWashFreq)

        let avg = (array) => array.reduce((a, b) => a + b) / array.length;

        var traceGuage = {
            type: "indicator",
            mode: "guage+number+delta",
            value: guageData.wfreq,
            delta: { reference: avg(allWashFreq), increasing: { color: "RebeccaPurple" } },
            guage: {
                axis: { range: [Math.min(allWashFreq), Math.max(allWashFreq)], tickwidth: 2, tickcolor: "darkblue" },
                bar: { color: "darkblue" },
                bgcolor: "white",
                borderwidth: 2,
                bordercolor: "gray",
                steps: [
                    { range: [Math.min(allWashFreq), Math.max(allWashFreq)], color: "cyan" }
                ],
                threshold: {
                    line: { color: "red", width: 4 },
                    thickness: 0.75,
                    value: guageData.wfreq
                }
            }
        }
        var guage = [traceGuage];

        var layoutGuage = {
            title: "Belly Button Wash Frequency \n Compared to Sample Average"
        };

        Plotly.newPlot('gauge', guage, layoutGuage);

    });
}


function optionChanged(sampleId) {
    getData(sampleId);
    getMetaData(sampleId);
    plotBar(sampleId);
    plotBubble(sampleId);
    plotGuage(sampleId);
};