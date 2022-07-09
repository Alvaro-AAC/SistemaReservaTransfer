var planeUp = `
<h3 style="position: relative; top: 0px; width: auto; left: 0; right: 0; text-align: center;">Cargando...</h3>
<svg class="slide-tr" xml:space="preserve" viewBox="0 0 150 150" y="0" x="0" xmlns="http://www.w3.org/2000/svg" id="圖層_1" version="1.1" width="200px" height="200px"><g class="ldl-scale" style="transform-origin: 50% 50%; transform: rotate(0deg) scale(0.8, 0.8);"><g class="ldl-ani"><g class="ldl-layer"><g class="ldl-ani" style="transform-origin: 50px 50px;"><path fill="#333" d="M32.9 21.1L28 22.8c-1.4.5-1.8 2-.9 3l18.6 19.1L63.5 39 34.6 21.3c-.5-.3-1.1-.4-1.7-.2z" style="fill: rgb(51, 51, 51);"></path></g></g><g class="ldl-layer"><g class="ldl-ani" style="transform-origin: 50px 50px;"><path fill="#333" d="M87.6 31.8c-2.4 0-4.9.6-7.2-.3-5.5-2.2-11.8-2.4-17.6-.4l-40.4 18-5-5.9c-1.7-2-6.1-2.6-8.4-1.1-1.2.8-1.9 2.6-1.3 4l5.4 13.1c.6 1.9 2.6 3.1 4.6 2.7l4.2-.8c2.4-.4 4.6-1 6.9-1.6 4.2-1.2 8.3-2.6 12.5-4 5.4-1.8 10.7-3.6 16.1-5.4 5.4-1.8 10.7-3.6 16.1-5.4l10.8-3.6 1.8-.6c2.6-.9 5-2.1 6.2-4.7.3-.7.5-1.4.3-2.1-.3-1.1-1.7-1.6-2.8-1.8-.9-.1-1.5-.1-2.2-.1z" style="fill: rgb(51, 51, 51);"></path></g></g><g class="ldl-layer"><g class="ldl-ani" style="transform-origin: 50px 50px;"><path fill="#333" d="M50.2 77.2l-4.9 1.7c-1.4.5-2.7-.6-2.6-2.1l2.6-27.4c.1-.6.5-1.1 1.1-1.3l13.8-4.6c1.2-.4 2.4.8 2 2L51.5 76c-.2.6-.7 1-1.3 1.2z" style="fill: rgb(51, 51, 51);"></path></g></g></g></g></svg>
<p style="position: relative; bottom: 80px; height: 2px; border: 4px dashed black; width: 300px; margin: auto; test-align: center; left: 0; right: 0;"></p>
`
var planeDown = `
<h3 style="position: relative; top: 0px; width: auto; left: 0; right: 0; text-align: center;">Cargando...</h3>
<svg class="slide-br" xml:space="preserve" viewBox="0 0 150 150" y="0" x="0" xmlns="http://www.w3.org/2000/svg" id="圖層_1" version="1.1" width="200px" height="200px"><g class="ldl-scale" style="transform-origin: 50% 50%; transform: rotate(45deg) scale(0.8, 0.8);"><g class="ldl-ani"><g class="ldl-layer"><g class="ldl-ani" style="transform-origin: 50px 50px;"><path fill="#333" d="M32.9 21.1L28 22.8c-1.4.5-1.8 2-.9 3l18.6 19.1L63.5 39 34.6 21.3c-.5-.3-1.1-.4-1.7-.2z" style="fill: rgb(51, 51, 51);"></path></g></g><g class="ldl-layer"><g class="ldl-ani" style="transform-origin: 50px 50px;"><path fill="#333" d="M87.6 31.8c-2.4 0-4.9.6-7.2-.3-5.5-2.2-11.8-2.4-17.6-.4l-40.4 18-5-5.9c-1.7-2-6.1-2.6-8.4-1.1-1.2.8-1.9 2.6-1.3 4l5.4 13.1c.6 1.9 2.6 3.1 4.6 2.7l4.2-.8c2.4-.4 4.6-1 6.9-1.6 4.2-1.2 8.3-2.6 12.5-4 5.4-1.8 10.7-3.6 16.1-5.4 5.4-1.8 10.7-3.6 16.1-5.4l10.8-3.6 1.8-.6c2.6-.9 5-2.1 6.2-4.7.3-.7.5-1.4.3-2.1-.3-1.1-1.7-1.6-2.8-1.8-.9-.1-1.5-.1-2.2-.1z" style="fill: rgb(51, 51, 51);"></path></g></g><g class="ldl-layer"><g class="ldl-ani" style="transform-origin: 50px 50px;"><path fill="#333" d="M50.2 77.2l-4.9 1.7c-1.4.5-2.7-.6-2.6-2.1l2.6-27.4c.1-.6.5-1.1 1.1-1.3l13.8-4.6c1.2-.4 2.4.8 2 2L51.5 76c-.2.6-.7 1-1.3 1.2z" style="fill: rgb(51, 51, 51);"></path></g></g></g></g></svg>
<p style="position: relative; bottom: 80px; height: 2px; border: 4px dashed black; width: 300px; margin: auto; test-align: center; left: 0; right: 0;"></p>
`

