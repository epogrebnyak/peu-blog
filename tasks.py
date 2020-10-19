from invoke import task
from peu import main
import distutils.dir_util

@task
def test(c):
    c.run("pytest --doctest-glob='*.md'")


@task
def build(c):
    main()
    distutils.dir_util.copy_tree(src="assets", dst="./_build/assets")
