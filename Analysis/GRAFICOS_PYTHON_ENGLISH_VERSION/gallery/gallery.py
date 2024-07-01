# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 19:32:25 2023

@author: ca-co
"""

# -*- coding: utf-8 -*-
""" ********************************************
SCRIPT PARA PLOTAGEM DA CURVA DE CONVERGÊNCIA
DAS ANÁLISES EM AXISSIMETRIA
Versão: 2023.1
Situação : Teste (11/07/2020) 
******************************************** """ 

#%% 1. IMPORTAR BIBLIOTECAS

import pandas as pd                    # importa o pacote para manmipular tabelas 
import matplotlib.pyplot as plt        # importa o módulo para plotagem
from scipy.signal import savgol_filter # importa filtro
import locale                          # importa módulo para definir a localização usada no ponto decimal
from matplotlib.ticker import StrMethodFormatter # importa módulo para formatar eixo

#%% 2. FUNÇÃO GRAFICAR

def graficar(arquivo,                   # nome do arquivo de leitura
             titulo,                    # titulo do gráfico
             eixox,eixoy,               # nome dos eixos x e y
             xmin,xmax,                 # intervalo eixo x
             ymin,ymax,                 # intervalo eixo y
             ncoluna,                   # numero da coluna (dados em y)
             lblcoluna,                 # legenda da coluna
             cor,tamanho,ordem,alpha,estilo,   # formatacao
             invertx,                   # inverter eixo x
             inserirx0,x0,              # adicionar linha pontilhada vertical
             suavizar,filterx1,filterx2,wl,poly, # parametros do filtro de suavização
             figura):
    
    # define localização para o ponto decimal
    locale.setlocale(locale.LC_NUMERIC,"ru_RU.utf8")
    
    # Lendo arquivo de dados      
    data = pd.read_csv(arquivo,delim_whitespace= True).values

    # Definindo as dimensões do layout da figura
    fig = plt.figure(figura,figsize = (9,5))

    # Eixo x
    if invertx == True:
        x = -(data[:,1]-max(data[:,1]))-x0
    elif invertx == False:
        x =  data[:,1]
    #x = data[:,1]

    # dados do eixo y
    y = data[:,ncoluna]
    #y = savgol_filter(data[:,ncoluna],20,10)
    
    if suavizar == True:
        for i in range(1,3):
            y[filterx1:filterx2] = savgol_filter(data[filterx1:filterx2,ncoluna],wl,poly, mode = 'interp')
        
    # Plotando os dados
    plt.plot(x,y,color = cor,
             zorder = ordem, 
             linestyle=estilo, 
             lw = tamanho, 
             alpha = alpha, 
             label = lblcoluna)

    # Formatando os eixos
    #plt.axvline(x0,color = 'k', label = lblx0, linestyle = '--')
    plt.ylim([ymin, ymax])
    plt.xlim([xmin-x0, xmax-x0])
    plt.ylabel(eixoy, fontsize=12)
    plt.xlabel(eixox, fontsize=12)
    plt.legend()
    
    # numero de dígitos após o ponto decimal
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter("{x:.2f}"))
    
    # aplica localização para o ponto decimal
    plt.rcParams['axes.formatter.use_locale'] = True
    
    # Formatando grades
    plt.rcParams['axes.axisbelow'] = True 
    plt.grid(True,which = 'major')
    plt.grid(True,which = 'minor', alpha = 0.3)
    plt.minorticks_on()
    
    # Inserir linha vertical em x0
    if inserirx0 == True:
        plt.axvline(x0-x0,color = 'k', lw = 2, linestyle = 'dotted')
    
    # adicionando título
    plt.title(titulo, fontsize = 16, fontweight="bold") 
    #plt.autoscale(axis='y')
    
    # Formatando a legenda
    plt.legend(
        loc = 'center',
        shadow=False,
        framealpha = 0,
        ncol = 3,
        columnspacing = 0.5,
        bbox_to_anchor=(0.5, -0.35),
        fontsize="11")
    
    # Salvando em arquivo    
    plt.savefig(str(titulo) + '.pdf', 
                dpi = fig.dpi, 
                bbox_inches='tight', 
                pad_inches=0.2)

#%% 3. DEFININDO OS DICIONÁRIOS COM AS COLUNAS DOS RESULTADOS
dicncolunalongterm = {

    'E_CRE_SG_D1_INF_AXI': 99,
    'E_CRE_CG_D1_16RE_3D': 127,
    'E_CRE_CG_D1_8RE_3D': 110,
    'E_CRE_CG_D1_4RE_3D': 101,
    
    'EP_SR_SG_D1_INF_AXI': 99,
    'EP_SR_SG_D1_16RE_3D': 99,
    'EP_SR_SG_D1_8RE_3D': 99,
    'EP_SR_SG_D1_4RE_3D': 99,
    
    'EP_SR_CG_D1_16RE_3D': 127,
    'EP_SR_CG_D1_8RE_3D': 110,
    'EP_SR_CG_D1_4RE_3D': 101,
 
    'EP_CRE_SG_D1_INF_AXI': 99,
    'EP_CRE_CG_D1_16RE_3D': 127,
    'EP_CRE_CG_D1_8RE_3D': 110,
    'EP_CRE_CG_D1_4RE_3D': 101,
    
    'EP_CRE_SG_D1_16RE_3D': 99,
    'EP_CRE_SG_D1_8RE_3D': 99,
    'EP_CRE_SG_D1_4RE_3D': 99,

    'VP_CRE_SG_D1_INF_AXI': 129,
    'VP_CRE_CG_D1_16RE_3D': 157,
    'VP_CRE_CG_D1_8RE_3D': 140,
    'VP_CRE_CG_D1_4RE_3D': 131, 
    
    'VP_CRE_SG_D1_16RE_3D': 129,
    'VP_CRE_SG_D1_8RE_3D': 129,
    'VP_CRE_SG_D1_4RE_3D': 129, 

    'EPVP_CRE_SG_D1_INF_AXI': 129,
    'EPVP_CRE_CG_D1_16RE_3D': 157,
    'EPVP_CRE_CG_D1_8RE_3D': 140,
    'EPVP_CRE_CG_D1_4RE_3D': 131,
    
    'EPVP_CRE_SG_D1_16RE_3D': 129,
    'EPVP_CRE_SG_D1_8RE_3D': 129,
    'EPVP_CRE_SG_D1_4RE_3D': 129,
    
    'EPVP_CRVE_SG_D1_INF_AXI': 129,
    'EPVP_CRVE_CG_D1_16RE_3D': 157,
    'EPVP_CRVE_CG_D1_8RE_3D': 140,
    'EPVP_CRVE_CG_D1_4RE_3D': 131,
    
    'EPVP_CRVE_SG_D1_16RE_3D': 129,
    'EPVP_CRVE_SG_D1_8RE_3D': 129,
    'EPVP_CRVE_SG_D1_4RE_3D': 129,
       
    }

dicncolunafinalexcavation = {

    'VP_CRE_SG_D1_INF_AXI': 99,
    'VP_CRE_CG_D1_16RE_3D': 127,
    'VP_CRE_CG_D1_8RE_3D': 110,
    'VP_CRE_CG_D1_4RE_3D': 101,
    
    'VP_CRE_SG_D1_16RE_3D': 99,
    'VP_CRE_SG_D1_8RE_3D': 99,
    'VP_CRE_SG_D1_4RE_3D': 99,

    'EPVP_CRE_SG_D1_INF_AXI': 99,
    'EPVP_CRE_CG_D1_16RE_3D': 127,
    'EPVP_CRE_CG_D1_8RE_3D': 110,
    'EPVP_CRE_CG_D1_4RE_3D': 101,
    
    'EPVP_CRE_SG_D1_16RE_3D': 99,
    'EPVP_CRE_SG_D1_8RE_3D': 99,
    'EPVP_CRE_SG_D1_4RE_3D': 99,
    
    'EPVP_CRVE_SG_D1_INF_AXI': 99,
    'EPVP_CRVE_CG_D1_16RE_3D': 127,
    'EPVP_CRVE_CG_D1_8RE_3D': 110,
    'EPVP_CRVE_CG_D1_4RE_3D': 101,
    
    'EPVP_CRVE_SG_D1_16RE_3D': 99,
    'EPVP_CRVE_SG_D1_8RE_3D': 99,
    'EPVP_CRVE_SG_D1_4RE_3D': 99,
       
    }

# Parametros para o túnel gêmeo
x0_twin_profile                         = 100*1/3
xmin_twin_profile                       = 5
xmax_twin_profile                       = 40
ymin_twin_convergence_profile           = 0
ymax_twin_convergence_profile           = 1.5
ymin_twin_pressure_profile              = -15
ymax_twin_pressure_profile              = 2.5

suavizar_twin                           = True

filterx1_twin_convergence_profile       = 40
filterx2_twin_convergence_profile       = 100
wl_twin_convergence_profile             = 30
poly_twin_convergence_profile           = 10

filterx1_twin_pressure_profile          = 40
filterx2_twin_pressure_profile          = 100
wl_twin_pressure_profile                = 30
poly_twin_pressure_profile              = 2

# Parametros para galeria
x0_gallery_profile                      = 0
xmin_gallery_profile                    = 0
xmax_gallery_profile                    = 12
ymin_gallery_convergence_profile        = 0
ymax_gallery_convergence_profile        = 2
ymin_gallery_pressure_profile           = 0
ymax_gallery_pressure_profile           = 1.5

suavizar_gallery                        = True

filterx1_gallery_convergence_profile    = 0
filterx2_gallery_convergence_profile    = 80
wl_gallery_convergence_profile          = 10
poly_gallery_convergence_profile        = 4

ncoluna = dicncolunalongterm['EP_CRE_SG_D1_INF_AXI']

figura = 1

#%% #. GALLERY CONVERGENCE PROFILES - CG_LP - D1=16Re e D1=4Re
""" ********************************************
GALLERY CONVERGENCE PROFILES - CG_LP - D1=16Re e D1=4Re
******************************************** """ 
# Formatação do gráfico
figura      = figura+1
titulo      = 'Gallery Convergence Profiles - WG_LT - $d_1=16R_i$ e $d_1=4R_i$'
eixox       = r'$x/R_{i1}$'
eixoy       = r'$U=-u(r = R_{i1},\theta = 90^\circ)/R_{i1}$ [%]'
ymin        = ymin_gallery_convergence_profile
ymax        = ymax_gallery_convergence_profile
xmin        = xmin_gallery_profile
xmax        = xmax_gallery_profile
invertx     = False
inserirx0   = False
x0          = 0
suavizar    = suavizar_gallery

# parametros para o filtro de suavização
filterx1    = filterx1_gallery_convergence_profile
filterx2    = filterx2_gallery_convergence_profile
wl          = wl_gallery_convergence_profile
poly        = poly_gallery_convergence_profile

modelo      = 'E_CRE_CG_D1_16RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'E_EL $d_1=16R_i$'
cor         = 'b'
tamanho     = 2
ordem       = 3
alpha       = 1
estilo      = 'solid'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          suavizar,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'E_CRE_CG_D1_4RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'E_EL $d_1=4R_i$'
cor         = 'b'
tamanho     = 2
ordem       = 3
alpha       = 1
estilo      = 'dashed'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          suavizar,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'EP_CRE_CG_D1_16RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'EP_EL $d_1=16R_i$'
cor         = 'orange'
tamanho     = 2
ordem       = 3
alpha       = 1
estilo      = 'solid'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          suavizar,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'EP_CRE_CG_D1_4RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'EP_EL $d_1=4R_i$'
cor         = 'orange'
tamanho     = 2
ordem       = 3
alpha       = 1
estilo      = 'dashed'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          suavizar,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'VP_CRE_CG_D1_16RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'VP_EL $d_1=16R_i$'
cor         = 'magenta'
tamanho     = 2
ordem       = 3
alpha       = 1
estilo      = 'solid'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          suavizar,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'VP_CRE_CG_D1_4RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'VP_EL $d_1=4R_i$'
cor         = 'magenta'
tamanho     = 2
ordem       = 3
alpha       = 1
estilo      = 'dashed'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          suavizar,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'EPVP_CRE_CG_D1_16RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'EPVP_EL $d_1=16R_i$'
cor         = 'g'
tamanho     = 2
ordem       = 3
alpha       = 1
estilo      = 'solid'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          suavizar,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'EPVP_CRE_CG_D1_4RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'EPVP_EL $d_1=4R_i$'
cor         = 'g'
tamanho     = 2
ordem       = 3
alpha       = 1
estilo      = 'dashed'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          suavizar,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'EPVP_CRVE_CG_D1_16RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'EPVP_VEL $d_1=16R_i$'
cor         = 'r'
tamanho     = 2
ordem       = 3
alpha       = 1
estilo      = 'solid'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          suavizar,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'EPVP_CRVE_CG_D1_4RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'EPVP_VEL $d_1=4R_i$'
cor         = 'r'
tamanho     = 2
ordem       = 3
alpha       = 1
estilo      = 'dashed'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          suavizar,filterx1,filterx2,wl,poly,
          figura)

#%% #.  GALLERY CONVERGENCE PROFILES - MODEL EPVP_CRE_EPVP_CRVE_LP

""" ********************************************
GALLERY CONVERGENCE PROFILES - MODEL EPVP_CRE_EPVP_CRVE_LP
******************************************** """ 

# Formatação do gráfico
figura      = figura + 1
titulo      = 'Gallery Convergence Profiles - EPVP_EL_EPVP_VEL_LT'
eixox       = r'$x/R_{i1}$'
eixoy       = r'$U=-u(r = R_{i1},\theta = 90^\circ)/R_{i1}$ [%]'
ymin        = ymin_gallery_convergence_profile
ymax        = ymax_gallery_convergence_profile
xmin        = xmin_gallery_profile
xmax        = xmax_gallery_profile
invertx     = False
inserirx0   = False
x0          = 0
suavizar    = suavizar_gallery

# parametros para o filtro de suavização
filterx1    = filterx1_gallery_convergence_profile
filterx2    = filterx2_gallery_convergence_profile
wl          = wl_gallery_convergence_profile
poly        = poly_gallery_convergence_profile

modelo      = 'EPVP_CRE_SG_D1_16RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'EPVP_EL_NG_$d_1 = 16R_i$'
cor         = 'k'
tamanho     = 1.5
ordem       = 4
alpha       = 1
estilo      = 'solid'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          False,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'EPVP_CRE_CG_D1_16RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'EPVP_EL_WG_$d_1 = 16R_i$'
cor         = 'orange'
tamanho     = 2
ordem       = 3
alpha       = 1
estilo      = 'solid'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          suavizar,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'EPVP_CRVE_SG_D1_16RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'EPVP_VEL_NG_$d_1 = 16R_i$'
cor         = 'k'
tamanho     = 1.5
ordem       = 4
alpha       = 1
estilo      = 'dashed'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          False,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'EPVP_CRVE_CG_D1_16RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'EPVP_VEL_WG_$d_1 = 16R_i$'
cor         = 'orange'
tamanho     = 2
ordem       = 3
alpha       = 1
estilo      = 'dashed'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          suavizar,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'EPVP_CRE_SG_D1_8RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'EPVP_EL_NG_$d_1 = 8R_i$'
cor         = 'magenta'
tamanho     = 1.5
ordem       = 4
alpha       = 1
estilo      = 'solid'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          False,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'EPVP_CRE_CG_D1_8RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'EPVP_EL_WG_$d_1 = 8R_i$'
cor         = 'g'
tamanho     = 2
ordem       = 2
alpha       = 1
estilo      = 'solid'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          suavizar,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'EPVP_CRVE_SG_D1_8RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'EPVP_VEL_NG_$d_1 = 8R_i$'
cor         = 'magenta'
tamanho     = 1.5
ordem       = 4
alpha       = 1
estilo      = 'dashed'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          False,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'EPVP_CRVE_CG_D1_8RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'EPVP_VEL_WG_$d_1 = 8R_i$'
cor         = 'g'
tamanho     = 2
ordem       = 2
alpha       = 1
estilo      = 'dashed'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          suavizar,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'EPVP_CRE_SG_D1_4RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'EPVP_EL_NG_$d_1 = 4R_i$'
cor         = 'b'
tamanho     = 1.5
ordem       = 4
alpha       = 1
estilo      = 'solid'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          False,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'EPVP_CRE_CG_D1_4RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'EPVP_EL_WG_$d_1 = 4R_i$'
cor         = 'r'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'solid'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          suavizar,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'EPVP_CRVE_SG_D1_4RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'EPVP_VEL_NG_$d_1 = 4R_i$'
cor         = 'b'
tamanho     = 1.5
ordem       = 4
alpha       = 1
estilo      = 'dashed'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          False,filterx1,filterx2,wl,poly,
          figura)

modelo      = 'EPVP_CRVE_CG_D1_4RE_3D'
arquivo     = modelo + '\convergencias1_90.txt'
ncoluna     = dicncolunalongterm[modelo]
lblcoluna   = 'EPVP_VEL_WG_$d_1 = 4R_i$'
cor         = 'r'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'dashed'
graficar(arquivo,titulo,eixox,eixoy,
          xmin,xmax,ymin,ymax,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          invertx,
          inserirx0,x0,
          suavizar,filterx1,filterx2,wl,poly,
          figura)