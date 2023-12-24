function domReady(fn) {
    if (
        document.readyState === "complete" ||
        document.readyState === "interactive"
    ) {
        setTimeout(fn, 1000);
    } else {
        document.addEventListener("DOMContentLoaded", fn);
    }
}

domReady(function () {

    // If found you qr code
    function onScanSuccess(decodeText, decodeResult) {
        alert("Confime los datos escaneados en el formulario de abajo");
        document.getElementById('id_codigoQR').value= decodeText, decodeResult
        document.getElementById('id_lote').value= decodeText.substr(decodeText.length - 9)
        document.getElementById('id_fecha_vencimiento').value= decodeText.substr(decodeText.length -13, 2) + '-' + decodeText.substr(decodeText.length -15, 2) + '-20' + decodeText.substr(decodeText.length -17, 2)
    }

    let htmlscanner = new Html5QrcodeScanner(
        "my-qr-reader",
        { fps: 10, qrbos: undefined, aspectRatio: 2 }
    );
    htmlscanner.render(onScanSuccess);
});