
//$('.slider').slick({ infinite: true, slidesToShow: 3, slidesToScroll: 3, accessibility: true });
$('.slider_main').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: true,
  fade: true,
  asNavFor: '.slider_nav',
  prevArrow: '<span class="prev_arrow"><i class="fa-solid fa-angle-left m-auto"></i></span>',
  nextArrow: '<span class="next_arrow"><i class="fa-solid fa-angle-right m-auto"></i></span>'
});
$('.slider_nav').slick({
  slidesToShow: 4,
  slidesToScroll: 1,
  asNavFor: '.slider_main',
  dots: false,
  focusOnSelect: true,
  arrows: false
});