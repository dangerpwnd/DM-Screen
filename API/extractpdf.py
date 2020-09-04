import pdfminer.high_level as pdfm

dnd_srd = pdfm.extract_text('SRD.pdf', page_numbers=[2])

print(dnd_srd)
