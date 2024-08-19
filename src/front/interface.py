import sys
import pygame
from src.front.colors import *
from src.front.node import Node
from src.back.graph import Graph  # Importa a classe Graph para encontrar o par mais próximo

pygame.init()

WIDTH, HEIGHT = 800, 600

font = pygame.font.Font(None, 32)

# Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Divide-and-Conquer Closest Pair of Points")

# Graph
nodes = []
node_color = BLUE

class Interface:
    def __init__(self) -> None:
        self.running = True
        self.clock = pygame.time.Clock()
        self.dragging = False
        self.selected_node = None

    def draw_graph(self):
        screen.fill(BLACK)
        for node in nodes:
            node.draw(screen)

    def critical_node(self, color, ids):
        global nodes
        for id in ids:
            nodes[id-1].toggle_color(color)

    def find_clicked_node(self, pos):
        for node in nodes:
            dist = ((pos[0] - node.pos[0])**2 + (pos[1] - node.pos[1])**2)**0.5
            if dist < 20:
                return node
        return None

    def find_closest_pair(self):
        points = [(node.pos[0], node.pos[1]) for node in nodes]
        
        graph = Graph(points)
        closest_pair = graph.run()
        
        if closest_pair:
            p1, p2 = closest_pair
            for node in nodes:
                if node.pos == p1 or node.pos == p2:
                    node.toggle_color(RED)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        self.selected_node = self.find_clicked_node(pos)
                        if self.selected_node is None:
                            new_node = Node(len(nodes) + 1, pos)
                            nodes.append(new_node)
                        else:
                            self.dragging = True
                    elif event.button == 3:
                        self.find_closest_pair()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.dragging = False
                        self.selected_node = None

            if self.dragging and self.selected_node is not None:
                pos = pygame.mouse.get_pos()
                self.selected_node.pos = pos

            self.draw_graph()
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Interface().run()
