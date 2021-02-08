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
    Array.from(document.getElementsByClassName("doctor-name")).forEach(e => { e.innerHTML = data.name });
    Array.from(document.getElementsByClassName("doctor-speciality")).forEach(e => { e.innerHTML = data.spec });
    document.getElementById("dr-licence").innerText = "شماره نظام پزشکی: " + data.number;
    document.getElementById("first-date").innerText = data.first_empty_date;

    const doc_times = document.getElementsByClassName("tabcontent doc-times")[0];
    const success = doc_times.getElementsByClassName("svg-success")[0];
    const fail = doc_times.getElementsByClassName("svg-fail")[0];
    success.setAttribute("display", "show");
    fail.setAttribute("display", "show");
    doc_times.removeChild(success);
    doc_times.removeChild(fail);
    for (let i = 0; i < data.week_days.length; i++) {
        if (data.week_days[i]) {
            doc_times.getElementsByClassName("date-" + i)[0].appendChild(success.cloneNode(true));
        }
        else {
            doc_times.getElementsByClassName("date-" + i)[0].appendChild(fail.cloneNode(true));
        }
    }

    document.getElementsByClassName("dr-office-address")[0].getElementsByTagName("p").innerText = data.address;
    document.getElementsByClassName("dr-office-phone")[0].innerText = data.phone;
    document.getElementsByClassName("dr-experience-years")[0].innerText = data.experience_years + " سال";
    if (data.online_pay) {
        document.getElementsByClassName("dr-online-pay")[0].innerText = "دارد";
    }
    else {
        document.getElementsByClassName("dr-online-pay")[0].innerText = "ندارد";
    }

    document.getElementsByClassName("commenter")[0].innerText = "نظر " + data.commenter + ": ";
    document.getElementById("rating-count").innerText = data.rate;
    const star_list = document.getElementsByClassName("rating-stars")[0];
    for (let i = 0; i < Math.ceil(5-data.stars); i++) {
        star_list.removeChild(star_list.lastElementChild);
    }
    document.getElementsByClassName("comment")[0].innerText = data.comment_text;
    document.getElementsByClassName("commenter-count")[0].innerText = "از " + data.comments + " نظر";
}

function change_tab(element) {
    if (element.id != "current-tab") {
        const tabs = Array.from(document.getElementsByClassName("dr-office-tablinks"));
        const otherButton = tabs.filter(e => e.classList != element.classList)[0];
        otherButton.removeAttribute("id");
        element.setAttribute("id", "current-tab");
        document.getElementsByClassName(element.classList[1])[1].classList.remove("tabcontent-hidden");
        document.getElementsByClassName(otherButton.classList[1])[1].classList.add("tabcontent-hidden");
    }

}

window.onload = () => {
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');
    httpGetAsync("https://intense-ravine-40625.herokuapp.com/doctors/" + id, init_doctor);
}