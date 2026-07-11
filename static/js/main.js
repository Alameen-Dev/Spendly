// main.js — students will add JavaScript here as features are built

// Video Modal functionality
document.addEventListener('DOMContentLoaded', function() {
    var openModalBtn = document.getElementById('open-modal');
    var modal = document.getElementById('video-modal');
    var closeModalBtn = document.getElementById('close-modal');
    var videoIframe = document.getElementById('modal-video');

    // Only run if modal elements exist on the page
    if (!openModalBtn || !modal) return;

    function openModal() {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeModal() {
        modal.classList.remove('active');
        document.body.style.overflow = '';
        // Stop the video by reloading the iframe src
        var videoSrc = videoIframe.src;
        videoIframe.src = '';
        videoIframe.src = videoSrc;
    }

    openModalBtn.addEventListener('click', openModal);
    closeModalBtn.addEventListener('click', closeModal);

    // Close when clicking outside the modal content
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Close on Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeModal();
        }
    });
});
