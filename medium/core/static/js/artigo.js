
// function textAreaAdjust(o) {
//     console.log('11');
//     o.style.height = "12px";
//     o.style.height = (25+o.scrollHeight)+"px";
//   }
//var textarea = document.querySelector('textarea');

//textarea.addEventListener('keydown', autosize);
             
//function autosize(){
//  var el = this;
//  setTimeout(function(){
//    el.style.cssText = 'height:auto; padding:0';
    // for box-sizing other than "content-box" use:
    // el.style.cssText = '-moz-box-sizing:content-box';
//    el.style.cssText = 'height:' + el.scrollHeight + 'px';
//  },0);
//}
// mozfullscreenerror event handler
function errorHandler() {
  alert('mozfullscreenerror');
}
document.documentElement.addEventListener('mozfullscreenerror', errorHandler, false);

// toggle full screen
function toggleFullScreen() { 
  $("#menu-superior").toggle();
  $(".footer").toggle();
 if (!document.fullscreenElement &&    // alternative standard method
     !document.mozFullScreenElement && !document.webkitFullscreenElement) {  // current working methods
   if (document.documentElement.requestFullscreen) {
     document.documentElement.requestFullscreen();
   } else if (document.documentElement.mozRequestFullScreen) {
     document.documentElement.mozRequestFullScreen();
   } else if (document.documentElement.webkitRequestFullscreen) {
     document.documentElement.webkitRequestFullscreen(Element.ALLOW_KEYBOARD_INPUT);
   }
 } else {
   if (document.cancelFullScreen) {
     document.cancelFullScreen();
   } else if (document.mozCancelFullScreen) {
     document.mozCancelFullScreen();
   } else if (document.webkitCancelFullScreen) {
     document.webkitCancelFullScreen();
   }
 }
}

// // keydown event handler
// document.addEventListener('keydown', function(e) {
//  if (e.keyCode == 13 || e.keyCode == 70) { // F or Enter key
//    toggleFullScreen();
//  }
// }, false);

document.addEventListener('fullscreenchange', exitHandler);
document.addEventListener('webkitfullscreenchange', exitHandler);
document.addEventListener('mozfullscreenchange', exitHandler);
document.addEventListener('MSFullscreenChange', exitHandler);

function exitHandler() {
    if (!document.fullscreenElement && !document.webkitIsFullScreen && !document.mozFullScreen && !document.msFullscreenElement) {
      toggleFullScreen();
    }
}  


$("p.artigo").on("dblclick",(function(e){    
    e.preventDefault();
    let artigo = $(this).data('artigo');
    let lei = $(this).data('lei');
    let usuario = $(this).data('usuario');
    let is_marcado;
    console.log(artigo);
    console.log(lei);
    console.log(usuario);
    console.log($(this));   

    if ($(this).hasClass( "highlight" )){
        $(this).removeClass("highlight");
        is_marcado = 0;
    }else{
        $(this).addClass("highlight");
        is_marcado = 1;
    }
        
    var urlRequest = '/leis/marcacao/' + lei + '/' + artigo + '/' + usuario + '/' + is_marcado;
    console.log(urlRequest);
    $.ajax({        
        url : urlRequest, // the endpoint
        type : "POST", // http method
        data : { 'lei' : lei, 
                 'artigo' : artigo,
                 'usuario' : usuario,
                 'is_marcado' : is_marcado
                }, // data sent with the post request                       
        
        dataType: 'json',
        success: function (data) { 
            console.log('----');
            console.log(data);
            console.log('----');            
          }
    });
   
}));

$('body').on('click', 'button.btn-fechar-comentario', function() {    
  console.log($(this).parents().parents().find('#comment').val());
  //$(this).parents().parents().find('#comment').val(""); 
  console.log('ok');
});

