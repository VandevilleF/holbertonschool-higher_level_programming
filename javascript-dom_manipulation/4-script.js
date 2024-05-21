const addButton = document.getElementById('add_item');

addButton.addEventListener('click', addlist);

function addlist () {
  const ul = document.querySelector('ul.my_list');
  const newList = document.createElement('li');
  newList.textContent = 'Item';
  ul.appendChild(newList);
}
