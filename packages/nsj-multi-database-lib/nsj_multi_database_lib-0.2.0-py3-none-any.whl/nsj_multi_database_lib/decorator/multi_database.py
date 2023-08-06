from functools import wraps
from flask import g, request

from nsj_multi_database_lib.injector_factory import InjectorFactory


def multi_database():
    """TODO
    """

    def __get_db_username(db_name: str, erp_login: str):
        return db_name.lower() + "_" + erp_login.lower()

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                with InjectorFactory() as factory:
                    database_dao = factory.database_dao()

                    # TODO pegar tenant na query string
                    tenant = int(request.args.get('tenant'))
                    database = database_dao.get_by_tenant(tenant)

                    # Definindo dados de conexão com o DB no contexto da aplicação
                    g.external_database = {
                        "host": database["host"],
                        "port": database["porta"],
                        "name": database["nome"],
                        "user": None,
                        "password": None
                    }

                with InjectorFactory(use_external_db_with_default_credentials=True) as factory:
                    usuario_dao = factory.usuario_dao()

                    usuario = usuario_dao.get_by_email(g.profile["email"])

                    g.external_database["user"] = __get_db_username(g.external_database["name"], usuario["login"])
                    g.external_database["password"] = usuario["senha"]

                return func(*args, **kwargs)
            except Exception as e:
                raise

        return wrapper

    return decorator
