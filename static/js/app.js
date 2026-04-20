// QuickQ Global JS
document.addEventListener("DOMContentLoaded", () => {
  console.log("QuickQ App Loaded ✅");

  // Example: Navbar active state
  const navLinks = document.querySelectorAll(".navbar a");
  navLinks.forEach(link => {
    if (link.href === window.location.href) {
      link.style.fontWeight = "bold";
    }
  });
});
