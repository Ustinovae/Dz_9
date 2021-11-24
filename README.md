# Dz_9 
Время работы файла filter.py 

![](filter.png) 
 
Время работы old_filter.py 

![](old_filter.png) 
 
Разность в временных затратах связанно с тем, что в filter.py используется библиотека numpy, которая обеспечивает 
высокую производительность.

Единственная проблема заключается в том, что в filter.py затрачивается много времени на ввод данных с клавиатуры.  
Для этого я сделал новый файл filter_with_filename.py в котором значения задаются в коде. 
 
filter_with_filename.py 

![](filter_with_filename.png) 

Вследствие этого мы получили более точную информацию о производительности.

# Результаты программ:

Тестовое изображение:

![](dog.jpg)

Результат old_filter.py: 

![](old_filter_res.jpg)

Результат filter.py: 

![](res.jpg)

Результат filter_with_filename.py: 

![](filter_with_filename_res.jpg)

Результаты тестов: 

![](test.png)
