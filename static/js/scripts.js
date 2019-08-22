function openNav() {
  document.getElementById("bar").style.height = "100%";
  document.getElementById("content").style.height = "100%";
}

function closeNav() {
  document.getElementById("bar").style.height = "0";
  document.getElementById("content").style.visible = "0";
}

function change() {
	if(document.getElementById("bar").style.height === "0") {
		openNav();
	}
	else {
		closeNav();
	}
}