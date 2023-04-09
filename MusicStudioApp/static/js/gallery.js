let popup = document.querySelector(".popup-background")
let cross = document.querySelector(".close")
let photos = document.querySelectorAll(".concert-photo")
let body = document.querySelector("body")
let popupImage = popup.querySelector(".popup-image img")

for(let i = 0; i < photos.length; i++){
    photos[i].addEventListener("click", openPopup)
}

function openPopup(event){
    popup.style.display = "flex"
    body.classList.add("disable-scroll")
    let imageUrl = event.target.getAttribute("src")
    popupImage.setAttribute("src", imageUrl)
}
function closePopup(){
    popup.style.display = "none"
    body.classList.remove("disable-scroll")
}
cross.addEventListener("click", closePopup)