#!/usr/bin/env python3
"""
Database utility script for checking and managing the database
"""

from db.postgresql import (
    check_database_exists,
    create_database,
    DB_NAME,
    DB_HOST,
    DB_PORT,
    DB_USER,
)
import sys


def print_header(title: str):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def check_db():
    """Check if database exists"""
    print_header("Database Status Check")
    
    print(f"\n📋 Database Details:")
    print(f"   Host:     {DB_HOST}")
    print(f"   Port:     {DB_PORT}")
    print(f"   Database: {DB_NAME}")
    print(f"   User:     {DB_USER}")
    
    print(f"\n🔍 Checking database existence...")
    
    if check_database_exists():
        print(f"✅ Database '{DB_NAME}' EXISTS")
        return True
    else:
        print(f"❌ Database '{DB_NAME}' DOES NOT EXIST")
        return False


def create_db():
    """Create database if it doesn't exist"""
    print_header("Database Creation")
    
    if check_database_exists():
        print(f"\n✅ Database '{DB_NAME}' already exists!")
        return True
    
    print(f"\n📝 Creating database '{DB_NAME}'...")
    
    if create_database():
        print(f"✅ Database created successfully!")
        return True
    else:
        print(f"❌ Failed to create database!")
        return False


def main():
    """Main function"""
    if len(sys.argv) < 2:
        print_header("Database Utility Tool")
        print("\nUsage: python manage_db.py <command>")
        print("\nAvailable commands:")
        print("  check   - Check if database exists")
        print("  create  - Create database if it doesn't exist")
        print("  setup   - Check and create database if needed")
        print("\nExample:")
        print("  python manage_db.py check")
        print("  python manage_db.py create")
        print("  python manage_db.py setup")
        return
    
    command = sys.argv[1].lower()
    
    if command == "check":
        exists = check_db()
        sys.exit(0 if exists else 1)
    
    elif command == "create":
        success = create_db()
        sys.exit(0 if success else 1)
    
    elif command == "setup":
        print_header("Database Setup")
        print(f"\n🔄 Checking and setting up database '{DB_NAME}'...")
        
        if not check_database_exists():
            print(f"⚠️  Database does not exist. Creating...")
            if not create_database():
                print(f"❌ Failed to create database!")
                sys.exit(1)
        
        print(f"\n✅ Database is ready!")
        sys.exit(0)
    
    else:
        print(f"❌ Unknown command: {command}")
        print("Use 'check', 'create', or 'setup'")
        sys.exit(1)


if __name__ == "__main__":
    main()
