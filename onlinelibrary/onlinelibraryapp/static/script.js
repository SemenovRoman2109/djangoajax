// проверяем загружен ли документ
$(document).ready(function () {
    // Проверяем что форма отправлнна
    $('#filter-form').on("submit", function (event) {
        // останавливаем отправку формы
        event.preventDefault();
        // Отправляем AJAX запрос
        $.ajax({
            // тип запроса
            type: "POST",
            // Указываем адрес на который отпраляем запрос значение берем из атрибута форм
            url: $('#filter-form').action,
            // указуємо дані з форми які ми будемо відправляти
            data: $(this).serialize(),
            // мы указываем тип данных, которые будем "принимать" 
            dataType: "json",
            // якщо все пройшло успішно то виконуємо функцію
            success: function(response){
                //замінюємо все з діва book-list на потрібні дані
                $("#book-list").html(response.html_books_list)
            }
        });
    })
})