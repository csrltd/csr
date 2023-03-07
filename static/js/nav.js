
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

const title = document.title

// let link = document.querySelector('.nav-link')
let link = document.querySelector('title')

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
  } else if (headerBg.classList.contains('finance-acc-header')) {
    headerBg.style.background = 'white'
  }
  
  else {
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

  if(title.includes('Finance and Accounting') && scrolledPixels === 0) {
    logoBlue.style.display = 'block'
    logoWhite.style.display ='none'
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
