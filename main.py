# Noktaların Tanımlanması:

points = [
    (1,2),  # 1. nokta
    (4,3),  # 2. nokta
    (5,9),  # 3. nokta
    (10,7)   # 4. nokta
]



# Öklid mesafesi için bir fonksiyon yazma:

def euclideanDistance(x1,y1,x2,y2):
    x_diff = (x2 - x1) ** 2  # x farkının karesi
    y_diff = (y2 - y1) ** 2  # y farkının karesi
    distance = (x_diff + y_diff) ** 0.5  # Karekök alıyoruz
    return distance



# Tüm mesafelerin değerini koyacağımız boş bir liste:

distances = []

# Bütün noktalara bakarak mesafeleri hesaplayalım
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]

        # Fonksiyonu kullanarak mesafeyi hesaplıyoruz
        distance = euclideanDistance(x1, y1, x2, y2)

        # Mesafeyi listeye ekliyoruz
        distances.append(distance)

# Minimum Mesafenin Bulunması:

# Minimum mesafeyi bulalım
min_distance = min(distances)  # Mesafelerin en küçüğünü bul

print("Minimum Mesafe:", min_distance)  # Ekrana yazdır