from sqlalchemy import create_engine,Column,String,Integer,Boolean,ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base
db = create_engine('sqlite:///castaldi.db')
Session = sessionmaker(bind=db)
session = Session()
Base=declarative_base() 
class Aluno(Base):
    __tablename__='alunos'
    nome = Column('nome',String,primary_key=True)
    email = Column('email',String)
    idade = Column('idade',Integer)
class Curso(Base):
    __tablename__='cursos'
    id = Column('id',Integer,primary_key=True,autoincrement=True)
    nome_do_curso = Column('nome do curso',String)
    duracao_em_meses = Column('duração em meses',Integer)
    aluno_responsavel = Column('aluno responsável',ForeignKey('alunos.nome'))
Base.metadata.create_all(bind=db)
aluno1 = Aluno(nome='Felipe',email='felipe@gmail.com',idade=15)
'''session.add(aluno1)
session.commit()'''
aluno2 = Aluno(nome='Pedro',email='pedro@gmail.com',idade=17)
'''session.add(aluno2)
session.commit()'''
curso1 = Curso(nome_do_curso='Desenvolvimento de Sistemas',duracao_em_meses =33,aluno_responsavel ='Felipe')

curso2 = Curso(nome_do_curso='Marketing',duracao_em_meses =33,aluno_responsavel ='Pedro')
'''session.add(curso2)
session.commit()'''
'''dono_de_tudo = session.query(Curso).filter_by(aluno_responsavel='Pedro').first()
dono_de_tudo.aluno_responsavel = 'Felipe'
session.add(dono_de_tudo)
session.commit()'''
aluno_deletado = session.query(Aluno).filter_by(email='pedro@gmail.com').first()
session.delete(aluno_deletado)
session.commit()