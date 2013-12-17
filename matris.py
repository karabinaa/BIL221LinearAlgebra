# -*- coding: cp1254 -*-
import sys

class Matris(object):

    def __init__(self, m, n, init=True):
        if init:
            self.rows = [[0]*n for x in range(m)]
        else:
            self.rows = []
        self.m = m
        self.n = n
        
    def __getitem__(self, idx):
            return self.rows[idx]
    
    def __setitem__(self, idx, item):
            self.rows[idx] = item
        
    def __str__(self):
            s='\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
            return s + '\n'


    def __repr__(self):
        s=str(self.rows)
        
        rep="Matris: \"%s\"" % (s)
        return rep

        
    @classmethod
    def _makeMatris(cls, rows):

        m = len(rows)
        n = len(rows[0])
        # Validity check
        if any([len(row) != n for row in rows[1:]]):
            raise MatrisError, "matrislerin satırları eşit sayıda elemana sahip olmalıdır"
        mat = Matris(m,n, init=False)
        mat.rows = rows

        return mat

    
    @classmethod
    def readStdin(cls,aciklama=True):
        """ Klavyeden matris oku """
        if aciklama:
            print 'Elemanları aralarında birer boşluk bırakarak satır satır girip enter a basınız. Bitirmek için B yazınız.'
        rows = []
        while True:
            line = sys.stdin.readline().strip()
            if line=='B' or line=='b': break

            row = [int(x) for x in line.split()]
            rows.append(row)
            
        return cls._makeMatris(rows)

    @classmethod
    def fromList(cls, listoflists):
        """ Matrisi listelerin listesi formatında oku

            Örnek kullanım :
            Matris.fromList([[1 2 3], [4,5,6], [7,8,9]])
        """

        rows = listoflists[:]
        return cls._makeMatris(rows)
