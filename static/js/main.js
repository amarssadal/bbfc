const hamburger_button = document.querySelector('.hamburger_button');
const hamburger_button_color_object = document.querySelectorAll('.hamburger_button div');
const nav_bar = document.querySelector('.nav_bar');

hamburger_button.addEventListener('click', () => {
    //Toggle Nav
    nav_bar.classList.toggle('open');
    hamburger_button.classList.toggle('toggle');
    hamburger_button.classList.toggle('make_light');
});

// Open the menu for current webpage:
const page = window.location.href.split("/").pop().split('#');
const current_bookmark = page[1];
const current_page = page[0];
console.log(current_page, current_bookmark);

const menus = document.querySelectorAll('.nav_bar > .menu > .item');
for (const menu of menus) {
    menu.addEventListener('click', function() {
        [...document.querySelectorAll('.nav_bar > .menu > .item > .sub_menu a')].forEach(link => {
            link.parentElement.setAttribute('style', 'max-height: 0em');
        })
        this.getElementsByClassName('sub_menu')[0].setAttribute('style', 'max-height: 10em');
    })
}

if (current_page !== 'index') {
    document.getElementById(current_page).getElementsByClassName("sub_menu")[0].style.maxHeight = '10em';
}

// make current selection bold
[...document.querySelectorAll('.links')].forEach(link => {
    link.addEventListener('click', function() {
        [...document.querySelectorAll('.links')].forEach(x => {
            if (x.classList[1] == link.classList[1]) {
                x.setAttribute('style', 'font-weight: 800');
            } else {
                x.setAttribute('style', 'font-weight: 400');
            }
        })
    })
})

// change mobile logo to black or white depending on page selected
if (current_page == 'index') {
    document.querySelector('.mobile_head_logo').src = '/images/logo_mobile_white.png';
} else if (current_page == 'our_work') {
    document.querySelector('.mobile_head_logo').src = '/images/logo_mobile_black.png';
}

// if menu drop is enabled closing the menu once a link is clicked
function closeNav() {
    nav_bar.classList.toggle('open');
    hamburger_button_color_object.classList.toggle('hamburger_button_color');
    hamburger_button.classList.toggle('toggle');
}
