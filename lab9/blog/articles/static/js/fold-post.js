var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(event) {
        var postDiv = event.target.closest('.one-post');
        if (!postDiv) return;
        var btn = event.target;

        if (postDiv.classList.contains('folded')) {
            // Разворачиваем
            postDiv.classList.remove('folded');
            btn.textContent = "Свернуть";
        } else {
            // Сворачиваем
            postDiv.classList.add('folded');
            btn.textContent = "Развернуть";
        }
    });
}