$('body').on('click', 'span.nota', function() {    
    
    // console.log( $(this).data('comentario'));
    // console.log('^');
    $(".btn-salvar-comentario").attr('data-artigo', $(this).data('artigo'));    
    $(".btn-salvar-comentario").attr('data-lei', $(this).data('lei'));
    $(".btn-salvar-comentario").attr('data-usuario', $(this).data('usuario'));    

    $(".btn-del-comentario").attr('data-artigo', $(this).data('artigo'));    
    $(".btn-del-comentario").attr('data-lei', $(this).data('lei'));
    $(".btn-del-comentario").attr('data-usuario', $(this).data('usuario'));   

    
    $('#comment').val(this.getAttribute('data-comentario'));


    //$(".btn-salvar-comentario").attr('data-comentario', $(this).data('comentario')); //atribui ao botao 
    // if((this.getAttribute('data-comentario')) == ""){
    //     $('#comment').val(this.getAttribute('data-comentario'));
    // }else{
    //     $('#comment').attr('placeholder','Some New Text');
    // }
    

    console.log($('#comment').val());
    //$(this).parents().find('#comment').val($(this).parents().children('.nota[data-nota-linha="'+ $(this).data('artigo') +'"]').getAttribute('data-comentario'));

    $('#modelComentario').modal('show');
});

