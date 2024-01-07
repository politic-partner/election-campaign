window.addEventListener("load", func = () => {
	for (const external_link of document.querySelectorAll("a.external")) {
		external_link.setAttribute("target", "_blank");
		external_link.setAttribute("rel", "noopener noreferrer");
	}
	for (const div of document.querySelectorAll("svg div")) {
		switch (div.style.color) {
			case "rgb(42, 90, 223)":
				div.style.color = "var(--color-link)";
				break;
			case "rgb(0, 0, 0)":
				div.style.color = "var(--color-content-foreground)";
				break;
		}
	}
});
