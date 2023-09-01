const profileSahibi = document.getElementById('profileSahip')
const profileEditBtn = document.getElementById('ProfileEdit')
const profileEkran = document.getElementById('profileShow')
const form = document.getElementById('formEdit')
const formbtn = document.getElementById('btnformGonder')


if(profileSahibi.innerHTML == ""){
    profileEditBtn.style.display = "none"
    profileEkran.style.display = "none"
    form.style.display = "block"
}else if(profileSahibi){
    form.style.display = "none"
    profileEditBtn.style.display = "inline"
    profileEkran.style.display = "block"
}

profileEditBtn.addEventListener('click', function(){
    profileEkran.style.display = "none"
    form.style.display = "block"
    profileEditBtn.style.display = "none"
})

formbtn.addEventListener("click" ,function (){
    profileEkran.style.display = "block"
    form.style.display = "none"
    profileEditBtn.style.display = "inline"
})