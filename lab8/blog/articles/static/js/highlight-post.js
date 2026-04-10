$(document).ready(function() {
    // Эффект затемнения при наведении на пост
    $('.one-post').hover(
        function() {
            $(this).find('.one-post-shadow').animate({ opacity: 0.1 }, 300);
        },
        function() {
            $(this).find('.one-post-shadow').animate({ opacity: 0 }, 300);
        }
    );

    // Эффект увеличения логотипа при наведении
    $('.header img').hover(
        function() {
            $(this).animate({ width: '+=20' }, 200);
        },
        function() {
            $(this).animate({ width: '-=20' }, 200);
        }
    );
});