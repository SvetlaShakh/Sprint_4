# qa_python
### Mетод add_new_book:
**1. test_add_new_book_add_two_books().** 

   Новая книга записывается в словарь, а не перезаписывает данные словаря. Откорректированн assert - в проверке задействован только один метод

**2. test_add_new_book_len_name_more_then_0_and_less_then_41_add_one_book()** 

   Проверка разрешенной длинны имени книги. Граничные значения длинны - 1 и 40, шаг в нутрь диапазона - 2 и 39

**3. test_add_new_book_len_name_0_and_more_then_40_add_zero_book()**

   Проверка длинны имени книги за пределами разрешенной длинны. Граничные значения длинны - 0 и 41, шаг в нутрь диапазона - 42, значение за границей - 57

**4. test_add_new_book_same_name_add_one_book()**

   Одну и туже книгу можно добавить только один раз

**5. test_add_new_book_add_book_without_genre()** 

   Новая книга добавляется без жанра

### Метод set_book_genre:
**1. test_set_book_genre_from_genre_set_genre()** 

   Kниге устанавливается жанр из списка жанров

**2. test_set_book_genre_not_from_genre_genre_isnt_genre()** 
   
При установке книге жанра не из списка жанров, книга остается без жанра

**3. test_set_book_genre_not_from_books_genre_is_none()** 

При установке жанра для не существующей книги, действия не происходит

### Метод get_book_genre:
**1. test_get_book_genre_get_set_genre()**

   Получение ранее установленного жанра для книги

**2. test_get_book_is_not_books_genre_is_none()** 

   При запросе с несуществующей книгой, действия не происходит

### Метод get_books_with_specific_genre:
**1. test_get_books_with_specific_genre_get_lst_books_for_genre()**

   При запросе с существующим жанром, возвращается список книг с соответствующим жанром

**2. test_get_books_with_specific_genre_not_genre_in_lst_empty_list()**

   При запросе с не существующим жанром, возвращается пустой список

### Meтод get_books_genre:
**1. test_get_books_genre_get_dict_all_books()**

   При запросе возвращается словарь со всеми книгами и их жанрами

### Метод get_books_for_children:
**1. test_get_books_for_children_get_list_books_without_age_rating()**

   При запросе возвращается список книг, жанры книг без возрастного рейтинга

### Метод add_book_in_favorite:
**1. test_add_book_in_favorite_add_two_book()**

   При добавлении существующей книги в избранное, книга добавляется в список, а не перезаписывает список

**2. test_add_book_in_favorite_book_not_in_books_genre_add_zero_book()**

   При добавлении в избранное не существующей книги, книга в список не добавляется

**3. test_add_book_in_favorite_two_same_book_add_one_book()**

   При добавлении ранее добавленной книги в избранное, дубликат книги в список не добавляется

### Метод delete_book_from_favorites:
**1. test_delete_book_from_favorites_zero_book_in_favorites()**

   При удалении ранее записанной книги из избранного, книга из списка удаляется

**2. test_delete_book_from_favorites_book_not_in_lst_one_book_in_favorites()**

   При удалении не существующей книги из избранного, список избранных книг не изменяется

### Метод get_list_of_favorite_books:
**1. test_get_list_of_favorites_books_get_lst_name_of_favorites_books()**

   При запросе выводится список книг добавленных в избранное

