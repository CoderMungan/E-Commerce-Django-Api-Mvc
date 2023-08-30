const profile = document.getElementById('profileEdit')
const profileShow = document.getElementById('profileShow')
const formGonderBtn = document.getElementById('formGonder')
const nokta = document.getElementById(nokta)

if(profile){
    profile.style.display = "none";
}

if(nokta.innerHTML == ""){
    profile.style.display = "block";
}else {
    editprofile()
}

const editprofile = () => {
    profileShow.style.display = "none";
    profile.style.display = "block";
}

const resetProfile = () => {
    profileShow.style.display = "block";
    profile.style.display = "none"
}

formGonderBtn.addEventListener('submit', function(){
    resetProfile()
})