var myInterval;
var form = document.getElementById('form');
var formStay = form.innerHTML;
var input;
var rutChofer;

function changeErr() {
    if ($('#direccion').val()) {
        $('#err').html('&nbsp;');
    }
    else {
        $('#err').html(`
        <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-alert-circle" width="20" height="20" viewBox="0 0 24 24" stroke-width="1.5" stroke="tomato" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
            <circle cx="12" cy="12" r="9" />
            <line x1="12" y1="8" x2="12" y2="12" />
            <line x1="12" y1="16" x2="12.01" y2="16" />
        </svg>
        El campo no puede estar vacio.`);
        $('#err').change(changeErr);
    }
}

function back() {
    form.innerHTML = formStay;
    $('#titulo').html('Reserva de transfer');
}

function loading(elem) {
    elem.innerHTML = planeUp;
    var i = 1;
    myInterval = setInterval(function() {
        if(i%2 == 0) {
            elem.innerHTML = planeUp;
        } else {
            elem.innerHTML = planeDown;
        }
        i += 1;
    }, 1400)
}

function next1() {
    input = $('#direccion').val()
    if(input) {
        loading(form);
        $.ajax({
            type: 'GET',
            url: '/api/chofer/all/disponible/?format=json',
            success: function(data) {
                setTimeout(function() {
                    clearInterval(myInterval)
                    $('#titulo').html('Transfer disponibles');
                    var table = `
                    <button class="nav-link p-0 border-0 mb-2" style="background-color: rgba(0,0,0,0);" onclick="back()"><- Volver</button><h6 class="d-inline">Dirección ingresada: </h6><p class="d-inline">${input}</p>
                    <table class="table table-striped text-center table-light m-0 mb-5 w-100" style="border-collapse: collapse; border-radius: 1em; overflow: hidden; width: 500px;">
                                    <thead>
                                        <tr>
                                            <td>Nombre chofer</td>
                                            <td>Tipo vehículo</td>
                                            <td>Empresa</td>
                                            <td>Reservar</td>
                                        </tr>
                                    </thead>
                                    <tbody>`;
                    for (elem of data) {
                        table +=    `<tr>
                                        <td>${elem.nombre} ${elem.apellido}</td>
                                        <td>${elem.vehiculo.tipo_vehiculo.descripcion}</td>
                                        <td>${elem.empresa.nombre}</td>
                                        <td><button class="btn btn-primary" id="${elem.rut}" onclick="saveChofer(this)">Reservar</button></td>
                                    </tr>`;
                    }
                    table += '</tbody></table>';
                    $('#form')[0].innerHTML = table;
                }, 500);
            },
            error: function(data){
                clearInterval(myInterval)
                console.log(data);
            }
        });
    } else {
        $('#err').html(`
        <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-alert-circle" width="20" height="20" viewBox="0 0 24 24" stroke-width="1.5" stroke="tomato" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
            <circle cx="12" cy="12" r="9" />
            <line x1="12" y1="8" x2="12" y2="12" />
            <line x1="12" y1="16" x2="12.01" y2="16" />
        </svg>
        El campo no puede estar vacio.`);
        $('#direccion').keyup(changeErr);
    }
}

