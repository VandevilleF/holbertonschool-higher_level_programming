const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url).then((response) => {
  if (!response.ok) {
    throw new Error(response.statusText);
  }
  return response.json();
}) /*Gère le retour de la réponse et renvoi le contenu sous format json*/
  .then((data) => {
    const charElement = document.getElementById('character');
    charElement.textContent = data.name;
  }); /*Récupère le contenu par (key, value)*/
