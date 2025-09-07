let JOKES = [];

async function loadJokes() {
  try {
    const res = await fetch('jokes.json');
    JOKES = await res.json();
  } catch (e) {
    console.error('Failed to load jokes.json', e);
    JOKES = [];
  }
}

function formatJoke(j) {
  if (!j) return 'د ټوکو ډیټا شتون نلري.';
  if (j.type === 'single') return j.joke;
  if (j.type === 'twopart') return `${j.setup}\n\n${j.delivery}`;
  // backward compatibility: string
  if (typeof j === 'string') return j;
  return 'بې نومه ټوکه';
}

function getRandomJokeObj() {
  if (!Array.isArray(JOKES) || JOKES.length === 0) return null;
  const idx = Math.floor(Math.random() * JOKES.length);
  return JOKES[idx];
}

function showRandomJoke() {
  const el = document.getElementById('joke');
  el.classList.add('loading');
  el.style.color = '#ffd700';
  el.textContent = 'لوستل کیږي...';
  setTimeout(() => {
    const j = getRandomJokeObj();
    el.textContent = formatJoke(j);
    el.style.color = '';
    el.classList.remove('loading');
  }, 800); // Slightly longer for better UX
}

document.addEventListener('DOMContentLoaded', async () => {
  await loadJokes();
  document.getElementById('get-joke').addEventListener('click', showRandomJoke);
});

// expose for console/tests
window._PJ = {loadJokes, getRandomJokeObj, formatJoke};
