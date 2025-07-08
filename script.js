import confetti from 'https://cdn.skypack.dev/canvas-confetti';

const canvas = document.getElementById('sparkles');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

class Sparkle {
  constructor() {
    this.x = Math.random() * canvas.width;
    this.y = Math.random() * canvas.height;
    this.size = Math.random() * 2 + 1;
    this.speed = Math.random() * 1 + 0.5;
    this.opacity = Math.random() * 0.5 + 0.5;
  }
  update() {
    this.y -= this.speed;
    if (this.y < 0) this.y = canvas.height;
  }
  draw() {
    ctx.fillStyle = `rgba(255,255,255,${this.opacity})`;
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.size, 0, Math.PI*2);
    ctx.fill();
  }
}

const sparkles = Array.from({length: 200}, () => new Sparkle());
function animate() {
  ctx.clearRect(0,0,canvas.width,canvas.height);
  sparkles.forEach(s => { s.update(); s.draw(); });
  requestAnimationFrame(animate);
}
animate();

document.getElementById('confettiBtn').addEventListener('click', () => {
  confetti({ particleCount: 200, spread: 70, origin: { y: 0.6 } });
});

const bgm = document.getElementById('bgm');
const cry = document.getElementById('cry');

window.addEventListener('DOMContentLoaded', () => {
  bgm.volume = 0.5;
  bgm.play().catch(() => {
    const btn = document.createElement('button');
    btn.textContent = 'Play music 🎵';
    btn.className = 'mt-4 px-4 py-2 bg-blue-500 text-white rounded';
    btn.onclick = () => bgm.play();
    document.querySelector('main').appendChild(btn);
  });
});

document.getElementById('playCry').addEventListener('click', () => {
  cry.play();
});

// Countdown to Nicole’s next birthday
const targetDate = new Date("2026-07-08T00:00:00");
const countdownEl = document.getElementById("countdown");

function updateCountdown() {
  const now = new Date();
  const diff = targetDate - now;
  if (diff <= 0) {
    countdownEl.textContent = "It’s your birthday again!! 🎉";
    return;
  }
  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
  const minutes = Math.floor((diff / 1000 / 60) % 60);
  countdownEl.textContent = `Next chaos drop in ${days}d ${hours}h ${minutes}m`;
}
setInterval(updateCountdown, 1000);
updateCountdown();