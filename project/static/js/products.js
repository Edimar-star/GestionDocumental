const productos = window.data.products;
const cliente = window.data.cliente;
const options = document.getElementsByClassName('card');
const doc = document.getElementById('idDocumento')
const cli = document.getElementById('idCliente')
const total = document.getElementById('total')
const btn = document.getElementById('newOrder')

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
            <b>Precio: </b>${p.precio}
            <br>
            <b>Autor: </b>${p.autor}
            <br>
            <b>Tipo de documento: </b>${p.nombreTipo}
            <br>
            <b>Tipo: </b>${p.tipo}`,
            showDenyButton: true,
            showConfirmButton: p.tipo == "Fisico",
            showCancelButton: true,
            confirmButtonText: "Comprar",
            denyButtonText: "Alquilar",
            cancelButtonText: 'Cancelar',
            imageUrl: (p.imag) ? p.img : "../static/img/libro.webp",
            imageWidth: 400,
            imageHeight: 200,
            imageAlt: 'Custom image',
        }).then(result => {
            if (result.isConfirmed) {
                if(p.cantidad > 0) {
                    doc.setAttribute('value', p.id)
                    cli.setAttribute('value', cliente.data.id)
                    total.setAttribute('value', p.precio)
                    btn.setAttribute('value', 'comprar')
                    btn.click();
                } else {
                    Swal.fire('Agotado', '', 'info')
                }
            } else if (result.isDenied) {
                if(p.cantidad > 0) {
                    doc.setAttribute('value', p.id)
                    cli.setAttribute('value', cliente.data.id)
                    total.setAttribute('value', p.precio)
                    btn.setAttribute('value', 'alquilar')
                    btn.click();
                } else {
                    Swal.fire('Agotado', '', 'info')
                }
            }
        })
    })
}