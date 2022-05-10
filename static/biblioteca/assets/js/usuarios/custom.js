var $ = jQuery.noConflict();

function registrar(){
    botonActivo();
    
    $.ajax({
        data: $('#form_creacion').serialize(),
        url: $('#form_creacion').attr('action'),
        type: $('#form_creacion').attr('method'),
        success: function(response){
            notificacionSuccess(response.mensaje);
            setTimeout(function() {
                redirigirPagina(success_url);
            }, 2000);
        },
        error: function(error){
            botonActivo();
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresCreacion(error);
        }
    });
}

function botonActivo(){
    if($("#boton_registrar").prop('disabled')){
        $("#boton_registrar").prop('disabled', false);
    }else{
        $("#boton_registrar").prop('disabled', true);
    }
}

function mostrarErroresCreacion(errores){
    $('#errores').html("");
    let error = "";

    for(let item in errores.responseJSON.error){
        error += '<div class="alert alert-danger"><strong>' +errores.responseJSON.error[item]+'</strong></div>';
    }

    $("#errores").append(error);
}

function notificacionError(mensaje){
    Swal.fire({
        title: 'Error',
        text: mensaje,
        icon: 'error'
    })
}

function notificacionSuccess(mensaje){
    Swal.fire({
        title: 'Buen trabajo',
        text: mensaje,
        icon: 'success'
    })
}

function redirigirPagina(url){
    window.location.href = url;
}