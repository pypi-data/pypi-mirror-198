import nox


@nox.session(venv_backend='venv', reuse_venv=True)
def local(session):
    install(session)


def install(session):
    session.install("-U", "pip")
    session.install("-e", ".")
