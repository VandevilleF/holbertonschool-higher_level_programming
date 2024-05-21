const header = document.getElementById('red_header');

header.addEventListener('click', updateColor);

function updateColor () {
  header.style.color = '#FF0000';
}
