scrollPosition = window.pageYOffset  //recupero la posizione dello scoll verticale in px

window.onscroll = function() {
    navScroll();
};

function navScroll() {
    currentScrollPosition = window.pageYOffset
    if (scrollPosition > currentScrollPosition) {
        document.getElementById('navbar').style.display = "block"
    } else {
        document.getElementById('navbar').style.display = "none"
    }
    scrollPosition = currentScrollPosition
}

function piante_scopri_più() {
    var button = document.getElementById('buttonPic');
    var divTxt = document.getElementById('desc_piante');
    if (button.style.display = "block") {
      button.style.display = "none"
      divTxt.style.display = "block"
    }
}

function piante_scopri_meno() {
    var close_txt = document.getElementById('close_txt');
    var button = document.getElementById('buttonPic');
    var namePic = document.getElementById('namePic');
    close_txt.parentNode.style.display = "none";
    button.style.display = "block";
    button.style.margin = "auto";
    namePic.style.marginTop = "5px";
}