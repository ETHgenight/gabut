document.addEventListener("DOMContentLoaded", () => {
  // Tombol Beli Sekarang
  const beliButton = document.querySelector("button");
  beliButton.addEventListener("click", () => {
      beliButton.innerText = "Memproses...";
      beliButton.style.backgroundColor = "#333";

      setTimeout(() => {
          alert("Selamat! Anda akan diarahkan ke halaman pembelian.");
          beliButton.innerText = "Beli Sekarang";
          beliButton.style.backgroundColor = "#ff3e00";
      }, 2000);
  });

  // Dark Mode Toggle
  const toggleDarkMode = document.createElement("button");
  toggleDarkMode.innerText = "Toggle Dark Mode";
  toggleDarkMode.style.position = "fixed";
  toggleDarkMode.style.top = "10px";
  toggleDarkMode.style.right = "10px";
  toggleDarkMode.style.backgroundColor = "#444";
  toggleDarkMode.style.color = "white";
  toggleDarkMode.style.padding = "10px 15px";
  toggleDarkMode.style.border = "none";
  toggleDarkMode.style.cursor = "pointer";
  document.body.appendChild(toggleDarkMode);

  let darkMode = true;
  toggleDarkMode.addEventListener("click", () => {
      if (darkMode) {
          document.body.style.backgroundColor = "white";
          document.body.style.color = "black";
          toggleDarkMode.innerText = "Toggle Light Mode";
      } else {
          document.body.style.backgroundColor = "#111";
          document.body.style.color = "white";
          toggleDarkMode.innerText = "Toggle Dark Mode";
      }
      darkMode = !darkMode;
  });

  // Hover Effect pada Fitur
  const features = document.querySelectorAll(".feature");
  features.forEach(feature => {
      feature.addEventListener("mouseenter", () => {
          feature.style.transform = "scale(1.15)";
          feature.style.transition = "transform 0.3s ease-in-out";
      });

      feature.addEventListener("mouseleave", () => {
          feature.style.transform = "scale(1)";
      });
  });
});
