let menuBtn = document.querySelector("#menu-btn")
let menu = document.querySelector(".menu-content")

function toggleMenu(){
    menu.classList.toggle("menu-active")
}
menuBtn.addEventListener("click", toggleMenu)
