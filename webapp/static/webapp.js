/*
 * webapp.js
 * Matthew Rasmussen, Nacho Rodriguez-Cortes
 * 21 February 2021
 *
 * A little bit of Javascript for the web app sample for CS257.
 */


document.getElementById('spells').addEventListener('click', get_spells);
document.getElementById('bard').addEventListener('click', function() {get_spells_for_class('Bard')});
document.getElementById('cleric').addEventListener('click', function() {get_spells_for_class('Cleric')});
document.getElementById('druid').addEventListener('click', function() {get_spells_for_class('Druid')});
document.getElementById('paladin').addEventListener('click', function() {get_spells_for_class('Paladin')});
document.getElementById('ranger').addEventListener('click', function() {get_spells_for_class('Ranger')});
document.getElementById('sorcerer').addEventListener('click', function() {get_spells_for_class('Sorcerer')});
document.getElementById('wizard').addEventListener('click', function() {get_spells_for_class('Wizard')});
document.getElementById('warlock').addEventListener('click', function() {get_spells_for_class('Warlock')});
document.getElementById('equipment').addEventListener('click', get_equipment);

var sideBar = document.getElementById("side_bar");
var bttns = sideBar.getElementsByClassName("bttn");

for (var i = 0; i < bttns.length; i++) {
    bttns[i].addEventListener('click', function () {
        var current = document.getElementsByClassName("active");
        if (current.length > 0) {
            current[0].className = current[0].className.replace(" active", "");
        }
        this.className += " active";
    });
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

$(document).ready( function() {
    var baseurl = getAPIBaseURL();
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open('GET', baseurl+'/spells', true);
    xmlhttp.onreadystatechange = function(){
        if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
            var spell = JSON.parse(xmlhttp.responseText);
            $('#example').DataTable( {
                data : spell,
                'columns':[
                    {'data':'spell_name'},
                    {'data':'spell_level'},
                    {'data':'casting_time'},
                    {'data':'ritual'}
                ]
            });
        }
    }  
    xmlhttp.send();     
});


$(document).ready( function() {
    var baseurl = getAPIBaseURL() + '/spells/classes/';
    var api_list = ['bard', 'cleric', 'druid', 'paladin', 'ranger', 'sorcerer', 'wizard', 'warlock']
    var xmlhttp = new XMLHttpRequest();
    for (name in api_list){
        xmlhttp.open('GET', baseurl+name, true);
        xmlhttp.onreadystatechange = function(){
            if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
                console.log(name);
                var spell = JSON.parse(xmlhttp.responseText);
                $('#' + name).DataTable( {
                    data : spell,
                    'columns':[
                        {'data':'spell_name'},
                        {'data':'spell_level'},
                        {'data':'casting_time'},
                        {'data':'ritual'}
                    ]
                });
            }
        }  
        xmlhttp.send();
    }     
});

/*
function get_spells() {
    var url = getAPIBaseURL() + '/spells';

    fetch(url, {method: 'get'})

    .then((response) => response.json())


    .then(function(spells) {
        var listBody = '';
        for (var k = 0; k < spells.length; k++) {
            var spell = spells[k];
            listBody += '<li>' + spell['spell_name']
                      + ', ' + spell['spell_level']
                      + '-' + spell['casting_time']
                      + ', ' + spell['ritual']
                      + '</li>\n';
        }

        var contentLabelElement = document.getElementById('content_label');
        contentLabelElement.innerHTML = 'All spells';
        var spellListElement = document.getElementById('spell_list');
        if (spellListElement) {
            spellListElement.innerHTML = listBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}
*/

function get_spells() {
    var url = getAPIBaseURL() + '/spells';

    fetch(url, {method: 'get'})

    .then((response) => response.json())
    
    .then(function(spells) {
        var baseurl = getAPIBaseURL();
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.open('GET', baseurl+'/spells', true);
        if ($.fn.dataTable.isDataTable('#example')){
            //pass        
            var table = document.getElementsByClassName("table table-striped table-bordered")[0];
            var tableId = table.id;
            tableId = hide;
 
        } 
        else{
            xmlhttp.onreadystatechange = function(){
                if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
                    var spell = JSON.parse(xmlhttp.responseText);
                    $('#example').DataTable( {
                        data : spell,
                        'columns':[
                            {'data':'spell_name'},
                            {'data':'spell_level'},
                            {'data':'casting_time'},
                            {'data':'ritual'}
                        ]
                    });
                }
            }  
        }
    xmlhttp.send(); 
        }
    )

    .catch(function(error) {
        console.log(error);
    });
}

/*
function get_spells_for_class(class_name) {
    var url = getAPIBaseURL() + '/spells/classes/' +  class_name;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(spells) {
        var listBody = '';
        for (var k = 0; k < spells.length; k++) {
            var spell = spells[k];
            listBody += '<li>' + spell['spell_name']
                      + ', ' + spell['spell_level']
                      + '-' + spell['casting_time']
                      + ', ' + spell['ritual']
                      + '</li>\n';
        }
        
        var contentLabelElement = document.getElementById('content_label');
        contentLabelElement.innerHTML = class_name + ' spells';
        var spellListElement = document.getElementById('spell_list');
        if (spellListElement) {
            spellListElement.innerHTML = listBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}
*/

function get_spells_for_class(class_name) {
    var url = getAPIBaseURL() + '/spells/classes/' +  class_name;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(spells) {
        var baseurl = getAPIBaseURL();
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.open('GET', url, true);
        xmlhttp.onreadystatechange = function(){
        if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
            var spell = JSON.parse(xmlhttp.responseText);
            $('#'+ class_name).DataTable( {
                data : spell,
                'columns':[
                    {'data':'spell_name'},
                    {'data':'spell_level'},
                    {'data':'casting_time'},
                    {'data':'ritual'}
                ]
            });
        }
        //var table = document.getElementsByClassName("table table-striped table-bordered")[0];
        //var tableId = table.id;
        //tableId = class_name;
        //console.log(tableId); 
    }  
    xmlhttp.send(); 
        }
    )

    .catch(function(error) {
        console.log(error);
    });
}


function get_equipment() {
    var url = getAPIBaseURL() + '/equipment';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(equipments) {
        var listBody = '';
        for (var k = 0; k < equipments.length; k++) {
            var equipment = equipments[k];
            listBody += '<li>' + equipment['tool_name']
                      + ', ' + equipment['tool_cost']
                      + ', ' + equipment['tool_weight']
                      + '</li>\n';
        }
        var contentLabelElement = document.getElementById('content_label');
        contentLabelElement.innerHTML = 'Equipment';
        var spellListElement = document.getElementById('spell_list');
        if (spellListElement) {
            spellListElement.innerHTML = listBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });

}
