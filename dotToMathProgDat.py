from os import remove
import sys
from typing import Generator


def readFile(path: str) -> Generator[str,None,None]:
    
    try:
        with open(file=path, mode='r', encoding='utf-8') as file:
        
            while True:
                line = file.readline().strip()

                if not line: break

                yield line

    except Exception as e:
        print(f'Error while reading data from: {e.args[0]}')


def getGraphName(data: str) -> str:
    
    try:
        return data.split(" ")[1]
    except Exception as e:
        print(f'Error while parsing graph name: {e.args[0]}')


def getVertices(data: str) -> list[str]:
    try:
        return data.split(";")[:-1]
    except Exception as e:
        print(f'Error while parsing graph vertices: {e.args[0]}')


def getEdges(data: str) -> Generator[tuple[str],None,None]:
    edges = data.split(";")

    try:
        for edge in edges:
            edgeParts = edge.strip().split(" ")
            
            if len(edgeParts) == 3:
                yield (edgeParts[0], edgeParts[2])

    except Exception as e:
        print(f'Error while parsing graph edges: {e.args[0]}')


def removeNewLineChars(text: str) -> str:
    return text.replace("\n", "").replace("\r", "")


def parseGraphData(data: Generator[str,None,None]) -> tuple[str,list[str],Generator[tuple[str],None,None]]:
    try:
        namePart = next(data)
        name = getGraphName(namePart)

        vertexPart = next(data)
        vertices = ""
        while "-" not in vertexPart:
            vertices += vertexPart
            vertexPart = next(data)
        vertices = removeNewLineChars(vertices)
        vertices = getVertices(vertices)

        edgePart = vertexPart
        edges = ""
        while "}" not in edgePart:
            edges += edgePart
            edgePart = next(data)
        edges = removeNewLineChars(edges)
        edges = getEdges(edges)

        return (name, vertices, edges)

    except Exception as e:
        print(f'Error while parsing graph: {e.args[0]}')


def verticesToParam(vertices: list[str]) -> str:
    return f"param n := {len(vertices)};"


def edgesToParam(edges: Generator[tuple[str],None,None]) -> str:
    res = "set E := "

    try:
        for edge in edges:
            res += f"{str(edge[0])} {str(edge[1])} "
        
        return res.strip() + ";"
    
    except Exception as e:
        print(f'Error while generating parameter E: {e.args[0]}')


def getDotContent(vertices: list[str], edges: Generator[tuple[str],None,None]) -> list[str]:
    
    v = verticesToParam(vertices)
    e = edgesToParam(edges)

    return f"data;\n\n{v}\n\n{e}\n\nend;"


def getOutputFilePath(path: str) -> str:
    parts = path.split(".")

    return f"{parts[0]}.dat"


if __name__ == "__main__":
    
    try:
        if len(sys.argv) < 2: raise IndexError(".dot file path was not given") 

        inputPath = sys.argv[1];
        outputPath = getOutputFilePath(inputPath)
        
        data = readFile(inputPath)

        name, vertices, edges = parseGraphData(data)

        dat = getDotContent(vertices, edges)

        with open(outputPath, mode='w', encoding='utf-8') as file:
            file.write(dat)
        
        print(f"File was successfully written as:\n{outputPath}")
    
    except IndexError as e: 
        print(e.args[0])
    except Exception as e:
        print(f"Unspecified error has occured: {e.args[0]}")

