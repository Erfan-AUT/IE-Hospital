function add_href_cards() {
    const cards = document.getElementsByClassName("specialty-card-a");
    console.log("kossher");
    
    for (var i = 0, max = cards.length; i < max; i++) {
        cards[i].setAttribute('href', 'dr-list.html');
    }
}

window.onload = () => {
    add_href_cards();
}