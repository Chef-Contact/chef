
/*!
 * Let's start js homemeal
 * 
 */


// let btn = document.getElementById('more-btn');

// let links = document.getElementById('more-links');

// btn.onclick = () =>{
//   if(links.className.includes(' more-show')){
//     links.className = links.className.replace(/ more-show/, '')
//   } else{
//     links.className += ' more-show'
//   }
// }




$(document).ready(function () {

    
 

  /** datepicker material debut */
  
  $('#date').bootstrapMaterialDatePicker
      ({
        time: false,
        clearButton: true
      });

      $('#time').bootstrapMaterialDatePicker
      ({
        date: false,
        shortTime: false,
        format: 'HH:mm'
      });

      $('#date-format').bootstrapMaterialDatePicker
      ({
        format: 'dddd DD MMMM YYYY - HH:mm'
      });
      $('.date-fr').bootstrapMaterialDatePicker
      ({
        format: 'YYYY-MM-DD HH:mm',
        lang: 'fr',
        weekStart: 1, 
        cancelText : 'ANNULER',
        nowButton : true,
        switchOnClick : true
      });

      $('#date-end').bootstrapMaterialDatePicker
      ({
        weekStart: 0, format: 'DD/MM/YYYY HH:mm'
      });
      $('#date-start').bootstrapMaterialDatePicker
      ({
        weekStart: 0, format: 'DD/MM/YYYY HH:mm', shortTime : true
      }).on('change', function(e, date)
      {
        $('#date-end').bootstrapMaterialDatePicker('setMinDate', date);
      });

      $('#min-date').bootstrapMaterialDatePicker({ format : 'DD/MM/YYYY HH:mm', minDate : new Date() });

      $.material.init()

  /** datepicker material fin */

  
/*
  hljs.initHighlightingOnLoad();

        // Datetime picker initialization.
        // See http://eonasdan.github.io/bootstrap-datetimepicker/
        $('[data-toggle="datetimepicker"]').datetimepicker({
            icons: {
                time: 'fa fa-clock-o',
                date: 'fa fa-calendar',
                up: 'fa fa-chevron-up',
                down: 'fa fa-chevron-down',
                previous: 'fa fa-chevron-left',
                next: 'fa fa-chevron-right',
                today: 'fa fa-check-circle-o',
                clear: 'fa fa-trash',
                close: 'fa fa-remove'
            }
        });


  $(".js-datepicker").datepicker( $.datepicker.regional[ "fr" ] );
  $( "#locale" ).on( "change", function() {
      $( ".js-datepicker" ).datepicker( "option",$.datepicker.regional[ 'fr' ] );
  });
*/
  $('.js-datepicker').datepicker({

    dateFormat: 'yy-mm-dd',
    timeFormat: 'hh:mm tt'
  });

  //sample for xiao
  $('#myModal').on('hidden', function () {
  // Load up a new modal...
  $('#myModalNew').modal('show')
  })

  $("#sticker").stick_in_parent();


  $( "#slider-range" ).slider({
    range: true,
    min: 0,
    max: 20000,
    values: [ 1, 20000 ],
    slide: function( event, ui ) {
      $( "#amount" ).val( + ui.values[ 0 ]+"$" + " - " + ui.values[ 1 ]+"$" );
      //console.log("slide");
      //$( "#prixmin" ).val(ui.values[ 0 ]);
      //$( "#prixmax" ).val(ui.values[1]);      
    },
    change: function(event, ui) {
      //console.log("change"+ui.values[0]);
      //alert(ui.values[0]);
      //$('#amount').attr('value', ui.value);
      //$('#prixmin1').attr('value', ui.values[0]);
      $('#prixminhidden').val(ui.values[0]);
      $('#prixmaxhidden').val(ui.values[1]);
      console.log($('#prixmaxhidden'));
      //$( "#aaaa" ).val( $( "#slider-range" ).slider( "values", 0 ) );
    }    
  });
  $( "#amount" ).val( $( "#slider-range" ).slider( "values", 0 ) + " - " + $( "#slider-range" ).slider( "values", 1 ) );
  //$( "#prixmin" ).val( $( "#slider-range" ).slider( "values", 0 ));
  //var mini = $( "#slider-range" ).slider( "values", 0 );
  //console.log(mini);
     // $('#prixmin').val(ui.values[0]);
     // $('#prixmax').val(ui.values[1]);
  


  $('[data-toggle="popover"]').popover(); 

  $(document).on('submit', 'form[data-confirmation]', function (event) {
    var $form = $(this),
    $confirm = $('#confirmationModal');

    if ($confirm.data('result') !== 'yes') {
        //cancel submit event
        event.preventDefault();

        $confirm
            .off('click', '#btnYes')
            .on('click', '#btnYes', function () {
                $confirm.data('result', 'yes');
                $form.find('input[type="submit"]').attr('disabled', 'disabled');
                $form.submit();
            })
            .modal('show');
    }
  });

  $('#confirmationModal').on('show.bs.modal', function(e) {
    $(this).find('#btnYes').attr('href', $(e.relatedTarget).data('load-remote'));
  });


  $('[data-load-remote]').on('click',function(e) {
        e.preventDefault();
        var $this = $(this);
        var remote = $this.data('load-remote');
        if (!$this.data('isloaded')) {
            if(remote) {
                $($this.data('remote-target')).load(remote);
                $this.data('isloaded', true)
            }
        }
    });

  if ( $( ".chatscroll" ).length ) {
    $(".chatscroll").scrollTop($(".chatscroll")[0].scrollHeight);
  }



  $('#myTab a').click(function (e) {
      e.preventDefault()
      $(this).tab('show')
    })

  // Get the modal
  var modal = document.getElementById('myModal');





  // When the user clicks on the button, open the modal
   if ( $( "#myBtn" ).length ) {
    // Get the button that opens the modal
    var btn = document.getElementById("myBtn");    
    btn.onclick = function() {
        modal.style.display = "block";
    }
  }

  if ( $( ".close" ).length ) {
    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];
    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    }
  }
  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
      if (event.target == modal) {
          modal.style.display = "none";
      }
  }


  $('#loading').hide();


