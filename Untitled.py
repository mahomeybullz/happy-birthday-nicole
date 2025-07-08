from zipfile import ZipFile
import os

# Create directory and files
project_dir = "/mnt/data/happy-birthday-nicole"
os.makedirs(project_dir, exist_ok=True)

# index.html content
index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Happy Birthday Nicole — From Mahomey 💖</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body { background: #fff1f2; }
    .handwritten { font-family: 'Segoe Script', cursive; }
  </style>
</head>
<body class="min-h-screen flex flex-col items-center justify-center relative overflow-hidden">
  <!-- Sparkles -->
  <canvas id="sparkles" class="absolute inset-0"></canvas>

  <main class="p-6 bg-white bg-opacity-80 rounded-lg shadow-lg max-w-lg z-10">
    <h1 class="handwritten text-4xl text-pink-600 mb-4 text-center animate-pulse">
      🎂 Happy Birthday, Nicole 🎂
    </h1>
    <div class="text-gray-800 whitespace-pre-line leading-relaxed">
Let’s be honest, we’re both mentally cooked. Burnt out. Fried. Fuckrd up. Spiraling on a loop. But somehow, despite all that, we still have each other. And honestly? That’s kind of beautiful (and a little unhinged). Thank you for being my go-to person when I’m overthinking, crying, or just staring at the ceiling wondering what the hell is going on with life. Thank you for staying, even when I make zero sense, even when I disappear sometimes, even when I act like I’m okay when I’m very much not. You’re the one person I can be completely weird with — like ugly laugh, ugly cry, full mental breakdown at 1am weird — and never feel judged. I love that about us. No matter how messy life gets, no matter how many mental resets we need in a week, we always somehow end up sending each other TikToks or trauma-dumping at random times of day. I don’t always say this, but I’m really glad I have you. If I ever start acting like I don’t care, just know I do. Always. In my own non-clingy, sarcastic, emotionally constipated way. Love you, freak.
    </div>
    <button id="breakdown" class="mt-6 px-6 py-3 bg-pink-500 text-white rounded-full handwritten hover:bg-pink-600 transition">
      Let’s have a breakdown together 💀
    </button>
    <p class="text-center text-gray-500 mt-4">From Mahomey, your favorite freak.</p>
  </main>

  <audio id="bgm" src="happy.mp3" loop></audio>

  <script src="script.js" type="module"></script>
</body>
</html>"""

# script.js content
script_js = """// Sparkles background
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
"""

# Write files
with open(f"{project_dir}/index.html", "w") as f:
    f.write(index_html)
with open(f"{project_dir}/script.js", "w") as f:
    f.write(script_js)
# Create a placeholder MP3
with open(f"{project_dir}/happy.mp3", "wb") as f:
    f.write(b"\0" * 1000)

# Zip it
zip_path = "/mnt/data/happy-birthday-nicole.zip"
with ZipFile(zip_path, 'w') as zipf:
    for root, dirs, files in os.walk(project_dir):
        for file in files:
            filepath = os.path.join(root, file)
            arcname = os.path.relpath(filepath, project_dir)
            zipf.write(filepath, arcname)

zip_path 