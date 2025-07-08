// Sparkles background
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

// Confetti on button click
import confetti from 'https://cdn.skypack.dev/canvas-confetti';
document.getElementById('breakdown').addEventListener('click', () => {
  confetti({
    particleCount: 150,
    spread: 70,
    origin: { y: 0.6 }
  });
});

// Play music on load
window.addEventListener('DOMContentLoaded', () => {
  const bgm = document.getElementById('bgm');
  bgm.volume = 0.5;
  bgm.play().catch(() => {
    const btn = document.createElement('button');
    btn.textContent = 'Play music 🎵';
    btn.className = 'mt-4 px-4 py-2 bg-blue-500 text-white rounded';
    btn.onclick = () => bgm.play();
    document.querySelector('main').appendChild(btn);
  });
});
