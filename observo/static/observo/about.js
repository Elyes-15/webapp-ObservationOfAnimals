document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("toggle-btn");
    const techList = document.getElementById("tech-list");

    btn.addEventListener("click", () => {
        techList.classList.toggle("hidden");
    });
});