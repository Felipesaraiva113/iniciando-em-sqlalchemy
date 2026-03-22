from sqlalchemy import create_engine,Column,String,Integer,Boolean,ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base
db = create_engine('sqlite:///funcionarioseProjetos.db')
Session = sessionmaker(bind=db)
session = Session()
Base=declarative_base() 
class Funcionario(Base):
    __tablename__= 'funcionarios'
    id=Column(Integer,primary_key=True,autoincrement=True)
    nome = Column(String)
    cargo = Column(String)
    salario = Column(Integer)
class Projeto(Base):
    __tablename__='projetos'
    id=Column(Integer,primary_key=True,autoincrement=True)
    nome_do_projeto= Column(String)
    prazo_em_meses= Column(Integer)
    funcionario_responsavel = Column(ForeignKey('funcionarios.id'))
Base.metadata.create_all(bind=db)
'''funcionario1 = Funcionario(nome='Cláudio',cargo='Desenvovedor front-end',salario=5000)'''
funcionario1=session.query(Funcionario).filter_by(id=1).first()
'''session.add(funcionario1)
session.commit()'''
funcionario2 = Funcionario(nome='John Watson',cargo='Desenvovedor back-end',salario=10000)
'''session.add(funcionario2)
session.commit()'''
projeto2 = Projeto(nome_do_projeto='Mentes na Pista',prazo_em_meses=1,funcionario_responsavel = funcionario1.id)
projeto3 = Projeto(nome_do_projeto='Bot de Leitura',prazo_em_meses=1,funcionario_responsavel = funcionario1.id)
'''session.add(projeto3)
session.commit()'''
projetos = session.query(Projeto.nome_do_projeto,Projeto.funcionario_responsavel).all()
for nomeProjto,idFuncionario in projetos:
    print(f'Projeto: {nomeProjto}, ID do Funcionário Responsável: {idFuncionario}')
