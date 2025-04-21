document.addEventListener('DOMContentLoaded', function () {
    // Scroll to section functionality
    const point1 = document.getElementById('point-1');
    const point2 = document.getElementById('point-2');
    if (point1 && point2) {
        point1.addEventListener('click', function () {
            point2.scrollIntoView({ behavior: 'smooth' });
        });
    }

    // Reusable modal functionality
    function setupModal(openBtnId, modalId) {
        const openBtn = document.getElementById(openBtnId);
        const modal = document.getElementById(modalId);
        const closeBtn = modal ? modal.querySelector('.close') : null;

        if (openBtn && modal) {
            openBtn.onclick = function () {
                modal.style.display = 'block';
            };
        }
        if (closeBtn && modal) {
            closeBtn.onclick = function () {
                modal.style.display = 'none';
            };
        }
        window.addEventListener('click', function (event) {
            if (event.target == modal) {
                modal.style.display = 'none';
            }
        });
    }

    // Initialize modals
    setupModal('openReservationModal', 'reservationModal');
    setupModal('openWellnessModal', 'wellnessReservationModal');
});
