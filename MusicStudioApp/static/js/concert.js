const swiper = new Swiper('.swiper', {
    // Optional parameters

  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },
    slidesPerView: 1,
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    breakpoints: {
      820: {
        slidesPerView: 2
      }
    }
    // // And if we need scrollbar
    // scrollbar: {
    //   el: '.swiper-scrollbar',
    // },
  });