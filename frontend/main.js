document.getElementById("load").addEventListener("click", async () => {
  const res = await fetch("https://cristal-backend.onrender.com/api/phrases");
  const data = await res.json();
  document.getElementById("phrase").innerText = data[0] || "Aucune phrase disponible.";
});
