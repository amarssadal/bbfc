const hamburger_button = document.querySelector('.hamburger_button');
const hamburger_button_color_object = document.querySelectorAll('.hamburger_button div');
const nav_bar = document.querySelector('.nav_bar');

////////////////////////HAMBURGER BUTTON ACTION
hamburger_button.addEventListener('click', () => {
    //Toggle Nav
    nav_bar.classList.toggle('open');
    hamburger_button.classList.toggle('toggle');
    hamburger_button.classList.toggle('make_light');
});

////////////////////////TO OPEN THE MENU OF CURRENT WEBPAGE WHEN A USER HAS ARRIVED AT THAT PAGE
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

////////////////////////MAKE LINK TO THE CURRENTLY OPENED PAGE BOLD IN THE MENU
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

////////////////////////CHANGE THEN MOBILE LOGO TO BLACK OR WHITE DEPENDING ON THE PAGE OPENED
if (current_page == 'index') {
    document.querySelector('.mobile_head_logo').src = '/images/logo_mobile_white.png';
} else if (current_page == 'our_work') {
    document.querySelector('.mobile_head_logo').src = '/images/logo_mobile_black.png';
}

////////////////////////IF MENU DROP IS ENABLED - THIS WILL CLOSE THE MENU ONCE A LINK IS CLICKED
function closeNav() {
    nav_bar.classList.toggle('open');
    hamburger_button_color_object.classList.toggle('hamburger_button_color');
    hamburger_button.classList.toggle('toggle');
}


////////////////////////MODAL WINDOW
const modal = document.querySelector('.modal_window');
const modal_button = document.querySelector('.modal_button');
const modal_close = document.querySelector('.modal_close');
const vid = document.querySelector(".YouTube");
modal_button.addEventListener('click', function () {
    vid.src="https://www.youtube.com/embed/Ghy7sYavIbw?enablejsapi=1";
    modal.style.display = 'grid';
})
modal_close.addEventListener('click', function() {
    modal.style.display = 'none';
    vid.src = '';
})
window.addEventListener('click', function(event) {
    if(event.target == modal) {
        modal.style.display = 'none';
        vid.src = '';
    }
})