#Импорт модулей
#Напишите функцию lam(U), которая по данным об ускоряющем напряжении между электродами рентгеновской трубки U и набору констант:
#    c (скорость света в вакууме)
#    e (заряд электрона, элементарный заряд)
#    h (постоянная Планка)
#найдёт длину волны λ \lambda λ рентгеновского излучения.
#Используйте формулу:
#    h*(c*λ)=eU
#    #Импортируйте значения констант из модуля scipy - https://docs.scipy.org/doc/scipy/reference/constants.html

import scipy.constants as sci

def lam(U):
    h=sci.Planck
    e=sci.elementary_charge
    c=sci.speed_of_light
    lmb=h*c/(e*U)
    return lmb

print(lam(1))