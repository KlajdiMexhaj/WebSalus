(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let header = select('#header')
    let offset = header.offsetHeight

    let elementPos = select(el).offsetTop
    window.scrollTo({
      top: elementPos - offset,
      behavior: 'smooth'
    })
  }

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select('#header')
  let selectTopbar = select('#topbar')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add('header-scrolled')
        if (selectTopbar) {
          selectTopbar.classList.add('topbar-scrolled')
        }
      } else {
        selectHeader.classList.remove('header-scrolled')
        if (selectTopbar) {
          selectTopbar.classList.remove('topbar-scrolled')
        }
      }
    }
    window.addEventListener('load', headerScrolled)
    onscroll(document, headerScrolled)
  }

  /**
   * Mobile nav toggle
   */
  on('click', '.mobile-nav-toggle', function(e) {
    select('#navbar').classList.toggle('navbar-mobile')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')
  })


  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on('click', '.scrollto', function(e) {
    if (select(this.hash)) {
      e.preventDefault()

      let navbar = select('#navbar')
      if (navbar.classList.contains('navbar-mobile')) {
        navbar.classList.remove('navbar-mobile')
        let navbarToggle = select('.mobile-nav-toggle')
        navbarToggle.classList.toggle('bi-list')
        navbarToggle.classList.toggle('bi-x')
      }
      scrollto(this.hash)
    }
  }, true)

  /**
   * Scroll with ofset on page load with hash links in the url
   */
  window.addEventListener('load', () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash)
      }
    }
  });

  /**
   * Initiate glightbox 
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  /**
   * Back to top button
   */
   let backtotop = select('.back-to-top')
   if (backtotop) {
     const toggleBacktotop = () => {
       if (window.scrollY > 100) {
         backtotop.classList.add('active')
       } else {
         backtotop.classList.remove('active')
       }
     }
     window.addEventListener('load', toggleBacktotop)
     onscroll(document, toggleBacktotop)
   }

})()











//Slider last
document.addEventListener('DOMContentLoaded', function() {
  // Your JavaScript code here
  const slider = document.querySelector('.slider');
  const slides = document.querySelectorAll('.slide');
  const popupContainer = document.querySelector('.popup-container');
  const popupImage = document.querySelector('.popup-image');

  let currentIndex = 0;

  function nextSlide() {
      if (currentIndex === slides.length - 1) {
          currentIndex = 0;
      } else {
          currentIndex++;
      }
      updateSlider();
  }

  function prevSlide() {
      if (currentIndex === 0) {
          currentIndex = slides.length - 1;
      } else {
          currentIndex--;
      }
      updateSlider();
  }

  function updateSlider() {
      const offset = -currentIndex * slides[0].offsetWidth;
      slider.style.transform = `translateX(${offset}px)`;
  }

  document.querySelector('.prev').addEventListener('click', prevSlide);
  document.querySelector('.next').addEventListener('click', nextSlide);

  // Open popup when clicking on slide image
  slides.forEach((slide, index) => {
      slide.addEventListener('click', () => {
          popupImage.src = slide.querySelector('.slide-image').src;
          popupContainer.style.display = 'flex';
      });
  });

  // Close popup when clicking on close button
  document.querySelector('.close').addEventListener('click', () => {
      popupContainer.style.display = 'none';
  });
});


//Slider for home page doctor section
document.addEventListener("DOMContentLoaded", function() {
  const slider = document.querySelector('.slider');
  const nextBtn = document.querySelector('.next-btn');
  const prevBtn = document.querySelector('.prev-btn');
  let slidePosition = 0;
  const slides = document.querySelectorAll('.card');
  const totalSlides = slides.length;

  nextBtn.addEventListener('click', () => {
    if (slidePosition < totalSlides - 1) {
      slidePosition++;
      updateSlidePosition();
    }
  });

  prevBtn.addEventListener('click', () => {
    if (slidePosition > 0) {
      slidePosition--;
      updateSlidePosition();
    }
  });

  function updateSlidePosition() {
    const slideWidth = slides[0].offsetWidth;
    slider.style.transform = `translateX(-${slideWidth * slidePosition}px)`;
  }
});






//Google Translate
function loadGoogleTranslate(){
  new google.translate.TranslateElement("google_element");
}



