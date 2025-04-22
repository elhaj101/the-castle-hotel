document.addEventListener('DOMContentLoaded', function () {
    // Room reservation modal logic
    const modal = document.getElementById('roomReservationModal');
    const closeBtn = modal ? modal.querySelector('.close') : null;
    const modalRoomType = document.getElementById('modal_room_type');
    const modalRoomPrice = document.getElementById('modal_room_price');
    const modalCheckIn = document.getElementById('modal_check_in');
    const modalCheckOut = document.getElementById('modal_check_out');
    const modalTotalPrice = document.getElementById('modal_total_price');
    const mainCheckIn = document.getElementById('main_check_in_date');
    const mainCheckOut = document.getElementById('main_check_out_date');
    const bookDetailsLink = document.getElementById('bookDetailsLink');

    // Restaurant reservation modal logic
    const restaurantBtn = document.getElementById('openReservationModal');
    if (restaurantBtn) {
        restaurantBtn.addEventListener('click', function() {
            const modal = document.getElementById('reservationModal');
            if (modal) modal.style.display = 'block';
        });
    }

    // Wellness reservation modal logic
    const wellnessBtn = document.getElementById('openWellnessModal');
    if (wellnessBtn) {
        wellnessBtn.addEventListener('click', function() {
            const modal = document.getElementById('wellnessReservationModal');
            if (modal) modal.style.display = 'block';
        });
    }

    // Room booking button logic
    document.querySelectorAll('.book-room-btn').forEach(function(btn) {
        btn.addEventListener('click', function() {
            if (modalRoomType) modalRoomType.textContent = btn.getAttribute('data-room-type');
            if (modalRoomPrice) modalRoomPrice.textContent = "$" + btn.getAttribute('data-room-price');
            if (modalCheckIn && mainCheckIn) modalCheckIn.textContent = mainCheckIn.value;
            if (modalCheckOut && mainCheckOut) modalCheckOut.textContent = mainCheckOut.value;

            // Calculate total price
            let total = '';
            const price = parseFloat(btn.getAttribute('data-room-price'));
            const checkInVal = mainCheckIn.value;
            const checkOutVal = mainCheckOut.value;
            if (checkInVal && checkOutVal && !isNaN(price)) {
                const checkInDate = new Date(checkInVal);
                const checkOutDate = new Date(checkOutVal);
                const diffTime = checkOutDate - checkInDate;
                const nights = Math.max(1, Math.ceil(diffTime / (1000 * 60 * 60 * 24)));
                total = "$" + (nights * price).toFixed(2);
            }
            if (modalTotalPrice) modalTotalPrice.textContent = total;

            if (modal) modal.style.display = 'block';

            // Set up the Book button to pass all info to the details page
            if (bookDetailsLink) {
                const roomType = encodeURIComponent(btn.getAttribute('data-room-type'));
                const roomPrice = encodeURIComponent(btn.getAttribute('data-room-price'));
                const checkIn = encodeURIComponent(mainCheckIn.value);
                const checkOut = encodeURIComponent(mainCheckOut.value);
                bookDetailsLink.href = `/rooms/details/?room_type=${roomType}&room_price=${roomPrice}&check_in_date=${checkIn}&check_out_date=${checkOut}`;
            }
        });
    });

    // Room modal close logic
    if (closeBtn && modal) {
        closeBtn.onclick = function () {
            modal.style.display = 'none';
        };
    }
    window.addEventListener('click', function (event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
        // Restaurant modal close logic
        const restaurantModal = document.getElementById('reservationModal');
        if (restaurantModal && event.target == restaurantModal) {
            restaurantModal.style.display = 'none';
        }
        // Wellness modal close logic
        const wellnessModal = document.getElementById('wellnessReservationModal');
        if (wellnessModal && event.target == wellnessModal) {
            wellnessModal.style.display = 'none';
        }
    });

    // Smooth scroll for elements with data-scroll-to
    document.querySelectorAll('[data-scroll-to]').forEach(function(link) {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = link.getAttribute('data-scroll-to');
            const target = document.getElementById(targetId);
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Restaurant modal close button logic (if you have a close button)
    const restaurantModal = document.getElementById('reservationModal');
    if (restaurantModal) {
        const restaurantCloseBtn = restaurantModal.querySelector('.close');
        if (restaurantCloseBtn) {
            restaurantCloseBtn.onclick = function () {
                restaurantModal.style.display = 'none';
            };
        }
    }

    // Wellness modal close button logic (if you have a close button)
    const wellnessModal = document.getElementById('wellnessReservationModal');
    if (wellnessModal) {
        const wellnessCloseBtn = wellnessModal.querySelector('.close');
        if (wellnessCloseBtn) {
            wellnessCloseBtn.onclick = function () {
                wellnessModal.style.display = 'none';
            };
        }
    }
});