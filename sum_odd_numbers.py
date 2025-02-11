from manim import *


class SumOddNumbersArithmetic(Scene):
    def construct(self):
        # Display the arithmetic series formula
        formula = MathTex("S_n = \\frac{n}{2} (a + l)")
        self.play(Write(formula))
        self.wait(1)

        # Step 1: Define values for n, a, l
        step_1 = MathTex("S_{100} = \\frac{100}{2} (1 + 199)")
        self.play(Transform(formula, step_1))
        self.wait(1)

        # Step 2: Compute division
        step_2 = MathTex("S_{100} = 50 \\times (1 + 199)")
        self.play(Transform(formula, step_2))
        self.wait(1)

        # Step 3: Compute sum inside parentheses
        step_3 = MathTex("S_{100} = 50 \\times 200")
        self.play(Transform(formula, step_3))
        self.wait(1)

        # Step 4: Compute final product
        result = MathTex("S_{100} = 10000")
        self.play(Transform(formula, result))
        self.wait(2)

        # Fade out final result
        self.play(FadeOut(formula))
