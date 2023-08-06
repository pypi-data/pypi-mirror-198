# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright 2023 David Seaward and contributors

import black
import coverage
import mdformat
import mdformat_mkdocs
import mkdocs
import pytest
import reuse

# import mkdocs_awesome_pages_plugin
# import mermaid2


def invoke():
    versions = {
        "black": black.__version__,
        "coverage": coverage.__version__,
        "mdformat": mdformat.__version__,
        "mdformat_mkdocs": mdformat_mkdocs.__version__,
        "mkdocs": mkdocs.__version__,
        "mkdocs_awesome_pages_plugin": "No builtin value",
        "mkdocs_mermaid2_plugin": "No builtin value",
        "pytest": pytest.__version__,
        "reuse": reuse.__version__,
    }

    for library, version in versions.items():
        print(f"{library}: {version}")


if __name__ == "__main__":
    invoke()
