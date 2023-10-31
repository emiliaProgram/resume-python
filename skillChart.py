from fpdf import FPDF
import matplotlib.pyplot as plt
import random

# Create a PDF class inheriting from FPDF
class PDF(FPDF):
    def header(self):
        self.set_fill_color(52, 152, 219)
        self.rect(0, 0, 210, 40, 'F')
        self.set_font('Arial', 'B', 20)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, 'Resume', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(44, 62, 80)
        self.cell(0, 10, title, 0, 1, 'L')
    
    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.set_text_color(44, 62, 80)
        self.multi_cell(0, 10, body)

# Getting user information
name = input("Enter your name: ")
bio = input("Enter your bio: ")

skills = []
scales = []

while True:
    skill = input("Enter a skill (or 'done' to finish): ")
    if skill.lower() == 'done':
        break
    scale = int(input(f"Enter the scale for {skill}: "))
    skills.append(skill)
    scales.append(scale)

# Visualizing skills and scales separately
plt.figure(figsize=(8, 6))
colors = [(random.random(), random.random(), random.random()) for _ in range(len(skills))]
plt.bar(skills, scales, color=colors)
plt.xlabel('Skills')
plt.ylabel('Scales')
plt.title('Skills Visualization')
plt.savefig('skills_chart.png', dpi=300, bbox_inches='tight')

# Creating the PDF resume
pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', size=12)

pdf.chapter_title('Name:')
pdf.chapter_body(name)

pdf.chapter_title('Bio:')
pdf.chapter_body(bio)

pdf.chapter_title('Skills Visualization:')
pdf.image('skills_chart.png', x=10, y=None, w=180, h=150)

pdf_file_name = f'{name}_resume.pdf'
pdf.output(pdf_file_name)

print(f"Resume saved as {pdf_file_name}.")