import pandas as pd

ecom = pd.read_csv('/home/lucas/Área de Trabalho/IC/ex_pd/Ecommerce Purchases')

print (ecom.info())
print ('\n\n\n')

#print (ecom.head())

#print(ecom.shape)

# ---
# Preco medio de compras
#print (ecom['Purchase Price'].mean())

# ---
# Preco de compra mais alto
#print (ecom['Purchase Price'].max())
# Preco de compra mais baixo
#print (ecom['Purchase Price'].min())

# ---
# Quantas pessoas escolheram en como lingua do site
#print (ecom.columns) # Informacoes das colunas do data frame
#print (ecom[ecom['Language'] == 'en'].shape)

# ---
# Quantas pessoas tem o acargo de advogado
#print (ecom[ecom['Job'] == 'Lawyer'].shape)

# ---
# Quantas pessoas fizeram compras em AM e quantas fizeram em PM
#print (ecom['AM or PM'].value_counts())

# ---
# Quais sao os 5 tipos de trabalhos mais comuns         
#print (ecom['Job'].value_counts()[:5])

# ---
# Qual o preco de transacao da compra que veio do Lot "90 WT".
#print (ecom[ecom['Lot'] == '90 WT']['Purchase Price'])

# ---
# Qual o email da pessoa com o cartao de credito 4926535242672853
#print (ecom[ecom['Credit Card'] == 4926535242672853]['Email'])

# ---
# Quantas pessoas tem o American Express como fornecedor de cartao de credito e fizeram uma compra acima de 95
#print(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].shape)

# ---
# Quantas pessoas tem o cartao de credito que expira em 2025
#print(sum((ecom['CC Exp Date']).apply(lambda x: x[3:]) == '25'))

# ---
# Quais sao os 5 principais provedores de email mais populares
#print (ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts()[:5])













