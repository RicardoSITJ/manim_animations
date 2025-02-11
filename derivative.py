from manim import *


class DerivativeScene(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-10, 10],
            axis_config={"color": BLUE},
        )

        # Define the function f(x) = 8x^2 - 2x + 4
        def f(x):
            return 8 * x**2 - 2 * x + 4

        # Plot the function
        graph_f = axes.plot(f, color=WHITE)
        graph_f_label = axes.get_graph_label(graph_f, label="f(x)")

        # Define the derivative f'(x) = 16x - 2
        def f_prime(x):
            return 16 * x - 2

        # Plot the derivative
        graph_f_prime = axes.plot(f_prime, color=YELLOW)
        graph_f_prime_label = axes.get_graph_label(graph_f_prime, label="f'(x)")

        # Display everything
        self.play(Create(axes), Write(graph_f_label))
        self.play(Create(graph_f))
        self.wait(1)
        self.play(
            Transform(graph_f, graph_f_prime),
            Transform(graph_f_label, graph_f_prime_label),
        )
        self.play(Create(graph_f_prime))
        self.wait(2)
