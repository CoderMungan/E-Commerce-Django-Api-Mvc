const profile = document.getElementById('profileEdit')
const profileShow = document.getElementById('profileShow')
const formGonderBtn = document.getElementById('formGonder')

if(profile){
    profile.style.display = "none";
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