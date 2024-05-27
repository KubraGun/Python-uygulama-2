'''
Göreviniz:

Python'da fonksiyonlar ve döngüler kavramlarını kullanarak, aşağıdaki işlemleri gerçekleştiren bir program yazmanız gerekmektedir:

Noktaların Tanımlanması:

‘points’ adında bir liste oluşturun. Bu liste, 2D uzaydaki noktaları temsil eden demetler (tuple) içermelidir. Örneğin, ‘(x, y)’ noktası bir demet ‘(x, y)’ olarak temsil edilecektir.

Öklid Mesafesi İçin Bir Fonksiyon Yazma:

‘euclideanDistance’ adında bir fonksiyon tanımlayın. Bu fonksiyon, iki demet (her biri bir noktayı temsil eder) almalı ve bu iki nokta arasındaki Öklid mesafesini döndürmelidir.

Mesafelerin Hesaplanması:

Bir döngü kullanarak, ‘points’ listesindeki her nokta çifti arasındaki Öklid mesafesini hesaplayın. Bu mesafeleri ‘distances’ adında başka bir listede saklayın.

Minimum Mesafenin Bulunması:

‘distances’ listesinden minimum mesafeyi bulun ve yazdırın.


Not: Eğer daha zorlayıcı bir görevlendirme istiyorsanız herhangi bir kütüphane ve modül kullanmadan da yapabilrsiniz.

Görevi Oryantasyon haftasında öğrendiğiniz gibi GİtHub üzerinden paylaşın.
'''

#1 hiçbir metot kullanmadan:
def euclidDistance(points):

    x1, y1 = points[0]
    x2, y2 = points[1]

    distance = ( (x2 - x1)**2 + (y2 - y1)**2)**(1/2)
    return distance

points = ((3, 6), (7, 2))
dis = float(euclidDistance(points))
print(dis)



