let JOKES = [];
let currentJoke = null;

async function loadJokes() {
  try {
    const res = await fetch('jokes.json');
    JOKES = await res.json();
    // Show a joke on initial load
    showRandomJoke();
  } catch (e) {
    console.error('Failed to load jokes.json', e);
    const jokeEl = document.getElementById('joke');
    jokeEl.textContent = 'د ټوکو په بارولو کې ستونزه وشوه. مهرباني وکړئ وروسته بیا هڅه وکړئ.';
  }
}

function formatJoke(j) {
  if (!j) return 'یوه ټوکه هم پیدا نه شوه.';
  if (j.type === 'single') return j.joke;
  if (j.type === 'twopart') return `${j.setup}\n\n${j.delivery}`;
  if (typeof j === 'string') return j;
  return 'بې نومه ټوکه';
}

function getRandomJokeObj() {
  if (!Array.isArray(JOKES) || JOKES.length === 0) return null;
  
  let newJoke = null;
  // Ensure we don't show the same joke twice in a row
  do {
    const idx = Math.floor(Math.random() * JOKES.length);
    newJoke = JOKES[idx];
  } while (JOKES.length > 1 && newJoke === currentJoke);
  
  currentJoke = newJoke;
  return currentJoke;
}

function showRandomJoke() {
  const jokeEl = document.getElementById('joke');
  
  jokeEl.classList.add('fade-out');
  
  setTimeout(() => {
    const j = getRandomJokeObj();
    jokeEl.textContent = formatJoke(j);
    jokeEl.classList.remove('fade-out');
  }, 500); // Corresponds to the fade-out animation duration
}

document.addEventListener('DOMContentLoaded', async () => {
  await loadJokes();
  document.getElementById('get-joke').addEventListener('click', showRandomJoke);
});

// Expose for console/tests
window._PJ = {loadJokes, getRandomJokeObj, formatJoke};
