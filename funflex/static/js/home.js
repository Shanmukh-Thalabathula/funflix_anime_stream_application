function showPopup(title, category, description) {
    const popup = document.getElementById('popup');
    const overlay = document.getElementById('overlay');

    // Set popup content
    document.getElementById('popup-title').innerText = title;
    document.getElementById('popup-category').innerText = category;
    document.getElementById('popup-description').innerText = description;

    // Show the popup and overlay
    popup.style.display = 'flex';
    overlay.style.display = 'block';

    // Add animation to show popup (Netflix-style animation)
    setTimeout(() => {
        popup.classList.add('show');
    }, 50);
}

function closePopup() {
    const popup = document.getElementById('popup');
    const overlay = document.getElementById('overlay');

    // Remove popup animation class
    popup.classList.remove('show');

    // Add Netflix-style closing animation
    setTimeout(() => {
        popup.style.display = 'none';
        overlay.style.display = 'none';
    }, 300); // Delay to match the animation
}
