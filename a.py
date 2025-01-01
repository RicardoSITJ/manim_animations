from manim import *


class MathFormulaScene(Scene):
    def construct(self):
        # Animate linear algebra concepts
        # Define vectors and matrices
        vector = MathTex("\\vec{v} = \\begin{bmatrix} x \\ y \\end{bmatrix}")
        matrix = MathTex("A = \\begin{bmatrix} a & b \\ c & d \\end{bmatrix}")
        result = MathTex(
            "A \\vec{v} = \\begin{bmatrix} ax + by \\ cx + dy \\end{bmatrix}"
        )

        # Position them
        vector.move_to(UP * 2)
        matrix.next_to(vector, DOWN, buff=1)
        result.next_to(matrix, DOWN, buff=1)

        # Animate
        self.play(Write(vector))
        self.wait(1)
        self.play(Write(matrix))
        self.wait(1)
        self.play(Write(result))
        self.wait(2)
