// Function to create the centered div with text
function createCenteredDivWithText() {
    // Listen for the custom event 'showMessage'
    document.addEventListener('showMessage', function(event) {
        const text = event.detail.text;

        // Create the overlay div
        const overlay = document.createElement('div');
        overlay.style.position = 'fixed';
        overlay.style.top = '0';
        overlay.style.left = '0';
        overlay.style.width = '100%';
        overlay.style.height = '100%';
        overlay.style.display = 'flex';
        overlay.style.justifyContent = 'center';
        overlay.style.alignItems = 'center';
        overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
        overlay.style.zIndex = '1000'; // Ensure it's on top of other elements

        // Create the content div
        const contentDiv = document.createElement('div');
        contentDiv.style.backgroundColor = 'white';
        contentDiv.style.padding = '20px';
        contentDiv.style.borderRadius = '8px';
        contentDiv.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)';
        contentDiv.style.textAlign = 'center';

        // Create the text element
        const textElement = document.createElement('p');
        textElement.textContent = text;
        contentDiv.appendChild(textElement);

        // Create the button
        const button = document.createElement('button');
        button.textContent = 'OK';
        button.style.marginTop = '10px';
        button.addEventListener('click', () => {
            document.body.removeChild(overlay);
        });
        contentDiv.appendChild(button);

        // Append the content div to the overlay
        overlay.appendChild(contentDiv);

        // Append the overlay to the body
        document.body.appendChild(overlay);
    });
}

// Call the function to set up the event listener
createCenteredDivWithText();