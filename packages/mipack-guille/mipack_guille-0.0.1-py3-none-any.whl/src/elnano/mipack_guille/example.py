__author__ = 'Guillermo González'
__version__ = '1.0.0'
__email__ = 'guillermogonzalezcamara@gmail.com'
__status__ = 'Development'
__date__ = '2023/01/01'
import matplotlib.pyplot as plt

def resultados(text,):
    if text=="alonso":
        tabla = {
        2001: 0,
        2002: 0,
        2003: 55,
        2004: 59,
        2005: 133,
        2006: 134,
        2007: 109,
        2008: 61,
        2009: 26,
        2010: 252,
        2011: 257,
        2012: 278,
        2013: 242,
        2014: 161,
        2015: 11,
        2016: 54,
        2017: 17,
        2018: 50,
        2019: 0,
        2020: 0,
        2021: 81,
        2022: 81}
        
    elif text =="hamilton":
        tabla = {
        2007: 109,
        2008: 98,
        2009: 49,
        2010: 240,
        2011: 227,
        2012: 190,
        2013: 189,
        2014: 384,
        2015: 381,
        2016: 380,
        2017: 363,
        2018: 408,
        2019: 413,
        2020: 347,
        2021: 387
    }
    x=list(tabla.keys())
    y=list(tabla.values())
    plt.bar(x,y)
    plt.show()


