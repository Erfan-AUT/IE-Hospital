function httpGetAsync(theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(JSON.parse(xmlHttp.responseText));
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}

function init_doctor(data) {
    Array.from(document.getElementsByClassName("doctor-name")).forEach((e) => {e.innerHTML = data.name});
    Array.from(document.getElementsByClassName("doctor-speciality")).forEach((e) => {e.innerHTML = data.spec});
    document.getElementById("dr-licence").innerText = "شماره نظام پزشکی: " + data.number;
    document.getElementById("first-date").innerText = data.first_empty_date;
}

function change_tab(classList) {
    console.log(classList);
}

window.onload = () => {    
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');
    httpGetAsync("https://intense-ravine-40625.herokuapp.com/doctors/" + id , init_doctor);
}