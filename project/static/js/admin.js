const documentos = window.data.documentos;
const accordion = document.getElementsByClassName('contentBx')

const searchProduct = (id) => {
    var producto = null;

    documentos.map((p) => {
        if (p.id == id) {
            producto = p
        }
    })

    return producto;
}

for (const op of accordion) {
    op.querySelector('.label').addEventListener('click', () => {
        op.classList.toggle('active')
    })
}

const dropdowns = document.querySelectorAll('.dropdown')
dropdowns.forEach(dropdown => {
    const select = dropdown.querySelector('.select')
    const caret = dropdown.querySelector('.caret')
    const menu = dropdown.querySelector('.menu')
    const options = dropdown.querySelectorAll('.menu li')
    const selected = dropdown.querySelector('.selected')
    const button = dropdown.querySelector('input')

    select.addEventListener('click', () => {
        select.classList.toggle('select-clicked')
        caret.classList.toggle('caret-rotate')
        menu.classList.toggle('menu-open')
    })

    options.forEach(option => {
        option.addEventListener('click', () => {
            selected.innerHTML = option.innerHTML
            button.setAttribute('value', option.getAttribute('value'))
            select.classList.remove('select-clicked')
            caret.classList.remove('caret-rotate')
            menu.classList.remove('menu-open')

            options.forEach(op => {
                op.classList.remove('active')
            })

            option.classList.add('active')

            //Si es el de actualizar documento
            console.log(caret.getAttribute('value'))
            if (caret.getAttribute('value') == "update") {
                const idDocument = option.getAttribute('value');
                const producto = searchProduct(idDocument)
                document.getElementById('nombreDocumento').setAttribute('value', producto.nombre);
                document.getElementById('autor').setAttribute('value', producto.autor);
                document.getElementById('cantidad').setAttribute('value', producto.cantidad);
                document.getElementById('precio').setAttribute('value', producto.precio);
                document.getElementById('descripcion').innerHTML = producto.descripcion;

                document.getElementById('td' + producto.tipoDoc).click();
                document.getElementById(producto.tipo).click();
            }
        })
    })
})