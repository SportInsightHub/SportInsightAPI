# Fichier de configuration de l'api

class ConfigManager:
    # Variable de configuration de l'application
    APP_IP: str = "127.0.0.1" # Variable: APP_IP
    APP_PORT: int = 7676

    AUTH_ACCESS_TOKEN: str = "lTiekFB9jmvZNmMuwuvDrAbSwp0NUPExUeB1auAO1BCiJJH3T1XtUFkzXZRJQwIO"
    AUTH_REFRESH_TOKEN: str = "GU0wEIULTwsvbb0Q0ooAtEiytDPvwPLlb4dBiDVPGDYMeF4vibMBDIks8tqafkh4"

    DATABASE_HOST: str = "aws-0-eu-west-3.pooler.supabase.com" # Variable: DATABASE_HOST qui contient le nom de l'host de connexion à la base de donnée
    DATABASE_PORT: int = 6543 # Variable DATABASE_PORT qui contient le port de l'host de connexion à la base de donnée
    DATABASE_USER: str = "postgres.hlbqxrzefieilfoxpyfx" # Variable: DATABASE_USER qui contient l'identifiant de l'utilisateur de connexion à la base de donnée
    DATABASE_PASSWORD: str = "#GF^HI92#pt00nk$SF" # Variable: DATABASE_PASSWORD qui contient le mot de passe de l'utilisateur de connexion à la base de donnée

    @classmethod
    def AUTH(cls):
        keys = ["ACCESS_TOKEN", "REFRESH_TOKEN"]
        return {key: getattr(cls, f"AUTH_{key}") for key in keys} # Boucle pour récupérer les variables contenant le prefix "AUTH"

    @classmethod
    def APP(cls):
        keys = ["IP", "PORT"]
        return {key: getattr(cls, f"APP_{key}") for key in keys} # Boucle pour récupérer les variables contenant le prefix "APP"

    @classmethod
    def DATABASE(cls): # Définition des variables au groupe DATABASE -> ConfigManager.DATABASE()["...."]
        keys = ["HOST", "PORT", "USER", "PASSWORD"]
        return {key: getattr(cls, f"DATABASE_{key}") for key in keys} # Boucle pour récupérer les variables contenant le prefix "DATABASE"

ConfigManager()