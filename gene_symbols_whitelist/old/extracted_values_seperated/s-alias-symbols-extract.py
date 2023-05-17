import re
fin = open("HGNC-gene-names.txt")

# find and write all "Alias Symbols" from HGNC_gene_names.txt
fout = open("alias-symbols.txt", "w")
l = re.findall('(?:Approved|Entry Withdrawn)\t\S*\t[\S ]*\t(\S+)', fin.read())
l1 = []
for s in l:
    if s in l1:
        continue
    else:
        l1.append(s)
        fout.write(s)
        fout.write("\n")
fout.close()
fin.close()