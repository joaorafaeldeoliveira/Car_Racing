"""
Main game class for the 2D car racing game.
"""
import pygame
import time
import sys
from car import Car
from track import Track

class Game:
    def __init__(self):
        """Initialize the game."""
        # Screen dimensions
        self.width = 1000
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("2D Car Racing Game")
        
        # Game clock
        self.clock = pygame.time.Clock()
        self.fps = 60
        
        # Game objects
        self.track = Track(self.width, self.height)
        start_pos = self.track.get_start_position()
        self.car = Car(start_pos[0], start_pos[1])
        
        # Game state
        self.running = True
        self.paused = False
        
        # Lap timing
        self.lap_times = []
        self.current_lap_start = time.time()
        self.current_lap = 1
        self.best_lap_time = None
        self.previous_car_pos = None
        
        # Fonts for HUD
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Initialize mixer for sound (optional)
        self.sound_enabled = False
        try:
            pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
            self.create_sounds()
            # Sound channels
            self.engine_channel = pygame.mixer.Channel(0)
            self.collision_channel = pygame.mixer.Channel(1)
            self.sound_enabled = True
        except pygame.error:
            print("Warning: Audio device not available. Running without sound.")
            self.engine_channel = None
            self.collision_channel = None
        
    def create_sounds(self):
        """Create simple sound effects."""
        # Create engine sound (simple tone)
        sample_rate = 22050
        duration = 0.1
        frequency = 100
        
        # Engine sound - low frequency tone
        frames = int(duration * sample_rate)
        engine_array = []
        for i in range(frames):
            wave = 4096 * (i % (sample_rate // frequency) < (sample_rate // frequency) // 2)
            engine_array.append([wave, wave])
        
        self.engine_sound = pygame.sndarray.make_sound(engine_array)
        
        # Collision sound - higher frequency burst
        collision_frames = int(0.2 * sample_rate)
        collision_array = []
        for i in range(collision_frames):
            wave = 2048 * (i % 50 < 25)  # Higher frequency
            collision_array.append([wave, wave])
        
        self.collision_sound = pygame.sndarray.make_sound(collision_array)
    
    def handle_events(self):
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pygame.K_r:
                    self.reset_game()
    
    def update_game(self):
        """Update game state."""
        if self.paused:
            return
        
        # Store previous position for lap detection
        self.previous_car_pos = self.car.get_position()
        
        # Handle car input and movement
        keys = pygame.key.get_pressed()
        accelerating, turning = self.car.handle_input(keys)
        self.car.update()
        
        # Handle engine sound
        if self.sound_enabled and self.engine_channel:
            if accelerating and not self.engine_channel.get_busy():
                self.engine_channel.play(self.engine_sound, loops=-1)
                self.engine_channel.set_volume(self.car.engine_volume * 0.3)
            elif not accelerating:
                self.engine_channel.stop()
            else:
                self.engine_channel.set_volume(self.car.engine_volume * 0.3)
        
        # Check collision with track
        if self.car.collision_with_track(self.track):
            self.car.handle_collision()
            # Play collision sound
            if self.sound_enabled and self.collision_channel and not self.collision_channel.get_busy():
                self.collision_channel.play(self.collision_sound)
        
        # Check lap completion
        current_pos = self.car.get_position()
        if self.track.check_start_line_crossing(current_pos, self.previous_car_pos):
            self.complete_lap()
    
    def complete_lap(self):
        """Handle lap completion."""
        current_time = time.time()
        lap_time = current_time - self.current_lap_start
        
        # Only count laps after the first crossing (to avoid counting start as lap 1)
        if self.current_lap > 1 or len(self.lap_times) > 0:
            self.lap_times.append(lap_time)
            
            # Update best lap time
            if self.best_lap_time is None or lap_time < self.best_lap_time:
                self.best_lap_time = lap_time
        
        # Start new lap
        self.current_lap += 1
        self.current_lap_start = current_time
    
    def reset_game(self):
        """Reset the game to initial state."""
        start_pos = self.track.get_start_position()
        self.car.reset_position(start_pos[0], start_pos[1])
        
        # Reset lap timing
        self.lap_times = []
        self.current_lap_start = time.time()
        self.current_lap = 1
        self.best_lap_time = None
        self.previous_car_pos = None
        
        # Stop all sounds
        if self.sound_enabled:
            pygame.mixer.stop()
    
    def format_time(self, time_seconds):
        """Format time in MM:SS.mmm format."""
        if time_seconds is None:
            return "--:--.---"
        
        minutes = int(time_seconds // 60)
        seconds = time_seconds % 60
        return f"{minutes:02d}:{seconds:06.3f}"
    
    def draw_hud(self):
        """Draw the heads-up display."""
        # Current lap time
        current_time = time.time() - self.current_lap_start
        current_time_text = self.font.render(
            f"Current: {self.format_time(current_time)}", 
            True, (255, 255, 255)
        )
        self.screen.blit(current_time_text, (10, 10))
        
        # Lap counter
        lap_text = self.font.render(f"Lap: {self.current_lap}", True, (255, 255, 255))
        self.screen.blit(lap_text, (10, 50))
        
        # Best lap time
        best_text = self.font.render(
            f"Best: {self.format_time(self.best_lap_time)}", 
            True, (255, 255, 0)
        )
        self.screen.blit(best_text, (10, 90))
        
        # Last lap time
        if self.lap_times:
            last_lap = self.lap_times[-1]
            last_text = self.font.render(
                f"Last: {self.format_time(last_lap)}", 
                True, (255, 255, 255)
            )
            self.screen.blit(last_text, (10, 130))
        
        # Speed indicator
        speed = abs(self.car.velocity)
        speed_text = self.font.render(f"Speed: {speed:.1f}", True, (255, 255, 255))
        self.screen.blit(speed_text, (self.width - 200, 10))
        
        # Controls help
        help_texts = [
            "Controls:",
            "Arrow Keys / WASD - Move",
            "SPACE - Pause",
            "R - Reset",
            "ESC - Quit"
        ]
        
        for i, text in enumerate(help_texts):
            color = (255, 255, 0) if i == 0 else (200, 200, 200)
            help_surface = self.small_font.render(text, True, color)
            self.screen.blit(help_surface, (self.width - 200, 50 + i * 25))
        
        # Pause indicator
        if self.paused:
            pause_text = self.font.render("PAUSED", True, (255, 0, 0))
            pause_rect = pause_text.get_rect(center=(self.width // 2, self.height // 2))
            
            # Draw background for pause text
            background_rect = pause_rect.inflate(20, 10)
            pygame.draw.rect(self.screen, (0, 0, 0), background_rect)
            pygame.draw.rect(self.screen, (255, 255, 255), background_rect, 2)
            
            self.screen.blit(pause_text, pause_rect)
    
    def draw(self):
        """Draw all game elements."""
        # Draw track
        self.track.draw(self.screen)
        
        # Draw car
        self.car.draw(self.screen)
        
        # Draw HUD
        self.draw_hud()
        
        # Update display
        pygame.display.flip()
    
    def run(self):
        """Main game loop."""
        print("Starting 2D Car Racing Game...")
        print("Controls: Arrow Keys/WASD to move, SPACE to pause, R to reset, ESC to quit")
        
        while self.running:
            # Handle events
            self.handle_events()
            
            # Update game state
            self.update_game()
            
            # Draw everything
            self.draw()
            
            # Control frame rate
            self.clock.tick(self.fps)
        
        print("Game ended.")
        print(f"Total laps completed: {len(self.lap_times)}")
        if self.best_lap_time:
            print(f"Best lap time: {self.format_time(self.best_lap_time)}")
