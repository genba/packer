from invoke import run, task

@task
def test():
    run('py.test tests')