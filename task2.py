import re
import scraper_helper


def transformer_dic(text):
    #expression réguliére
    pattern = re.compile(r'([A-Za-zÀ-Ö\(\)éè\s,\-0-9]+)\s*:\s*([\d,\.]+\s*[%mgUI]+)')
    
    matches = pattern.findall(text)
    
    dic= {match[0]:match[1] for match in matches}
    
    return dic

text = """Additifs nutritionnels : Vitamine C-D3 : 160 UI, Fer (3b103) : 4mg, Iode (3b202) : 0,28 mg, Cuivre (3b405, 3b406) : 2,2 mg, Manganèse (3b502, 3b503, 3b504) : 1,1 mg, Zinc (3b603, 3b605, 3b606) : 11 mg – Clinoptilolite d’origine sédimentaire : 2 g. Protéine : 11,0 % - Teneur en matières grasses : 4,5 % - Cendres brutes : 1,7 % - Cellulose brute : 0,5 % - Humidité : 80,0 %."""

dictionaire= transformer_dic(text)
print(dictionaire)