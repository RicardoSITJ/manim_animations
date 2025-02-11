from manim import *


class IntegralScene(Scene):
    def construct(self):
        # Add the integral expression as MathTex
        integral_text = MathTex(r"\int (3x^2 - 4x + 5) \, dx", color=WHITE).to_edge(UP)
        self.play(Write(integral_text))

        # Define each step of the integral
        step1 = MathTex(r"\int 3x^2 \, dx = x^3", color=WHITE)
        step2 = MathTex(r"\int -4x \, dx = -2x^2", color=WHITE)
        step3 = MathTex(r"\int 5 \, dx = 5x", color=WHITE)
        step4 = MathTex(r"x^3 - 2x^2 + 5x", color=WHITE)
        step5 = MathTex(r"x^3 - 2x^2 + 5x + C", color=WHITE)

        # Position the steps on the screen
        step1.move_to(UP * 2)
        step2.next_to(step1, DOWN)
        step3.next_to(step2, DOWN)
        step4.next_to(step3, DOWN)
        step5.next_to(step4, DOWN)

        # Animate the steps one by one
        self.play(Write(step1))
        self.wait(3)
        self.play(Transform(step1, step2))
        self.wait(3)
        self.play(Transform(step1, step3))
        self.wait(3)
        self.play(Transform(step1, step4))
        self.wait(3)
        self.play(Transform(step1, step5))
        self.wait(3)
