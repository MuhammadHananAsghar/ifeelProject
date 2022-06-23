let menu = document.getElementById("menu");
let cancel = document.getElementById("cancel");


menu.onclick = () => {
    let sidebar = document.querySelector(".sidebar");
    let bodySidebar = document.querySelector(".body");
    if(sidebar.style.width === "" || sidebar.style.width === "0px"){
        sidebar.style.height = "100%";
        sidebar.style.width = "100%";
        sidebar.style.position = "fixed";
        sidebar.style.zIndex = "10";
        sidebar.style.left = "0";
        sidebar.style.right = "0";
        sidebar.style.backgroundColor = "rgb(27, 42, 53)";
        bodySidebar.style.padding = "0rem 3rem";
        bodySidebar.style.marginTop = "3rem";
    }else{
        return
    }
}
cancel.onclick = () => {
    let sidebar = document.querySelector(".sidebar");
    sidebar.style.width = "0px";
}


