function httpGetAsync(theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(JSON.parse(xmlHttp.responseText));
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}

function init_doctors(data) {
    const first_doc = document.getElementsByClassName("doctor-detail-a")[0];
    const doc_list = document.getElementsByClassName("doctors-list")[0];
    for (let index = 1; index < data.length; index++) {
        const new_node = first_doc.cloneNode(true);
        doc_list.appendChild(new_node);
    }

    for (let i = 0; i < doc_list.children.length; i++) {
        const el = doc_list.children[i];
        const el_url = el.getAttribute("href");
        el.setAttribute("href", el_url + "?id=" + data[i].id);
        // const img_element = dr_el.firstElementChild;
        // img_element.firstElementChild.src = data[i].avatar;
        el.getElementsByClassName("doctor-image")[0].firstElementChild.src = data[i].avatar;

        const detail_element = el.getElementsByClassName("doctor-detail-name")[0];
        detail_element.getElementsByTagName("h3")[0].innerHTML = data[i].name;
        detail_element.getElementsByTagName("h4")[0].innerHTML = data[i].spec;
        detail_element.getElementsByTagName("p")[0].innerHTML = `( ${data[i].comments} نظر)`;

        el.getElementsByClassName("doctor-location")[0].innerHTML = data[i].location;
        el.getElementsByClassName("doctor-experience")[0].innerHTML = `تجربه: ${data[i].experience_years} سال`;
        el.getElementsByClassName("doctor-popularity")[0].innerHTML = `${data[i].user_percent} درصد رضایت ملت`;
        el.getElementsByClassName("first-reserve-time")[0].innerHTML = `اولین وقت خالی: ${data[i].first_empty_date}`;

        el.getElementsByClassName("doctor-comment")[0].innerHTML = data[i].comment_text;
        el.setAttribute("stars", data[i].stars);

        for (let j = 1; j < data[i].stars + 1; j++) {
            el.getElementsByClassName("star" + j)[0].style.color = "#deb217";
        }
    }
}

function compare_doctor_nodes(a, b) {
    if (a.getAttribute("stars") < b.getAttribute("stars")) {
        return -1;
    }
    else if (a.getAttribute("stars") > b.getAttribute("stars")) {
        return 1;
    }
    return 0;
}

window.onload = () => {
    httpGetAsync("https://intense-ravine-40625.herokuapp.com/doctors", init_doctors);
    document.getElementsByClassName("sort-by-stars")[0].onclick = () => {
        const doc_list = document.getElementsByClassName("doctors-list")[0];
        const doc_nodes = doc_list.children;
        const doctors = [];
        for (let i = 0; i < doc_nodes.length; i++) {
            doctors.push(
                doc_nodes[i].cloneNode(true)
            );
        }
        doc_list.textContent = "";
        doctors.sort(compare_doctor_nodes);
        doctors.forEach((e) => {
            doc_list.appendChild(e);
        });
        console.log("mamad!");
    }
}