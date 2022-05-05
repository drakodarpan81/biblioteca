var $ = jQuery.noConflict();

function registrar(listado){
    $.ajax({
        data: $('#form_creacion').serialize(),
        url: $('#form_creacion').attr('action'),
        type: $('#form_creacion').attr('method'),
        success: function(response){
            listado;
        },
        error: function(error){
            console.log(error);
        }
    });
}