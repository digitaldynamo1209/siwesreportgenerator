import docx
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def apply_booktabs_borders(table):
    tblPr = table._tbl.tblPr
    # Horizontal rules only: top (single), bottom (single), inside horizontal (light single), left/right/insideVertical (none)
    xml_str = (
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="8" w:space="0" w:color="000000"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:bottom w:val="single" w:sz="8" w:space="0" w:color="000000"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="D0D0D0"/>'
        f'  <w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(parse_xml(xml_str))

doc = docx.Document()
t = doc.add_table(rows=3, cols=3)
apply_booktabs_borders(t)
doc.save("test_table.docx")
print("Table created successfully!")
