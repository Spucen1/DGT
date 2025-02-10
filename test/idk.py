import pygame
import math

# Pygame Initialization
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
GRAVITY = 0.2
FRICTION = 0.99
HEX_RADIUS = 200
ROTATION_SPEED = 1  # Degrees per frame

# Colors
WHITE = (255, 119, 41)
BLACK = (37, 36, 47)
RED = (118, 135, 172)

# Ball Properties
ball_pos = [WIDTH // 2, HEIGHT // 2 - 100]
ball_vel = [2, -2]
ball_radius = 15

# Pygame Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

angle = 0  # Rotation angle of hexagon

def hexagon_points(center, radius, angle):
    """Returns the vertices of a rotated hexagon."""
    points = []
    for i in range(6):
        theta = math.radians(angle + i * 60)
        x = center[0] + radius * math.cos(theta)
        y = center[1] + radius * math.sin(theta)
        points.append((x, y))
    return points

def reflect(ball_velocity, normal):
    """Reflects the velocity vector based on the wall's normal."""
    dot = ball_velocity[0] * normal[0] + ball_velocity[1] * normal[1]
    return [
        ball_velocity[0] - 2 * dot * normal[0],
        ball_velocity[1] - 2 * dot * normal[1]
    ]

def line_normal(p1, p2):
    """Finds the normal of a line segment (perpendicular unit vector)."""
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    length = math.sqrt(dx**2 + dy**2)
    return (-dy / length, dx / length)

# Game Loop
running = True
while running:
    screen.fill(BLACK)

    # Update Hexagon Rotation
    angle += ROTATION_SPEED
    hex_points = hexagon_points((WIDTH // 2, HEIGHT // 2), HEX_RADIUS, angle)

    # Draw Hexagon
    pygame.draw.polygon(screen, WHITE, hex_points, 2)

    # Apply Gravity
    ball_vel[1] += GRAVITY

    # Move Ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Ball-Hexagon Collision Detection
    for i in range(6):
        p1, p2 = hex_points[i], hex_points[(i + 1) % 6]

        # Edge vector
        edge_vec = (p2[0] - p1[0], p2[1] - p1[1])
        edge_length = math.sqrt(edge_vec[0] ** 2 + edge_vec[1] ** 2)

        # Normal vector
        normal = line_normal(p1, p2)

        # Distance from ball to edge
        edge_to_ball = (ball_pos[0] - p1[0], ball_pos[1] - p1[1])
        projection = (edge_to_ball[0] * edge_vec[0] + edge_to_ball[1] * edge_vec[1]) / edge_length
        closest_x = p1[0] + projection * edge_vec[0] / edge_length
        closest_y = p1[1] + projection * edge_vec[1] / edge_length
        distance = math.sqrt((closest_x - ball_pos[0])**2 + (closest_y - ball_pos[1])**2)

        if 0 <= projection <= edge_length and distance <= ball_radius:
            # Reflect the velocity
            ball_vel = reflect(ball_vel, normal)
            # Move ball slightly away from the wall to avoid sticking
            ball_pos[0] += normal[0] * (ball_radius - distance)
            ball_pos[1] += normal[1] * (ball_radius - distance)

            # Apply friction
            ball_vel[0] *= FRICTION
            ball_vel[1] *= FRICTION

    # Draw Ball
    pygame.draw.circle(screen, RED, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update Display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
