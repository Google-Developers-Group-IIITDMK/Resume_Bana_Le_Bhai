import os
import subprocess
from jinja2 import Template

class ResumeService:
    def __init__(self, template_path: str, output_dir: str):
        self.template_path = template_path
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_tex(self, user_data: dict) -> str:
        """Fill LaTeX template with user data."""
        with open(self.template_path, 'r') as f:
            template = Template(f.read())
        filled_tex = template.render(user_data)
        tex_path = os.path.join(self.output_dir, "resume.tex")
        with open(tex_path, 'w') as f:
            f.write(filled_tex)
        return tex_path

    def compile_pdf(self, tex_path: str) -> str:
        """Compile LaTeX file into PDF using pdflatex."""
        current_dir = os.getcwd()
        os.chdir(self.output_dir)
        try:
            subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", tex_path],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"LaTeX compilation failed: {e.stderr.decode()}")
        finally:
            os.chdir(current_dir)
        return os.path.join(self.output_dir, "resume.pdf")

    def create_resume(self, user_data: dict) -> str:
        tex_path = self.generate_tex(user_data)
        return self.compile_pdf(os.path.basename(tex_path))


resume_service = ResumeService(
    template_path="src/templates/resume_template.tex",
    output_dir="src/outputs"
)