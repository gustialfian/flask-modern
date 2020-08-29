from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DB_URI = 'postgresql://sandbox:sandbox@localhost:6543/sandbox'
engine = create_engine(DB_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db(app):
    print('database.init_db(app)')
    Base.metadata.create_all(bind=engine)
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.commit()
        db_session.remove()



