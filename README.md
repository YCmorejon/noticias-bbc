# 📰 Noticias BBC - Web Scraper con Playwright

Este proyecto es un **web scraper en Python** que extrae titulares, descripciones y enlaces de artículos de la sección **Culture** de BBC.  
Los datos se almacenan en un archivo CSV para facilitar su análisis y uso posterior.

---

## 🚀 Tecnologías usadas
- [Python 3.10+](https://www.python.org/)  
- [Playwright](https://playwright.dev/python/) (automatización de navegador)  
- [Pandas](https://pandas.pydata.org/) (procesamiento y exportación de datos)  
- [Rich](https://github.com/Textualize/rich) (logs con formato)  

---

## 📂 Estructura del proyecto
```

noticias-bbc/
├── src/
│   ├── main.py
│   ├── contexto.py
│   ├── simulacion.py
├── data/
│   └── noticias\_bbc.csv
├── requirements.txt
├── README.md
└── .gitignore

````

---

## ⚙️ Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/noticias-bbc.git
   cd noticias-bbc
````

2. Crea un entorno virtual e instala las dependencias:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows

   pip install -r requirements.txt
   ```

3. Instala los navegadores de Playwright:

   ```bash
   playwright install
   ```

---

## ▶️ Uso

Ejecuta el scraper:

```bash
python src/main.py
```

Esto generará un archivo CSV en la carpeta `data/` con el siguiente formato:

| titulo               | descripcion              | urls                                                                            |
| -------------------- | ------------------------ | ------------------------------------------------------------------------------- |
| Ejemplo de titular 1 | Ejemplo de descripción 1 | [https://www.bbc.com/culture/article/](https://www.bbc.com/culture/article/)... |
| Ejemplo de titular 2 | Ejemplo de descripción 2 | [https://www.bbc.com/culture/article/](https://www.bbc.com/culture/article/)... |

---

## 📌 Notas

* Se bloquean imágenes durante la navegación para **acelerar la carga**.
* Se implementa **logging** para seguimiento de errores y eventos importantes.
* Las URLs son filtradas para incluir únicamente artículos relevantes.

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT.

```

