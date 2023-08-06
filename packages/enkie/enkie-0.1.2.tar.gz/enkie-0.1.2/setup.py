import pkg_resources
import setuptools

pkg_resources.require("setuptools>=39.2")
setuptools.setup(
    setuptools_git_versioning={
        "enabled": True,
    },
    setup_requires=["setuptools-git-versioning<2"],
)
