# 🤖 Chatbot FastAPI

Este proyecto es una API RESTful desarrollada con **FastAPI**, que simula un chatbot configurable por roles. Utiliza la API gratuita de OpenAI y guarda el historial de conversaciones en una base de datos **SQLite**.

---

## 🛠️ Instrucciones completas de instalación y ejecución

Sigue estos pasos en orden para ejecutar el proyecto correctamente, ya sea en **Windows**, **Linux** o **macOS**:

```bash
# 1. Clona el repositorio
git clone https://github.com/ruben3185/chatbot_fastapi.git
cd chatbot_fastapi

# 2. Crea un entorno virtual
# En Windows
python -m venv env
env\Scripts\activate

# En Linux o macOS
python3 -m venv env
source env/bin/activate

# 3. Instala las dependencias
pip install -r requirements.txt

# 4. Crea el archivo .env en la raíz del proyecto con tu API key de OpenAI
# Puedes usar cualquier editor o este comando:
echo OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx > .env

# 5. Ejecuta el servidor
uvicorn main:app --reload


# 6. Run test 
pytest