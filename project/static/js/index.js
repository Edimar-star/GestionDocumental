$('.mobile-menu-toggler').on('click', function (e) {
    $('body').toggleClass('mmenu-active');
    $(this).toggleClass('active');
    e.preventDefault();
});

$('.mobile-menu-overlay, .mobile-menu-close').on('click', function (e) {
    $('body').removeClass('mmenu-active');
    $('.menu-toggler').removeClass('active');
    e.preventDefault();
});