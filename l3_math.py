from math import sqrt # Открыть библиотеку math
p = input("Введите радиус круга в сантиметрах: ") # Вводим радиус круга с клавиатуры 
print("Длина окружности в сантиметрах:", 2*int(p)*3.14) # Найдем длину окружности в сантиметрах
print("Длина окружности в метрах:", 2*int(p)*3.14/100) # Найдем длину окружности в метрах
print("Площадь круга в сантиметрах:", 3.14*int(p)*int(p)) # Найдем площадь круга в сантиметрах
print("Площадь круга в метрах:", 3.14*int(p)*int(p)/10000) # Найдем площадь круга в метрах
print("Сторона вписанного квадрата:", 2*int(p)/sqrt(2)) # Найдем сторону вписанного квадрата
print("Сторона равностороннего треугольника:", int(p)*sqrt(3)) # Найдем сторону равностороннего треугольника 
print("Сторона описанного квадрата:", 2*int(p)) # Найдем сторону описанного квадрата 
print("Сторона описанного треугольника:", 6*int(p)/sqrt(3)) # Найдем сторону описанного треугольника
print("Сторона описанного восьмиугольника:", int(p)*2*(sqrt(2)-1)) # Найдем сторону описанного восьмиугольника 