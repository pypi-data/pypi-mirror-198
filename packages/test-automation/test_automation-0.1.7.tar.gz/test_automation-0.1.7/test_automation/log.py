from test_automation import vault
import logging
class SingletonLogger:
    _instance = None

    def __new__(cls, project_name: str, is_test=False):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.setup_logger(project_name, is_test)
        return cls._instance

    def setup_logger(self, project_name, is_test):
        log_level = logging.DEBUG
        self.logger = logging.getLogger()
        self.logger.setLevel(log_level)

        if is_test :
            file_path = f".{project_name}.log"
        else :
            file_path = f"{vault.get_key_value('logging', 'logfile_path')}/{project_name}.log"

        file_handler = logging.FileHandler(file_path, mode='a', encoding='utf-8')
        file_handler.setLevel(log_level)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger
