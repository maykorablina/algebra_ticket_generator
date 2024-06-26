import random
from PyPDF2 import PdfReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text


def clean_text(text):
    replacements = {
        "�": "",
        "UFD": "Unique Factorization Domain",
        "fi": "fi",
        "Fi": "Fi",
        "ﬃ": "ffi",
        "ﬀ": "ff",
        "ﬁ": "fi",
        "ﬂ": "fl",
        "ﬂ": "fl",
        "ﬂ": "fl",
        "ﬀ": "ff",
        "ﬂ": "fl",
        "ﬃ": "ffi",
        "ﬄ": "ffl",
        "ﬅ": "st",
        "ﬆ": "st",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


definitions_text = extract_text_from_pdf('definitions_list.pdf')
statements_text = extract_text_from_pdf('question_list.pdf')

definitions = definitions_text.split('\n')[5:]
statements = statements_text.split('\n')[5:]

definitions = [clean_text(d) for d in definitions]
statements = [clean_text(s) for s in statements]

clean_definitions = [d.split('.', 1)[-1].strip().split(' Definition')[0].split('.')[0] for d in definitions]
clean_statements = [s.split('.', 1)[-1].strip().split(' Claim')[0].split('.')[0] for s in statements]

simple_statements = [
    "There is at most one neutral element for a binary operation",
    "There is at most one inverse for an associative binary operation",
    "Properties of powers in a group",
    "Classification of cyclic groups",
    "Subgroups of the group Z",
    "Subgroups of the group Zn",
    "Equivalent definitions of a normal subgroup",
    "Relation between cosets of a group",
    "Number of elements in a coset",
    "Formulas for the number of cosets",
    "The relation between the order of an element the order of a group",
    "A group of a prime order",
    "The Fermat Little Theorem",
    "A homomorphism of groups preserves the identity and the inverses",
    "Properties of the kernel of a group homomorphism",
    "Properties of the image of a group homomorphism",
    "The Additive Chinese Remainder Theorem for integers",
    "The Multiplicative Chinese Remainder Theorem for integers",
    "Ideals of the ring Z",
    "Ideals of the ring Zn",
    "Properties of the kernel of a ring homomorphism",
    "Properties of the image of a ring homomorphism",
    "Ideals of the polynomial ring in one variable",
    "Expression of gcd as a linear combination of given polynomials",
    "Ideals of a ring of polynomial remainders",
    "The Chinese Remainder Theorem for the ring of polynomial remainders",
    "Options for the characteristic of a field",
    "When a ring of integer remainders is a field",
    "Number of elements of a finite field",
    "Structure of the multiplicative group of a finite field",
    "Property of a descending chain of monomials",
]

interesting_statements = [
    stmt for stmt in clean_statements if stmt not in simple_statements
]


def generate_exam_ticket(definitions, simple_statements, interesting_statements):
    ticket = {
        'definitions': random.sample(definitions, 4),
        'statements': random.sample(clean_statements, 2),
        'simple_proof': random.choice(simple_statements),
        'interesting_proof': random.choice(interesting_statements)
    }
    return ticket


def create_pdf(ticket, filename='exam_ticket.pdf'):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont('Helvetica', 12)
    width, height = letter

    c.drawString(100, height - 100, "Exam Ticket")

    y = height - 150
    line_height = 24
    c.drawString(100, y, "• Give four definitions, 0.5 each:")
    y -= line_height
    for definition in ticket['definitions']:
        c.drawString(120, y, definition)
        y -= line_height

    y -= line_height
    c.drawString(100, y, "• Formulate two statements without proof, 1.5 each:")
    y -= line_height
    for statement in ticket['statements']:
        c.drawString(120, y, statement)
        y -= line_height

    y -= line_height
    c.drawString(100, y, "• Prove a simple statement, 2 points:")
    y -= line_height
    c.drawString(120, y, ticket['simple_proof'])

    y -= line_height * 2
    c.drawString(100, y, "• Prove an interesting statement, 3 points:")
    y -= line_height
    c.drawString(120, y, ticket['interesting_proof'])

    c.save()


ticket = generate_exam_ticket(clean_definitions, simple_statements, interesting_statements)
create_pdf(ticket)

print("Exam ticket generated and saved as 'exam_ticket.pdf'.")
