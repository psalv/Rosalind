


class Edge(object):
    """An edge connecting two nodes of a graph."""

    def __init__(self, start, dest):
        self.start = start
        self.dest = dest

    def __str__(self):
        return str(self.dest) + " " + str(self.start)



class seqNode(object):
    """A representation of a DNA sequence as a node."""

    def __init__(self, seq, ID, k=3):
        self.seq = seq
        self.ID = ID

        self.start = seq[:k]
        self.end = seq[-k:]

    def hasOverlap(self, other):
        """Returns true if the k length sequence at the start of this seqNode matches the k length sequence at the end of the other seqNode."""
        if self.start == other.end:
            return True
        else:
            return False

    def __str__(self):
        return self.ID



def loadNodesFromFASTA(file, k):
    """Loads sequences from a FASTA file and returns a list of seqNode objects encompassing all sequences of the file."""
    file = open(file, 'r')
    seq = ''
    nodes = []
    for line in file:
        line = line.rstrip()
        if line[0] == '>':
            if seq != '':
                nodes += [seqNode(seq, ID, k), ]
            ID = line[1:]
            seq = ''
        else:
            seq += line

    nodes += [seqNode(seq, ID, k), ]

    return nodes



class seqOverlapDigraph(object):
    """Creates a digraph of all sequences from a FASTA file.
    Nodes are connected by edges determined by a k length overlap at the opposing ends of sequences."""

    def __init__(self, file, k=3):
        self.nodes = loadNodesFromFASTA(file, k)

        self.edges = []
        self.buildEdges()
        self.k = k

    def buildEdges(self):
        for node in self.nodes:
            for node2 in self.nodes:
                if node == node2:
                    continue
                if node.hasOverlap(node2):
                    self.edges.append(Edge(node, node2))

    def addNode(self, node):
        self.nodes.append(node)

        for n in nodes[:-1]:
            if node.hasOverlap(n):
                self.edges.append(Edge(node, n))

    def __str__(self):
        toPrint = ''
        for edge in self.edges:
            toPrint += str(edge) + "\n"
        return toPrint




t = seqOverlapDigraph('test1')
print t