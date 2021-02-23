/*
 * webapp.js
 * Matthew Rasmussen, Nacho Rodriguez-Cortes
 * 21 February 2021
 *
 * A little bit of Javascript for the web app sample for CS257.
 */

window.onload = initialize;

function initialize() {
    var element = document.getElementById('spell_list');
    if (true) {
        getSpells;
    }

    var element = document.getElementById('dogs_button');
    if (element) {
        element.onclick = onDogsButton;
    }
}

function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

function getSpells() {
    var url = getAPIBaseURL() + '/spells';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(get_spells) {
        var listBody = '';
        for (var k = 0; k < spells.length; k++) {
            var spell = spells[k];
            listBody += '<li>' + spell['spell_name']
                      + ', ' + spell['spell_description']
                      + '-' + spell['components']
                      + ', ' + spell['ritual'];
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

function onDogsButton() {
    var url = getAPIBaseURL() + '/dogs/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(dogs) {
        var listBody = '';
        for (var k = 0; k < dogs.length; k++) {
            var dog = dogs[k];
            listBody += '<li>' + dog['name']
                      + ', ' + dog['birth_year']
                      + '-' + dog['death_year']
                      + ', ' + dog['description'];
                      + '</li>\n';
        }

        var animalListElement = document.getElementById('animal_list');
        if (animalListElement) {
            animalListElement.innerHTML = listBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}
