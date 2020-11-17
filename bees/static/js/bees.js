//query per gestire il modal della cookie policy
$(document).ready(function(){
    var cook1 = getCookie()
    console.log(cook1)
    if (cook1 != "yes") {
       setTimeout(function(){
          $('#cookie_modal').modal('show');
       }, 2000);
       setCookie()
    }
 })
 
 function setCookie() {
    document.cookie = "accepted=yes; path=/";
 }
 
 function getCookie() {
    var decodedCookie = decodeURIComponent(document.cookie);
    var cookieList = decodedCookie.split(";");
    console.log(cookieList)
    var firstCookie = cookieList[0].split("=");
    console.log(firstCookie)
    var cookieResponse = firstCookie[1];
    console.log(cookieResponse)
    return cookieResponse
 }
 
 //funzione per far comparire il modal dei cookies all'onclick nel footer
 $('#policy').click(function(){
    $('#cookie_modal').modal('show');
 });