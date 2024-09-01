import serial
import pygame
import time

# Initialize Pygame and Serial Communication
pygame.init()
ser = serial.Serial("COM3", 9600)

# Set up screen dimensions
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("7 Segment Display Interface")

# Colors
BACKGROUND_COLOR = (34, 34, 34)
LOADING_COLOR = (255, 255, 255)


class Light(pygame.sprite.Sprite):
    def __init__(self, image, pos, pin):
        super().__init__()

        # Image paths
        base_name, ext = image.rsplit('.', 1)
        self.white_img_path = image
        self.red_img_path = f"{base_name}-red.{ext}"

        # Load images
        self.white_image = pygame.image.load(
            self.white_img_path).convert_alpha()
        self.red_image = pygame.image.load(self.red_img_path).convert_alpha()
        self.image = self.white_image

        # Set position and pin
        self.rect = self.image.get_rect(topleft=pos)
        self.pin = pin
        self.turned_on = False

    def toggle(self):
        """Toggle the light on or off and update the Arduino."""
        self.turned_on = not self.turned_on
        self.image = self.red_image if self.turned_on else self.white_image
        ser.write(self.pin.encode('utf-8'))
        time.sleep(0.1)  # Ensure the Arduino processes the command

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                self.toggle()


def show_loading_screen(screen, width, height):
    """Display a loading screen while the Arduino initializes."""
    screen.fill(BACKGROUND_COLOR)
    font = pygame.font.Font(None, 36)
    text = font.render("Initializing Arduino...", True, LOADING_COLOR)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)
    pygame.display.update()


def flash_lights(lights):
    """Flash all lights in a pattern."""
    for light in lights:
        light.toggle()
    time.sleep(0.5)
    for light in lights:
        light.toggle()


def main():
    images = {
        "top_left_img": ["assets/top-left.png", (152, 88), "7\n"],
        "top_right_img": ["assets/top-right.png", (347, 88), "9\n"],
        "top_img": ["assets/top.png", (197, 87), "8\n"],
        "bottom_right_img": ["assets/bottom-right.png", (347, 255), "4\n"],
        "bottom_left_img": ["assets/bottom-left.png", (152, 255), "2\n"],
        "bottom_img": ["assets/bottom.png", (197, 387), "3\n"],
        "middle_img": ["assets/middle.png", (197, 235), "6\n"],
        "circle_img": ["assets/circle.png", (391, 381), "5\n"]
    }

    lights = pygame.sprite.Group()
    for img in images.values():
        light = Light(img[0], img[1], img[2])
        lights.add(light)

    # Show loading screen while Arduino initializes
    show_loading_screen(screen, width, height)
    time.sleep(2)  # Wait for Arduino to initialize
    flash_lights(lights)

    try:
        while True:
            screen.fill(BACKGROUND_COLOR)
            events = pygame.event.get()

            lights.update(events)
            lights.draw(screen)

            for event in events:
                if event.type == pygame.QUIT:
                    ser.write("reset".encode('utf-8'))
                    pygame.quit()
                    ser.close()
                    exit()

            pygame.display.update()
    except Exception as e:
        ser.write("reset".encode('utf-8'))
        pygame.quit()
        ser.close()
        print(f"An error occurred: {e}")
        exit()


if __name__ == "__main__":
    main()
