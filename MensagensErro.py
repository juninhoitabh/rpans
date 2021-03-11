# Mensagem de erro para data incorreta
def erroData(linha):
    mensagem = 'Olá,\nOcorreu um erro com o campo data no registro da linha '+str(linha+1)+' da tabela.'
    mensagem = mensagem + '\nFavor verificar o problema.'
    mensagem = mensagem + '\n\nEssa mensagem foi gerada automaticamente, favor não responder.'
    mensagem = mensagem + '\n\nAtenciosmente,\n PCI.'
    return mensagem

# Mensagem de erro para Fornecedor que não atende à filial
def erroFornecedor(linha):
    mensagem = 'Olá,\nOcorreu um erro no registro da linha '+str(linha+1)+' da tabela.'
    mensagem = mensagem + '\nO fornecedor informado não fornece para a filial informada.'
    mensagem = mensagem + '\nFavor verificar o problema.'
    mensagem = mensagem + '\n\nEssa mensagem foi gerada automaticamente, favor não responder.'
    mensagem = mensagem + '\n\nAtenciosmente,\n PCI.'
    return mensagem

# Mensagem de erro para CNPJ não cadastrado
def erroCNPJ(linha):
    mensagem = 'Olá,\nOcorreu um erro no registro da linha '+str(linha+1)+' da tabela.'
    mensagem = mensagem + '\nO CNPJ informado não corresponde a nenhum fornecedor cadastrado.'
    mensagem = mensagem + '\nFavor verificar o problema.'
    mensagem = mensagem + '\n\nEssa mensagem foi gerada automaticamente, favor não responder.'
    mensagem = mensagem + '\n\nAtenciosmente,\n PCI.'
    return mensagem

# Mensagem de erro para Filial incorreta
def erroFilial(linha):
    mensagem = 'Olá,\nOcorreu um erro no registro da linha '+str(linha+1)+' da tabela.'
    mensagem = mensagem + '\nA Filial informado não está cadastrada.'
    mensagem = mensagem + '\nFavor verificar o problema.'
    mensagem = mensagem + '\n\nEssa mensagem foi gerada automaticamente, favor não responder.'
    mensagem = mensagem + '\n\nAtenciosmente,\n PCI.'
    return mensagem


# Mensagem de erro para Produto incorreto
def erroProduto(linha):
    mensagem = 'Olá,\nOcorreu um erro no registro da linha '+str(linha+1)+' da tabela.'
    mensagem = mensagem + '\nO produto informado não é válido.'
    mensagem = mensagem + '\nFavor verificar o problema.'
    mensagem = mensagem + '\n\nEssa mensagem foi gerada automaticamente, favor não responder.'
    mensagem = mensagem + '\n\nAtenciosmente,\n PCI.'
    return mensagem