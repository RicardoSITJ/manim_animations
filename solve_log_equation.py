from manim import *


class SolveLogEquation(Scene):
    def construct(self):
        # Step 1: Display the given equation
        equation = MathTex(r"\ln(x) + \ln(x - 2) = 2")
        self.play(Write(equation))
        self.wait(1)

        # Step 2: Apply log property ln(A) + ln(B) = ln(A * B)
        step_1 = MathTex(r"\ln(x(x - 2)) = 2")
        self.play(Transform(equation, step_1))
        self.wait(1)

        # Step 3: Convert to exponential form
        step_2 = MathTex(r"x^2 - 2x = e^2")
        self.play(Transform(equation, step_2))
        self.wait(1)

        # Step 4: Solve the quadratic equation
        step_3 = MathTex(r"x^2 - 2x - e^2 = 0")
        self.play(Transform(equation, step_3))
        self.wait(1)

        # Step 5: Apply quadratic formula
        step_4 = MathTex(r"x = \frac{2 \pm \sqrt{4 + 4e^2}}{2}")
        self.play(Transform(equation, step_4))
        self.wait(1)

        step_5 = MathTex(r"x = \frac{2 \pm 2\sqrt{1 + e^2}}{2}")
        self.play(Transform(equation, step_5))
        self.wait(1)

        step_6 = MathTex(r"x = 1 \pm \sqrt{1 + e^2}")
        self.play(Transform(equation, step_6))
        self.wait(1)

        # Step 6: Valid solution check (x > 2)
        step_7 = MathTex(r"x = 1 + \sqrt{1 + e^2}")
        self.play(Transform(equation, step_7))
        self.wait(2)

        # Fade out final result
        self.play(FadeOut(equation))
