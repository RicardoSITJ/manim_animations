from manim import *


class SinLimitScene(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes(
            x_range=[-2, 2],
            y_range=[-2, 2],
            axis_config={"color": BLUE},
        )

        # Create the graph of sin(x) / x
        graph = axes.plot(lambda x: np.sin(x) / x if x != 0 else 1, color=WHITE)

        # Label the axes
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Display the graph
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph))

        # Add a dot on the graph to indicate the limit at x = 0
        limit_dot = Dot(color=RED).move_to(axes.c2p(0, 1))
        self.play(FadeIn(limit_dot))

        # Display the limit expression using MathTex
        limit_text = MathTex(
            r"\lim_{x \to 0} \frac{\sin(x)}{x} = 1", color=WHITE
        ).next_to(limit_dot, UP)
        self.play(Write(limit_text))

        # Wait before ending the scene
        self.wait(2)
