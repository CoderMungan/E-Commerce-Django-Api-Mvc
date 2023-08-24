const kullaniciAdi = document.getElementById('kullanici');
if (kullaniciAdi) {
    const beniHatirla = document.getElementById('checkbox');
    const girisButton = document.getElementById('girisButton');
    if (girisButton) {
        girisButton.addEventListener('click', function () {
            if (beniHatirla.checked) {
                localStorage.setItem('username', kullaniciAdi.value)
            }
        })
    }
    
    window.onload = function () {
        if (kullaniciAdi) {
            kullaniciAdi.value = localStorage.getItem('username')
        }
    }
}




