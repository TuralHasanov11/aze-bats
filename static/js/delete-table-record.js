document.querySelectorAll('.btn-delete').forEach(el => {
    el.addEventListener("click", function (e) {
        fetch(e.target.dataset.url, {
            method: 'DELETE',
            headers: { "X-CSRFToken": csrftoken }
        })
            .then(response => {
                if (response.ok) {
                    el.closest('.data-row').style.display = "none"
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
})