from manim import *


class SolveExponentialEquation(Scene):
    def construct(self):
        # Step 1: Display the given equation
        equation = MathTex(r"e^x = 20")
        self.play(Write(equation))
        self.wait(1)

        # Step 2: Apply natural logarithm to both sides
        step_1 = MathTex(r"\ln(e^x) = \ln(20)")
        self.play(Transform(equation, step_1))
        self.wait(1)

        # Step 3: Use logarithm property ln(e^x) = x * ln(e)
        step_2 = MathTex(r"x \ln(e) = \ln(20)")
        self.play(Transform(equation, step_2))
        self.wait(1)

        # Step 4: Since ln(e) = 1, simplify to x = ln(20)
        step_3 = MathTex(r"x = \ln(20)")
        self.play(Transform(equation, step_3))
        self.wait(1)

        # Step 5: Approximate the value of ln(20)
        step_4 = MathTex(r"x \approx 2.9957")
        self.play(Transform(equation, step_4))
        self.wait(2)

        # Fade out final result
        self.play(FadeOut(equation))
