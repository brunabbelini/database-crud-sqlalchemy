from pathlib import Path

from sqlalchemy import create_engine, String, Boolean, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

from werkzeug.security import generate_password_hash, check_password_hash
 
pasta_atual = Path(__file__).parent
PATH_TO_BD = pasta_atual / 'bd_usuarios.sqlite'

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))
    senha: Mapped[str] = mapped_column(String(128))
    email: Mapped[str] = mapped_column(String(30))
    acesso_gestor: Mapped[bool] = mapped_column(Boolean(), default=False)

    def __repr__(self):
        return f"Usuario({self.id=}, {self.nome=})"
    
    def define_senha(self, senha):
        self.senha = generate_password_hash(senha)

    def verifica_senha(self,senha):
        return check_password_hash(self.senha, senha)

engine = create_engine(f'sqlite:///{PATH_TO_BD}')
Base.metadata.create_all(bind=engine)


# CRUD ========================
def cria_usuarios(
        nome,
        senha,
        email,
        **kwargs      
):
    with Session(bind=engine) as session:
        usuario = Usuario(
            nome=nome,
            email=email,
            **kwargs  
        )
        usuario.define_senha(senha)
        session.add(usuario)
        session.commit()

def le_todos_usuarios():
    with Session(bind=engine) as session:
        comando_sql = select(Usuario)
        usuarios = session.execute(comando_sql).fetchall()
        usuarios = [user[0] for user in usuarios]
        return usuarios

def le_usuario_por_id(id):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuarios = session.execute(comando_sql).fetchall()
        return usuarios[0][0]
    
def modifica_usuario(
        id,
        **kwargs
        ):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuarios = session.execute(comando_sql).fetchall()
        for usuario in usuarios:
            for key, value in kwargs.items():
                if key == 'senha':
                    usuario[0].define_senha(value)
                else:
                    setattr(usuario[0], key, value)
        session.commit()

def deleta_usuario(id):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuarios = session.execute(comando_sql).fetchall()
        for usuario in usuarios:
            session.delete(usuario[0])
        session.commit()


if __name__ == '__main__':
    # cria_usuarios(
    #     'Bruna Belini',
    #     senha='minha_senha',
    #     email='meuemail.com',
    #     acesso_gestor=True
    # )

    # usuarios = le_todos_usuarios()
    # usuario_0 = usuarios[0]
    # print(usuario_0)
    # print(usuario_0.nome, usuario_0.senha, usuario_0.email)

    # usuario_bruna = le_usuario_por_id(id=1)
    # print(usuario_bruna)
    # print(usuario_bruna.nome, usuario_bruna.senha, usuario_bruna.email)

    # modifica_usuario(id=1, nome='Novo Nome da Bruna', senha='Nova senha Bruna')

    # deleta_usuario(id=4)

    usuario_bruna = le_usuario_por_id(id=1)
    print(usuario_bruna.verifica_senha('minha_senha'))




