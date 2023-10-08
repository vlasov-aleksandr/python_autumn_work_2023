# задача 9-1 ДНК -> РНК
print('задача 9-1')
dna_rna_dct = {'G':'C','C':'G','T':'A','A':'T'}
dna = list(input('DNA input: '))
i = 0
rna = ""
while i < len(dna):
    k = dna[i]
    i += 1
    rna += dna_rna_dct.get(k)
print('RNA output: ', rna)
print()

# заадча 9-2 похожие слова
print('задача 9-2')



# задача 9-3 частотный анализ
print('задча 9-3')


