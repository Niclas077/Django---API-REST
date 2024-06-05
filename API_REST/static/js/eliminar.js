(function () {
    btndelete.addEventListener("click", function(event){ // Corregir
        event.preventDefault();
        Swal.fire({
          title: "Desea eliminar el registro?",
          showCancelButton: true,
          confirmButtonText: "Eliminar",
          confirmButtonColor: "#d33",
          backdrop: false,
          showLoaderOnConfirm: true,
          preconfirm: () =>{
            return new Promise((resolve)=>{
              resolve();
            });
          },
          allowsOutsideClick: () => false,
        }).then((result) => {
          if (result.isConfirmed) {
            document.getElementById('deleteForm').submit()
          }
        });
      });
})();