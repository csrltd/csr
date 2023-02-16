// //sliders
// var slideIndex = 0;
// var slider = document.querySelector(".slider");
// var cards = document.querySelectorAll(".card");

// function showSlides() {
//   for (let i = 0; i < cards.length; i++) {
//     if (i >= slideIndex && i < slideIndex + 4) {
//       cards[i].style.display = "inline-block";
//     } else {
//       cards[i].style.display = "none";
//     }
//   }
//   if (slideIndex === 0) {
//     document.querySelector(".prev-btn").style.display = "none";
//   } else {
//     document.querySelector(".prev-btn").style.display = "block";
//   }
//   if (slideIndex === cards.length - 4) {
//     document.querySelector(".next-btn").style.display = "none";
//   } else {
//     document.querySelector(".next-btn").style.display = "block";
//   }
// }

// document.querySelector(".prev-btn").addEventListener("click", function () {
//   slideIndex--;
//   showSlides();
// });

// document.querySelector(".next-btn").addEventListener("click", function () {
//   slideIndex++;
//   showSlides();
// });

// showSlides();

// //date on the footer
// const date = document.getElementById('date')
// date.innerHTML = new Date().getFullYear()

//nav 
const mobileMenu = document.querySelector('.nav-menu')
const navToggle = document.querySelector('.nav-toggle')
const closeBtn = document.querySelector('.nav-close-btn')
const headerBg = document.querySelector('.header')
const navLinks = document.querySelectorAll('.link')
const navLink = document.querySelectorAll('.nav-link')
const logoBlue = document.querySelector('.blue-logo')
const logoWhite = document.querySelector('.white-logo')
const btnHeader = document.querySelector('.btn-header')

window.addEventListener('scroll', () => {
  let scrolledPixels = window.scrollY

  if (scrolledPixels >= 50) {
    headerBg.style.background = 'white'
    headerBg.style.boxShadow = "10px 20px 50px rgba(0, 0, 0, 0.070)";
    logoBlue.style.display = 'block'
    logoWhite.style.display = 'none'
    navToggle.style.color = '#2A2D7C'
    navLink.forEach((link) => {
      link.style.color = '#2A2D7C'
    })
    btnHeader.classList.add('btn-blue-outline')

    closeBtn.addEventListener('click', () => {
      headerBg.style.background = 'white'
      logoBlue.style.display = 'block'
      logoWhite.style.display = 'none'
    })
  } else {
    headerBg.style.background = 'transparent'
    headerBg.style.boxShadow = 'none'
    logoBlue.style.display = 'none'
    logoWhite.style.display = 'block'
    navToggle.style.color = 'white'
    navLink.forEach((link) => {
      link.style.color = 'white'
    })

    closeBtn.addEventListener('click', () => {
      headerBg.style.background = 'transparent'
      logoBlue.style.display = 'none'
      logoWhite.style.display = 'block'
    })

    btnHeader.classList.remove('btn-blue-outline')
  }
})



//Closing menu when link clicked
// corrections made closeBtn dissapear when a link is clicked

navLinks.forEach((link) => {
  link.addEventListener('click', () => {
    
    if (window.innerWidth < 1200) {
      mobileMenu.style.display = 'none'
      closeBtn.style.display = 'none'
      navToggle.style.display = 'block'
    }
  })
})


//opening the mobile menu
navToggle.addEventListener('click', () => {
  mobileMenu.style.display = 'block'
  closeBtn.style.display = 'block'
  navToggle.style.display = 'none'
  headerBg.style.background = 'white'
  logoBlue.style.display = 'block'
  logoWhite.style.display = 'none'
  navLink.forEach((link) => {
    link.style.color = '#2A2D7C'
  })
})
// closing the fixed nav
closeBtn.addEventListener('click', () => {
  mobileMenu.style.display = 'none'
  closeBtn.style.display = 'none'
  navToggle.style.display = 'block'
  logoBlue.style.display = 'none'
  logoWhite.style.display = 'block'
  headerBg.style.background = 'transparent'
  navLink.forEach((link) => {
    link.style.color = 'white'
  })
})

