$(document).ready(function() {
    $("[data-fancybox='gallery']").fancybox({
        loop: true
    });

    function ziskajPolohu() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(zobraziPocasie, zobrazChybovuHlasku, { enableHighAccuracy: true });
        } else {
            console.log("Geolokácia nie je podporovaná vášim prehliadačom.");
        }
    }

    function zobrazChybovuHlasku(error) {
        console.log("Chyba při získávání polohy: " + error.message);
    }

    function zobraziPocasie(pozicia) {
        var latitude = pozicia.coords.latitude;
        var longitude = pozicia.coords.longitude;
        var apiKluc = "4169ee98ee4362e161d86e3c1223abd3";

        $.get(`https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${apiKluc}&lang=sk`, function(data) {
            var popisPocasia = data.weather[0].description.charAt(0).toLowerCase() + data.weather[0].description.slice(1);
            var teplota = Math.round(data.main.temp - 273.15);
            var mesto = data.name;

            var pocasieElement = document.createElement("div");
            pocasieElement.innerHTML = `${mesto}: ${popisPocasia} ${teplota} °C`;
            pocasieElement.style.position = "fixed";
            pocasieElement.style.top = "10px";
            pocasieElement.style.right = "10px";
            pocasieElement.id = "pocasieElement";

            localStorage.setItem("pocasie", pocasieElement.innerHTML);

            document.body.appendChild(pocasieElement);
        });
    }

    var ulozenyPocasie = localStorage.getItem("pocasie");
    if (ulozenyPocasie) {
        var pocasieElement = document.createElement("div");
        pocasieElement.innerHTML = ulozenyPocasie;
        pocasieElement.style.position = "fixed";
        pocasieElement.style.top = "10px";
        pocasieElement.style.right = "10px";
        pocasieElement.id = "pocasieElement";
        document.body.appendChild(pocasieElement);
    } else {
        ziskajPolohu();
    }
});
