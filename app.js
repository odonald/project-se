const observer = new IntersectionObserver(entries => {
  // Loop over the entries
  entries.forEach(entry => {
    // If the element is visible
    if (entry.isIntersecting) {
      // Add the animation class
      entry.target.classList.add('rectangle-animation-one', entry.isIntersecting);
    }
  });
});

observer.observe(document.querySelector('.rectangle-one'));

const observer2 = new IntersectionObserver(entries => {
  // Loop over the entries
  entries.forEach(entry => {
    // If the element is visible
    if (entry.isIntersecting) {
      // Add the animation class
      entry.target.classList.add('rectangle-animation-two', entry.isIntersecting);
    }
  });
});

observer2.observe(document.querySelector('.rectangle-two'));

const observer3 = new IntersectionObserver(entries => {
  // Loop over the entries
  entries.forEach(entry => {
    // If the element is visible
    if (entry.isIntersecting) {
      // Add the animation class
      entry.target.classList.add('rectangle-animation-three', entry.isIntersecting);
    }
  });
});
observer3.observe(document.querySelector('.rectangle-three'));


