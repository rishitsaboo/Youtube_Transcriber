document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('submitButton').addEventListener('click', function() {
        var videoIdOrUrl = document.getElementById('videoInput').value;
        var baseUrl = 'http://localhost:5000/api/summarize?youtube_url='; // Replace this with your actual backend URL
        var completeUrl = baseUrl  + videoIdOrUrl;

        // Open the response from the backend in a new tab
        window.open(completeUrl, '_blank');
    });
});
