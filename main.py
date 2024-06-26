import random
from PyPDF2 import PdfReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def extract_text_from_pdf(pdf_path, page_number):
    reader = PdfReader(pdf_path)
    text = reader.pages[page_number].extract_text()
    return text

def clean_text(text):
    replacements = {
        "�": "",
        "UFD": "Unique Factorization Domain",
        "fi": "fi",
        "Fi": "Fi",
        "ﬃ": "ffi",  # common ligatures
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

def split_penultimate_period(text):
    parts = text.rsplit('.', 2)
    if len(parts) >= 2:
        try:
            return parts[0].split(".", 1)[1].split(".", 1)[0]
        except:
            return ""
    return text

definitions_text = extract_text_from_pdf('definitions_list.pdf', 0)
statements_text = extract_text_from_pdf('definitions_list.pdf', 1)
proofs_text = extract_text_from_pdf('question_list.pdf', 0)

definitions = definitions_text.split('\n')[5:]
statements = statements_text.split('\n')[5:]
proofs = proofs_text.split('\n')[5:]

definitions = [clean_text(d) for d in definitions]
statements = [clean_text(s) for s in statements]
proofs = [clean_text(p) for p in proofs]

clean_definitions = [split_penultimate_period(d) for d in definitions]
clean_statements = [split_penultimate_period(s) for s in statements]
clean_proofs = [split_penultimate_period(p) for p in proofs]

clean_definitions = [x for x in clean_definitions if x.isdigit() == 0]
clean_statements = [x for x in clean_statements if x.isdigit() == 0]
clean_proofs = [x for x in clean_proofs if x.isdigit() == 0]
for i in range(len(clean_statements)):
    if clean_statements[i] == 'Cryptography':
        clean_statements[i] = 'Cryptography. Describe Diffie-Hellman communication process'

simple_proof_list = [
    "There is at most one neutral element for a binary operation",
    "There is at most one inverse for an associative binary operation",
    "Properties of powers in a group",
    "Classification of cyclic groups",
    "Subgroups of the group Z",
    "Subgroups of the group Zn",
    "Number of elements in a coset",
    "Formulas for the number of cosets",
    "The relation between the order of an element and the order of a group",
    "A group of a prime order",
    "The Fermat Little Theorem",
    "A homomorphism of groups preserves the identity and the inverses",
    "Properties of the kernel of a group homomorphism",
    "Properties of the image of a group homomorphism",
    "Ideals of the ring Z",
    "Number of elements of a finite field"
]

simple_proofs = [p for p in clean_proofs if any(simple in p for simple in simple_proof_list)]
interesting_proofs = [p for p in clean_proofs if p not in simple_proofs]

def generate_exam_ticket(definitions, clean_statements, simple_proofs, interesting_proofs):
    ticket = {
        'definitions': random.sample(definitions, 4),
        'statements': random.sample(clean_statements, 2),
        'simple_proof': random.choice(simple_proofs),
        'interesting_proof': random.choice(interesting_proofs)
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

ticket = generate_exam_ticket(clean_definitions, clean_statements, simple_proofs, interesting_proofs)
create_pdf(ticket)

print("Exam ticket generated and saved as 'exam_ticket.pdf'.")
