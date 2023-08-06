import yfinance
import pandas as pd
import requests
#from displayfunction import display
from pandas_datareader import data as web
import datetime
import matplotlib.pyplot as plt
def conversao(valor,atual,convertida):

    ''' essa função recebe tres parametros
    valor:valor a ser covertido:float
    atual:codigo da moeda atual:string
    convertida:codigo da moeda a ser convertida:string
    retorna: o valor convertido'''

    atual = atual.upper()
    convertida = convertida.upper()
    
    if len(atual) == 3 and len(convertida) == 3 and (type(valor) == float or type(valor) == int) and (type(atual) == str and type(convertida) == str):
        cotacoes = requests.get("https://economia.awesomeapi.com.br/last/"+atual + '-' + convertida)
        if cotacoes.status_code==200:
            cotacoes = cotacoes.json()
            conversao = float(cotacoes[atual+convertida]['bid'])
            return float(f'{valor * conversao:.2f}')
        else:
            return 'site fora do ar'
    else:
        return ('escreva uma abreviação valida: como BRL,USD,EUR')

def cotacao(atual,convertida):

    '''essa funçãom recebe dois paramentros
    atual:codigo da moeda atual:string
    convertida:codigo da moeda a ser convertida:string
    retorna: a cotação dessas moedas'''

    atual = atual.upper()
    convertida = convertida.upper()
    if (len(atual) == 3 and len(convertida)==3) and (type(atual) == str and type(convertida)== str):

        cotacoes = requests.get("https://economia.awesomeapi.com.br/last/"+atual + '-' + convertida)
        cotacoes = cotacoes.json()
        conversao = float(cotacoes[atual+convertida]['bid'])
        return float(f'{conversao:.2f}')
    else:
        return 'escreva uma abrevia valida: como brl,usd,eur'

def dados(atual,convertida,dado):

    '''essa funçãom recebe tres paramentros
       atual:codigo da moeda atual:string
       convertida:codigo da moeda a ser convertida:string
       dado:é o dado expecificom q vai retornar(high,low,bind):string
       retorna: os dados da moeda'''
    
    atual = atual.upper()
    convertida = convertida.upper()
    if (len(atual) == 3 and len(convertida)==3) and (type(atual) == str and type(convertida)== str) and type(dado) == str:

        cotacoes = requests.get("https://economia.awesomeapi.com.br/last/"+atual + '-' + convertida)
        cotacoes = cotacoes.json()
        conversao = cotacoes[atual+convertida][dado]
        return conversao
    else:
        return 'escreva uma abrevia valida: como brl,usd,eur'

def tabelasfech(info,br,dias):

    '''essa função recebe tres parametros
    info: codigo da moeda:string
    br:codigo da moeda brasileira:string
    dias:qauntidade de dias:int
    retorna: o fechamento da moeda entre a data de hj e o quantidade de dias do paramentro dias'''

    info = info.upper()
    br=br.upper()
    if(len(info)==3) and (type(info)== str):
        cotacoes = requests.get('https://economia.awesomeapi.com.br/json/daily/{}-{}/{}'.format(info,br,dias))
        r=cotacoes.json()
        f=open('fechamento dos ultimos dias.txt','w')
        for i in r:
            f.write('{}\n'.format(i))
        return f
    
def tabelacotacao(data,convertida,atual):

    '''essa função recebe tres parametros
    data: data do inicial:string
    convertida: codigo da moeda para ser convertida::string
    atual: codigo da moeda atual:string
    retorna: cotação da moeda entre a data inicial ate hj'''

    info=data.split('/')
    dt=''
    y=str(datetime.date.today().year)
    m=str(datetime.date.today().month)
    d=str(datetime.date.today().day)
    print(y+m+d)
    for i in range(2,-1,-1):
        dt=dt+info[i]
    print(dt)
    atual = atual.upper()
    convertida = convertida.upper()
    cotacoes = requests.get('https://economia.awesomeapi.com.br/{}-{}/10?start_date={}&end_date={}'.format( convertida, atual,dt,y+'0'+m+d))
    r = cotacoes.json()
    f = open('cotações_dos_ultimos_dias.txt', 'w')
    print(r)
    for i in r:
        f.write('{}\n'.format(i))
    return f

def CTacoes(datai,dataf,nome):
    
    '''Essa função recebe tres parametros
    datai:data inicial:string
    dataf:data final:string
    nome: que é o codigo das ações:string
    e retorna o fechamento das ações entre as duas datas'''

    yfinance.pdr_override()
    cotacao=web.get_data_yahoo(nome,start=datai,end=dataf)
    print(cotacao)
    cotacao['Adj Close'].plot()
    plt.show()
    f=open('info açoes.txt','w')
    f.write('{}\n'.format(cotacao))
    return cotacao