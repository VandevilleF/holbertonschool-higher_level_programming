const changeText = document.getElementById('update_header');

changeText.addEventListener('click', changeheader);

function changeheader () {
  const newtext = document.querySelector('header')
  newtext.textContent = 'New Header!!!';
}
