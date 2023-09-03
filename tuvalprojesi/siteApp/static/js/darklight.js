const darklightbtn = document.getElementById("darklightbtn");
const bodySelect = document.getElementById('body');
const hrler = document.querySelectorAll("hr")
const currentMode = localStorage.getItem("mode");


if (currentMode === "dark") {
    enableDarkMode();
} else {
    enableLightMode();
}

darklightbtn.addEventListener("click", () => {
    if (localStorage.getItem('mode') == 'dark') {
        enableLightMode();
    }else if(localStorage.getItem('mode') == 'light'){
        enableDarkMode();
    }
});


function enableDarkMode() {
    body.setAttribute('data-bs-theme', 'dark')
    localStorage.setItem("mode", "dark");
    darklightbtn.innerHTML = '<i class="fa-solid fa-umbrella-beach"></i>'
}

function enableLightMode() {
    body.setAttribute('data-bs-theme', 'light')
    localStorage.setItem("mode", "light");
    darklightbtn.innerHTML = '<i class="fa-solid fa-moon"></i>'
}

