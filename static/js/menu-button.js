window.onload = function (){
    window.addEventListener('scroll', function (e){
        if (window.pageXOffset > 100){
            document.querySelector("header").classList.add('is-scrolling');
        } else {
            document.querySelector("header").classList.remove('is-scrolling');
        }
    });

    const menu_btn = document.querySelector('.menu-button');
    const navbar_menu_btn = document.querySelector('.navbar-links');

    menu_btn.addEventListener('click', function (){
        menu_btn.classList.toggle('is-active')
        navbar_menu_btn.classList.toggle('is-active');
    });
}