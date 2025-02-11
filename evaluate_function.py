from manim import *


class EvaluateFunction(Scene):
    def construct(self):
        # Display the given function
        function = MathTex("f(x) = 2x^2 + 3x - 5")
        self.play(Write(function))
        self.wait(1)

        # Step 1: Evaluate f(-2)
        step_1 = MathTex("f(-2) = 2(-2)^2 + 3(-2) - 5")
        self.play(Transform(function, step_1))
        self.wait(1)

        step_2 = MathTex("= 2(4) + (-6) - 5")
        self.play(Transform(function, step_2))
        self.wait(1)

        step_3 = MathTex("= 8 - 6 - 5")
        self.play(Transform(function, step_3))
        self.wait(1)

        step_4 = MathTex("= -3")
        self.play(Transform(function, step_4))
        self.wait(2)

        # Step 2: Evaluate f(3)
        step_5 = MathTex("f(3) = 2(3)^2 + 3(3) - 5")
        self.play(Transform(function, step_5))
        self.wait(1)

        step_6 = MathTex("= 2(9) + 9 - 5")
        self.play(Transform(function, step_6))
        self.wait(1)

        step_7 = MathTex("= 18 + 9 - 5")
        self.play(Transform(function, step_7))
        self.wait(1)

        step_8 = MathTex("= 22")
        self.play(Transform(function, step_8))
        self.wait(2)

        # Final fade out
        self.play(FadeOut(function))
