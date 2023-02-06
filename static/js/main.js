const playBtn = document.querySelector(".youtube")
const popUp = document.getElementById("pop-up")
const closePopupBtn = document.querySelector(".close-pop-up")

playBtn.addEventListener("click", openPopUp);
closePopupBtn.addEventListener("click", closePopup)
function openPopUp() {
    popUp.style.display = "flex"
}
function closePopup() {
    popUp.style.display = "none"
}