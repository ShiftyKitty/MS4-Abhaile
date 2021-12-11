const root = document.documentElement;
    const marqueeElementsDisplayed = getComputedStyle(root).getPropertyValue("--marquee-elements-displayed");
    const marqueeElementsDisplayed2 = getComputedStyle(root).getPropertyValue("--marquee-elements-displayed2");

    const marqueeContent = document.querySelector("ul.marquee-content");
    const marqueeContent2 = document.querySelector("ul.marquee-content2");

    root.style.setProperty("--marquee-elements", marqueeContent.children.length);

    root.style.setProperty("--marquee-elements2", marqueeContent2.children.length);

    for (let i = 0; i < marqueeElementsDisplayed; i++) {
        marqueeContent.appendChild(marqueeContent.children[i].cloneNode(true));
    }

    for (let i = 0; i < marqueeElementsDisplayed2; i++) {
        marqueeContent2.appendChild(marqueeContent2.children[i].cloneNode(true));
    }