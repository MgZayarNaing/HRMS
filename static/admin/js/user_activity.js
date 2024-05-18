document.addEventListener('DOMContentLoaded', function () {
    const users = document.querySelectorAll('span[id^="user-"]');
    const userIds = Array.from(users).map(user => user.id.split('-')[1]);

    const socket = new WebSocket('ws://' + window.location.host + '/ws/activity/');

    socket.onopen = function () {
        console.log('WebSocket connection established');
        socket.send(JSON.stringify({ 'user_ids': userIds }));
    };

    socket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        for (const userId in data) {
            const status = data[userId] ? 'Online' : 'Offline';
            document.getElementById(`user-${userId}`).innerText = status;
        }
    };

    socket.onclose = function (e) {
        console.error('WebSocket closed unexpectedly');
    };
});
