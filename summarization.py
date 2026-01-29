from docx import Document
from transformers import pipeline
import os

summarizer = pipeline("summarization")

def read_docx(docx_path):
    document = Document(docx_path)
    full_text = []
    for para in document.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def summarize_text(text, max_length=130, min_length=30, do_sample=False):
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=do_sample)
    return summary[0]['summary_text']    

def save_summary_to_txt(summarize_text, txt_path):
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(summarize_text)

if __name__ == '__main__':
    docx_path = 'documento.docx'
    txt_path = 'resumo.txt'
    
    full_text = read_docx(docx_path)   
    summary = summarize_text(full_text)
    save_summary_to_txt(summary, txt_path)
    print(f"Resumo salvo em {txt_path}")