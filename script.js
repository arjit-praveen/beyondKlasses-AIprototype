async function fetchImages() {
    const input = document.getElementById("inputBox").value;

    // fetch JSON
    const response = await fetch("http://127.0.0.1:5000/get-images", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input: input })
    });

    // debug
    console.log(response)

    const data = await response.json();
    const container = document.getElementById("imageContainer");
    container.innerHTML = "";

    // Drawing name + text
    const title = document.createElement("h3");
    title.textContent = data.name;
    container.appendChild(title);

    const desc = document.createElement("p");
    desc.textContent = data.description;
    container.appendChild(desc);

    // Show images and Step text
    data.steps.forEach(step => {
        const stepDiv = document.createElement("div");
        stepDiv.style.marginBottom = "1rem";

        const img = document.createElement("img");
        img.src = step.imageUrl;
        img.width = 200;

        const caption = document.createElement("p");
        caption.textContent = `Step ${step.stepNumber}: ${step.steps}`;

        stepDiv.appendChild(caption);
        stepDiv.appendChild(img);
                
        container.appendChild(stepDiv);
    });
}