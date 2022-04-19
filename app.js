const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    const square = entry.target.querySelector('.rectangle-' + entry.target.dataset.name);

    if (entry.isIntersecting) {
      square.classList.add('rectangle-animation-' + entry.target.dataset.name);
	  return; // if we added the class, exit the function
    }

    // We're not intersecting, so remove the class!
    square.classList.remove('rectangle-animation-' + entry.target.dataset.name);
  });
});

observer.observe(document.querySelector('.sectionlistener-one'));
observer.observe(document.querySelector('.sectionlistener-two'));
observer.observe(document.querySelector('.sectionlistener-three'));