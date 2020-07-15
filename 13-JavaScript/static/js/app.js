// from data.js
var tableData = data;

// Select the Button
var button = d3.select("#filter-btn");

// Select the form
var form = d3.select("#form");

// Event handlers 
button.on("click", runEnter);
form.on("submit", runEnter);

// Initial Page Load
runEnter();

// Event Handler
function runEnter() {

    // Prevent the page from refreshing
    if (d3.event) {
        d3.event.preventDefault();
    }

    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#datetime");

    // Get the value property of the input element
    var inputValue = inputElement.property("value");

    // Use the form input to filter the data by blood type
    //alert(inputValue);
    var sub_data = tableData;
    if (inputValue !== "") {
        sub_data = tableData.filter(x => x.datetime === inputValue);
    }

    function runStateFilter() {
        var states = [...new Set(tableData.map(x => x.state))];
        states.sort();

        states.forEach(function(state) {
            let stateOptions = `<option>${state}</option>`
            select("#stateFilter").append(stateOptions)
        });
    }




    // Loading Data
    var table = d3.select("#ufo-table");
    table.select('tbody').html("");
    sub_data.forEach(function(ufo) {
        let newRow = table.select("tbody").append("tr");
        Object.entries(ufo).forEach(function([key, value]) {
            newRow.append("td").text(value);
        });
    });
};