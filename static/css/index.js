// Sidebar Panel events
let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".fa-circle-chevron-left");
const toggleBtn = document.querySelector("#toggle-btn");

sidebarBtn.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    if (sidebar.classList.contains("close")) {
        sidebarBtn.classList.remove('fa-circle-chevron-left');
        sidebarBtn.classList.add('fa-circle-chevron-right');
        toggleBtn.style.color = 'black';
    } else {
        sidebarBtn.classList.remove('fa-circle-chevron-right');
        sidebarBtn.classList.add('fa-circle-chevron-left');
        toggleBtn.style.color = 'white';
    }
});

const menu = document.querySelector(".menu-content");
const menuItems = document.querySelectorAll(".submenu-item");
const subMenuTitles = document.querySelectorAll(".submenu .menu-title");

// Handle submenu clicks
menuItems.forEach((item, index) => {
    item.addEventListener("click", () => {
        if (menu) {
            menu.classList.add("submenu-active");
        }
        item.classList.add("show-submenu");
        menuItems.forEach((item2, index2) => {
            if (index !== index2) {
                item2.classList.remove("show-submenu");
            }
        });
    });
});

subMenuTitles.forEach((title) => {
    title.addEventListener("click", () => {
        if (menu) {
            menu.classList.remove("submenu-active");
        }
    });
});

console.log(menuItems, subMenuTitles);

document.querySelectorAll('.submenu').forEach(function(submenu) {
    submenu.addEventListener('click', function(e) {
        e.stopPropagation();
    });
});

// JavaScript for handling submenu clicks and active class toggling
document.addEventListener("DOMContentLoaded", function() {
    // Function to set active state based on URL path
    function setActiveNav() {
        const path = window.location.pathname;
        
        // Add active class to current navigation
        document.querySelectorAll(".item a").forEach((item) => {
            if (item.getAttribute("href") === path) {
                item.parentElement.classList.add("active");
            }
        });

        // Open submenu if necessary
        document.querySelectorAll(".submenu-item").forEach((item) => {
            const link = item.querySelector("a");
            if (link && link.getAttribute("href") === path) {
                item.classList.add("active");
                const submenu = item.closest(".submenu");
                if (submenu) {
                    submenu.classList.add("show-submenu");
                }
            }
        });
    }

    // Set active navigation on load
    setActiveNav();

    // Handle submenu item clicks
    document.querySelectorAll(".submenu-item").forEach((item) => {
        item.addEventListener("click", function(event) {
            event.preventDefault(); // Prevent default link behavior

            // Remove 'active' class from all submenu items
            document.querySelectorAll(".submenu-item").forEach((item) => {
                item.classList.remove("active");
            });

            // Add 'active' class to the clicked submenu item
            this.classList.add("active");

            // Close other submenus if any are open
            document.querySelectorAll(".menu-items.submenu").forEach((submenu) => {
                if (submenu !== this.nextElementSibling) {
                    submenu.classList.remove("show-submenu");
                }
            });

            // Load content dynamically in the main section
            const link = this.querySelector("a");
            if (link) {
                let url = link.getAttribute("href");
                fetchContent(url);
            }
        });
    });

    // Function to fetch and display content
    function fetchContent(url) {
        fetch(url)
            .then(response => response.text())
            .then(data => {
                document.querySelector(".home-section").innerHTML = data;
            })
            .catch(error => console.error('Error fetching content:', error));
    }

    // Optional: Close submenu if clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.submenu-item')) {
            document.querySelectorAll('.submenu').forEach(submenu => {
                submenu.classList.remove('show-submenu');
            });
        }
    });
});
