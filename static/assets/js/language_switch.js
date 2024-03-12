document.addEventListener('DOMContentLoaded', function () {
    const languageSwitches = document.querySelectorAll('.language-switch');

    // Пытаемся определить текущий язык из URL, предполагая, что он может быть первым сегментом пути
    const currentLanguage = window.location.pathname.split('/')[1];

    languageSwitches.forEach(function (languageSwitch) {
        const selectedLanguage = languageSwitch.getAttribute('data-language');

        // Выделение активного языка
        if (selectedLanguage === currentLanguage) {
            languageSwitch.classList.add('active-language');
        }

        languageSwitch.addEventListener('click', function () {
            // Строим URL с учетом возможных случаев структуры путей
            const pathSegments = window.location.pathname.split('/');
            if (['ru', 'en'].includes(pathSegments[1])) {
                // Если первый сегмент — код языка, заменяем его
                pathSegments[1] = selectedLanguage;
            } else {
                // Если первый сегмент не код языка, добавляем код языка в начало
                pathSegments.splice(1, 0, selectedLanguage);
            }

            // Объединяем сегменты обратно в строку пути и формируем новый URL
            const newPath = pathSegments.join('/');
            const newUrl = window.location.origin + newPath + window.location.search;

            window.location.href = newUrl;
        });
    });
});
