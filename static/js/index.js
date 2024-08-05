const sidebar = document.querySelector(".sidebar");
const sidebarToggle = document.querySelector("#sidebar-close");
const menu = document.querySelector(".menu-content");
const menuItems = document.querySelectorAll(".submenu-item");
const subMenuTitles = document.querySelectorAll(".submenu .menu-title");

// sidebarClose.addEventListener("click", () => sidebar.classList.toggle("close"))
sidebarToggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    sidebarToggle.classList.toggle("fa-bars");
    sidebarToggle.classList.toggle("fa-xmark");
});

menuItems.forEach((item,index) => {
    item.addEventListener("click", () => {
        menu.classList.add("submenu-active");
        item.classList.add("show-submenu");
        menuItems.forEach((item2, index2) => {
            if (index !== index2){
                item2.classList.remove("show-submenu")
            }
        }) 
    })
})

subMenuTitles.forEach((title) => {
    title.addEventListener("click", () => {
        menu.classList.remove("submenu-active");
    })
})

console.log(menuItems, subMenuTitles)