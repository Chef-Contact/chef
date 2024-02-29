$('.wiper-track').slick({
  dots: true,
  infinite: false,
  speed: 300,
  slidesToShow: 4,
  slidesToScroll: 4,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 2,
        infinite: true,
        dots: true
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
  ]
});

$(document).ready(function () {
  var $mobileMenu = $('.mobile-menu');
  var $newHeader = $('.new-header');

  $newHeader.click(function () {
    $mobileMenu.slideToggle();

    // Add or remove overlay
    if ($mobileMenu.is(':visible')) {
      $('body').append('<div class="overlay"></div>');
    } else {
      $('.overlay').remove();
    }
  });

  // Close mobile menu when overlay is clicked
  $(document).on('click', '.overlay', function () {
    $mobileMenu.slideUp();
    $('.overlay').remove();
  });
});