const redheader = document.getElementById('red_header');

redheader.addEventListener('click', updateClass);

function updateClass () {
  const header = document.querySelector('header');
  header.classList.add('red');
}
