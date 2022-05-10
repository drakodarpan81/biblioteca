var $ = jQuery.noConflict();

function registrar(){
    botonActivo();
    
    $.ajax({
        data: $('#form_creacion').serialize(),
        url: $('#form_creacion').attr('action'),
        type: $('#form_creacion').attr('method'),
        success: function(response){
            window.location.href = success_url;
        },
        error: function(error){
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