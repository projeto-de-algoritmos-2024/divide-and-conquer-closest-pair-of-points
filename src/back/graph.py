class Graph:
    def __init__(self, points):
        self.points = sorted(points, key=lambda p: p[0]) 

    def euclidean_distance(self, p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

    def closest_pair_recursive(self, points_sorted_by_x, points_sorted_by_y):
        n = len(points_sorted_by_x)
        
        # Caso base
        if n <= 3:
            min_dist = float('inf')
            closest_pair = None
            for i in range(n):
                for j in range(i + 1, n):
                    dist = self.euclidean_distance(points_sorted_by_x[i], points_sorted_by_x[j])
                    if dist < min_dist:
                        min_dist = dist
                        closest_pair = (points_sorted_by_x[i], points_sorted_by_x[j])
            return closest_pair

        # Divisão
        mid = n // 2
        mid_point = points_sorted_by_x[mid]

        left_half_x = points_sorted_by_x[:mid]
        right_half_x = points_sorted_by_x[mid:]

        left_half_y = list(filter(lambda p: p[0] <= mid_point[0], points_sorted_by_y))
        right_half_y = list(filter(lambda p: p[0] > mid_point[0], points_sorted_by_y))

        # Conquista
        closest_pair_left = self.closest_pair_recursive(left_half_x, left_half_y)
        closest_pair_right = self.closest_pair_recursive(right_half_x, right_half_y)

        # Combina
        d_left = self.euclidean_distance(*closest_pair_left)
        d_right = self.euclidean_distance(*closest_pair_right)
        d = min(d_left, d_right)
        closest_pair = closest_pair_left if d_left < d_right else closest_pair_right

        # Verifica a faixa central
        strip = [p for p in points_sorted_by_y if abs(p[0] - mid_point[0]) < d]

        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                p1, p2 = strip[i], strip[j]
                dist = self.euclidean_distance(p1, p2)
                if dist < d:
                    d = dist
                    closest_pair = (p1, p2)

        return closest_pair
    
    def run(self):
        points_sorted_by_y = sorted(self.points, key=lambda p: p[1])
        return self.closest_pair_recursive(self.points, points_sorted_by_y)
