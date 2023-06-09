function addInputFile(){
    let fotoEncargo = document.getElementById("foto-encargo");
    let content = fotoEncargo.innerHTML
    let countFiles = fotoEncargo.children.length
    if (countFiles < 4){
        content += `<input class="form-control-file" type='file' name='foto-encargo-${countFiles}'>`
    } else {
        document.getElementById("errorFoto").innerText = "No puede agregar más fotos"
    }
    fotoEncargo.innerHTML = content;
}

document.addEventListener("DOMContentLoaded", () => {
    const rows = document.querySelectorAll("tr[data-href]");
    rows.forEach(row => {
        row.addEventListener("click", () => {
            window.location.href = row.dataset.href
        })
    })
})

function changeSize(){
    image = document.getElementById("img")
    if (image.width == "640") {
        image.width = "1280"
        image.height = "1024"
    } else {
        image.width = "640"
        image.height = "480"
    }
}
