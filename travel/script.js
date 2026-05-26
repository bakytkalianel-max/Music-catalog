let rotation = 0;

const places = [
  "Алматы",
  "Маңғыстау",
  "Түркістан",
  "Көлсай",
  "Шарын",
  "Бурабай"
];

function spin() {
  const wheel = document.getElementById("wheel");
  const result = document.getElementById("result");

  const randomIndex = Math.floor(Math.random() * places.length);
  const deg = 360 / places.length;

  const finalDeg = 360 * 6 + (360 - randomIndex * deg - deg / 2);

  rotation += finalDeg;

  wheel.style.transform = rotate(${rotation}deg);

  result.innerHTML = "Айналып жатыр...";

  setTimeout(() => {
    result.innerHTML = `
      <h2>Сенің бағытың: ${places[randomIndex]}</h2>
    `;
  }, 4000);
}