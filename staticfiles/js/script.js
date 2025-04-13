
    document.addEventListener('DOMContentLoaded', function () {
        // Get the elements
        const point1 = document.getElementById('point-1');
        const point2 = document.getElementById('point-2');

        // Add a click event listener to #point-1
        point1.addEventListener('click', function () {
            // Scroll to #point-2
            point2.scrollIntoView({ behavior: 'smooth' });
        });
    });
