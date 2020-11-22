import dotToMathProgDat as code

path = "test.dot"


def test_readFile1():
    
    data = code.readFile(path)
    actual = "0;" in data
    expect = True

    assert actual == expect


def test_readFile2():
    
    data = code.readFile(path)
    actual = "0 -- 1;" in data
    expect = True

    assert actual == expect


def test_readFile3():
    
    data = code.readFile(path)
    actual = "graph G {" in data
    expect = True

    assert actual == expect


def test_getGraphName():

    actual = code.getGraphName("graph G {")
    expect = "G"

    assert actual == expect


def test_getVertices1():

    data = "0;1;2;3;4;"

    vertices = code.getVertices(data)

    actual = vertices[1]
    expect = "1"

    assert actual == expect


def test_getVertices2():

    data = "0;1;2;3;4;"

    vertices = code.getVertices(data)

    actual = vertices[-1]
    expect = "4"

    assert actual == expect


def test_getVertices3():

    data = "0;1;2;3;4;"

    vertices = code.getVertices(data)

    actual = len(vertices)
    expect = 5

    assert actual == expect


def test_getEdges1():

    data = "0 -- 1; 1 -- 2; 2 -- 3; 0 -- 2;4 -- 5"

    vertices = code.getEdges(data)

    edge = next(vertices)
    edge = next(vertices)
    actual = edge[0]
    expect = "1"

    assert actual == expect


def test_getEdges2():

    data = "0 -- 1; 1 -- 2; 2 -- 3; 0 -- 2;4 -- 5"

    vertices = code.getEdges(data)

    edge = next(vertices)
    edge = next(vertices)
    actual = edge[1]
    expect = "2"

    assert actual == expect


def test_getEdges3():

    data = "0 -- 1; 1 -- 2; 2 -- 3; 0 -- 2;4 -- 5"

    vertices = code.getEdges(data)

    edge = next(vertices)
    actual = edge[0]
    expect = "0"

    assert actual == expect


def test_parseGraphData_name():

    data = code.readFile(path)

    name, vertices, edges = code.parseGraphData(data)

    actual = name
    expect = "G"

    assert actual == expect


def test_parseGraphData_vertices1():

    data = code.readFile(path)

    name, vertices, edges = code.parseGraphData(data)

    actual = vertices[0]
    expect = "0"

    assert actual == expect


def test_parseGraphData_vertices2():

    data = code.readFile(path)

    name, vertices, edges = code.parseGraphData(data)

    actual = vertices[-1]
    expect = "5"

    assert actual == expect


def test_parseGraphData_edges1():

    data = code.readFile(path)

    name, vertices, edges = code.parseGraphData(data)

    edge = next(edges)

    actual = edge[0]
    expect = "0"

    assert actual == expect


def test_parseGraphData_edges2():

    data = code.readFile(path)

    name, vertices, edges = code.parseGraphData(data)

    edge = next(edges)

    actual = edge[1]
    expect = "1"

    assert actual == expect


def test_parseGraphData_edges3():

    data = code.readFile(path)

    name, vertices, edges = code.parseGraphData(data)

    edge = next(edges)
    edge = next(edges)
    edge = next(edges)

    actual = edge[1]
    expect = "2"

    assert actual == expect


def test_parseGraphData_edges4():

    data = code.readFile(path)

    name, vertices, edges = code.parseGraphData(data)

    edge = next(edges)
    edge = next(edges)
    edge = next(edges)
    edge = next(edges)
    edge = next(edges)

    actual = edge[0]
    expect = "3"

    assert actual == expect


def test_verticesToParam():

    vertices = ['0', '1', '2', '3', '4', '5']

    actual = code.verticesToParam(vertices)
    expect = "param n := 6;"

    assert actual == expect


def test_edgesToSet():

    edges = [("0", "1"), ("0", "2"), ("1", "2"), ("1", "4")]
    edges = (x for x in edges)

    actual = code.edgesToParam(edges)
    expect = "set E := 0 1 0 2 1 2 1 4;"

    assert actual == expect


def test_getDotContent():

    file = code.readFile(path)
    
    graphName, vertices, edges = code.parseGraphData(file)

    actual = code.getDotContent(vertices, edges)
    expected = "data;\n\nparam n := 6;\n\nset E := 0 1 0 2 1 2 1 4 3 2 3 5 4 5;\n\nend;"

    assert actual == expected


def test_getOutputFilePath_fullInputFileName():

    path = r"C:\Users\piotr\Desktop\Optymalizacja kombinatoryczna\Zadanie03\test.dot"

    actual = code.getOutputFilePath(path)
    expect = r"C:\Users\piotr\Desktop\Optymalizacja kombinatoryczna\Zadanie03\test.dat"

    assert actual == expect

def test_getOutputFilePath_onlyInputFileName():

    path = r"C:\Users\piotr\Desktop\Optymalizacja kombinatoryczna\Zadanie03\test"

    actual = code.getOutputFilePath(path)
    expect = r"C:\Users\piotr\Desktop\Optymalizacja kombinatoryczna\Zadanie03\test.dat"

    assert actual == expect


