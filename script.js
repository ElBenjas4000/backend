const enviar = document.getElementById("enviar");
const mostrar = document.getElementById("mostrar");
const name = document.getElementById("name");
const id = document.getElementById("id");


function enviarDatos() {
    fetch("http://127.0.0.1:8000/enviar_usuario", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({name: name.value, id: id.value})})
    .then(response => response.json())
    .then(result => {
        console.log("Respuesta del servidor:", result);
        name.value = "";
        id.value = "";
    });
}

enviar.addEventListener("click", enviarDatos);

// Leer datos desde Python
fetch("http://127.0.0.1:8000/cargar_usuario")
  .then(response => response.json())
  .then(data => {
    console.log("Datos desde Python:", data);
    mostrar.innerHTML = JSON.stringify(data);
  });