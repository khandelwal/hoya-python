from Bio.Seq import Seq

if __name__ == '__main__':
    sequence = Seq('AGTACACTGGT')

    print "Here is a sequence: "
    print sequence

    print "And here is it's complement: "
    print sequence.complement()


