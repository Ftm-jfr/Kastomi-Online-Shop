document.addEventListener("DOMContentLoaded", () => {

  const filterLinks = document.querySelectorAll(".filter_container a");
  const mainSection = document.querySelector(".main-section");

  const sections = {
    current  : document.getElementById("current"),
    delivered: document.getElementById("delivered"),
    returned : document.getElementById("returned"),
    canceled : document.getElementById("canceled")
  };

  const targets = ["current", "delivered", "returned", "canceled"];

  filterLinks.forEach((link, idx) => {
    link.addEventListener("click", (e) => {
      e.preventDefault();

      filterLinks.forEach(l => l.classList.remove("active"));
      link.classList.add("active");

      const id = targets[idx];
      Object.values(sections).forEach(sec => sec.classList.add("hidden"));
      sections[id].classList.remove("hidden");

      mainSection.className = "main-section";
      mainSection.classList.add(`${id}-main`);
    });
  });
});
