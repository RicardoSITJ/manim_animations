from manim import *


class EuclideanDistanceScene(Scene):
    def construct(self):
        # Create the vertices of a right triangle
        A = LEFT + DOWN  # Point A at (-1, -1)
        B = RIGHT + DOWN  # Point B at (1, -1)
        # C = LEFT + UP  # Point C at (-1, 1)
        C = RIGHT + UP  # Point C at (-1, 1)

        # Create the triangle
        triangle = Polygon(A, B, C, color=WHITE)

        # Labels for the points
        label_A = Text("A", color=WHITE).next_to(A, DOWN + LEFT, buff=0.1)
        label_B = Text("B", color=WHITE).next_to(B, DOWN + RIGHT, buff=0.1)
        label_C = Text("C", color=WHITE).next_to(C, UP + RIGHT, buff=0.1)

        # # Create the Euclidean distance formula using BasicTex
        # distance_formula = MathTex(
        #     "d = sqrt((x2 - x1)^2 + (y2 - y1)^2)", color=WHITE
        # ).shift(
        #     UP * 2
        # )  # Position at the top

        # Add distance formula
        distance_formula = MathTex(
            "d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}", color=WHITE
        ).shift(
            UP * 2
        )  # Position at the top

        # Display the triangle and labels
        self.play(Create(triangle), Write(label_A), Write(label_B), Write(label_C))

        # Highlight one side of the triangle (distance between A and B)
        distance_line = Line(A, B, color=YELLOW)
        self.play(Create(distance_line))

        # Animate the Euclidean distance formula appearing on screen
        self.play(Write(distance_formula))

        # Move the formula down to emphasize its relevance
        self.play(distance_formula.animate.shift(DOWN * 2))
        self.wait(2)
