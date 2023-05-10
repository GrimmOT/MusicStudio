let backButton = document.querySelector("#back-button")
let member = document.querySelectorAll(".member")
for (let i = 0; i < member.length; i++){
    member[i].addEventListener("click", memberHover)
}

function memberHover(event){
    event.target.classList.toggle("hover-on")
}

backButton.addEventListener("click", (event) => {
    window.history.back()
})

