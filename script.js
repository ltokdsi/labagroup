// Функция для обновления времени и отсчета
function updateTime() {
    const now = new Date();

    // Текущее время
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');

    // Форматирование даты
    const options = {
        day: 'numeric',
        month: 'long',
        weekday: 'long'
    };
    const dateString = now.toLocaleDateString('ru-RU', options);

    // Отсчет до конца дня
    const endOfDay = new Date(now);
    endOfDay.setHours(23, 59, 59, 999);
    const timeLeft = endOfDay - now;

    const hoursLeft = String(Math.floor(timeLeft / (1000 * 60 * 60))).padStart(2, '0');
    const minutesLeft = String(Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60))).padStart(2, '0');
    const secondsLeft = String(Math.floor((timeLeft % (1000 * 60)) / 1000)).padStart(2, '0');

    // Обновление элементов на странице
    document.getElementById('time').textContent = `${hours}:${minutes}:${seconds}`;
    document.getElementById('date').textContent = dateString;
    document.getElementById('countdown').textContent = `${hoursLeft}:${minutesLeft}:${secondsLeft}`;
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    // Запускаем обновление времени
    updateTime();
    setInterval(updateTime, 1000);
});