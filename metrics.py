# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 18:13:36 2025

@author: CSU5KOR
"""

# metrics_mcp.py
from fastmcp import FastMCP
#from fastmcp.decorators import tool
from radon.metrics import mi_visit, h_visit
from radon.complexity import cc_visit

app = FastMCP("metrics")

@app.tool()
def analyze_code(code: str):
    """
    Compute Halstead Volume, Cyclomatic Complexity, LOC, and Maintainability Index for given code string.
    """
    halstead = h_visit(code)
    complexity = cc_visit(code)
    mi_score = mi_visit(code, True)

    return {
        "halstead_volume": sum(h for h in halstead.total),
        "cyclomatic_complexity": sum(c.complexity for c in complexity),
        "loc": code.count("\n") + 1,
        "maintainability_index": mi_score
    }

if __name__ == "__main__":
    app.run(transport="http")

