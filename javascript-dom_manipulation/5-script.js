const changeText = document.getElementById('update_header');

changeText.addEventListener('click', changeheader);

function changeheader () {
  changeText.textContent = 'New Header!!!';
}
