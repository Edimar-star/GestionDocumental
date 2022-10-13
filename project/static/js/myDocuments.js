const productos = window.data.products;
const archivos = window.data.archivos;
const cliente = window.data.cliente;
const options = document.getElementsByClassName('card');

const searchProduct = (id) => {
    var producto = null;

    productos.map((p) => {
        if (p.id == id) {
            producto = p
        }
    })

    return producto;
}

const searchFile = (id) => {
    var fd = null

    archivos.map((a) => {
        if(a.idDocumento == id) {
            fd = a
        }
    })

    return fd
}

for (const op of options) {
    op.addEventListener('click', () => {
        const p = searchProduct(op.getAttribute('id'))
        Swal.fire({
            title: p.nombre,
            html: `
            <p>${p.descripcion}</p>
            <br>
            <b>Precio: </b>${p.precio}
            <br>
            <b>Autor: </b>${p.autor}
            <br>
            <b>Tipo de documento: </b>${p.nombreTipo}
            <br>
            <b>Tipo: </b>${p.tipo}`,
            showConfirmButton: true,
            showCancelButton: true,
            confirmButtonText: "Descargar",
            cancelButtonText: 'Cancelar',
            imageUrl: "../static/img/libro.webp",
            imageWidth: 400,
            imageHeight: 200,
            imageAlt: 'Custom image',
        }).then(result => {
            if (result.isConfirmed) {
                const enlace = document.getElementById('enlaceArchivo')
                const img = searchFile(p.id)
                enlace.setAttribute('href', '/media/' + img.archivo)
                enlace.setAttribute('download', img.archivo.split('/')[1])
                enlace.click()
            }
        })
    })
}