#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    /*----------------------------------------------------------------------*\
     * Copyright (C) 2014  Danilo da Silva Maciel
     *
     * This program is free software: you can redistribute it and/or modify
     * it under the terms of the GNU General Public License as published by
     * the Free Software Foundation, either version 3 of the License, or
     * (at your option) any later version.
     *
     * This program is distributed in the hope that it will be useful,
     * but WITHOUT ANY WARRANTY; without even the implied warranty of
     * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     * GNU General Public License for more details.
     *
     * You should have received a copy of the GNU General Public License
     * along with this program.  If not, see <http://www.gnu.org/licenses/>.
     *
    \*----------------------------------------------------------------------*/
"""
nomeArquivoLeitura = ''
nomeArquivoEscrita = ''
 
while nomeArquivoLeitura == '' or nomeArquivoLeitura == 'sair':
    nomeArquivoLeitura = raw_input('Digite o nome do arquivo para ler ou sair\n')
while nomeArquivoEscrita == '' or nomeArquivoEscrita == 'sair':
    nomeArquivoEscrita= raw_input('Digite o nome do arquivo que será gravado ou sair\n')

#criamos dois ponteiros que apontam para arquivos, um para leitura e outro para escrita
arquivoLeitura = open (nomeArquivoLeitura , 'r')
arquivoEscrita = open (nomeArquivoEscrita , 'w')

#pega a primeira linha do arquivo html
linha = arquivoLeitura.readline()

#se a linha rebida não estiver fazia
while len(linha) > 0:
    #naoPegar já começa com False para iniciar pegando o caractere
    naoPegar = False
    
    #letra irá receber caractere por caractere
    for letra in linha:
        if letra == '<':
            #se o caractere for abre que especifica o inicio de uma tag em html, então não pegamos
            naoPegar = True
            letra = ''
        elif letra == '>':
            #se o caractere for fecha que especifica o fim de uma tag em html, então setamos como False a variavel naoPegar
            naoPegar = False
            letra = ''
        
        #se naoPegar estiver em False, gravamos o caractere no outro arquivo
        if naoPegar == False:
            arquivoEscrita.write(letra)
            
    #atualiza a linha que será lida novamente no loop
    linha = arquivoLeitura.readline()

#fecha os dois ponteiros de arquivos abertos, o de leitura e o de escrita
arquivoLeitura.close()
arquivoEscrita.close()

print 'Leitura e Gravação encerradas...'
print ('O arquivo %s com as informações, foi escrito com sucesso ' % nomeArquivoEscrita)
