from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    # --- Database ---
    db_name: str
    db_user: str
    db_password: str
    database_url: str


    # --- Auth ---
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    oauth2_scheme: str
    SCOPES: dict[str, str]


    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "allow",
    }

# --- Créer une instance ---
config = AppConfig()  # type: ignore
