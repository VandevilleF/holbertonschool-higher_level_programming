const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

fetch(url).then((response) => {
  if (!response.ok) {
    throw new Error(response.statusText);
  }
  return response.json();
})
  .then((data) => {
    const hellodiv = document.getElementById('hello');
    hellodiv.textContent = data.hello;
  })
