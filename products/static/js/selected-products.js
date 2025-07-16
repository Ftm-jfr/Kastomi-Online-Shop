
document.addEventListener("DOMContentLoaded", () => {
  const openBtn   = document.getElementById("openCommentModalBtn");
  const modal     = document.getElementById("commentModal");
  const closeBtn  = modal.querySelector("#close");
  const submitBtn = modal.querySelector("#submitComment");
  const stars     = modal.querySelectorAll(".modal-stars button");

  let currentRating = 0;

  openBtn.addEventListener("click", () => {
    modal.classList.remove("hidden");
    resetStars();
  });

  closeBtn.addEventListener("click", hideModal);

  modal.addEventListener("click", (e) => {
    if (e.target === modal) hideModal();
  });


  submitBtn.addEventListener("click", () => {
    hideModal();
  });


  stars.forEach((star, index) => {
    star.addEventListener("click", () => {
      currentRating = (currentRating === index + 1) ? 0 : index + 1;
      updateStars();
    });
  });

  function updateStars() {
    stars.forEach((star, i) => {
      star.classList.toggle("filled", i < currentRating);
    });
  }

  function resetStars() {
    currentRating = 0;
    updateStars();
  }

  function hideModal() {
    modal.classList.add("hidden");
  }
});

