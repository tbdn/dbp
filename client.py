import sys

def select_query():
    def _m():
        print "------------------------------------"
        print "Select a Query:"
        print "[1] All active connections at a certain point in time"
        print "[2] Average data volume for all connections between IP a.b.c.d and IP w.x.y.z"
        print "[3] All hosts that had connections to IP a.b.c.d on a given port number"
        print "[4] All hosts that had incoming connections on well-known ports"
        print "[5] All packets that contain a given byte sequence"
        print "[6] Ratio of SYN packets to FIN packets in a given time period"
        print "[exit] Exit Program"
        print "------------------------------------"
    
    def _clear():
        print("\033[H\033[J")

    _clear()
    while True:
        _m()
        qry = raw_input("Query selection: ")
        qry = qry.strip()

        if qry not in ["1", "2", "3", "4", "5", "6", "exit"]:
            _clear()
            print "Invalid Input!"
            continue

        if qry == "exit":
            sys.exit()

        return qry
        


while True:
    qry = select_query()

    raw_input("Press Enter to continue")