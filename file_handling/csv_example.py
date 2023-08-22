import csv

# with open('newcsv_ex.csv','r')as file:
#     x = csv.reader(file)
#     for i in x:
#         print(x)
#
#
# with open('newcsv_ex.csv','a')as file:
#     x=csv.writer(file)
#     x.writerow(['ECTA.S19A9,2003.03,,,C,Dollars,6,Electronic Card Transactions (ANZSIC06) - ECT,sagil - Electronic card transactions A/S/T by division,Actual,Total,,,'])
#     file.close()
#
# with open('python_class.csv','w')as file:
#     writer = csv.writer(file)
#     writer.writerow(['hii'])
#     writer.writerow(['hello'])
#     writer.writerow(['how are you'])
#
#
# with open('python_class.csv','r',newline='\n')as file:
#     reader = csv.reader(file)
#     for i in reader:
#         print(i)
#

with open('python_class.csv','w')as file:
    fieldnames=['first_name','last_name']
    writer = csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first_name':'sagil','last_name':'kottapally'})
    writer.writerow({'first_name': 'sarang', 'last_name': 'pokkan'})


with open('python_class.csv','r')as file:
    reader=csv.DictReader(file)
    for i in reader:
        print(reader)
