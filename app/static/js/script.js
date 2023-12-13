nCol = 1006;
nRow = 16;
nSize = 40;
maxPeroid = 3000;
maxInterval = 5000;
baseColor = "#222";

// Function to generate a random color
function getRandomColor() {
  const letters = "0123456789ABCDEF";
  let color = "#";
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

// Function to set a random color to a star
function setRandomColor(star) {
  const color = getRandomColor();
  star.style.backgroundColor = color;
}

// Function to reset a star to blue color
function resetColor(star) {
  star.style.backgroundColor = baseColor;
}

// Function to randomly change a star's color at random intervals
function randomColorChange(star) {
  setInterval(() => {
    setRandomColor(star);
    setTimeout(() => {
      resetColor(star);
    }, Math.random() * maxPeroid); // Random period to keep the star in the new color
  }, Math.random() * (maxInterval - 1000) + 1000); // Random interval for color change
}

// Function to create a star element
function createStar() {
  const star = document.createElement("div");
  star.className = "star";
  return star;
}

// Function to randomly generate a frequency for the swing animation
function getRandomFrequency() {
  return Math.random() * 5 + 1; // Adjust the range of frequencies as needed
}

// Function to apply swing animation to a star with a random frequency
function applySwingAnimation(star) {
  const frequency = getRandomFrequency();
  star.style.animationDuration = `${frequency}s`;
}

// Create 12 x 12 matrix of stars
for (let i = 0; i < nRow; i++) {
  for (let j = 0; j < nCol; j++) {
    const star = createStar();
    star.style.top = `${i * nSize}px`; // Adjust spacing
    star.style.left = `${j * nSize}px`; // Adjust spacing
    document.body.appendChild(star);
    randomColorChange(star);
    applySwingAnimation(star);
  }
}
