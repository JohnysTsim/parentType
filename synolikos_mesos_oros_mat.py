# coding: utf-8

""" Συνολικός μέσος όρος μαθημάτων """


# 3 μεταβλητές οι οποίες η καθεμία θα κρατάει το άθροισμα των βαθμών στο κάθε μάθημα, με αρχική τιμή 0
sum_mathimatika=0
sum_istoria=0
sum_glossa=0


# 3 μεταβλητές οι οποίες η καθεμία θα κρατάνε, το πλήθος των βαθμών σε κάθε ένα από τα 3 μαθήματα
n_mathimatika = int(input("dwse plhthos vathmon sta mathimatika: "))
n_istoria = int(input("dwse plhthos vathmon sthn istoria: "))
n_glossa = int(input("dwse plhthos vathmon sthn glossa: "))


# μια επανάληψη for, στην ο οποία ο χρήστης θα δίνει τους βαθμούς σε κάθε μάθημα και οι βαθμοί θα προστέθονται στο άθροισμα των βαθμών του κάθε μαθήματος
# η επανάληση θα εκετελείτε 3 φορές
for i in range(1, 3+1, 1):
    vathmos_mathimatika = int(input("dwse vathmo mathimatika: "))
    vathmos_istoria = int(input("dwse vathmo istoria: "))
    vathmos_glossa = int(input("dwse vathmo glossa: "))

    sum_mathimatika+=vathmos_mathimatika
    sum_istoria+=vathmos_istoria
    sum_glossa+=vathmos_glossa


# έπειτα θα βρίσκει τον μέσο όρο σε κάθε ένα από τα 3 μαθήματα
mo_mathimatika = sum_mathimatika / n_mathimatika
mo_istoria = sum_istoria / n_istoria
mo_glossa = sum_glossa / n_glossa

# τέλος θα βρίσκει τον συνολικό μέσο όρο από τους μέσους όρους και των 3ων μαθημάτων
mo_ola = (mo_mathimatika+mo_istoria+mo_glossa) / 3


# θα εμφανίζει τον συνολικό μέσο όρο
print(mo_ola)
