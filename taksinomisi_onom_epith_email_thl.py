# coding: utf-8

""" Ταξινόμηση λίστας ονομάτων, επιθέτων, emails και τηλεφώνων σύμφωνα με την λίστα των επιθέτων των μαθητών """



# 4 άδειες λίστες μία στην οποία θα μπουν τα ονόματα, μία στην οποία θα μπούν τα επίθετα, μια στην οποία θα μπούν emails 
# και μια στην οποία θα μπούν τηλέφωνα
fNameList = []
lNameList  = []
emails = []
thlefwna = []

# δίνουμε το πλήθος των μαθητών, το οποίο θα είναι ταυτόχρονα και το μέγεθος όλων των λιστών μας
n = int(input("dwse plhthos mathitwn: "))

# επανάληψη for στην οποία το πρόγραμμα ζητάει από τον χρήστη, να δώσει από το πληκρολόγιο 4 διαφορετικά πράγματα όνομα, επίθετο, email, τηλέφωνο
# και έπειτα τα εισάγει σε 4 διαφορετικές λίστες το καθένα εκεί που αναλογεί
# αυτή η επανάληψη θα εκτελεστεί ανάλογα με το πλήθος των μαθητών, δηλαδή τόσες φορές, όσες το πλήθος
for i in (1, n+1, 1):
    onoma = str(input("dwse onoma mathith: "))
    epwnumo = str(input("dwse epwnumo mahtith: "))
    # to kserw oti sthn python2.7 einai raw_input
    email = str(input("dwse email mathith: "))
    thlefwno = int(input("dwse thlefwno mathith: "))
    fNameList.append(onoma)
    lNameList .append(epwnumo)
    emails.append(email)
    thlefwna.append(thlefwno)


# μας δίνει το μέθγεθος της λίστας των επιθέτων
lNameListLength = len(lNameList )


# εφόσον το πρώτο γράμμα του επιθέτου που δείχνει τώρα το j προηγείτεαι αλφαβητικά από αυτό που έδειχνε προηγουμένος 
# το j(δηλαδή j-1) στην λίστα, κάνε ανταλλαγή μεταξύ των επιθέτων και ταυτόχρονα άλλαξε και τα ονόματα, emails, τηλέφωνα
# και αυτό θα εκτελεστει μέχρι οι τα επίθετα να μπουν σε αλφαβητική σειρά από το a-z
# αν θέλαμε να κάνουμε από το z-a απλά θα αλλάζαμε το < πιο κάτω με >
for i in range(1, lNameListLength, 1):
    for j in range(1, lNameListLength - 1, -1):
        if lNameList [j] < lNameList [j - 1]:
            lNameList [j], lNameList [j - 1] = lNameList [j - 1], lNameList [j]
            fNameList[j], fNameList[j - 1] = fNameList[j - 1], fNameList[j]
            emails[j], emails[j - 1] = emails[j-1], emails[j]
            thlefwna[j], thlefwna[j - 1] = thlefwna[j - 1], thlefwna[j]


# εμφανίζει την λίστα με τα επίθετα, την λίστα με τα ονόματα, την λίστα με τα emails και την λίστα με τα τηλέφωνα
print("onomata: ", fNameList)
print("epwnuma: ", lNameList )
print("emails: ", emails)
print("thlefwna: ", thlefwna)
