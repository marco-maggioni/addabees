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

//funzione che permette di mostrare solo un tipo di miele alla volta cliccando sul link nella tab
function openTab(idMiele, idBtn) {
    var i;
    var tipoMiele = document.getElementsByClassName("miele");
    var btns = document.getElementsByClassName("nav-link");
    for (i = 0; i < tipoMiele.length; i++) {
      tipoMiele[i].style.display = "none";  
    }
    for (i = 0; i < btns.length; i++) {
        btns[i].classList.remove("active");
    }
    document.getElementById(idMiele).style.display = "block";  
    document.getElementById(idBtn).classList.add("active"); //aggiungo la classe bootstrap "active"
  }