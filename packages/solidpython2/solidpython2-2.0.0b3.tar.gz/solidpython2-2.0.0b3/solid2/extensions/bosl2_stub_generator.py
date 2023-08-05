#! /usr/bin/env python

from pathlib import Path
from openscad_extension_generator import generateStub

def generateBoslStd(bosl2_dir):
    stubFile = Path(__file__).absolute().parent / "bosl2" / "all.py"

    with open(stubFile, "w") as std_f:
        stdlibs = []
        with open(bosl2_dir / "std.scad") as f:
            for l in f.readlines():
                l = l.strip()
                if not l.startswith("include <"):
                    continue
                l = l.replace("include <", "").replace(">", "")
                std_f.write(f"from .{Path(l).stem} import *\n")
                stdlibs.append(l)

        for f in bosl2_dir.iterdir():
            if not f.suffix == ".scad" or f.name in stdlibs:
                continue
            if f.name in ["std.scad", "builtins.scad", "bosl1compat.scad"]:
                continue

            name = f.name.replace(".scad","")
            std_f.write(f"from . import {name}\n")


bosl2_dir = Path("../libs/BOSL2")

generateBoslStd(bosl2_dir)

for f in bosl2_dir.iterdir():
    if not f.suffix == ".scad":
        continue
    if f.name in ["std.scad", "builtins.scad", "bosl1compat.scad"]:
        continue

    generateStub(f, Path(__file__).parent / "bosl2", False)

