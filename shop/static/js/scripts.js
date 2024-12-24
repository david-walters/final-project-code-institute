// Remove alert messages after 5 seconds
document.addEventListener('DOMContentLoaded', function () {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'opacity 0.5s';
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.form');
    
    const fields = {
        streetAddress: document.getElementById('id_street_address'),
        city: document.getElementById('id_city'),
        postalCode: document.getElementById('id_postal_code'),
        country: document.getElementById('id_country'),
        phoneNumber: document.getElementById('id_phone_number'),
    };

    // Trim and normalize whitespace in all fields
    Object.values(fields).forEach(field => {
        if (field && field.value) {
            // Trim leading and trailing spaces, and replace consecutive spaces with a single space
            field.value = field.value.trim().replace(/\s+/g, ' ');
        }
    });

    form.addEventListener('submit', (event) => {
        let isValid = true;

        // Clear previous errors
        document.querySelectorAll('.text-danger').forEach(e => e.remove());
        Object.values(fields).forEach(field => field.classList.remove('is-invalid'));

        // Validate fields
        if (fields.streetAddress && fields.streetAddress.value.trim() === '') {
            showError(fields.streetAddress, 'Street address is required.');
            isValid = false;
        }
        if (fields.city && fields.city.value.trim() === '') {
            showError(fields.city, 'City is required.');
            isValid = false;
        }
        if (fields.postalCode && !/^[A-Za-z0-9\s\-]+$/.test(fields.postalCode.value)) {
            showError(fields.postalCode, 'Please enter a valid postal code.');
            isValid = false;
        }
        if (fields.country && fields.country.value.trim() === '') {
            showError(fields.country, 'Country is required.');
            isValid = false;
        }
        if (fields.phoneNumber && fields.phoneNumber.value && !/^\d{10,11}$/.test(fields.phoneNumber.value)) {
            showError(fields.phoneNumber, 'Phone number must be 10-11 digits.');
            isValid = false;
        }

        if (!isValid) {
            event.preventDefault();
        }
    });

    function showError(input, message) {
        const error = document.createElement('div');
        error.className = 'text-danger small';
        error.innerText = message;
        input.classList.add('is-invalid');
        input.parentElement.appendChild(error);
    }
});