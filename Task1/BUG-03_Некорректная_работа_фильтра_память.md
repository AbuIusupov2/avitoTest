Заголовок: 
Поиск карточек товара: некорректное отображение карточки товаров при использовании фильтра "Память".

Идентификатор: BUG-03

Приоритет: Высокий
Серьезность: Значительная (major)

Описание:
После применения фильтра "Память" в поиске, карточки товаров отображаются с некорректными объемами памяти.

Шаги для воспроизведения:

1 - открываем сайт https://www.avito.ru/
2 - вводим в строку поиска «Смартфоны и мобильные телефоны в Москве»
3 - выбираем в фильтре "Память" значение 512 гб
4 - обратите внимание, что на открывшейся странице отображаются карточки товаров с объемом памяти не равным 512 ГБ

Ожидаемый результат:
Должны отображаться карточки товаров с объемом памяти "512гб"

Фактический результат:
Отображаются карточки и с другим объемом памяти (256 гб)

Среда:
ОС: mac os
Девайс: macbook air 2021
Браузер: chrome

Прикрепленный файл:
https://github.com/AbuIusupov2/avitoTest/blob/main/Images/BUG-03.png?raw=true
