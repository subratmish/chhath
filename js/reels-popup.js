document.addEventListener('DOMContentLoaded', function () {
    const reelItems = document.querySelectorAll('.reel-item');
    const modal = document.getElementById('reelsModal');
    if (!modal) return; // Stop if modal doesn't exist

    const videoTrack = modal.querySelector('.reels-video-track');
    const videoSlides = {
        prev: modal.querySelector('#reelVideoPrev'),
        current: modal.querySelector('#reelsVideoPlayer'),
        next: modal.querySelector('#reelVideoNext')
    };
    const videoTitle = document.getElementById('reelsVideoTitle');
    const closeBtn = modal.querySelector('.reels-modal-close');
    const prevBtn = document.getElementById('reelPrevBtn');
    const nextBtn = document.getElementById('reelNextBtn');
    const muteBtn = document.getElementById('reelMuteBtn');
    const playPauseIcon = document.getElementById('reelPlayPauseIcon');

    let reelsData = [];
    let currentIndex = 0;
    let touchStartY = 0;
    let isAnimating = false;
    const animationDuration = 500; // This should match the CSS transition duration in milliseconds

    // 1. Collect all video data
    reelItems.forEach((item, index) => {
        reelsData.push({
            src: item.dataset.videoSrc,
            title: item.dataset.videoTitle,
        });
        item.dataset.index = index;
        item.addEventListener('click', () => {
            currentIndex = parseInt(item.dataset.index, 10);
            openModal();
        });
    });

    // 2. Core Functions
    function openModal() {
        updateVideoSlides();
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeModal() {
        modal.classList.remove('active');
        document.body.style.overflow = 'auto';
        Object.values(videoSlides).forEach(video => {
            video.pause();
            video.src = '';
        });
    }

    function updateVideoSlides() {
        const prevIndex = (currentIndex - 1 + reelsData.length) % reelsData.length;
        const nextIndex = (currentIndex + 1) % reelsData.length;

        videoSlides.prev.src = reelsData[prevIndex].src;
        videoSlides.current.src = reelsData[currentIndex].src;
        videoSlides.next.src = reelsData[nextIndex].src;

        videoTitle.textContent = reelsData[currentIndex].title;

        videoSlides.current.play().catch(e => console.log("Autoplay prevented"));
        updateMuteIcon();
    }

    // =======================================================
    // == UPDATED: More robust slide animation function ==
    // =======================================================
    function slideTo(direction) {
        if (isAnimating) return;
        isAnimating = true;

        // Apply the transition class to start the animation
        videoTrack.style.transition = `top ${animationDuration / 1000}s cubic-bezier(0.23, 1, 0.32, 1)`;
        
        if (direction === 'next') {
            videoTrack.style.top = '-200%';
            currentIndex = (currentIndex + 1) % reelsData.length;
        } else { // prev
            videoTrack.style.top = '0%';
            currentIndex = (currentIndex - 1 + reelsData.length) % reelsData.length;
        }

        // Use a reliable timer to reset the state after the animation
        setTimeout(() => {
            // Pause all videos during the reset
            Object.values(videoSlides).forEach(video => video.pause());

            // Quietly reset the track to the middle position without animating
            videoTrack.style.transition = 'none';
            videoTrack.style.top = '-100%';
            
            // Load the new set of videos
            updateVideoSlides();
            
            // Re-enable animation for the next swipe
            // A tiny delay ensures the browser applies the 'none' transition first
            setTimeout(() => {
                isAnimating = false; // Release the lock for the next swipe
            }, 50);

        }, animationDuration);
    }

    // 3. Event Listeners (no changes here, but kept for context)
    closeBtn.addEventListener('click', closeModal);
    nextBtn.addEventListener('click', () => slideTo('next'));
    prevBtn.addEventListener('click', () => slideTo('prev'));

    window.addEventListener('keydown', (e) => {
        if (!modal.classList.contains('active')) return;
        if (e.key === 'ArrowDown' || e.key === 'ArrowRight') slideTo('next');
        if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') slideTo('prev');
        if (e.key === 'Escape') closeModal();
    });

    // Tap to Play/Pause
    videoSlides.current.addEventListener('click', () => {
        if (videoSlides.current.paused) {
            videoSlides.current.play();
        } else {
            videoSlides.current.pause();
        }
    });
    videoSlides.current.addEventListener('play', () => playPauseIcon.classList.remove('visible'));
    videoSlides.current.addEventListener('pause', () => playPauseIcon.classList.add('visible'));

    // Mute/Unmute
    function updateMuteIcon() {
        const icon = muteBtn.querySelector('i');
        if (videoSlides.current.muted) {
            icon.classList.remove('bi-volume-up-fill');
            icon.classList.add('bi-volume-mute-fill');
        } else {
            icon.classList.add('bi-volume-up-fill');
            icon.classList.remove('bi-volume-mute-fill');
        }
    }
    muteBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        videoSlides.current.muted = !videoSlides.current.muted;
        updateMuteIcon();
    });

    // Swipe Listeners
    modal.addEventListener('touchstart', (e) => { touchStartY = e.touches[0].clientY; });
    modal.addEventListener('touchend', (e) => {
        const touchEndY = e.changedTouches[0].clientY;
        const deltaY = touchEndY - touchStartY;
        if (Math.abs(deltaY) > 50) {
            if (deltaY < 0) slideTo('next'); // Swipe Up
            else slideTo('prev'); // Swipe Down
        }
    });
});