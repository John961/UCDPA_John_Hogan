from sqlalchemy import create_engine
engine = create_engine('sqlite:///football.sql')
table_names = engine.table_names()
print(table_names)

