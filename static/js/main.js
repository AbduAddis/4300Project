/**
 * Change color scheme of page from Dark to light or vice versa.
 */
function changeColor() {
  if (document.body.style.background != "gray") {
    document.getElementById("dark-mode-btn").src =
      "/static/images/lightmode.png";
    document.body.style.background = "gray";
    document.getElementById("profile-bg").style.background = "gray";
  } else {
    document.getElementById("dark-mode-btn").src =
      "/static/images/darkmode.png";
    document.body.style.background = "#ebeff5";
    document.getElementById("profile-bg").style.background = "#ebeff5";
  }
}
