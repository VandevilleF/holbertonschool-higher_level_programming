const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url).then((response) => {
  if (!response.ok) {
    throw new Error(response.statusText);
  }
  return response.json();
})
  .then((data) => {
    for (let i = 0; i < data.results.length; i++) {
      const ul = document.getElementById('list_movies');
      const li = document.createElement('li');
      li.textContent = data.results[i].title;
      ul.appendChild(li);
    }
  });
