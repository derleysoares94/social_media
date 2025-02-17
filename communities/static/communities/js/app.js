document.addEventListener("DOMContentLoaded", function () {
    let messages = document.getElementById("django-messages");
    if (messages) {
        let alerts = JSON.parse(messages.textContent); // Convert JSON string to object
        alerts.forEach(msg => {
            Swal.fire({
                title: msg.tags === "success" ? "Success!" : msg.tags === "error" ? "Error!" : "Notification",
                text: msg.message,
                icon: msg.tags,
                confirmButtonText: "OK"
            });
        });
    }
});
