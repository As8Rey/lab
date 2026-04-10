$(document).ready(function() {
    var scrolled = 0;
    var $parallaxElements = $('.icons-for-parallax img');
    var $logo = $('.logo');

    $(window).scroll(function() {
        scrolled = $(window).scrollTop();
        // Для иконок
        for (var i = 0; i < $parallaxElements.length; i++) {
            var speed = 0.1 * (i + 1);
            var yPosition = scrolled * speed;
            $parallaxElements.eq(i).css({ top: yPosition });
        }
        // Для логотипа (скорость 0.05)
        var logoY = scrolled * 0.05;
        $logo.css({ transform: 'translateY(' + logoY + 'px)' });
    });
});