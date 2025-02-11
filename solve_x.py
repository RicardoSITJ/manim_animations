from manim import *


class SolveForX(Scene):
    def construct(self):
        # Display the original equation
        equation = MathTex("3(x + 5) - 4 = 2x - 3")
        self.play(Write(equation))
        self.wait(1)

        # Step 1: Distribute 3
        step_1 = MathTex("3x + 15 - 4 = 2x - 3")
        self.play(Transform(equation, step_1))
        self.wait(1)

        # Step 2: Simplify constants on the left
        step_2 = MathTex("3x + 11 = 2x - 3")
        self.play(Transform(equation, step_2))
        self.wait(1)

        # Step 3: Move 2x to the left side
        step_3 = MathTex("3x - 2x + 11 = -3")
        self.play(Transform(equation, step_3))
        self.wait(1)

        # Step 4: Simplify left-hand side
        step_4 = MathTex("x + 11 = -3")
        self.play(Transform(equation, step_4))
        self.wait(1)

        # Step 5: Subtract 11 from both sides
        step_5 = MathTex("x = -3 - 11")
        self.play(Transform(equation, step_5))
        self.wait(1)

        # Step 6: Final calculation
        result = MathTex("x = -14")
        self.play(Transform(equation, result))
        self.wait(2)

        # Fade out
        self.play(FadeOut(equation))
