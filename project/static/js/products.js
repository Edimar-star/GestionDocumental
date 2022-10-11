const productos = window.data.products;
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

for (const op of options) {
    op.addEventListener('click', () => {
        const p = searchProduct(op.getAttribute('id'))
        Swal.fire({
            title: p.nombre,
            html: `
            <p>${p.descripcion}</p>
            <br>
            <b>Price: </b>${p.price}
            <br>
            <b>Autor: </b>${p.autor}
            <br>
            <b>Tipo de documento: </b>${p.nombreTipo}
            <br>
            <b>Tipo: </b>${p.tipo}`,
            showCancelButton: true,
            confirmButtonText: (p.type == "Fisico") ? "Comprar" : "Alquilar",
            cancelButtonText: 'Cancelar',
            imageUrl: p.img,
            imageWidth: 400,
            imageHeight: 200,
            imageAlt: 'Custom image',
        })
    })
}