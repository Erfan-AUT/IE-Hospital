function httpGetAsync(theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(JSON.parse(xmlHttp.responseText));
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    // xmlHttp.setRequestHeader("Access-Control-Allow-Origin", "*");
    xmlHttp.send(null);
}

var spec_list = [];

function get_specs(data) {
    console.log(data);
    spec_list = data;
    data.forEach(element => {
        document.getElementById("specs-list").innerText += element.id + ": " + element.name;
    });
}

function signup() {
    phone = document.getElementById("phone").innerText;
    username = document.getElementById("username").innerText;
    name = document.getElementById("name").innerText;
    pay = document.getElementById("online-pay").innerText;
    experience = document.getElementById("experience").innerText;
    address = document.getElementById("address").innerText;
    spec = document.getElementById("spec").innerText;
    week_days = JSON.parse(document.getElementById("week-days").innerText);
    week_days_bool = [];
    week_days.forEach(element => {
        if (element == "1") {
            week_days_bool.add(true);
        }
        else {
            week_days_bool.add(false)
        }
    });
    httpGetAsync("");

}

window.onload = () => {
    httpGetAsync("http://localhost:8000/spec/", get_specs);
}