from manim import *


class EvaluateExpression(Scene):
    def construct(self):
        # Display the original expression
        expression = MathTex("5 + 3 \\times (6^2 - 4) \\div 2 - 8")
        self.play(Write(expression))
        self.wait(1)

        # Step 1: Solve inside the parentheses
        step_1 = MathTex("5 + 3 \\times (36 - 4) \\div 2 - 8")
        self.play(Transform(expression, step_1))
        self.wait(1)

        # Step 2: Simplify inside the parentheses
        step_2 = MathTex("5 + 3 \\times 32 \\div 2 - 8")
        self.play(Transform(expression, step_2))
        self.wait(1)

        # Step 3: Multiplication
        step_3 = MathTex("5 + 96 \\div 2 - 8")
        self.play(Transform(expression, step_3))
        self.wait(1)

        # Step 4: Division
        step_4 = MathTex("5 + 48 - 8")
        self.play(Transform(expression, step_4))
        self.wait(1)

        # Step 5: Addition
        step_5 = MathTex("53 - 8")
        self.play(Transform(expression, step_5))
        self.wait(1)

        # Step 6: Final Subtraction
        result = MathTex("45")
        self.play(Transform(expression, result))
        self.wait(2)

        # Show final result
        self.play(FadeOut(expression))
