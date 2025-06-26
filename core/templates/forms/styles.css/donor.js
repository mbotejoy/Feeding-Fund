// Animate progress bar on load
window.onload = function() {
  const progress = document.getElementById('progressBar');
  setTimeout(() => {
    progress.style.width = '70%'; // Animate to 70%
  }, 300);

  // Simple animated chart (bar)
  const ctx = document.getElementById('donationChart').getContext('2d');
  ctx.fillStyle = '#e91e63';
  ctx.fillRect(20, 80, 30, -40); // Jan
  ctx.fillRect(60, 80, 30, -60); // Feb
  ctx.fillRect(100, 80, 30, -70); // Mar
  ctx.fillRect(140, 80, 30, -50); // Apr

  ctx.fillStyle = '#0097a7';
  ctx.font = "12px Arial";
  ctx.fillText("Jan", 25, 95);
  ctx.fillText("Feb", 65, 95);
  ctx.fillText("Mar", 105, 95);
  ctx.fillText("Apr", 145, 95);
};
