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

// document.querySelector(".prev-btn").addEventListener("click", function () {
//   slideIndex--;
//   showSlides();
// });

// document.querySelector(".next-btn").addEventListener("click", function () {
//   slideIndex++;
//   showSlides();
// });

showSlides();

//date on the footer
const date = document.getElementById('date')
date.innerHTML = new Date().getFullYear()

//nav 
const mobileMenu = document.querySelector('.nav-menu')
const navToggle = document.querySelector('.nav-toggle')
const closeBtn = document.querySelector('.nav-close-btn')
const headerBg = document.querySelector('.header')
const navLinks = document.querySelectorAll('.link')

window.addEventListener('scroll', () => {
  let scrolledPixels = window.scrollY

  if (scrolledPixels >= 50) {
    headerBg.style.background = '#00000077'  
  }else {
    headerBg.style.background = 'transparent'
  }
})



//Closing menu when link clicked

navLinks.forEach((link) => {
  link.addEventListener('click', () => {
    if (window.innerWidth < 1200 ) {
      mobileMenu.style.display = 'none'
    }
  })
})


//opening the mobile menu
navToggle.addEventListener('click', () => {
  mobileMenu.style.display = 'block'
  closeBtn.style.display = 'block'
  navToggle.style.display = 'none'
})
// closing the fixed nav
closeBtn.addEventListener('click', () => {
  mobileMenu.style.display = 'none'
  closeBtn.style.display = 'none'
  navToggle.style.display = 'block'
  headerBg.style.background = 'transparent'
})

