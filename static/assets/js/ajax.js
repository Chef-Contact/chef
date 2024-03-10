$(document).ready(function() {
    try{
        $('#chat_form-btn').click(function(e) {
            e.preventDefault(); // Предотвращаем отправку формы по умолчанию
    
            let user_id = $('#user_id').val();
            let chat_id = $('#chat_id').val();
            let message = $('#message-input').val();
            let csrf_token = $('input[name=csrfmiddlewaretoken]').val();
            let url = $('#url').val();
    
            // Проверяем, есть ли данные для отправки
            if (!user_id || !chat_id || !message) {
                alert('Пожалуйста, заполните все обязательные поля.');
                return;
            }
            $.ajax({
                type: 'POST',
                url: url,
                headers: { "X-CSRFToken": csrf_token },
                data: JSON.stringify({
                    user_id: user_id,
                    chat_id: chat_id,
                    message: message
                }),
                contentType: 'application/json',
                success: function(response) {
                    $('#message-input').val('');
                    loadChatMessages(chat_id); // Обновляем сообщения чата после успешной отправки сообщения
                },
                error: function(xhr, status, error) {
                    alert('Произошла ошибка: ' + xhr.responseText);
                }
            });
        });
    
        // Функция для загрузки сообщений чата
        function loadChatMessages(chat_id) {
            $.ajax({
                url: `/get_chat_messages/${chat_id}/`,
                type: 'GET',
                dataType: 'json',
                success: function(response) {
                    $('.chat-messages').empty(); // Очищаем предыдущие сообщения чата
                    $.each(response.messages, function(index, message) {
                        if (message.user_id && message.user_id == $('#user_id').val()) {
                            var messageHtml = '<div class="message user-message">';
                        } else {
                            var messageHtml = '<div class="message support-message">';
                        }
                        messageHtml += '<img src="' + message.profile_image + '" alt="User Profile" class="profile-image" />';
                        messageHtml += '<div class="message-content"><p>' + message.text + '</p></div>';
                        messageHtml += '<span class="time">' + formatDate(message.created) + '</span></div></div>';
                        $('.chat-messages').append(messageHtml); // Добавляем новые сообщения чата
                    });
                },
                error: function(xhr, status, error) {
                    console.log('Вы не на странице чата');
                }
            });
        }
    
        // Функция для форматирования даты и времени в "M d H:i"
        function formatDate(dateTimeStr) {
            let dateTime = new Date(dateTimeStr);
            let monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
            let month = monthNames[dateTime.getMonth()];
            let day = dateTime.getDate();
            let hours = dateTime.getHours();
            let minutes = dateTime.getMinutes();
            return month + ' ' + day + ' ' + hours + ':' + (minutes < 10 ? '0' : '') + minutes;
        }
    
        // Загружаем сообщения чата при загрузке страницы
        let chat_id = $('#chat_id').val();
        try{

            loadChatMessages(chat_id);
        }catch{
            console.log('Вы не на странице чата');
        }
    }
    catch{
        console.log("Вы не на странице чата");
    }
});
