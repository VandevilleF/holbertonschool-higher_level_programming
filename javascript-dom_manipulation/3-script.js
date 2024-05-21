const redheader = document.getElementById('toggle_header');

redheader.addEventListener('click', updateClass);

function updateClass () {
  const header = document.querySelector('header');
  header.classList.toggle('red');
  header.classList.toggle('green');
}
