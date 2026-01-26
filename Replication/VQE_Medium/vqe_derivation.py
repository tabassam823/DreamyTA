from manim import *
from manim_slides import Slide

class VQEDerivation(Slide):
    def construct(self):
        # Configuration
        title_font_size = 40
        math_font_size = 36
        
        # --- TITLE ---
        title = Text("Markowitz to QUBO Derivation", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.next_slide()

        # --- STEP 1: MARKOWITZ OBJECTIVE ---
        step1_title = Text("1. Markowitz Objective", font_size=title_font_size, color=BLUE).to_edge(UP).shift(DOWN * 1)
        
        # Objective Function
        # Minimize w * Risk - (1-w) * Return
        obj_text = MathTex(
            r"\text{Minimize }", 
            r"w \sum_{i,j} \sigma_{ij} x_i x_j", 
            r"-", 
            r"(1-w) \sum_i \mu_i x_i",
            font_size=math_font_size
        )
        
        # Labels for Risk and Return
        risk_brace = Brace(obj_text[1], UP)
        risk_label = risk_brace.get_text("Risk (Variance)").set_color(RED)
        
        return_brace = Brace(obj_text[3], UP)
        return_label = return_brace.get_text("Return").set_color(GREEN)

        self.play(Transform(title, step1_title))
        self.play(Write(obj_text))
        self.play(GrowFromCenter(risk_brace), Write(risk_label))
        self.play(GrowFromCenter(return_brace), Write(return_label))
        
        self.next_slide()

        # Clean up braces for next part, keep equation but move it up
        self.play(FadeOut(risk_brace), FadeOut(risk_label), FadeOut(return_brace), FadeOut(return_label))
        self.play(obj_text.animate.shift(UP * 2))

        # --- STEP 2: CONSTRAINT ---
        step2_title = Text("2. Cardinality Constraint", font_size=title_font_size, color=BLUE).to_edge(UP).shift(DOWN * 1)
        
        constraint_text = MathTex(
            r"\text{Select exactly } B \text{ assets: }",
            r"\sum_{i=1}^N x_i = B",
            font_size=math_font_size
        )
        
        self.play(Transform(title, step2_title))
        self.play(Write(constraint_text))
        self.next_slide()

        # --- STEP 3: PENALTY METHOD ---
        step3_title = Text("3. Penalty Method (QUBO)", font_size=title_font_size, color=BLUE).to_edge(UP).shift(DOWN * 1)
        
        # Explanation: Constraint -> Penalty
        penalty_text = MathTex(
            r"\text{Penalty} = P \left( \sum_{i=1}^N x_i - B \right)^2",
            font_size=math_font_size
        ).next_to(constraint_text, DOWN, buff=1)

        self.play(Transform(title, step3_title))
        self.play(
            constraint_text.animate.set_color(GRAY),
            Write(penalty_text)
        )
        self.next_slide()

        # --- STEP 4: TOTAL COST FUNCTION ---
        step4_title = Text("4. Total Cost Function", font_size=title_font_size, color=BLUE).to_edge(UP).shift(DOWN * 1)
        
        # Combine everything
        # C(x) = Objective + Penalty
        final_eq = MathTex(
            r"C(x) =",
            r"w x^T \Sigma x",
            r"-",
            r"(1-w) \mu^T x",
            r"+",
            r"P \left( \sum x_i - B \right)^2",
            font_size=math_font_size
        )
        
        # Arrange final equation
        final_eq.move_to(ORIGIN)

        self.play(Transform(title, step4_title))
        self.play(
            FadeOut(obj_text),
            FadeOut(constraint_text),
            FadeOut(penalty_text),
            Write(final_eq)
        )
        
        # Highlight parts
        self.play(Indicate(final_eq[1], color=RED)) # Risk
        self.play(Indicate(final_eq[3], color=GREEN)) # Return
        self.play(Indicate(final_eq[5], color=YELLOW)) # Penalty

        self.next_slide()
        
        # Final cleanup
        self.play(FadeOut(final_eq), FadeOut(title))
        end_text = Text("Ready for VQE Mapping", font_size=48)
        self.play(Write(end_text))
