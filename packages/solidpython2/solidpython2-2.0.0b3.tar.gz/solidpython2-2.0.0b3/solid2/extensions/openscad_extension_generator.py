#! /usr/bin/env python

from pathlib import Path

from solid2.core.utils import escape_openscad_identifier as escape
from solid2.libs.py_scadparser import scad_parser

headerTemplate = """\
from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{{Path(__file__).parent.parent / '{scadFile}'}}", use_not_include={use_not_include})

"""

constantTemplate = "{name} = OpenSCADConstant('{name}')"

callableTemplate = """\
class {name}(OpenSCADObject):
    def __init__({paramStr}):
       super().__init__({initStr})

"""

def generateStub(scadFile, outputDir, use_not_include):
    def generateHeader():
        return headerTemplate.format(__file__=__file__,
                                     scadFile=scadFile,
                                     use_not_include=use_not_include)

    def generateConstant(c):
        return constantTemplate.format(name=escape(c.name)) + "\n"

    def generateCallable(c):
        name = escape(c.name)
        paramNames = [escape(p.name) for p in c.parameters]

        paramStr = ", ".join(["self"] +
                             [f"{p}=None" for p in paramNames] +
                             ["**kwargs"])
        initList = [f'"{p}" : {p}' for p in paramNames]
        initList.append("**kwargs")
        initStr = f'"{name}", {{{", ".join(initList)}}}'
        return callableTemplate.format(name=name, paramStr=paramStr, initStr=initStr)

    modules, functions, global_vars = scad_parser.parseFile(scadFile)

    escaped_filename = escape(scadFile.stem) + ".py"
    with open(outputDir / escaped_filename, "w") as f:
        f.write(generateHeader())

        for c in global_vars:
            f.write(generateConstant(c))

        for c in modules + functions:
            f.write(generateCallable(c))

def generateInit(inDir, outputDir, packageName):
    import os
    try:
        os.mkdir(outputDir / packageName)
    except FileExistsError:
        pass

    stubFile = outputDir / packageName / "__init__.py"

    with open(stubFile, "w") as std_f:
        for f in inDir.iterdir():
            if not f.suffix == ".scad":
                continue

            std_f.write(f"from . import {escape(Path(f.name).stem)}\n")


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(description="generates a solidpython2 extensions "
                                        "from a OpenSCAD library")
    parser.add_argument("scadInDir",
                        help="directory containing the scad (library) files")
    parser.add_argument("packageName",
                        help="name of the generated python package")
    parser.add_argument("-i", "--include", action='store_false', default=True,
                        help="use OpenSCADs 'include' to import the library. "
                             "Otherwiese OpenSCADs 'use' is used")

    args = parser.parse_args()

    generateInit(Path(args.scadInDir), Path("."), args.packageName)

    for f in Path(args.scadInDir).iterdir():
        if not f.suffix == ".scad":
            continue

        generateStub(f, Path(".") / args.packageName, args.include)

