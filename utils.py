"""
Utility functions for the racing game.
"""
import math
import pygame

def rotate_point(point, angle, center):
    """Rotate a point around a center by a given angle."""
    cos_angle = math.cos(angle)
    sin_angle = math.sin(angle)
    
    # Translate point to origin
    x = point[0] - center[0]
    y = point[1] - center[1]
    
    # Rotate
    new_x = x * cos_angle - y * sin_angle
    new_y = x * sin_angle + y * cos_angle
    
    # Translate back
    return (new_x + center[0], new_y + center[1])

def point_in_polygon(point, polygon):
    """Check if a point is inside a polygon using ray casting algorithm."""
    x, y = point
    n = len(polygon)
    inside = False
    
    p1x, p1y = polygon[0]
    for i in range(1, n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    
    return inside

def distance(point1, point2):
    """Calculate distance between two points."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def normalize_angle(angle):
    """Normalize angle to be between 0 and 2*pi."""
    while angle < 0:
        angle += 2 * math.pi
    while angle >= 2 * math.pi:
        angle -= 2 * math.pi
    return angle