/**************************** start STAR rating *********************/ 
// DOC   https://github.com/kartik-v/bootstrap-star-rating


   $("#input-21f").rating({
    starCaptions: function (val) {
        if (val < 3) {
            return val;
        } else {
            return 'high';
        }
    },
    starCaptionClasses: function (val) {
        if (val < 3) {
            return 'label label-danger';
        } else {
            return 'label label-success';
        }
    },
    hoverOnClear: false
});





/**************  cuisine **********/
var $inp = $('#rating-cuisine-input');
$inp.rating({
    min: 0,
    max: 5,
    step: 1,
    size: 'xs',
    showClear: false,
});
$inp.on('rating.change', function () {
    $('#form_cuisine').val($('#rating-cuisine-input').val());
    //alert($('#rating-input').val());
});

/**************  ambiance **********/
var $inp2 = $('#rating-ambiance-input');
$inp2.rating({
    min: 0,
    max: 5,
    step: 1,
    size: 'xs',
    showClear: false,
});
$inp2.on('rating.change', function () {
    $('#form_ambiance').val($('#rating-ambiance-input').val());
    //alert($('#rating-input').val());
});


/**************  lieu **********/
var $inp3 = $('#rating-lieu-input');
$inp3.rating({
    min: 0,
    max: 5,
    step: 1,
    size: 'xs',
    showClear: false,
});
$inp3.on('rating.change', function () {
    $('#form_lieu').val($('#rating-lieu-input').val());
    //alert($('#rating-input').val());
});
/**************  qualite prix **********/
var $inp4 = $('#rating-qualite-input');
$inp4.rating({
    min: 0,
    max: 5,
    step: 1,
    size: 'xs',
    showClear: false,
});
$inp4.on('rating.change', function () {
    $('#form_qualite').val($('#rating-qualite-input').val());
    //alert($('#rating-input').val());
});

$('#rating-reset').on('click', function () {
    $('#form_cuisine').val();  
    $('#form_qualite').val(); 
    $('#form_lieu').val()
    $('#form_ambiance').val();           
});

/*
$('#btn-rating-input').on('click', function () {
    $inp.rating('refresh', {
        showClear: true,
        disabled: !$inp.attr('disabled')
    });
});


$('.btn-danger').on('click', function () {
    $("#kartik").rating('destroy');
});

$('.btn-success').on('click', function () {
    $("#kartik").rating('create');
});


$('.rb-rating').rating({
    'showCaption': false,
    'stars': '3',
    'min': '0',
    'max': '3',
    'step': '1',
    'size': 'xs',
    'starCaptions': {0: 'status:nix', 1: 'status:wackelt', 2: 'status:geht', 3: 'status:laeuft'}
});
$("#input-21c").rating({
    min: 0, max: 8, step: 0.5, size: "xl", stars: "8"
});
*/
/**************************** end  STAR rating *********************/ 
});

function switchLanguage(language) {
  // Remove 'act' class from all buttons
  document.querySelectorAll('.language_switcher button').forEach((btn) => {
    btn.classList.remove('act');
  });

  // Add 'act' class to the clicked button
  document.getElementById(`${language}Btn`).classList.add('act');

  // You can add logic here to switch the content language on your website
  // For example, update text content, fetch translations, etc.
  // For this example, let's just log the selected language.
  console.log(`Switched to ${language.toUpperCase()} language`);
}