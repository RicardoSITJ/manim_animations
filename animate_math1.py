from manim import *


class MathFormulaScene(Scene):
    def construct(self):
        # Define the steps for expanding (x + 2)^2
        step1 = MathTex("(x + 2)^2")
        step2 = MathTex("(x + 2)(x + 2)")
        step3 = MathTex("x(x + 2) + 2(x + 2)")
        step4 = MathTex("x^2 + 2x + 2x + 4")
        step5 = MathTex("x^2 + 4x + 4")

        # Position the steps on the screen
        step1.move_to(UP * 2)
        step2.next_to(step1, DOWN)
        step3.next_to(step2, DOWN)
        step4.next_to(step3, DOWN)
        step5.next_to(step4, DOWN)

        # Animate the steps one by one
        self.play(Write(step1))
        self.wait(2)
        self.play(Transform(step1, step2))
        self.wait(2)
        self.play(Transform(step1, step3))
        self.wait(2)
        self.play(Transform(step1, step4))
        self.wait(2)
        self.play(Transform(step1, step5))
        self.wait(2)