function ingresar_datos() {
    var validado = $('#pasajeroForm')[0].reportValidity();

    if(validado) {
        var data = $('#pasajeroForm').serialize();
        crear_reserva(data);
    }

}

function saveChofer(e) {
    $('#datosPasajero').modal('toggle');
    rutChofer = e.id;
}

function crear_reserva(data) {
    var cookies_array = document.cookie.split(';');
    var cookies_dict = [];
    var csrftoken;
    cookies_array.forEach(elem => {
        var temp = elem.split('=');
        cookies_dict.push({
            key: temp[0],
            value: temp[1]
        });
    })
    cookies_dict.forEach(elem => {
        if(elem.key == 'csrftoken') {
            csrftoken = elem.value;
        }
    })
    $('#btnReserva').addClass('disabled');
    $('#bodyModal').html('<progress class="pure-material-progress-circular"></progress>');
    $('#bodyModal').addClass('text-center');
    $.ajax({
        type: 'POST',
        url: '/api/viaje/post/',
        headers: {"X-CSRFToken": csrftoken},
        data: data + `&direccion=${input}&chofer=${rutChofer}&`,
        success: function(data1) {
            console.log(data1);
            $.ajax({
                type: 'GET',
                url: `/api/viaje/${data1.id}/?format=json`,
                success: function(data2) {
                    $('#datosPasajero').modal('hide');
                    $('#titulo').html('Su transfer ha sido reservado exitosamente.');
                    var info = `
                    <div class="bg-light p-5 rounded-pill text-center">
                    <h3 class="text-decoration-underline">Datos del transfer</h3><be>
                    <p>Nombre chofer: ${data2.chofer.nombre}  ${data2.chofer.apellido}</p>
                    <p>Tipo vehículo: ${data2.chofer.vehiculo.tipo_vehiculo.descripcion}</p>
                    <p>Color vehículo: ${data2.chofer.vehiculo.color}</p>
                    <p>Patente: ${data2.chofer.vehiculo.patente}</p>
                    <button class="btn btn-primary" onclick="reloadPage()">Finalizar</button>
                    </div>
                    <br>
                    <div class="text-center">
                    <img alt="Codigo QR" id="QRinfo"/>
                    </div>
                    `
                    form.innerHTML = info;
                    new QRious({
                        element: $('#QRinfo')[0],
                        value: `
                            Chofer:
                        Nombre - ${data2.chofer.nombre}  ${data2.chofer.apellido}
                        Tipo -  ${data2.chofer.vehiculo.tipo_vehiculo.descripcion}
                        Color - ${data2.chofer.vehiculo.color}
                        Patente - ${data2.chofer.vehiculo.patente}

                            Pasajero:
                        Nombre - 
                        `,
                        size: 200,
                        foreground: 'black',
                        level: 'H'
                    });
                    setTimeout(function() {
                        window.location.reload();
                    }, 15000);
                }
            });
        }
    });

}

function reloadPage() {
    window.location.reload();
}

function listenerInput() {
    var rut = $('#id_rut').val().substring(0, $('#id_rut').val().length-2);
    $.ajax({
        type: 'GET',
        url: `/api/pasajero/${rut}/?format=json`,
        success: function(data) {
            $('#id_nombre').val(data.nombre);
            $('#id_apellido').val(data.apellido);
            $('#id_telefono').val(data.telefono);
            $('#id_nombre').attr('readonly', 'readonly');
            $('#id_apellido').attr('readonly', 'readonly');
            $('#id_telefono').attr('readonly', 'readonly');
        },
        error: function(data) {
            $('#id_nombre').val($('#id_nombre').val());
            $('#id_apellido').val($('#id_apellido').val());
            $('#id_telefono').val($('#id_telefono').val());
            $('#id_nombre').removeAttr('readonly', 'readonly');
            $('#id_apellido').removeAttr('readonly', 'readonly');
            $('#id_telefono').removeAttr('readonly', 'readonly');
        }
    });
}

$(document).ready(function() {
    var timer;
    $('#id_nombre').attr('readonly', 'readonly');
    $('#id_apellido').attr('readonly', 'readonly');
    $('#id_telefono').attr('readonly', 'readonly');
    $('#id_rut').on('input', function() {
        window.clearTimeout(timer);
        timer = setTimeout(listenerInput.bind(this), 1000);
    });
});