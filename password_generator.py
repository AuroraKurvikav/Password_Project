import random
import string

def generate_password(length, use_special_chars):
    characters = string.ascii_letters + string.digits
    
    if use_special_chars:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("=== Генератор паролей ===")
    try:
        length = int(input("Введите желаемую длину пароля: "))
        if length <= 0:
            print("Длина должна быть больше 0!")
            return
            
        use_special = input("Использовать спецсимволы? (да/нет): ").strip().lower()
        use_special_chars = use_special in ['да', 'yes', 'y']
        
        password = generate_password(length, use_special_chars)
        
        print("\n" + "="*30)
        print(f"Ваш сгенерированный пароль: {password}")
        print("="*30)
        
    except ValueError:
        print("Ошибка: введите целое число для длины пароля.")

if __name__ == "__main__":
    main()