from sqlalchemy import create_engine,Column,String,Integer,Boolean,ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base
from dataclasses import dataclass
db=create_engine('sqlite:///loja.db')
Session = sessionmaker(bind=db)
session = Session()
Base=declarative_base()
class Produto(Base):
    __tablename__='produtos'
    id = Column('id',Integer,primary_key=True,autoincrement=True)
    nome= Column('nome',String)
    preco = Column('preço',Integer)
    quantidade_estoque = Column('quantidade_estoque',Integer)
    disponivel = Column('disponível',Boolean)
Base.metadata.create_all(bind=db)
'''produto1 = Produto(nome='Camiseta Preta',preco=80,quantidade_estoque=10,disponivel=True)
session.add(produto1)
session.commit()
produto2 = Produto(nome='Mouse Gamer',preco=93,quantidade_estoque=20,disponivel=True)
session.add(produto2)
session.commit()
produto3 = Produto(nome='Fone Bluetooth',preco=404,quantidade_estoque=1,disponivel=True)
session.add(produto3)
session.commit()'''
#produto1=session.query(Produto).filter_by(quantidade_estoque=10).first()
produto3=session.query(Produto).filter_by(nome='Fone Bluetooth').first()
'''produto1.quantidade_estoque = 25
session.add(produto1)
session.commit()'''
'''produto3.disponivel=False
session.add(produto3)
session.commit()'''
session.delete(produto3)
session.commit()