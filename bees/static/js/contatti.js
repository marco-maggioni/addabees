//durante il caricamento imposto il margin auto del div del campo recaptcha
window.onload = function() {
    recaptcha_div = document.getElementById('recaptcha');
    recaptcha_div.childNodes[5].children[0].style.margin = "auto";
}

scrollPosition = window.pageYOffset  //recupero la posizione dello scoll verticale in px
//imposto la navabar a scomparsa
function navScroll() {
    currentScrollPosition = window.pageYOffset
    if (scrollPosition > currentScrollPosition) {
        document.getElementById('navbar').style.display = "block"
    } else {
        document.getElementById('navbar').style.display = "none"
    }
    scrollPosition = currentScrollPosition
}

window.onscroll = function() {
    navScroll();
};