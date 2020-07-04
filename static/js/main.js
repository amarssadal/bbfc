const hamburger_button = document.querySelector('.hamburger_button');
const nav_bar = document.querySelector('.nav_bar');
const nav_items = document.querySelectorAll('.nav_items li');

hamburger_button.addEventListener('click', () => {
    //Toggle Nav
    nav_bar.classList.toggle('open');
    hamburger_button.classList.toggle('hamburger_button_color')
    //Animate links
    // nav_items.forEach((link, index) => {
    //     if (link.style.animation) {
    //         link.style.animation = '';
    //     } else {
    //         link.style.animation = `nav_items_fade 0.5s ease forwards ${index / 7 + .5}s`
    //     }
    // });
    //Burger animation
    hamburger_button.classList.toggle('toggle');
});
