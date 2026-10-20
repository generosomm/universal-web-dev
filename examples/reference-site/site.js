// Saltrum reference site. Every feature here has a no-script fallback in the HTML.

// Sample tide model: one reference low water and the mean semidiurnal period.
// Good enough to show the interaction; not for navigation.
const REFERENCE_LOW = new Date(2026, 0, 1, 3, 12).getTime();
const PERIOD = 745.2 * 60000; // 12 h 25.2 min
const WINDOW = 90 * 60000; // walkable for about 90 minutes either side

const time = (ms) => new Date(ms).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', hour12: false });

function lowTides(day) {
  const start = new Date(day.getFullYear(), day.getMonth(), day.getDate()).getTime();
  const end = start + 86400000;
  const lows = [];
  for (let k = Math.ceil((start - REFERENCE_LOW) / PERIOD); REFERENCE_LOW + k * PERIOD < end; k++) {
    lows.push(REFERENCE_LOW + k * PERIOD);
  }
  return lows;
}

function describe(day) {
  const start = new Date(day.getFullYear(), day.getMonth(), day.getDate()).getTime();
  const lows = lowTides(day);
  // Windows that cross midnight are cut to this day so every time shown belongs to it.
  const walks = lows.map((t) => {
    if (t - WINDOW < start) return `until ${time(t + WINDOW)}`;
    if (t + WINDOW >= start + 86400000) return `from ${time(t - WINDOW)}`;
    return `${time(t - WINDOW)}–${time(t + WINDOW)}`;
  });
  return `Low water at ${lows.map(time).join(' and ')}. The lighthouse path is open ${walks.join(', and again ')}.`;
}

function tide() {
  const input = document.getElementById('tide-date');
  const out = document.getElementById('tide-out');
  if (!input || !out) return;
  const today = new Date();
  const pad = (n) => String(n).padStart(2, '0');
  input.value = `${today.getFullYear()}-${pad(today.getMonth() + 1)}-${pad(today.getDate())}`;
  const update = () => {
    const [y, m, d] = input.value.split('-').map(Number);
    out.textContent = y ? describe(new Date(y, m - 1, d)) : 'Pick a day to see its low tides.';
  };
  input.addEventListener('input', update);
  update();
}

function preview() {
  const list = document.querySelector('.facts');
  const frame = document.getElementById('frame-img');
  if (!list || !frame) return;
  const facts = [...list.querySelectorAll('.fact')];
  const show = (fact) => {
    const img = document.getElementById(fact.dataset.img);
    facts.forEach((f) => f.classList.toggle('active', f === fact));
    list.classList.add('has-active');
    if (frame.src === img.src) return;
    frame.classList.add('swap');
    setTimeout(() => { frame.src = img.src; frame.alt = ''; frame.classList.remove('swap'); }, 120);
  };
  facts.forEach((fact) => {
    fact.addEventListener('pointerenter', () => show(fact));
    fact.addEventListener('focus', () => show(fact));
    fact.addEventListener('click', () => show(fact));
  });
  list.addEventListener('pointerleave', () => {
    list.classList.remove('has-active');
    facts.forEach((f) => f.classList.remove('active'));
  });
}

function deck() {
  const section = document.querySelector('.rooms');
  const cards = [...document.querySelectorAll('.card')];
  const wide = matchMedia('(min-width: 768px)');
  if (!section || !cards.length) return;
  const update = () => {
    if (!wide.matches) { cards.forEach((c) => c.classList.remove('spine')); return; }
    const range = section.offsetHeight - innerHeight;
    const progress = Math.min(1, Math.max(0, -section.getBoundingClientRect().top / range));
    const active = Math.min(cards.length - 1, Math.floor(progress * cards.length));
    cards.forEach((c, i) => c.classList.toggle('spine', i < active));
  };
  cards.forEach((card, i) => card.addEventListener('click', () => {
    if (!card.classList.contains('spine')) return;
    const range = section.offsetHeight - innerHeight;
    scrollTo({ top: section.offsetTop + range * (i + 0.5) / cards.length });
  }));
  addEventListener('scroll', update, { passive: true });
  wide.addEventListener('change', update);
  update();
}

function entrances() {
  const items = document.querySelectorAll('[data-enter]');
  if (!('IntersectionObserver' in window)) { items.forEach((el) => el.classList.add('in')); return; }
  const seen = new IntersectionObserver((entries) => entries.forEach((e) => {
    if (e.isIntersecting) { e.target.classList.add('in'); seen.unobserve(e.target); }
  }), { rootMargin: '0px 0px -10% 0px' });
  items.forEach((el) => seen.observe(el));
}

if (typeof document !== 'undefined') {
  document.documentElement.classList.add('js');
  tide(); preview(); deck(); entrances();
}
