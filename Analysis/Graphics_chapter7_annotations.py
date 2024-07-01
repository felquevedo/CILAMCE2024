import svgutils.compose as sc
from IPython.display import SVG
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def anotar(titulo, coords, texts, styles, cores, xytexts):

    # drawing a random figure on top of your SVG
    fig, ax = plt.subplots(1, figsize=(9,5))
    
    # Definir a fonte Times New Roman
    font = FontProperties()
    font.set_name('Times')
    
    ax.axis('off')
    ax.set_frame_on(False)
    ax.invert_yaxis() 
    
    for (x, y), text, style, cor,xytext in zip(coords, texts, styles, cores,xytexts):
        ax.annotate(
            text,
            xy=(x, y),  # Coordenadas da anotação
            textcoords='offset points',
            xytext = xytext,
            arrowprops=dict(arrowstyle="-",
                            connectionstyle=style),
            bbox=dict(boxstyle="round,pad=0.1", edgecolor='black', facecolor='white', alpha=1),
            fontsize=12,
            fontname='Times New Roman',
            fontweight='bold',
            color=cor
            ) 
    
    fig.savefig('cover.svg', transparent=True)
    plt.close(fig)
    
    sc.Figure("648","360", 
        sc.Panel(sc.SVG("./" + titulo + ".svg").scale(1).move(0,0)),
        sc.Panel(sc.SVG("cover.svg"))
        ).save(titulo + "_anotate.svg")
    SVG(titulo + '_anotate.svg')

    display(SVG(filename=titulo + '_anotate.svg'))

# Dimensões da imagem no inkscape
L1 = 33
A1 = 1.5


#%% #.  CONVERGENCE PROFILES - MODEL EP_D1_16RE
""" ********************************************
CONVERGENCE PROFILES - MODEL EP_D1_16RE
******************************************** """ 

# Dimensões da imagem no inkscape
L1 = 33
A1 = 2.5


# Adicionar anotações
coords = [(11.2/L1, (A1-1.63)/A1), (11.2/L1, (A1-1.16)/A1), (11.2/L1, (A1-1.00)/A1)]

texts = ['1.63', '1.16', '1.00']

styles = ['arc', 'arc', 'arc']

cores = ['blue', 'blue', 'blue']

xytexts =[(50, 20), (50, 10), (50, -23)]

titulo = 'Convergence Profiles - EP_d1_16Ri'
anotar(titulo, coords, texts, styles, cores, xytexts)

#%% #.  CONVERGENCE PROFILES - MODEL EP_D1_4RE
""" ********************************************
CONVERGENCE PROFILES - MODEL EP_D1_4RE
******************************************** """ 
# Adicionar anotações
coords = [(11.2/L1, (A1-2.03)/A1), (11.2/L1, (A1-1.28)/A1), (11.2/L1, (A1-1.10)/A1)]

texts = ['2.03', '1.28', '1.10']

styles = ['arc', 'arc', 'arc']

cores = ['blue', 'blue', 'blue']

xytexts =[(50, 20), (50, 30), (50, -33)]

titulo = 'Convergence Profiles - EP_d1_4Ri'
anotar(titulo, coords, texts, styles, cores, xytexts)



