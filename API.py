import argparse

class InvalidNumberException(Exception):
    """Excepción personalizada para números inválidos."""
    def __init__(self, num: int):
        super().__init__(f"El número debe estar entre 1 y 100. Recibido: {num}")

class NumberSet:
    def __init__(self):
        """Inicializa el conjunto de los primeros 100 números naturales."""
        self.numbers = set(range(1, 101))
        self.extracted_number = None

    def extract(self, num):
        """Extrae un número del conjunto si es válido."""
        if not (1 <= num <= 100):  # Cláusula de guarda
            raise InvalidNumberException(num)
        
        if num in self.numbers:
            self.numbers.remove(num)
            self.extracted_number = num

    def find_missing_number(self):
        """Encuentra el número faltante en el conjunto."""
        return sum(range(1, 101)) - sum(self.numbers)

def main():
    """Función principal que recibe el número desde la línea de comandos."""
    parser = argparse.ArgumentParser(description="Extrae un número y lo detecta después.")
    parser.add_argument("number", type=int, help="Número a extraer del conjunto (1-100)")
    args = parser.parse_args()

    try:
        # Crear el conjunto de números y extraer el número indicado
        number_set = NumberSet()
        number_set.extract(args.number)
        
        if number_set.extracted_number is not None:
            # Determinar qué número falta
            missing_number = number_set.find_missing_number()
            print(f"Número extraído: {args.number}")
            print(f"Número calculado como faltante: {missing_number}")
        else:
            print(f"El número {args.number} ya había sido extraído previamente.")

    except InvalidNumberException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error fatal: {e}")
