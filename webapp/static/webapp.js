/*
 * webapp.js
 * Matthew Rasmussen, Nacho Rodriguez-Cortes
 * 21 February 2021
 *
 * A little bit of Javascript for the web app sample for CS257.
 */


document.getElementById('Spells').addEventListener('click', get_spells);
document.getElementById('Bard').addEventListener('click', function() {get_spells_for_class('Bard')});
document.getElementById('Cleric').addEventListener('click', function() {get_spells_for_class('Cleric')});
document.getElementById('Druid').addEventListener('click', function() {get_spells_for_class('Druid')});
document.getElementById('Paladin').addEventListener('click', function() {get_spells_for_class('Paladin')});
document.getElementById('Ranger').addEventListener('click', function() {get_spells_for_class('Ranger')});
document.getElementById('Sorcerer').addEventListener('click', function() {get_spells_for_class('Sorcerer')});
document.getElementById('Wizard').addEventListener('click', function() {get_spells_for_class('Wizard')});
document.getElementById('Warlock').addEventListener('click', function() {get_spells_for_class('Warlock')});
document.getElementById('equipment').addEventListener('click', get_equipment);

var sideBar = document.getElementById("side_bar");
var bttns = sideBar.getElementsByClassName("bttn");

for (var i = 0; i < bttns.length; i++) {
    bttns[i].addEventListener('click', function () {
        //checking what button is active
        var current = document.getElementsByClassName("active");
        if (current.length > 0) {
            var button_id = current[0].id;
            current[0].className = current[0].className.replace(" active", "");
            var visible_table = document.getElementById(button_id + '_visibility');
            visible_table.classList.add("hidden");
        }
        this.className += " active";
        
        //showing the correct table
        var new_visible_table = document.getElementById(this.id+'_visibility');
        new_visible_table.classList.remove("hidden");
   });
}

function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}
/*
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
*/
/*
$(document).ready( function() {
    var baseurl = getAPIBaseURL() + '/spells/classes/';
    var api_list = ['Bard', 'Cleric', 'Druid', 'Paladin', 'Ranger', 'Sorcerer', 'Wizard', 'Warlock'];
    var xmlhttp = new XMLHttpRequest();
    for (var name of api_list){
        console.log(name);
        xmlhttp.open('GET', baseurl+name, true);
        xmlhttp.onreadystatechange = function(){
            if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
                console.log(name);
                var spell = JSON.parse(xmlhttp.responseText);
                console.log(spell);
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
        if ($.fn.dataTable.isDataTable('#'+name)){
           console.log(name);
        }
    }     
});
*/
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
        if ($.fn.dataTable.isDataTable('#Spells_table')){
            //pass        
        } 
        else{
            var xmlhttp = new XMLHttpRequest();
            xmlhttp.open('GET', baseurl+'/spells', true);
            xmlhttp.onreadystatechange = function(){
                if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
                    var spell = JSON.parse(xmlhttp.responseText);
                    $('#Spells_table').DataTable( {
                        data : spell,
                        'columns':[
                            {'data':'spell_name',
                             'render':function(data){
                              data = '<a href=/api/spells/classes/bard>' + data + '</a>';
                              return data;
                            }
                            },
                            {'data':'spell_level'},
                            {'data':'casting_time'},
                            {'data':'ritual'}
                        ]
                    });
                }
            }  
    xmlhttp.send(); 
        }
        var contentLabelElement = document.getElementById('content_label');
        contentLabelElement.innerHTML = 'All spells';
        var spellListElement = document.getElementById('spell_list');
        if (spellListElement) {
            spellListElement.innerHTML = listBody;
        }
 
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
        if ($.fn.dataTable.isDataTable('#' + class_name + '_table')){
            //pass         
        } 
        else{
            var xmlhttp = new XMLHttpRequest();
            xmlhttp.open('GET', url, true);
            xmlhttp.onreadystatechange = function(){
                if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
                    var spell = JSON.parse(xmlhttp.responseText);
                    $('#'+class_name+'_table').DataTable( {
                        data : spell,
                        'columns':[
                            {'data':'spell_name',
                             'render':function(data){
                              data = '<a href=/api/spells/classes/bard>' + data + '</a>';
                              return data;
                            }
                            },
                            {'data':'spell_level'},
                            {'data':'casting_time'},
                            {'data':'ritual'}
                        ]
                    });
                }
            }  
    xmlhttp.send(); 
        }
        var contentLabelElement = document.getElementById('content_label');
        contentLabelElement.innerHTML = class_name + ' spells';
        var spellListElement = document.getElementById('spell_list');
        if (spellListElement) {
            spellListElement.innerHTML = listBody;
        }
 
        }
    )

    .catch(function(error) {
        console.log(error);
    });
}

function get_spell_information(spell_name){
    var url = getAPIBaseURL() + '/spells/' +  spell_name;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(spell) {
        var baseurl = getAPIBaseURL();
        var Body = '';
        for (var k = 0; k < spell.length; k++) {
            var spell_element = spell[k];
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
 
        }
    )

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
