var $ = jQuery.noConflict();

function registrar(){
    $.ajax({
        data: $('#form_creacion').serialize(),
        url: $('#form_creacion').attr('action'),
        type: $('#form_creacion').attr('method'),
        success: function(response){
            console.log("Se grabo el usuario...");
            window.location.href = success_url;
        },
        error: function(error){
            console.log(error);
        }
    });
}