function OpenCloseMenu() {
  const menu = document.getElementById("nav-menu");
  const OpenMenu = document.getElementById("OpenMenu");
  const CloseMenu = document.getElementById("CloseMenu");
  if (menu.style.display === "none") {
    menu.style.display = "flex";
    OpenMenu.style.display = "none";
    CloseMenu.style.display = "block";
  } else {
    menu.style.display = "none";
    OpenMenu.style.display = "block";
    CloseMenu.style.display = "none";
  }
}

//sliders
var slideIndex = 0;
var slider = document.querySelector(".slider");
var cards = document.querySelectorAll(".card");

function showSlides() {
  for (let i = 0; i < cards.length; i++) {
    if (i >= slideIndex && i < slideIndex + 4) {
      cards[i].style.display = "inline-block";
    } else {
      cards[i].style.display = "none";
    }
  }
  if (slideIndex === 0) {
    document.querySelector(".prev-btn").style.display = "none";
  } else {
    document.querySelector(".prev-btn").style.display = "block";
  }
  if (slideIndex === cards.length - 4) {
    document.querySelector(".next-btn").style.display = "none";
  } else {
    document.querySelector(".next-btn").style.display = "block";
  }
}

document.querySelector(".prev-btn").addEventListener("click", function () {
  slideIndex--;
  showSlides();
});

document.querySelector(".next-btn").addEventListener("click", function () {
  slideIndex++;
  showSlides();
});

showSlides();



