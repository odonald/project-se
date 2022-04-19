const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    const square = entry.target.querySelector('.rectangle-one');

    if (entry.isIntersecting) {
      square.classList.add('rectangle-animation-one');
	  return; // if we added the class, exit the function
    }

    // We're not intersecting, so remove the class!
    square.classList.remove('rectangle-animation-one');
  });
});

observer.observe(document.querySelector('.sectionflex'));

const observer2 = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    const square = entry.target.querySelector('.rectangle-two');

    if (entry.isIntersecting) {
      square.classList.add('rectangle-animation-two');
	  return; // if we added the class, exit the function
    }

    // We're not intersecting, so remove the class!
    square.classList.remove('rectangle-animation-two');
  });
});
observer2.observe(document.querySelector('.sectionlistener-two'));


const observer3 = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    const square = entry.target.querySelector('.rectangle-three');

    if (entry.isIntersecting) {
      square.classList.add('rectangle-animation-three');
	  return; // if we added the class, exit the function
    }

    // We're not intersecting, so remove the class!
    square.classList.remove('rectangle-animation-three');
  });
});
observer3.observe(document.querySelector('.sectionlistener-three'));
