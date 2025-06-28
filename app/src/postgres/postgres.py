import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Dict, List, Any, Optional, Union
import logging

class PostgresClient:
    """
    A PostgreSQL client that connects to the database defined in docker-compose.yaml.
    """
    def __init__(
        self,
        host: str = 'localhost',
        port: int = 5432,
        dbname: str = 'postgres',
        user: str = 'postgres',
        password: str = 'postgres'
    ):
        """Initialize the PostgreSQL client with connection parameters."""
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.conn = None
        self.cursor = None

    def connect(self) -> bool:
        """
        Connect to the PostgreSQL database.
        
        Returns:
            bool: True if connection is successful, False otherwise.
        """
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
            self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)
            logging.info("Successfully connected to PostgreSQL database")
            return True
        except psycopg2.Error as e:
            logging.error(f"Error connecting to PostgreSQL database: {e}")
            return False

    def close(self) -> None:
        """Close the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        logging.info("PostgreSQL connection closed")

    def execute_query(self, query: str, params: Optional[tuple] = None) -> Optional[List[Dict[str, Any]]]:
        """
        Execute a SQL query and return the results.
        
        Args:
            query: SQL query string
            params: Query parameters (to prevent SQL injection)
            
        Returns:
            List of dictionaries containing the query results, or None if an error occurred
        """
        try:
            if not self.conn or self.conn.closed:
                if not self.connect():
                    return None
                
            self.cursor.execute(query, params)
            
            # For SELECT queries, fetch and return results
            if query.strip().upper().startswith(('SELECT', 'WITH')):
                results = self.cursor.fetchall()
                return [dict(row) for row in results]
            
            # For other queries (INSERT, UPDATE, DELETE), commit the changes
            self.conn.commit()
            return [{'affected_rows': self.cursor.rowcount}]
        
        except psycopg2.Error as e:
            self.conn.rollback()
            logging.error(f"Database error: {e}")
            return None

    def execute_batch(self, query: str, params_list: List[tuple]) -> bool:
        """
        Execute a batch of SQL commands with different parameters.
        
        Args:
            query: SQL query with parameter placeholders
            params_list: List of parameter tuples
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not self.conn or self.conn.closed:
                if not self.connect():
                    return False
            
            with self.conn.cursor() as cur:
                psycopg2.extras.execute_batch(cur, query, params_list)
            
            self.conn.commit()
            return True
        
        except psycopg2.Error as e:
            self.conn.rollback()
            logging.error(f"Batch execution error: {e}")
            return False

    def table_exists(self, table_name: str) -> bool:
        """
        Check if a table exists in the database.
        
        Args:
            table_name: Name of the table to check
            
        Returns:
            bool: True if the table exists, False otherwise
        """
        query = """
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_name = %s
        );
        """
        result = self.execute_query(query, (table_name,))
        return result[0]['exists'] if result else False

    def create_table_if_not_exists(self, table_name: str, columns_definition: str) -> bool:
        """
        Create a table if it does not exist.
        
        Args:
            table_name: Name of the table to create
            columns_definition: SQL column definitions
            
        Returns:
            bool: True if successful, False otherwise
        """
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_definition})"
        result = self.execute_query(query)
        return result is not None


# Example usage:
if __name__ == "__main__":
    # Initialize the client
    postgres_client = PostgresClient()
    
    # Connect to the database
    if postgres_client.connect():
        # Example query
        result = postgres_client.execute_query("SELECT version();")
        if result:
            print(f"PostgreSQL version: {result[0]['version']}")
        
        # Close the connection
        postgres_client.close()
