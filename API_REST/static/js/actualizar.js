document.addEventListener("DOMContentLoaded", () => {
  btnBuscar.addEventListener("click", () => {
    const id = document.getElementById("txtid").value;
    if (id) {
      fetch(`/api/Vehiculos/${id}/`)
        .then((response) => response.json())
        .then((data) => {
          if (data) {
            console.log(data);
            document.getElementById("VhTabla").style.display = "table";
            document.getElementById("vehiculoid").value = data.id;
            document.getElementById("vehiculomarca").value = data.marca;
            document.getElementById("vehiculoanyo").value = data.anyo;
            document.getElementById("vehiculocolor").value = data.color;
          } else {
            console.log("Vehiculo encontrado");
          }
        })
        .catch((error) => console.error("Error", error));
    }
  });
});
