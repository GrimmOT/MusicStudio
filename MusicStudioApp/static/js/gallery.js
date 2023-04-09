let popup = document.querySelector(".popup-background")
let cross = document.querySelector(".close")
let photo = document.querySelector(".photo")
function openPopup(){
    popup.style.display = "flex"
}
function closePopup(){
    popup.style.display = "none"
}
photo.addEventListener("click", openPopup)
cross.addEventListener("click", closePopup)
popup.addEventListener("click", closePopup)