$('body').on('click', 'button.btn-salvar-comentario, .btn-del-comentario', function() {    
    
    let comentario =  $('#comment').val();  
    
    if ($(this).html() == 'delete'){        
        comentario = 'comentario_delete';
    }
    
    //console.log(comentario);
    let artigo = this.getAttribute('data-artigo');    
    let lei = $(this).data('lei');
    let usuario = $(this).data('usuario');    
    let nota = ($('span.nota[data-artigo="'+ artigo + '"]'));
    
    
    
    //let comment_html = $(this).parents().parents().find('#comment');
    //let btn = $('.btn-salvar-comentario');
    //console.log(btn.html())
    // console.log($(this).parents().parents().html());
    
    // console.log(artigo);
    // console.log(lei);
    // console.log(usuario);    
    // console.log(comentario);

    var urlRequest = '/leis/marcacao-nota/' + lei + '/' + artigo + '/' + usuario + '/' + comentario;
   
    console.log(urlRequest);
    $.ajax({        
        url : urlRequest, // the endpoint
        type : "POST", // http method
        data : { 'lei' : lei, 
                 'artigo' : artigo,
                 'usuario' : usuario,
                 'comentario' : comentario
                }, // data sent with the post request                       
        
        dataType: 'json',
        success: function (data) { 
           
          console.log(data.comentario);
           nota.find('svg').removeClass('opacidade');
             if (data.comentario == ''){                  
               nota.find('svg').addClass('opacidade');           
             }
            
            
            nota.attr('data-comentario', data.comentario); 
            //nota.attr('data-artigo', data.artigo); 
            ///[data-linha="'+ artigo +'"]
            //console.log(btn); 
            //console.log('btn'); 
            //btn.attr('data-comentario','----'); 
            $(".btn-salvar-comentario").attr('data-comentario', data.comentario); 
            //$(".btn-salvar-comentario").attr('data-artigo', data.artigo); 
            //let.attr('data-comentario', data.comentario);  
            //comment_html.html(data.comentario);  
            //console.log('comment_html');
            //console.log(comment_html.html());
          }
    });    
    $('#modelComentario').modal('hide');

  });


  $('body').on('click', 'span.voto-up, span.voto-down', function() {    
  //  console.log($(this).html());
    let artigo = $(this).data('artigo');
    let lei = $(this).data('lei');
    let usuario = $(this).data('usuario');
    let tipo_voto = $(this).data('tipo');    
    let qtd_voto_html = $(this).parents().children('.voto[data-linha="'+ artigo +'"]').find('.qtd-voto');    
    
    //console.log(qtd_voto_html.text());
//    console.log(artigo);
//    console.log(lei);
//    console.log(usuario);        
    //console.log(voto);
//    console.log(tipo_voto);        

    var urlRequest = '/leis/voto/' + lei + '/' + artigo + '/' + usuario + '/' + tipo_voto;
   // console.log(urlRequest);
     $.ajax({        
         url : urlRequest, // the endpoint
         type : "POST", // http method
         data : { 'lei' : lei, 
                  'artigo' : artigo,
                  'usuario' : usuario,
                  //'voto' : voto,
                  'tipo_voto' : tipo_voto
                 }, // data sent with the post request                       
        
         dataType: 'json',
         success: function (data) {               
            qtd_voto_html.html(data.voto);  
           }
     });
    
  });


  var $btnAumentar = $("#btnAumentar");
  var $btnDiminuir = $("#btnDiminuir");
  var $elemento = $("body #container-artigos").find("*"); //encontra todos os elementos dentro do #content
  var fonts = [];
  
  function obterTamanhoFonte() {
    for (var i = 0; i < $elemento.length; i++) {
      fonts.push(parseFloat($elemento.eq(i).css('font-size')));
    }
  }
  obterTamanhoFonte();
  $btnAumentar.on('click', function() {
    for (var i = 0; i < $elemento.length; i++) {
      ++fonts[i];
      $elemento.eq(i).css('font-size', fonts[i]);
    }
  });
  
  $btnDiminuir.on('click', function() {
    for (var i = 0; i < $elemento.length; i++) {
      --fonts[i];
      $elemento.eq(i).css('font-size', fonts[i]);
    }
  });


$('a#largura-conteudo').click(function () {  console.log('aas');
  $('#conteudo').toggleClass('largura-conteudo');

});

