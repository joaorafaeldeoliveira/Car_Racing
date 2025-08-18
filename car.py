"""
Car class for the racing game.
"""
import pygame
import math
from utils import rotate_point, normalize_angle

class Car:
    def __init__(self, x, y, width=20, height=40):
        """Initialize the car."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = 0  # Angle in radians
        self.velocity = 0
        self.max_velocity = 8
        self.acceleration = 0.3
        self.deceleration = 0.2
        self.turn_speed = 0.08
        self.friction = 0.1
        
        # Car corners for collision detection
        self.corners = []
        self.update_corners()
        
        # Engine sound simulation
        self.engine_volume = 0
        
    def update_corners(self):
        """Update car corner positions based on current position and angle."""
        half_width = self.width / 2
        half_height = self.height / 2
        
        # Car corners relative to center
        corners = [
            (-half_width, -half_height),  # Top-left
            (half_width, -half_height),   # Top-right
            (half_width, half_height),    # Bottom-right
            (-half_width, half_height)    # Bottom-left
        ]
        
        # Rotate corners around car center
        self.corners = []
        for corner in corners:
            rotated = rotate_point(corner, self.angle, (0, 0))
            self.corners.append((self.x + rotated[0], self.y + rotated[1]))
    
    def handle_input(self, keys):
        """Handle player input for car movement."""
        turning = False
        accelerating = False
        
        # Steering (only when moving)
        if abs(self.velocity) > 0.5:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.angle -= self.turn_speed * (abs(self.velocity) / self.max_velocity)
                turning = True
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.angle += self.turn_speed * (abs(self.velocity) / self.max_velocity)
                turning = True
        
        # Acceleration/Deceleration
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.velocity = min(self.velocity + self.acceleration, self.max_velocity)
            accelerating = True
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.velocity = max(self.velocity - self.acceleration, -self.max_velocity * 0.6)
            accelerating = True
        else:
            # Apply friction when no input
            if self.velocity > 0:
                self.velocity = max(0, self.velocity - self.friction)
            elif self.velocity < 0:
                self.velocity = min(0, self.velocity + self.friction)
        
        # Normalize angle
        self.angle = normalize_angle(self.angle)
        
        # Update engine volume for sound simulation
        self.engine_volume = min(abs(self.velocity) / self.max_velocity, 1.0)
        
        return accelerating, turning
    
    def update(self):
        """Update car position based on velocity and angle."""
        # Calculate movement based on angle and velocity
        dx = math.cos(self.angle) * self.velocity
        dy = math.sin(self.angle) * self.velocity
        
        # Update position
        self.x += dx
        self.y += dy
        
        # Update corner positions
        self.update_corners()
    
    def collision_with_track(self, track):
        """Check if car collides with track boundaries."""
        # Check if any corner is outside the track
        for corner in self.corners:
            if not track.point_on_track(corner):
                return True
        return False
    
    def handle_collision(self):
        """Handle collision by stopping/reversing the car."""
        # Stop the car and push it back slightly
        self.velocity = 0
        # Move car back a bit
        dx = -math.cos(self.angle) * 2
        dy = -math.sin(self.angle) * 2
        self.x += dx
        self.y += dy
        self.update_corners()
    
    def draw(self, screen):
        """Draw the car on the screen."""
        # Car body (rectangle)
        car_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(car_surface, (255, 0, 0), (0, 0, self.width, self.height))
        
        # Car front indicator (small rectangle at front)
        front_width = self.width // 3
        front_height = 4
        front_x = (self.width - front_width) // 2
        pygame.draw.rect(car_surface, (255, 255, 255), 
                        (front_x, 0, front_width, front_height))
        
        # Rotate the car surface
        rotated_car = pygame.transform.rotate(car_surface, -math.degrees(self.angle))
        
        # Get the rect and center it on the car position
        car_rect = rotated_car.get_rect()
        car_rect.center = (self.x, self.y)
        
        # Draw the car
        screen.blit(rotated_car, car_rect)
        
        # Draw collision points for debugging (optional)
        if False:  # Set to True for debugging
            for corner in self.corners:
                pygame.draw.circle(screen, (0, 255, 0), 
                                 (int(corner[0]), int(corner[1])), 2)
    
    def get_position(self):
        """Get car's current position."""
        return (self.x, self.y)
    
    def reset_position(self, x, y, angle=0):
        """Reset car to a specific position and angle."""
        self.x = x
        self.y = y
        self.angle = angle
        self.velocity = 0
        self.update_corners()
