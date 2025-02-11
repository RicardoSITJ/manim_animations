from manim import *


class IntegerSolutionsScene(Scene):
    def construct(self):
        # Define the given equation
        equation = MathTex("x^2 + y^2 = 100")
        equation.move_to(UP * 3)

        # Step 1: Identify perfect squares less than or equal to 100
        step1 = MathTex("x^2, y^2 \leq 100").next_to(equation, DOWN)

        # Step 2: List possible integer values for x and y
        step2 = MathTex("x, y \in \{-10, -9, ..., 9, 10\}").next_to(step1, DOWN)

        # Step 3: Check integer pairs for solutions
        step3 = MathTex("\\text{Find integer pairs where } x^2 + y^2 = 100").next_to(
            step2, DOWN
        )

        # Step 4: Compute valid (x, y) values
        step4 = MathTex("\\text{Compute: } x^2 = 100 - y^2").next_to(step3, DOWN)

        # Step 5: Take square root to find integer x-values
        step5 = MathTex("\\text{Solve: } x = \pm \sqrt{100 - y^2}").next_to(step4, DOWN)

        # Step 6: Extract integer solutions
        step6 = MathTex("\\text{Check integer values for } x").next_to(step5, DOWN)

        # Animate the equation and steps
        self.play(Write(equation))
        self.wait(1)
        self.play(Write(step1))
        self.wait(1)
        self.play(Write(step2))
        self.wait(1)
        self.play(Write(step3))
        self.wait(1)
        self.play(Write(step4))
        self.wait(1)
        self.play(Write(step5))
        self.wait(1)
        self.play(Write(step6))
        self.wait(1)

        # Clear the screen after step 6
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Step 7: Evaluate integer solutions step-by-step
        evaluations = [
            "\\text{If } y = 0, x = \pm \sqrt{100} = \pm10",
            "\\text{If } y = 6, x = \pm \sqrt{64} = \pm8",
            "\\text{If } y = 8, x = \pm \sqrt{36} = \pm6",
            "\\text{If } y = 10, x = \pm \sqrt{0} = 0",
        ]

        evaluation_texts = [MathTex(e).scale(0.8) for e in evaluations]

        # Position and animate evaluations
        for i, eval_text in enumerate(evaluation_texts):
            if i == 0:
                eval_text.move_to(UP * 2)
            else:
                eval_text.next_to(evaluation_texts[i - 1], DOWN)
            self.play(Write(eval_text))
            self.wait(1)
