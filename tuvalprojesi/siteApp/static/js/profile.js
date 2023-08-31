const profilGoster = document.getElementById('profileShow')
const profilEdit = document.getElementById('profileEdit')
const editBtn = document.getElementById('editBtn')
const formGonderBtn = document.getElementById('formGonder')


if(profilGoster){
    profilEdit.style.display = "none"
}

editBtn.addEventListener("click", function(){
    profilGoster.style.display="none";
    profilEdit.style.display ="block";
})

formGonderBtn.addEventListener("click",function(){
    profilGoster.style.display = "block";
    profilEdit.style.display = "none";
})