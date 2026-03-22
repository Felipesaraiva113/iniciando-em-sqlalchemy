from sqlalchemy import create_engine,Column,String,Integer,Boolean,ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base
db = create_engine('sqlite:///meubanco.db')
Session = sessionmaker(bind=db)
session = Session()
Base=declarative_base()
# as tabelas
class Usuario(Base):
    __tablename__='usuarios'
    id = Column('id',Integer,primary_key=True,autoincrement=True)
    nome=Column('nome',String)
    email= Column('email',String)
    senha=Column('senha',String)
    ativo =Column('ativo',Boolean)
    def __init__(self,nome,email,senha,ativo=True):
        self.nome = nome
        self.email=email 
        self.senha=senha 
        self.ativo = ativo
#livros
class Livro(Base):
    __tablename__='livros'
    id = Column('id',Integer,primary_key=True,autoincrement=True)
    titulo = Column('titulo',String)
    qtde_paginas= Column('qtde_paginas',Integer)
    dono = Column('dono',ForeignKey('usuarios.id'))
    def __init__(self,titulo,qtde_paginas,dono):
        self.titulo = titulo 
        self.qtde_paginas = qtde_paginas
        self.dono = dono
Base.metadata.create_all(bind=db)
#crud
#usuario = Usuario(nome='felipe2',email='felipe2@gmail.com',senha='123123')
#session.add(usuario) 
#session.commit()
#lista_usuarios = session.query(Usuario).all()
usuario_felipe =session.query(Usuario).filter_by(email='felipe@gmail.com').first()
'''usuario_felipe2 =session.query(Usuario).filter_by(email='felipe2@gmail.com').first()
print(usuario_felipe2)
print(usuario_felipe2.nome)
print(usuario_felipe2.email)'''
livro = Livro(titulo='O Guia do Mochileiro das Galáxias',qtde_paginas=204,dono=usuario_felipe.id)
#session.add(livro)
session.commit()
#usuario_felipe.nome='felipe emanuel'
#session.add(usuario_felipe)
#session.commit()
'''session.delete(usuario_felipe2)
session.commit()'''

