function mostrarQR() {
    var textInput = document.getElementById("textqr").value;
    console.log(textInput)

    fetch("/generator", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ textInput: textInput })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "qrcode_generated") {
            console.log(data.arquivo)
            swal.fire({
                html: `<img src="../../static/src/${data.arquivo}" alt="">`,
            })
        }
    });
}

document.querySelector('.btn').addEventListener('click', mostrarQR);