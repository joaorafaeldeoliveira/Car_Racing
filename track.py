"""
Track class for the racing game.
"""
import pygame
import math
from utils import point_in_polygon, distance

class Track:
    def __init__(self, width, height):
        """Initialize the track."""
        self.width = width
        self.height = height
        
        # Track boundaries (outer and inner polygons)
        self.outer_boundary = self.create_outer_boundary()
        self.inner_boundary = self.create_inner_boundary()
        
        # Start/finish line
        self.start_line = self.create_start_line()
        
        # Track colors
        self.track_color = (50, 50, 50)  # Dark gray
        self.grass_color = (0, 150, 0)   # Green
        self.line_color = (255, 255, 255)  # White
        
    def create_outer_boundary(self):
        """Create the outer boundary of the track."""
        margin = 50
        return [
            (margin, margin),
            (self.width - margin, margin),
            (self.width - margin, self.height - margin),
            (margin, self.height - margin)
        ]
    
    def create_inner_boundary(self):
        """Create the inner boundary of the track."""
        margin_outer = 50
        track_width = 100
        margin_inner = margin_outer + track_width
        
        return [
            (margin_inner, margin_inner),
            (self.width - margin_inner, margin_inner),
            (self.width - margin_inner, self.height - margin_inner),
            (margin_inner, self.height - margin_inner)
        ]
    
    def create_start_line(self):
        """Create the start/finish line."""
        # Start line at the top of the track
        margin = 50
        track_width = 100
        
        start_y = margin
        start_x1 = margin
        start_x2 = margin + track_width
        
        return [(start_x1, start_y), (start_x2, start_y)]
    
    def point_on_track(self, point):
        """Check if a point is on the track (between outer and inner boundaries)."""
        # Point must be inside outer boundary but outside inner boundary
        inside_outer = point_in_polygon(point, self.outer_boundary)
        inside_inner = point_in_polygon(point, self.inner_boundary)
        
        return inside_outer and not inside_inner
    
    def get_start_position(self):
        """Get the starting position for the car."""
        start_line = self.start_line
        center_x = (start_line[0][0] + start_line[1][0]) / 2
        start_y = start_line[0][1] + 30  # A bit behind the start line
        return (center_x, start_y)
    
    def check_start_line_crossing(self, car_pos, previous_pos):
        """Check if the car crossed the start/finish line."""
        if previous_pos is None:
            return False
        
        start_line = self.start_line
        line_y = start_line[0][1]
        line_x1 = start_line[0][0]
        line_x2 = start_line[1][0]
        
        # Check if car crossed the line (from behind to front)
        crossed_y = previous_pos[1] > line_y and car_pos[1] <= line_y
        within_x_range = line_x1 <= car_pos[0] <= line_x2
        
        return crossed_y and within_x_range
    
    def draw(self, screen):
        """Draw the track on the screen."""
        # Fill background with grass
        screen.fill(self.grass_color)
        
        # Draw track surface
        # Create a surface for the track
        track_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        
        # Draw outer boundary
        pygame.draw.polygon(track_surface, self.track_color, self.outer_boundary)
        
        # Draw inner boundary (cut out the center)
        pygame.draw.polygon(track_surface, self.grass_color, self.inner_boundary)
        
        screen.blit(track_surface, (0, 0))
        
        # Draw track boundaries
        pygame.draw.polygon(screen, self.line_color, self.outer_boundary, 3)
        pygame.draw.polygon(screen, self.line_color, self.inner_boundary, 3)
        
        # Draw start/finish line
        start_line = self.start_line
        pygame.draw.line(screen, self.line_color, start_line[0], start_line[1], 5)
        
        # Draw start/finish line pattern (checkered)
        line_length = distance(start_line[0], start_line[1])
        num_squares = 8
        square_size = line_length / num_squares
        
        for i in range(num_squares):
            if i % 2 == 0:
                color = (255, 255, 255)  # White
            else:
                color = (0, 0, 0)  # Black
            
            x = start_line[0][0] + (i * square_size)
            y = start_line[0][1] - 8
            width = square_size
            height = 16
            
            pygame.draw.rect(screen, color, (x, y, width, height))
