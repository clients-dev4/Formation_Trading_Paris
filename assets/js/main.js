document.documentElement.classList.add('js');

var reveals = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window && reveals.length) {
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('is-visible'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
  reveals.forEach(function (el) { io.observe(el); });
} else {
  reveals.forEach(function (el) { el.classList.add('is-visible'); });
}

var navToggle = document.getElementById('nav-toggle');
if (navToggle) {
  document.querySelectorAll('.nav a').forEach(function (a) {
    a.addEventListener('click', function () { navToggle.checked = false; });
  });
}
