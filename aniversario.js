const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

let w = window.innerWidth;
let h = window.innerHeight;
canvas.width = w;
canvas.height = h;

let message = "FELIZ ANIVERSÁRIO";
let letters = [];

const opts = {
  charSize: 40,
  fireworkSpawnTime: 30
};

let hw = w / 2;
let hh = h / 2;

function Letter(char, x, y) {
  this.char = char;
  this.x = x;
  this.y = y;
  this.dx = -ctx.measureText(char).width / 2;
  this.dy = +opts.charSize / 2;
  this.fireworkDy = this.y - hh;
  var hue = (x / (ctx.measureText(message).width)) * 360;
  this.color = `hsl(${hue}, 80%, 50%)`;
  this.lightColor = `hsl(${hue}, 100%, 75%)`;
  this.alphaColor = `hsla(${hue}, 80%, 50%, 0.5)`;
  this.reset();
}

Letter.prototype.reset = function () {
  this.phase = "firework";
  this.tick = 0;
  this.spawned = false;
  this.spawningTime = (opts.fireworkSpawnTime * Math.random()) | 0;
};

Letter.prototype.update = function () {
  if (this.phase === "firework") {
    if (this.tick++ > this.spawningTime) {
      this.phase = "shown";
    }
  }
};

Letter.prototype.draw = function () {
  ctx.fillStyle = this.color;
  ctx.font = opts.charSize + "px Arial";
  ctx.fillText(this.char, this.x + this.dx, this.y + this.dy);
};

function init() {
  ctx.font = opts.charSize + "px Arial";
  let totalWidth = ctx.measureText(message).width;
  let startX = hw - totalWidth / 2;

  letters = [];
  let x = startX;
  for (let i = 0; i < message.length; i++) {
    let ch = message[i];
    let letterWidth = ctx.measureText(ch).width;
    letters.push(new Letter(ch, x + letterWidth / 2, hh));
    x += letterWidth;
  }
}

function anim() {
  ctx.fillStyle = "rgba(0,0,0,0.2)";
  ctx.fillRect(0, 0, w, h);

  letters.forEach(l => {
    l.update();
    l.draw();
  });

  requestAnimationFrame(anim);
}

init();
anim();

window.onresize = function () {
  w = window.innerWidth;
  h = window.innerHeight;
  hw = w / 2;
  hh = h / 2;
  canvas.width = w;
  canvas.height = h;
  init();
};
