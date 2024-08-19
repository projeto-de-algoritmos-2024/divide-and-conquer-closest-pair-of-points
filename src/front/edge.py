import math
from typing import Any

import pygame

from src.front.node import Node
from src.front.colors import WHITE, GREEN


class Edge:
    def __init__(
            self, start_node: Node,
            end_node:Node, coust: int
            ):
        self.start_node = start_node
        self.end_node = end_node
        self.coust = coust
        self.color = WHITE
    
    def __str__(self) -> str:
        return (self.start_node.id, self.end_node.id)
    
    def toggle_color(self, color: Any) -> None:
        self.color = color
    
    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.start_node.pos, self.end_node.pos, 2)
