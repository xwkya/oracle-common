import struct
from azure.identity import DefaultAzureCredential
from sqlalchemy import event


# Constants for Azure SQL authentication
TOKEN_URL = "https://database.windows.net/"
SQL_COPT_SS_ACCESS_TOKEN = 1256


def setup_azure_token_provider(engine):
    """
    Sets up the Azure token provider for SQL Server authentication.
    This needs to be called before any connections are made.
    """
    azure_credentials = DefaultAzureCredential()

    @event.listens_for(engine, "do_connect")
    def provide_token(dialect, conn_rec, cargs, cparams):
        # Remove the "Trusted_Connection" parameter that SQLAlchemy adds
        cargs[0] = cargs[0].replace(";Trusted_Connection=Yes", "")

        # Create token credential
        raw_token = azure_credentials.get_token(TOKEN_URL).token.encode("utf-16-le")
        token_struct = struct.pack(f"<I{len(raw_token)}s", len(raw_token), raw_token)

        # Apply it to keyword arguments
        cparams["attrs_before"] = {SQL_COPT_SS_ACCESS_TOKEN: token_struct}


def get_connection_string(server_name, db_name, db_port) -> str:
    """
    Creates the connection string for Azure SQL Database.
    """

    return (
        f"mssql+pyodbc://@{server_name}:{db_port}/"
        f"{db_name}?driver=ODBC+Driver+18+for+SQL+Server"
    )