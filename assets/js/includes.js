async function loadNav() {
    const mount = document.getElementById("site-nav");
    if (!mount) return;
  
    const res = await fetch("/partials/nav.html");
    mount.innerHTML = await res.text();
  
    // Re-bind burger menu because nav was injected
    const nav = document.querySelector("nav");
    const burger = nav?.querySelector(".nav-burger");
  
    if (nav && burger) {
      burger.addEventListener("click", () => {
        const open = nav.classList.toggle("nav-open");
        burger.setAttribute("aria-expanded", String(open));
      });
    }
  }
  
  loadNav();