/*
 * webapp.js
 * Matthew Rasmussen, Nacho Rodriguez-Cortes
 * 21 February 2021
 *
 * A little bit of Javascript for the web app sample for CS257.
 */

window.onload = initialize;

function initialize() {
    var class_name = get_class();
    console.log(class_name)
    get_spells_for_class(class_name);
}

function get_class() {
    var pathname = window.location.pathname;
    var paths = pathname.split('/');
    for (path in paths) {
        if (path == 'api'){
            continue;
        }
        else if (path == 'spells') {
            continue;   
        }
        else if (path == 'classes') {
            continue;
        }
        else {
            var class_name = path;
        }
    }
    return class_name;
}

function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

function get_spells() {
    var url = getAPIBaseURL() + '/spells';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(spells) {
        var listBody = '';
        for (var k = 0; k < spells.length; k++) {
            var spell = spells[k];
            listBody += '<li>' + spell['spell_name']
                      + ', ' + spell['spell_description']
                      + '-' + spell['components']
                      + ', ' + spell['ritual']
                      + '</li>\n';
        }

        var spellListElement = document.getElementById('spell_list');
        if (spellListElement) {
            spellListElement.innerHTML = listBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}

function get_spells_for_class(class_name) {
    var url = getAPIBaseURL() + '/spells/classes/' +  class_name;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(spells) {
        var listBody = '';
        for (var k = 0; k < spells.length; k++) {
            var spell = spells[k];
            listBody += '<li>' + spell['spell_name']
                      + ', ' + spell['spell_description']
                      + '-' + spell['components']
                      + ', ' + spell['ritual']
                      + '</li>\n';
        }

        var spellListElement = document.getElementById('spell_list');
        if (spellListElement) {
            spellListElement.innerHTML = listBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}





}
