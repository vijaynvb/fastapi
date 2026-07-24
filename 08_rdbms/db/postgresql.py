from sqlalchemy import create_engine, text, event
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import NullPool
import time

# Database credentials
DB_USER = "postgres"
DB_PASSWORD = "mysecretpassword"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "todo_db"

# Connection URLs
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DEFAULT_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/postgres"

# SQLAlchemy setup
engine = None
SessionLocal = None
Base = declarative_base()


def check_database_exists(db_name: str = DB_NAME) -> bool:
    """Check if the database exists"""
    try:
        # Connect to the default 'postgres' database to check if our DB exists
        temp_engine = create_engine(
            DEFAULT_DATABASE_URL,
            poolclass=NullPool,
            connect_args={"connect_timeout": 5}
        )
        
        with temp_engine.connect() as conn:
            # Query to check if database exists
            result = conn.execute(
                text(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'")
            )
            exists = result.fetchone() is not None
            return exists
    except Exception as e:
        print(f"❌ Error checking database: {str(e)}")
        return False


def create_database(db_name: str = DB_NAME) -> bool:
    """Create the database if it doesn't exist"""
    try:
        # Connect to the default 'postgres' database
        temp_engine = create_engine(
            DEFAULT_DATABASE_URL,
            poolclass=NullPool,
            connect_args={"connect_timeout": 5}
        )
        
        with temp_engine.connect() as conn:
            # Set autocommit mode for CREATE DATABASE
            conn = conn.execution_options(isolation_level="AUTOCOMMIT")
            
            # Create database if it doesn't exist
            conn.execute(text(f"CREATE DATABASE {db_name}"))
            print(f"✅ Database '{db_name}' created successfully!")
            return True
    except Exception as e:
        if "already exists" in str(e):
            print(f"⚠️  Database '{db_name}' already exists")
            return True
        else:
            print(f"❌ Error creating database: {str(e)}")
            return False
    finally:
        if temp_engine:
            temp_engine.dispose()


def init_db_connection():
    """Initialize database connection with existence check"""
    global engine, SessionLocal
    
    print("\n" + "="*60)
    print("🔍 Checking Database Connection...")
    print("="*60)
    
    # Step 1: Check if database exists
    print(f"\n📋 Checking if database '{DB_NAME}' exists...")
    
    # Retry logic for database connection
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            if not check_database_exists():
                print(f"❌ Database '{DB_NAME}' does not exist")
                print(f"📝 Creating database '{DB_NAME}'...")
                
                if not create_database():
                    print("Failed to create database. Retrying...")
                    retry_count += 1
                    time.sleep(2)
                    continue
                
                print(f"✅ Database '{DB_NAME}' ready!")
            else:
                print(f"✅ Database '{DB_NAME}' exists")
            
            break
        except Exception as e:
            print(f"⚠️  Connection attempt {retry_count + 1}/{max_retries} failed: {str(e)}")
            retry_count += 1
            if retry_count < max_retries:
                time.sleep(2)
            else:
                raise
    
    # Step 2: Create main engine
    print(f"\n🔗 Connecting to database '{DB_NAME}'...")
    try:
        engine = create_engine(
            SQLALCHEMY_DATABASE_URL,
            connect_args={"connect_timeout": 10}
        )
        
        # Test connection
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        print(f"✅ Connected to database '{DB_NAME}' successfully!")
        
    except Exception as e:
        print(f"❌ Failed to connect to database: {str(e)}")
        raise
    
    print("="*60 + "\n")
    return engine, SessionLocal


# Dependency to provide a database session per request
def get_db():
    if SessionLocal is None:
        raise RuntimeError("Database not initialized. Call init_db_connection() first.")
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Initialize database connection and create tables"""
    global engine, SessionLocal
    
    # Initialize connection with existence check
    engine, SessionLocal = init_db_connection()
    
    # Import all models here to ensure they are registered with SQLAlchemy
    from models.Todo import Todo  # Import explicitly
    
    print("📊 Creating database tables...")
    try:
        # Create all tables in the database
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully!")
    except Exception as e:
        print(f"❌ Error creating tables: {str(e)}")
        raise
