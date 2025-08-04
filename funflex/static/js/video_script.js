const video = document.getElementById('myVideo');
const playPauseBtn = document.getElementById('playPauseBtn');
const progressBar = document.getElementById('progressBar');
const volumeBtn = document.getElementById('volumeBtn');
const volumeSlider = document.getElementById('volumeSlider');
const fullscreenBtn = document.getElementById('fullscreenBtn');
const videoContainer = document.querySelector('.video-container');
const videoTitle = document.querySelector('.video-title');
const videoControls = document.querySelector('.video-controls');

let controlsTimeout;

// Show Controls When Mouse Moves
videoContainer.addEventListener('mousemove', () => {
    showControls();
    resetHideControls();
});

// Hide Controls After 3 Seconds
function hideControls() {
    videoTitle.classList.add('hidden');
    videoControls.classList.add('hidden');
}

function showControls() {
    videoTitle.classList.remove('hidden');
    videoControls.classList.remove('hidden');
}

function resetHideControls() {
    clearTimeout(controlsTimeout);
    controlsTimeout = setTimeout(hideControls, 3000);
}

// Play/Pause Button
playPauseBtn.addEventListener('click', togglePlay);
video.addEventListener('click', togglePlay);

function togglePlay() {
    if (video.paused) {
        video.play();
        playPauseBtn.innerHTML = '<i class="fas fa-pause"></i>';
    } else {
        video.pause();
        playPauseBtn.innerHTML = '<i class="fas fa-play"></i>';
    }
}

// Progress Bar
video.addEventListener('timeupdate', updateProgress);
progressBar.addEventListener('input', seek);

function updateProgress() {
    const progress = (video.currentTime / video.duration) * 100;
    progressBar.value = progress;
}

function seek() {
    video.currentTime = (progressBar.value * video.duration) / 100;
}

// Volume Control
volumeSlider.addEventListener('input', updateVolume);
volumeBtn.addEventListener('click', toggleMute);

function updateVolume() {
    video.volume = volumeSlider.value;
    volumeBtn.innerHTML = video.volume === 0 ? 
        '<i class="fas fa-volume-mute"></i>' :
        '<i class="fas fa-volume-up"></i>';
}

function toggleMute() {
    if (video.muted || video.volume === 0) {
        video.muted = false;
        video.volume = 1;
        volumeSlider.value = 1;
        volumeBtn.innerHTML = '<i class="fas fa-volume-up"></i>';
    } else {
        video.muted = true;
        volumeSlider.value = 0;
        volumeBtn.innerHTML = '<i class="fas fa-volume-mute"></i>';
    }
}

// Fullscreen Toggle
fullscreenBtn.addEventListener('click', toggleFullscreen);

function toggleFullscreen() {
    if (!document.fullscreenElement) {
        video.parentElement.requestFullscreen();
        fullscreenBtn.innerHTML = '<i class="fas fa-compress"></i>';
    } else {
        document.exitFullscreen();
        fullscreenBtn.innerHTML = '<i class="fas fa-expand"></i>';
    }
}

// Start Hide Timer on Load
resetHideControls();

// Adding hover effect for Play/Pause button
playPauseBtn.addEventListener('mouseover', () => {
    playPauseBtn.classList.add('hovered');
});

playPauseBtn.addEventListener('mouseout', () => {
    playPauseBtn.classList.remove('hovered');
});

// Adding hover effect for Volume button
volumeBtn.addEventListener('mouseover', () => {
    volumeBtn.classList.add('hovered');
});

volumeBtn.addEventListener('mouseout', () => {
    volumeBtn.classList.remove('hovered');
});

// Adding hover effect for Fullscreen button
fullscreenBtn.addEventListener('mouseover', () => {
    fullscreenBtn.classList.add('hovered');
});

fullscreenBtn.addEventListener('mouseout', () => {
    fullscreenBtn.classList.remove('hovered');
});
