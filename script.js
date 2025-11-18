const enviar = document.getElementById("enviar");
const mostrar = document.getElementById("mostrar");
const name = document.getElementById("name");
const id = document.getElementById("id");



function enviarDatos() {
  if (name.value !== "" && id.value !== "") {
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
  
  else {
    alert("Por favor, completa todos los campos.");
  }
}

enviar.addEventListener("click", enviarDatos);

// Leer datos desde Python
fetch("http://127.0.0.1:8000/cargar_usuario")
  .then(response => response.json())
  .then(data => {
    console.log("Datos desde Python:", data);

    for (let i = 0; i < data.length; i++) {
      const nuevoElemento = document.createElement('li');
      nuevoElemento.textContent = data[i].name;
      mostrar.appendChild(nuevoElemento); 
    }
    
  })