from manim import *


class LinearEquationToVector(Scene):
    def construct(self):
        # Define axes
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": BLUE},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Linear equation: y = 2x + 1
        equation = MathTex("y = 2x + 1").to_corner(UL)
        line = axes.plot(lambda x: 2 * x + 1, color=YELLOW, x_range=[-5, 5])

        # A vector to animate
        vector = Vector([2, 5], color=RED).shift(axes.c2p(0, 0))

        # Add everything to the scene
        self.play(Create(axes), Write(labels))
        self.play(Write(equation))
        self.play(Create(line), run_time=2)

        # Animate a vector moving along the line
        moving_dot = Dot(axes.c2p(-2, -3), color=RED)
        self.play(FadeIn(moving_dot))
        self.play(
            moving_dot.animate.move_to(axes.c2p(2, 5)), GrowArrow(vector), run_time=3
        )

        # Transform equation into a vector description
        vector_eq = MathTex(r"\vec{v} = \begin{bmatrix} 2 \\ 5 \end{bmatrix}").next_to(
            equation, DOWN
        )
        self.play(Transform(equation, vector_eq))

        # Highlight the final vector
        self.wait(2)
        self.play(FadeOut(line), FadeOut(moving_dot))
        self.play(vector.animate.shift(axes.c2p(1, -1)), run_time=2)
        self.wait(2)
