from manim import *


class SimplifyExponent(Scene):
    def construct(self):
        # Step 1: Write the given expression
        expression = MathTex("2^3 \\times 2^3 \\div 2^2")
        self.play(Write(expression))
        self.wait(1)

        # Step 2: Apply the Product Rule: 2^3 * 2^3 = 2^6
        step_1 = MathTex("2^{3+3} \\div 2^2")
        self.play(Transform(expression, step_1))
        self.wait(1)

        step_2 = MathTex("2^6 \\div 2^2")
        self.play(Transform(expression, step_2))
        self.wait(1)

        # Step 3: Apply the Quotient Rule: 2^6 ÷ 2^2 = 2^4
        step_3 = MathTex("2^{6-2}")
        self.play(Transform(expression, step_3))
        self.wait(1)

        step_4 = MathTex("2^4")
        self.play(Transform(expression, step_4))
        self.wait(1)

        # Step 4: Compute the final value
        result = MathTex("16")
        self.play(Transform(expression, result))
        self.wait(2)

        # Fade out final result
        self.play(FadeOut(expression))
