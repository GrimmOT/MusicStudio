let groups = document.querySelectorAll(".group")

function redirect(event){
    let layer = event.target
    let i = layer.getAttribute("groupId")
    window.location.href = `${window.location}${i}`;
}


for (let i = 0; i < groups.length; i++ ){
    groups[i].addEventListener("click", redirect)
}