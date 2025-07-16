document.addEventListener("DOMContentLoaded", function () {
    const navItems = document.querySelectorAll(".nav-item");
    const productSections = document.querySelectorAll(".product-section");

    let currentOpenSection = null;

    navItems.forEach(item => {
        item.addEventListener("click", function (e) {
            e.preventDefault();
            const targetId = this.getAttribute("data-target");
            const targetSection = document.getElementById(targetId);


            if (currentOpenSection && currentOpenSection === targetSection) {
                currentOpenSection.classList.add("hidden");
                currentOpenSection = null;
                return;
            }

            productSections.forEach(section => section.classList.add("hidden"));

            if (targetSection) {
                targetSection.classList.remove("hidden");
                currentOpenSection = targetSection;
            }
        });
    });

    document.addEventListener("click", function (e) {
        const isClickInsideSection = currentOpenSection && currentOpenSection.contains(e.target);
        const isClickOnNavItem = e.target.closest(".nav-item");

        if (currentOpenSection && !isClickInsideSection && !isClickOnNavItem) {
            currentOpenSection.classList.add("hidden");
            currentOpenSection = null;
        }
    });
});
