import gzip
fp = gzip.open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa.gz')
contents = fp.read()
u_str = contents.decode('utf-8') 
str_list = u_str.split("\n>")
tet = []
name_list = []
len_list = []
for con in str_list:
    if "protein_coding" not in con:
        name_list.append(con.split(" gene_biotype:")[0].split("gene:")[-1])
        tet.append(con.split("]\n")[-1].replace("\n",""))
        len_list.append(len(con.split("]\n")[-1].replace("\n","")))

with open("noncoding_function.fa","w") as f:
    for i in range(len(name_list)):
        f.write(name_list[i])
        f.write(" ")
        f.write(str(len_list[i]))
        f.write(" ")
        f.write(tet[i])
        f.write("\n")
    f.close()
            
