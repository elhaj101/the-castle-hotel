document.addEventListener('DOMContentLoaded', function () {
    // Scroll to section functionality
    const point1 = document.getElementById('point-1');
    const point2 = document.getElementById('point-2');
    if (point1 && point2) {
        point1.addEventListener('click', function () {
            point2.scrollIntoView({ behavior: 'smooth' });
        });
    }

    // Modal functionality
    var openBtn = document.getElementById('openReservationModal');
    var modal = document.getElementById('reservationModal');
    var closeBtn = document.querySelector('.modal .close');

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
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});