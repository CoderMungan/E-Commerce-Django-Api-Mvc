const kayitForm = document.getElementById("kayit-form")
if (kayitForm) {
    kayitForm.addEventListener('submit', function (event) {
        const sifre = document.getElementById('password').value;
        const confirmSifre = document.getElementById("confirmPassword").value;
        const alert = document.getElementById("matchout")

        if (sifre !== confirmSifre) {
            alert.innerText = "Şifreleriniz Eşleşmemektedir. Lütfen tekrar deneyiniz."
            event.preventDefault();
        } else {
            null
        }
    })
}

