from PIL import Image, ImageDraw
import pprint
import random


class ArtElement:
    def __init__(self, attributes):
        self.attributes = attributes

    def draw(self, draw_context):
        shape = self.attributes.get("shape")
        x, y = self.attributes["position"]
        width = self.attributes["width"]
        length = self.attributes["length"]
        color = self.attributes["color"]

        if shape == "square":
            draw_context.rectangle((x, y, x + width, y + length), fill=color)
        elif shape == "circle":
            draw_context.ellipse((x, y, x + width, y + length), fill=color)

    def __str__(self):
        return pprint.pformat(self.attributes)


class Canvas:
    def __init__(self, width, height, background_color):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.elements = []
        self.image = Image.new("RGB", (width, height), (background_color))

    def add_element(self, element):
        self.elements.append(element)
        print(element)

    def render(self):
        draw = ImageDraw.Draw(self.image)
        for element in self.elements:
            element.draw(draw)
        self.image.show()
        self.image.save("output.png")

    def __str__(self):
        return pprint.pformat(
            f"{str(self.width)}, {str(self.height)}, {str(self.bg_color)}"
        )


def main():
    print("hello")
    canvas = Canvas(500, 500, (255, 255, 255))
    for _ in range(2000):
        attrs = {
            "shape": random.choice(["circle", "square"]),
            "position": (random.randint(0, 500), random.randint(0, 500)),
            "width": random.randint(1, 5),
            "length": random.randint(100, 200),
            "color": (
                random.randint(20, 205),
                random.randint(20, 205),
                random.randint(20, 2105),
            ),
        }

        rectangle = ArtElement(attrs)
        canvas.add_element(rectangle)
    canvas.render()


main()
