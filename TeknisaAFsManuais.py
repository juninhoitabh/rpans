import pyautogui as p
import Funcoes as f
import pandas as pd
# import imghdr as im
import xlrd
import Emails as e
import MensagensErro as m

# Inicialização de váriáveis
arquivo = xlrd.open_workbook('dados.xls')  # importa o arquivo com os dados
planilha = arquivo.sheet_by_index(0)  # extrai a planilha do arquivo para uma variável

# Dados para o envio de email
emailResponsavel = 'pci2@nsabor.com.br'
assuntoErro = 'Problema com AF manual'

contador = 1  # controle para a repetição iniciado na primeira linha da tabela

# Arquivo de saída
registro = {'Fornecedor': [],
            'Filial': [],
            'Produto': [],
            'Entrega': [],
            'Vunitario': [],
            'Status': []}

while contador < planilha.nrows:
    # atribuição de valores
    comprador = str('0026')  # Comprador não varia
    # print(comprador)
    fornecedor = planilha.cell_value(contador, 0)
    registro['Fornecedor'].append(fornecedor)
    # print(fornecedor)
    filial = planilha.cell_value(contador, 1)
    registro['Filial'].append(filial)
    # print(filial)
    produto = planilha.cell_value(contador, 2)
    registro['Produto'].append(produto)
    # print(produto)
    entrega = planilha.cell_value(contador, 3)
    registro['Entrega'].append(entrega)
    # print(entrega)
    marca = str('118')  # marca não varia
    # print(marca)
    quantidade = str('1')  # quantidade não varia
    # print(quantidade)
    vunitario = planilha.cell_value(contador, 4)
    registro['Vunitario'].append(vunitario)
    # print(vunitario)
    justificativa = 'AF gerada automaticamente BOT'
    # print(justificativa)
    # Abertura do sistema
    f.logaSistema('SUP', '0026', 'ren0504')
    p.click(f.posicaoMenu(3))
    p.sleep(1)
    p.click(f.posicaoSubmenu(3, 1))
    p.sleep(7)
    p.press('enter')
    p.sleep(4)
    # Tela de lançamento
    p.click(x=536, y=343)  # clica no icone novo
    p.sleep(3)
    p.typewrite(str(filial))
    p.press('tab')
    p.sleep(1)
    # Validação da Filial
    testeFilial = p.locateOnScreen('imagens/erroFilial.JPG', confidence=0.9)
    if testeFilial is not None:
        p.screenshot('imagens/telaErro.png')
        p.sleep(1)
        e.enviaEmail(emailResponsavel, assuntoErro, m.erroFilial(contador))
        testeData = None
        registro['Status'].append('Erro')
    else:
        p.press('tab')
        p.typewrite(str(comprador))
        p.press('tab')
        p.typewrite(str(fornecedor))
        p.press('tab')
        p.sleep(3)
        # Validação do CNPJ
        testeCNPJ = p.locateOnScreen('imagens/erroCNPJ.JPG', confidence=0.9)
        if testeCNPJ is not None:
            p.screenshot('imagens/telaErro.png')
            p.sleep(1)
            e.enviaEmail(emailResponsavel, assuntoErro, m.erroCNPJ(contador))
            testeData = None
            registro['Status'].append('Erro')
        else:
            p.sleep(2)
            p.click(x=736, y=360)  # clica na aba produto
            p.sleep(4)
            p.typewrite(produto)
            p.press('tab')
            p.sleep(2)
            testeProduto = p.locateOnScreen('imagens/erroProduto.JPG', confidence=0.9)
            if testeProduto is not None:
                p.screenshot('imagens/telaErro.png')
                p.sleep(1)
                e.enviaEmail(emailResponsavel, assuntoErro, m.erroProduto(contador))
                testeData = None
                registro['Status'].append('Erro')
            else:
                p.typewrite(entrega)
                p.press('tab')
                p.sleep(1)
                # Validação da data de entrega
                testeData = p.locateOnScreen('imagens/erroData.JPG', confidence=0.9)
                if testeData is not None:
                    p.screenshot('imagens/telaErro.png')
                    p.sleep(1)
                    e.enviaEmail(emailResponsavel, assuntoErro, m.erroData(contador))
                    testeData = None
                    registro['Status'].append('Erro')
                else:
                    p.typewrite(marca)
                    p.sleep(1)
                    p.press('tab')
                    p.typewrite(quantidade)
                    p.press('tab')
                    p.sleep(1)
                    p.click(x=1124, y=415)  # clica no campo valor unitário
                    p.sleep(1)
                    p.doubleClick(x=1124, y=415)  # clia no campo valor unitário
                    p.sleep(1)
                    p.typewrite(vunitario)
                    p.sleep(1)
                    p.click(x=1054, y=370)  # menu de justificativa
                    p.sleep(1)
                    p.press('enter')
                    p.sleep(2)
                    p.typewrite(justificativa)
                    p.press('tab')
                    p.click(x=672, y=345)  # icone de confirmação
                    p.sleep(1)
                    p.press('enter')
                    p.sleep(1)
                    testeFornecedor = p.locateOnScreen('imagens/erroFornecedor.JPG', confidence=0.9)
                    if testeFornecedor is not None:
                        p.screenshot('imagens/telaErro.png')
                        p.sleep(1)
                        e.enviaEmail(emailResponsavel, assuntoErro, m.erroFornecedor(contador))
                        testeData = None
                        registro['Status'].append('Erro')
                    else:
                        # p.click(x=1054, y=370)#sair da mensagem de inconsistencia
                        # e.EnviaEmail(emailResponsavel,assuntoErro,mensagemErro)
                        # p.hotkey('alt','n')
                        p.sleep(1)
                        registro['Status'].append('Concluido')
                        # p.press('right')
                        # p.press('enter')
    contador = contador + 1
    f.fecharModulo('SUP')
# Transfere o conteudo da matriz para um dataframe
saida = pd.DataFrame(registro, columns=['Fornecedor', 'Filial', 'Produto', 'Entrega', 'Vunitario', 'Status'])
# converte o dataframe para excel
saida.to_excel('saidas/'+f.dataHora()+'.xlsx', sheet_name='Planilha1')


