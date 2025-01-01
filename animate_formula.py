from manim import *


class MathFormulaScene(Scene):
    def construct(self):
        # Create a math formula
        formula = Text("E = mc^2")

        # Position the formula on the screen
        formula.move_to(ORIGIN)

        # Display the formula on screen
        self.play(Write(formula))

        # Pause for a moment
        self.wait(1)

        # Apply a transformation (e.g., scaling)
        self.play(formula.animate.scale(2))  # Fixed the scaling transformation

        # Wait before finishing the animation
        self.wait(1)
